import copy
import operator
import re
import statistics as s
import sys

class IRQBalancer(object):
	""" Determining whether interrupts are balanced and suggest fixes. """
	def __init__(self, interrupts_file='proc_interrupts.txt'):
		self.interrupts_file = interrupts_file
		self.cpu_count = 0
		self.irq_stats = []
		self.default_balance_algo = AlternatingBalanceAlgo
		self._populate_irq_stats()

	def get_stats(self):
		return self.irq_stats

	def get_balanced_irq_info(self, balanceAlgo=None):
		balanceAlgo = self.default_balance_algo if balanceAlgo is None else balanceAlgo
		algo = balanceAlgo(self.irq_stats)
		return algo.get_balance_info()

	def print_irq_stats(self, stats=None):
		if stats is None:
			stats = self.irq_stats
		for irq_stat in stats:
			pass
			# print irq_stat

	def _populate_irq_stats(self):
		""" Parse interrupts_file and populate self.irq_stats with IRQStat objects. """
		try:
			interrupt_file = open(self.interrupts_file)
		except IOError:
			# print "Unable to read IRQ info from: %s, exiting" % (self.interrupts_file)
			raise IOError

		first_line = True
		for line in interrupt_file:
			if first_line:
				first_line = False
				continue
			irq_stat = IRQStat().parse_line(line)
			if irq_stat[IRQStat.IRQ_DEVICE] is None:
				# print "**WARNING** Unable to parse line: %s skipping" % line
				continue
			my_cpu_count = len(irq_stat[IRQStat.CPU_INTERRUPTS])
			self.cpu_count = my_cpu_count if my_cpu_count > self.cpu_count else self.cpu_count
			self.irq_stats.append(irq_stat)
		interrupt_file.close()

class IRQStat(object):
	"""Interrupt details and counts object."""
	IRQ_NUM = 'irq_num'
	IRQ_TYPE = 'irq_type'
	IRQ_DEVICE = 'irq_device'
	CPU_INTERRUPTS = 'irq_cpu_interrupts'
	CPU_INTERRUPT_TOTAL = 'irq_cpu_interrupt_total'

	def __init__(self):
		self.irq_stat = {
				self.IRQ_NUM: None,
				self.IRQ_TYPE: None, 
				self.IRQ_DEVICE: None,
				self.CPU_INTERRUPTS: [],
				self.CPU_INTERRUPT_TOTAL: 0
			}

	def parse_line(self, line):
		return self._parse_interrupt_line(line)

	def _parse_interrupt_line(self, line):
		match = re.match('^\s?(\w*):\s*([0-9]*)\s*([0-9]*)\s*([\w-]*)\s*([\w-]*)', line)
		if match and len(match.groups()) > 3:
			if re.match('^[a-zA-Z]', match.group(1)):
				return irq_stat
			self.irq_stat[self.IRQ_NUM] = int(match.group(1))
			self.irq_stat[self.IRQ_DEVICE] = match.groups()[-1]
			self.irq_stat[self.IRQ_TYPE] = match.groups()[-2]
			self.irq_stat[self.CPU_INTERRUPTS] = [int(i) for i in match.groups()[1:-2]]
			self.irq_stat[self.CPU_INTERRUPT_TOTAL] = sum(self.irq_stat[self.CPU_INTERRUPTS])
		return self.irq_stat


class BalanceAlgo(object):

	STATS = 'balance_stats'
	INSTRUCTIONS = 'balance_instructions'
	DISTRIBUTION = 'balance_distribution'
	STDEV = 'balance_deviation'
	COUNTS = 'balance_count_distribution'

	def __init__(self, irq_stats=None):
		self.irq_stats_balanced       = []
		self.irq_balance_instructions = []
		self.irq_distribution         = []
		self.irq_counts               = []
		self.stdev                    = -1
		self.cpu_count                = 0
		self.irq_stats = [] if irq_stats is None else irq_stats 

		if len(irq_stats) > 0:
			self.cpu_count = len(irq_stats[0][IRQStat.CPU_INTERRUPTS])

	def get_balance_info(self):
		self.balance_stats()
		(self.irq_counts, self.irq_distribution) = self.get_irq_distribution()
		if len(self.irq_distribution) > 0:
			self.stdev = s.stdev(self.irq_distribution)
		return { 
			self.STATS: self.irq_stats_balanced, 
			self.INSTRUCTIONS: self.irq_balance_instructions,
			self.DISTRIBUTION: self.irq_distribution,
			self.COUNTS: self.irq_counts,
			self.STDEV: self.stdev
		}

	def balance_stats(self):
		self.irq_stats_balanced = self.irq_stats

	def get_irq_distribution(self, stats=None):
		cpu_sums = []
		cpu_percentages = []
		if stats is None:
			stats = self.irq_stats_balanced
		for irq_stat in stats:
			cpu_interrupts = irq_stat[IRQStat.CPU_INTERRUPTS]
			if len(cpu_sums) < 1:
				cpu_sums = [0,] * self.cpu_count
			i=0
			for cpu_interrupt_cnt in cpu_interrupts:
				cpu_sums[i] += cpu_interrupt_cnt
				i+=1
		total_interrupts = sum(cpu_sums)
		j=0
		cpu_percentages = [0,] * self.cpu_count
		for cpu_sum in cpu_sums:
			cpu_percentages[j] = (cpu_sum / float(total_interrupts)) * 100
			j+=1
		return (cpu_sums, cpu_percentages)

	def _sort_balanced_stats(self):
		self.irq_stats_balanced.sort(key=operator.itemgetter(IRQStat.IRQ_NUM))

