# apiclient.IrqApi

All URIs are relative to *http://localhost/irq*

Method | HTTP request | Description
------------- | ------------- | -------------
[**app_get_irq_balance_details**](IrqApi.md#app_get_irq_balance_details) | **GET** /irqBalance | 
[**app_get_irq_details**](IrqApi.md#app_get_irq_details) | **GET** /irqDetails | 
[**app_put_irq_set_affinity**](IrqApi.md#app_put_irq_set_affinity) | **PUT** /irqSetAffinity/{irq_num}/{cpu_num} | 


# **app_get_irq_balance_details**
> InlineResponse200 app_get_irq_balance_details()



Gets `IRQBalanceDetails`

### Example 
```python
import time
import apiclient
from apiclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apiclient.IrqApi()

try: 
    api_response = api_instance.app_get_irq_balance_details()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IrqApi->app_get_irq_balance_details: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_get_irq_details**
> InlineResponse2001 app_get_irq_details(begin_date, end_date, path=path)



Gets `IRQDetails` object. 

### Example 
```python
import time
import apiclient
from apiclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apiclient.IrqApi()
begin_date = 'begin_date_example' # str | Begin Date RFC#3339 Format ie. 1996-12-19T16:39:57-08:00
end_date = 'end_date_example' # str | End Date ie. 1996-12-19T16:39:57-08:00
path = 'path_example' # str | path where /proc/interrupts can be found (optional)

try: 
    api_response = api_instance.app_get_irq_details(begin_date, end_date, path=path)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IrqApi->app_get_irq_details: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin_date** | **str**| Begin Date RFC#3339 Format ie. 1996-12-19T16:39:57-08:00 | 
 **end_date** | **str**| End Date ie. 1996-12-19T16:39:57-08:00 | 
 **path** | **str**| path where /proc/interrupts can be found | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **app_put_irq_set_affinity**
> str app_put_irq_set_affinity(irq_num, cpu_num)



Sets the CPU affinity for a specific IRQ. 

### Example 
```python
import time
import apiclient
from apiclient.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = apiclient.IrqApi()
irq_num = 56 # int | The IRQ Channel
cpu_num = 56 # int | The CPU to set the IRQ affinity to. 

try: 
    api_response = api_instance.app_put_irq_set_affinity(irq_num, cpu_num)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IrqApi->app_put_irq_set_affinity: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **irq_num** | **int**| The IRQ Channel | 
 **cpu_num** | **int**| The CPU to set the IRQ affinity to.  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

