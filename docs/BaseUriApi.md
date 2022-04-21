# dtool_lookup_openapi_client.BaseUriApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_base_uri_list_get**](BaseUriApi.md#admin_base_uri_list_get) | **GET** /admin/base_uri/list | List all base_uris.
[**admin_base_uri_register_post**](BaseUriApi.md#admin_base_uri_register_post) | **POST** /admin/base_uri/register | Register a base URI.


# **admin_base_uri_list_get**
> list[BaseURI] admin_base_uri_list_get(page=page, page_size=page_size)

List all base_uris.

The user needs to be admin.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dtool_lookup_openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dtool_lookup_openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with dtool_lookup_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dtool_lookup_openapi_client.BaseUriApi(api_client)
    page = 1 # int |  (optional) (default to 1)
page_size = 10 # int |  (optional) (default to 10)

    try:
        # List all base_uris.
        api_response = api_instance.admin_base_uri_list_get(page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BaseUriApi->admin_base_uri_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]

### Return type

[**list[BaseURI]**](BaseURI.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-Pagination -  <br>  |
**422** | Unprocessable Entity |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_base_uri_register_post**
> Error admin_base_uri_register_post(base_uri)

Register a base URI.

The user needs to be admin.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import dtool_lookup_openapi_client
from dtool_lookup_openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dtool_lookup_openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dtool_lookup_openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with dtool_lookup_openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dtool_lookup_openapi_client.BaseUriApi(api_client)
    base_uri = dtool_lookup_openapi_client.BaseURI() # BaseURI | 

    try:
        # Register a base URI.
        api_response = api_instance.admin_base_uri_register_post(base_uri)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BaseUriApi->admin_base_uri_register_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_uri** | [**BaseURI**](BaseURI.md)|  | 

### Return type

[**Error**](Error.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

