# apiclient
No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.1
- Package version: 0.0.1
- Build date: 2016-08-22T07:56:15.093Z
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import apiclient 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import apiclient
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
import apiclient
from apiclient.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = apiclient.IrqApi

try:
    api_response = api_instance.app_get_irq_balance_details()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IrqApi->app_get_irq_balance_details: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost/irq*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*IrqApi* | [**app_get_irq_balance_details**](docs/IrqApi.md#app_get_irq_balance_details) | **GET** /irqBalance | 
*IrqApi* | [**app_get_irq_details**](docs/IrqApi.md#app_get_irq_details) | **GET** /irqDetails | 
*IrqApi* | [**app_put_irq_set_affinity**](docs/IrqApi.md#app_put_irq_set_affinity) | **PUT** /irqSetAffinity/{irq_num}/{cpu_num} | 


## Documentation For Models

 - [IRQDetails](docs/IRQDetails.md)
 - [IRQStat](docs/IRQStat.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



