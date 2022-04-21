# dtool_lookup_openapi_client.GraphApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**graph_config_get**](GraphApi.md#graph_config_get) | **GET** /graph/config | Return the JSON-serialized dependency graph plugin configuration.
[**graph_lookup_uuid_get**](GraphApi.md#graph_lookup_uuid_get) | **GET** /graph/lookup/{uuid} | List the datasets within the same dependency graph as &lt;uuid&gt;. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.
[**graph_lookup_uuid_post**](GraphApi.md#graph_lookup_uuid_post) | **POST** /graph/lookup/{uuid} | List the datasets within the same dependency graph as &lt;uuid&gt;. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.


# **graph_config_get**
> object graph_config_get()

Return the JSON-serialized dependency graph plugin configuration.

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
    api_instance = dtool_lookup_openapi_client.GraphApi(api_client)
    
    try:
        # Return the JSON-serialized dependency graph plugin configuration.
        api_response = api_instance.graph_config_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GraphApi->graph_config_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **graph_lookup_uuid_get**
> list[Dataset] graph_lookup_uuid_get(uuid, page=page, page_size=page_size)

List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.

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
    api_instance = dtool_lookup_openapi_client.GraphApi(api_client)
    uuid = 'uuid_example' # str | 
page = 1 # int |  (optional) (default to 1)
page_size = 10 # int |  (optional) (default to 10)

    try:
        # List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.
        api_response = api_instance.graph_lookup_uuid_get(uuid, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GraphApi->graph_lookup_uuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]

### Return type

[**list[Dataset]**](Dataset.md)

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

# **graph_lookup_uuid_post**
> list[Dataset] graph_lookup_uuid_post(uuid, dependency_keys, page=page, page_size=page_size)

List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.

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
    api_instance = dtool_lookup_openapi_client.GraphApi(api_client)
    uuid = 'uuid_example' # str | 
dependency_keys = dtool_lookup_openapi_client.DependencyKeys() # DependencyKeys | 
page = 1 # int |  (optional) (default to 1)
page_size = 10 # int |  (optional) (default to 10)

    try:
        # List the datasets within the same dependency graph as <uuid>. If not all datasets are accessible by the user, an incomplete, disconnected graph may arise.
        api_response = api_instance.graph_lookup_uuid_post(uuid, dependency_keys, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GraphApi->graph_lookup_uuid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **dependency_keys** | [**DependencyKeys**](DependencyKeys.md)|  | 
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]

### Return type

[**list[Dataset]**](Dataset.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | OK |  * X-Pagination -  <br>  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

