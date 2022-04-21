# dtool_lookup_openapi_client.UserAdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_user_list_get**](UserAdminApi.md#admin_user_list_get) | **GET** /admin/user/list | List the users in the dtool lookup server.
[**admin_user_register_post**](UserAdminApi.md#admin_user_register_post) | **POST** /admin/user/register | Register a user in the dtool lookup server.


# **admin_user_list_get**
> list[User] admin_user_list_get(page=page, page_size=page_size)

List the users in the dtool lookup server.

The user in the Authorization token needs to be admin.

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
    api_instance = dtool_lookup_openapi_client.UserAdminApi(api_client)
    page = 1 # int |  (optional) (default to 1)
page_size = 10 # int |  (optional) (default to 10)

    try:
        # List the users in the dtool lookup server.
        api_response = api_instance.admin_user_list_get(page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserAdminApi->admin_user_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] [default to 1]
 **page_size** | **int**|  | [optional] [default to 10]

### Return type

[**list[User]**](User.md)

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

# **admin_user_register_post**
> Error admin_user_register_post(register_user)

Register a user in the dtool lookup server.

The user in the Authorization token needs to be admin.

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
    api_instance = dtool_lookup_openapi_client.UserAdminApi(api_client)
    register_user = [dtool_lookup_openapi_client.RegisterUser()] # list[RegisterUser] | 

    try:
        # Register a user in the dtool lookup server.
        api_response = api_instance.admin_user_register_post(register_user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserAdminApi->admin_user_register_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_user** | [**list[RegisterUser]**](RegisterUser.md)|  | 

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

