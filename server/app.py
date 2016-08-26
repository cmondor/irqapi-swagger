import connexion
from connexion.resolver import Resolver
from ..core.irq import *
import logging
import os
import pathlib

logger = logging.getLogger(__name__)

def get_irq_details(beginDate=None, endDate=None, path='proc_interrupts.txt'):
	balancer = IRQBalancer(path)
	stats = balancer.get_stats()
	balance_info = BalanceAlgo(stats).get_balance_info()

	return {
		'irq_details': {
			'irq_cpu_percent_distribution': balance_info[BalanceAlgo.DISTRIBUTION],
			'irq_cpu_count_distribution': balance_info[BalanceAlgo.COUNTS],
			'irq_distribution_metric': balance_info[BalanceAlgo.STDEV],
			'irq_stats': stats,
		}
	}

def get_irq_balance_details(path='proc_interrupts.txt'):
	balancer = IRQBalancer(path)
	current_stats = balancer.get_stats()
	balanced_info = balancer.get_balanced_irq_info(
		ReverseSortedLeastUsedBalanceAlgo)

	return {
		'irq_balance_details': {
			'irq_balance_algo': 'irq.ReverseSortedLeastUsedBalanceAlgo',
			'irq_final_distribution_metric': balanced_info[BalanceAlgo.STDEV],
			'irq_final_cpu_distribution': balanced_info[BalanceAlgo.DISTRIBUTION],
			'irq_final_cpu_count_distribution': balanced_info[BalanceAlgo.COUNTS],
			'irq_final_stats': balanced_info[BalanceAlgo.STATS],
			'irq_balance_instructions': balanced_info[BalanceAlgo.INSTRUCTIONS]
		}
	}

def put_irq_set_affinity(irqNum, cpuNum):
	return 'OK'

def get_blueprint(swagger_json=True,
		swagger_ui=True,
		strict_validation=True,
		validate_responses=True,
		debug=True):
	return connexion.Api( 
		pathlib.Path("%s/../spec/swagger.yaml" % os.path.dirname(
			os.path.abspath(__file__))),
		swagger_json=True,
		swagger_ui=True,
		strict_validation=True,
		validate_responses=True,
		debug=True).blueprint

if __name__ == '__main__':
    app = connexion.App(__name__)
    app.add_api('../spec/swagger.yaml',strict_validation=True)
    app.run(port=80,debug=True)
