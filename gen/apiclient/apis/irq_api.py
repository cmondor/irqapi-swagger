# coding: utf-8

"""
    IRQ Balancer API

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class IrqApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def app_get_irq_balance_details(self, **kwargs):
        """
        
        Gets `IRQBalanceDetails`

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.app_get_irq_balance_details(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.app_get_irq_balance_details_with_http_info(**kwargs)
        else:
            (data) = self.app_get_irq_balance_details_with_http_info(**kwargs)
            return data

    def app_get_irq_balance_details_with_http_info(self, **kwargs):
        """
        
        Gets `IRQBalanceDetails`

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.app_get_irq_balance_details_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method app_get_irq_balance_details" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/irqBalance'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse200',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def app_get_irq_details(self, begin_date, end_date, **kwargs):
        """
        
        Gets `IRQDetails` object. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.app_get_irq_details(begin_date, end_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str begin_date: Begin Date RFC#3339 Format ie. 1996-12-19T16:39:57-08:00 (required)
        :param str end_date: End Date ie. 1996-12-19T16:39:57-08:00 (required)
        :param str path: path where /proc/interrupts can be found
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.app_get_irq_details_with_http_info(begin_date, end_date, **kwargs)
        else:
            (data) = self.app_get_irq_details_with_http_info(begin_date, end_date, **kwargs)
            return data

    def app_get_irq_details_with_http_info(self, begin_date, end_date, **kwargs):
        """
        
        Gets `IRQDetails` object. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.app_get_irq_details_with_http_info(begin_date, end_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str begin_date: Begin Date RFC#3339 Format ie. 1996-12-19T16:39:57-08:00 (required)
        :param str end_date: End Date ie. 1996-12-19T16:39:57-08:00 (required)
        :param str path: path where /proc/interrupts can be found
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['begin_date', 'end_date', 'path']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method app_get_irq_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'begin_date' is set
        if ('begin_date' not in params) or (params['begin_date'] is None):
            raise ValueError("Missing the required parameter `begin_date` when calling `app_get_irq_details`")
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params) or (params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `app_get_irq_details`")

        resource_path = '/irqDetails'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'begin_date' in params:
            query_params['begin_date'] = params['begin_date']
        if 'end_date' in params:
            query_params['end_date'] = params['end_date']
        if 'path' in params:
            query_params['path'] = params['path']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse2001',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def app_put_irq_set_affinity(self, irq_num, cpu_num, **kwargs):
        """
        
        Sets the CPU affinity for a specific IRQ. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.app_put_irq_set_affinity(irq_num, cpu_num, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int irq_num: The IRQ Channel (required)
        :param int cpu_num: The CPU to set the IRQ affinity to.  (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.app_put_irq_set_affinity_with_http_info(irq_num, cpu_num, **kwargs)
        else:
            (data) = self.app_put_irq_set_affinity_with_http_info(irq_num, cpu_num, **kwargs)
            return data

    def app_put_irq_set_affinity_with_http_info(self, irq_num, cpu_num, **kwargs):
        """
        
        Sets the CPU affinity for a specific IRQ. 

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.app_put_irq_set_affinity_with_http_info(irq_num, cpu_num, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int irq_num: The IRQ Channel (required)
        :param int cpu_num: The CPU to set the IRQ affinity to.  (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['irq_num', 'cpu_num']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method app_put_irq_set_affinity" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'irq_num' is set
        if ('irq_num' not in params) or (params['irq_num'] is None):
            raise ValueError("Missing the required parameter `irq_num` when calling `app_put_irq_set_affinity`")
        # verify the required parameter 'cpu_num' is set
        if ('cpu_num' not in params) or (params['cpu_num'] is None):
            raise ValueError("Missing the required parameter `cpu_num` when calling `app_put_irq_set_affinity`")

        resource_path = '/irqSetAffinity/{irq_num}/{cpu_num}'.replace('{format}', 'json')
        path_params = {}
        if 'irq_num' in params:
            path_params['irq_num'] = params['irq_num']
        if 'cpu_num' in params:
            path_params['cpu_num'] = params['cpu_num']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='str',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))