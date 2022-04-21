# dtool_lookup_openapi_client.DatasetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataset_annotations_post**](DatasetApi.md#dataset_annotations_post) | **POST** /dataset/annotations | Request the dataset annotations.
[**dataset_list_get**](DatasetApi.md#dataset_list_get) | **GET** /dataset/list | List the datasets a user has access to.
[**dataset_lookup_uuid_get**](DatasetApi.md#dataset_lookup_uuid_get) | **GET** /dataset/lookup/{uuid} | List all instances of a dataset in any base_uris the user has access to.
[**dataset_manifest_post**](DatasetApi.md#dataset_manifest_post) | **POST** /dataset/manifest | Request the dataset manifest.
[**dataset_readme_post**](DatasetApi.md#dataset_readme_post) | **POST** /dataset/readme | Request the dataset readme.
[**dataset_register_post**](DatasetApi.md#dataset_register_post) | **POST** /dataset/register | Register a dataset. The user needs to have register permissions on the base_uri.
[**dataset_search_post**](DatasetApi.md#dataset_search_post) | **POST** /dataset/search | List datasets the user has access to matching the query.
[**dataset_summary_get**](DatasetApi.md#dataset_summary_get) | **GET** /dataset/summary | Global summary of the datasets a user has access to.


# **dataset_annotations_post**
> object dataset_annotations_post(uri)

Request the dataset annotations.

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
    api_instance = dtool_lookup_openapi_client.DatasetApi(api_client)
    uri = dtool_lookup_openapi_client.Uri() # Uri | 

    try:
        # Request the dataset annotations.
        api_response = api_instance.dataset_annotations_post(uri)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetApi->dataset_annotations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | [**Uri**](Uri.md)|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**200** | OK |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dataset_list_get**
> list[Dataset] dataset_list_get(page=page, page_size=page_size)

List the datasets a user has access to.

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
    api_instance = dtool_lookup_openapi_client.DatasetApi(api_client)
    page = 1 # int |  (optional) (default to 1)
page_size = 10 # int |  (optional) (default to 10)

    try:
        # List the datasets a user has access to.
        api_response = api_instance.dataset_list_get(page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetApi->dataset_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **dataset_lookup_uuid_get**
> list[Dataset] dataset_lookup_uuid_get(uuid, page=page, page_size=page_size)

List all instances of a dataset in any base_uris the user has access to.

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
    api_instance = dtool_lookup_openapi_client.DatasetApi(api_client)
    uuid = 'uuid_example' # str | 
page = 1 # int |  (optional) (default to 1)
page_size = 10 # int |  (optional) (default to 10)

    try:
        # List all instances of a dataset in any base_uris the user has access to.
        api_response = api_instance.dataset_lookup_uuid_get(uuid, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetApi->dataset_lookup_uuid_get: %s\n" % e)
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

# **dataset_manifest_post**
> Error dataset_manifest_post(uri)

Request the dataset manifest.

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
    api_instance = dtool_lookup_openapi_client.DatasetApi(api_client)
    uri = dtool_lookup_openapi_client.Uri() # Uri | 

    try:
        # Request the dataset manifest.
        api_response = api_instance.dataset_manifest_post(uri)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetApi->dataset_manifest_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | [**Uri**](Uri.md)|  | 

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

# **dataset_readme_post**
> Error dataset_readme_post(uri)

Request the dataset readme.

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
    api_instance = dtool_lookup_openapi_client.DatasetApi(api_client)
    uri = dtool_lookup_openapi_client.Uri() # Uri | 

    try:
        # Request the dataset readme.
        api_response = api_instance.dataset_readme_post(uri)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetApi->dataset_readme_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | [**Uri**](Uri.md)|  | 

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

# **dataset_register_post**
> Uri dataset_register_post(register_dataset)

Register a dataset. The user needs to have register permissions on the base_uri.

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
    api_instance = dtool_lookup_openapi_client.DatasetApi(api_client)
    register_dataset = dtool_lookup_openapi_client.RegisterDataset() # RegisterDataset | 

    try:
        # Register a dataset. The user needs to have register permissions on the base_uri.
        api_response = api_instance.dataset_register_post(register_dataset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetApi->dataset_register_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_dataset** | [**RegisterDataset**](RegisterDataset.md)|  | 

### Return type

[**Uri**](Uri.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**422** | Unprocessable Entity |  -  |
**201** | Created |  -  |
**0** | Default error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dataset_search_post**
> list[Dataset] dataset_search_post(search_dataset, page=page, page_size=page_size)

List datasets the user has access to matching the query.

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
    api_instance = dtool_lookup_openapi_client.DatasetApi(api_client)
    search_dataset = dtool_lookup_openapi_client.SearchDataset() # SearchDataset | 
page = 1 # int |  (optional) (default to 1)
page_size = 10 # int |  (optional) (default to 10)

    try:
        # List datasets the user has access to matching the query.
        api_response = api_instance.dataset_search_post(search_dataset, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetApi->dataset_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_dataset** | [**SearchDataset**](SearchDataset.md)|  | 
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

# **dataset_summary_get**
> Summary dataset_summary_get()

Global summary of the datasets a user has access to.

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
    api_instance = dtool_lookup_openapi_client.DatasetApi(api_client)
    
    try:
        # Global summary of the datasets a user has access to.
        api_response = api_instance.dataset_summary_get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatasetApi->dataset_summary_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Summary**](Summary.md)

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

