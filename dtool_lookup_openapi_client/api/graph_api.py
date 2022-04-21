# coding: utf-8

"""
    dtool-lookup-server API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from dtool_lookup_openapi_client.api_client import ApiClient
from dtool_lookup_openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class GraphApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def graph_config_get(self, **kwargs):  # noqa: E501
        """Return the JSON-serialized dependency graph plugin configuration.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.graph_config_get(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        return self.graph_config_get_with_http_info(**kwargs)  # noqa: E501

    def graph_config_get_with_http_info(self, **kwargs):  # noqa: E501
        """Return the JSON-serialized dependency graph plugin configuration.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.graph_config_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_config_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        response_types_map = {
            200: "object",
        }

        return self.api_client.call_api(
            '/graph/config', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def graph_lookup_uuid_get(self, uuid, **kwargs):  # noqa: E501
        """List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.graph_lookup_uuid_get(uuid, async_req=True)
        >>> result = thread.get()

        :param uuid: (required)
        :type uuid: str
        :param page:
        :type page: int
        :param page_size:
        :type page_size: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: list[Dataset]
        """
        kwargs['_return_http_data_only'] = True
        return self.graph_lookup_uuid_get_with_http_info(uuid, **kwargs)  # noqa: E501

    def graph_lookup_uuid_get_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.graph_lookup_uuid_get_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param uuid: (required)
        :type uuid: str
        :param page:
        :type page: int
        :param page_size:
        :type page_size: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(list[Dataset], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'uuid',
            'page',
            'page_size'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_lookup_uuid_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'uuid' is set
        if self.api_client.client_side_validation and local_var_params.get('uuid') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `uuid` when calling `graph_lookup_uuid_get`")  # noqa: E501

        if self.api_client.client_side_validation and ('uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['uuid']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `uuid` when calling `graph_lookup_uuid_get`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `graph_lookup_uuid_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'page_size' in local_var_params and local_var_params['page_size'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `graph_lookup_uuid_get`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'page_size' in local_var_params and local_var_params['page_size'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `graph_lookup_uuid_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'uuid' in local_var_params:
            path_params['uuid'] = local_var_params['uuid']  # noqa: E501

        query_params = []
        if local_var_params.get('page') is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if local_var_params.get('page_size') is not None:  # noqa: E501
            query_params.append(('page_size', local_var_params['page_size']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        response_types_map = {
            200: "list[Dataset]",
            422: "Error",
        }

        return self.api_client.call_api(
            '/graph/lookup/{uuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def graph_lookup_uuid_post(self, uuid, dependency_keys, **kwargs):  # noqa: E501
        """List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.graph_lookup_uuid_post(uuid, dependency_keys, async_req=True)
        >>> result = thread.get()

        :param uuid: (required)
        :type uuid: str
        :param dependency_keys: (required)
        :type dependency_keys: DependencyKeys
        :param page:
        :type page: int
        :param page_size:
        :type page_size: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: list[Dataset]
        """
        kwargs['_return_http_data_only'] = True
        return self.graph_lookup_uuid_post_with_http_info(uuid, dependency_keys, **kwargs)  # noqa: E501

    def graph_lookup_uuid_post_with_http_info(self, uuid, dependency_keys, **kwargs):  # noqa: E501
        """List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.graph_lookup_uuid_post_with_http_info(uuid, dependency_keys, async_req=True)
        >>> result = thread.get()

        :param uuid: (required)
        :type uuid: str
        :param dependency_keys: (required)
        :type dependency_keys: DependencyKeys
        :param page:
        :type page: int
        :param page_size:
        :type page_size: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(list[Dataset], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'uuid',
            'dependency_keys',
            'page',
            'page_size'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_lookup_uuid_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'uuid' is set
        if self.api_client.client_side_validation and local_var_params.get('uuid') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `uuid` when calling `graph_lookup_uuid_post`")  # noqa: E501
        # verify the required parameter 'dependency_keys' is set
        if self.api_client.client_side_validation and local_var_params.get('dependency_keys') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `dependency_keys` when calling `graph_lookup_uuid_post`")  # noqa: E501

        if self.api_client.client_side_validation and ('uuid' in local_var_params and  # noqa: E501
                                                        len(local_var_params['uuid']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `uuid` when calling `graph_lookup_uuid_post`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'page' in local_var_params and local_var_params['page'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `graph_lookup_uuid_post`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'page_size' in local_var_params and local_var_params['page_size'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `graph_lookup_uuid_post`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'page_size' in local_var_params and local_var_params['page_size'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `graph_lookup_uuid_post`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'uuid' in local_var_params:
            path_params['uuid'] = local_var_params['uuid']  # noqa: E501

        query_params = []
        if local_var_params.get('page') is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if local_var_params.get('page_size') is not None:  # noqa: E501
            query_params.append(('page_size', local_var_params['page_size']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'dependency_keys' in local_var_params:
            body_params = local_var_params['dependency_keys']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json'],
                'POST', body_params))  # noqa: E501
        if content_types_list:
                header_params['Content-Type'] = content_types_list

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        response_types_map = {
            422: "Error",
            200: "list[Dataset]",
        }

        return self.api_client.call_api(
            '/graph/lookup/{uuid}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