class AlternatingBalanceAlgo(BalanceAlgo):
	def balance_stats(self):
		cpu_interrupt_accum = [0,] * self.cpu_count
		i=0
		for irq_stat in self.irq_stats:
			least_interrupts_index = i
			cpu_interrupt_accum[least_interrupts_index] += irq_stat[IRQStat.CPU_INTERRUPT_TOTAL]
			self.irq_balance_instructions.append("pin %s to CPU%d" % (irq_stat[IRQStat.IRQ_NUM],
				least_interrupts_index))
			balanced_irq_stat = copy.deepcopy(irq_stat)

			for num in range(self.cpu_count):
				if num is not i:
					balanced_irq_stat[IRQStat.CPU_INTERRUPTS][num] = 0
				else:
					balanced_irq_stat[IRQStat.CPU_INTERRUPTS][num] = irq_stat[IRQStat.CPU_INTERRUPT_TOTAL]
			self.irq_stats_balanced.append(balanced_irq_stat)
			i = i + 1 if i + 1 != self.cpu_count else 0
		self.irq_balance_instructions.sort()
		self._sort_balanced_stats()
		return self.irq_stats_balanced


class LeastUsedBalanceAlgo(BalanceAlgo):
	def balance_stats(self):
		return self._least_used_balance()

	def _least_used_balance(self, stats=None):
		stats = self.irq_stats if stats is None else stats
		cpu_interrupt_accum = [0,] * self.cpu_count
		for irq_stat in stats:
			least_interrupts_index = cpu_interrupt_accum.index(min(cpu_interrupt_accum))
			cpu_interrupt_accum[least_interrupts_index] += irq_stat[IRQStat.CPU_INTERRUPT_TOTAL]
			self.irq_balance_instructions.append("pin %s to CPU%d" % (irq_stat[IRQStat.IRQ_NUM],
				least_interrupts_index))
			balanced_irq_stat = copy.deepcopy(irq_stat)

			for num in range(self.cpu_count):
				if num is not least_interrupts_index:
					balanced_irq_stat[IRQStat.CPU_INTERRUPTS][num] = 0
				else:
					balanced_irq_stat[IRQStat.CPU_INTERRUPTS][num] = irq_stat[IRQStat.CPU_INTERRUPT_TOTAL]
			self.irq_stats_balanced.append(balanced_irq_stat)
		self.irq_balance_instructions.sort()
		self._sort_balanced_stats()
		return self.irq_stats_balanced		


class SortedLeastUsedBalanceAlgo(LeastUsedBalanceAlgo):
	def balance_stats(self):
		return self._least_used_balance(self._sort_stats())

	def _sort_stats(self):
		sorted_irq_stats = copy.deepcopy(self.irq_stats)
		sorted_irq_stats.sort(key=operator.itemgetter(IRQStat.CPU_INTERRUPT_TOTAL))
		return sorted_irq_stats

class ReverseSortedLeastUsedBalanceAlgo(LeastUsedBalanceAlgo):

	def balance_stats(self):
		return self._least_used_balance(self._sort_stats())

	def _sort_stats(self):
		sorted_irq_stats = copy.deepcopy(self.irq_stats)
		sorted_irq_stats.sort(key=operator.itemgetter(IRQStat.CPU_INTERRUPT_TOTAL), reverse=True)
		return sorted_irq_stats