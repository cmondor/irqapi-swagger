import argparse
from gen import apiclient
from gen.apiclient.rest import ApiException
from gen.apiclient.api_client import ApiClient
import logging
from pprint import pprint
import sys
import time

def main():
	#supress urllib3 logging
	config = apiclient.Configuration()
	config.logger["urllib3_logger"].setLevel(logging.CRITICAL)
	api_instance = apiclient.IrqApi(ApiClient(host='localhost'))

	beginDate = time.time()
	endDate = time.time()

	try:
	    api_response = api_instance.app_get_irq_details(beginDate, endDate)
	except ApiException as e:
	    print "ApiException when calling IrqApi->app_get_irq_details: %s" % e
	    sys.exit(1)
	except Exception as e:
	    print "General Exception when calling IrqApi->app_get_irq_details: %s" % e
	    sys.exit(1)

	if api_response is None:
		print "api_response is None, exiting."
		sys.exit(1)

	if 'irq_details' in api_response.attribute_map:
		irq_details = api_response.irq_details #gen.apiclient.models.irq_details.IRQDetails
		print "IRQ Distribution: %f" % irq_details.irq_distribution_metric

		i=0
		for percentage in irq_details.irq_cpu_percent_distribution :
			print "\tCPU%d: %d\t%4.2f%%" % (i,
				irq_details.irq_cpu_count_distribution[i], percentage)
			i+=1

if __name__ == '__main__':
	main()
