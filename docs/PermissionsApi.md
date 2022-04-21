# dtool_lookup_openapi_client.PermissionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_permission_info_post**](PermissionsApi.md#admin_permission_info_post) | **POST** /admin/permission/info | Get information about the permissions on a base URI.
[**admin_permission_update_on_base_uri_post**](PermissionsApi.md#admin_permission_update_on_base_uri_post) | **POST** /admin/permission/update_on_base_uri | Update the permissions on a base URI.


# **admin_permission_info_post**
> UriPermission admin_permission_info_post(base_uri)

Get information about the permissions on a base URI.

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
    api_instance = dtool_lookup_openapi_client.PermissionsApi(api_client)
    base_uri = dtool_lookup_openapi_client.BaseUri() # BaseUri | 

    try:
        # Get information about the permissions on a base URI.
        api_response = api_instance.admin_permission_info_post(base_uri)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PermissionsApi->admin_permission_info_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **base_uri** | [**BaseUri**](BaseUri.md)|  | 

### Return type

[**UriPermission**](UriPermission.md)

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

# **admin_permission_update_on_base_uri_post**
> Error admin_permission_update_on_base_uri_post(uri_permission)

Update the permissions on a base URI.

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
    api_instance = dtool_lookup_openapi_client.PermissionsApi(api_client)
    uri_permission = dtool_lookup_openapi_client.UriPermission() # UriPermission | 

    try:
        # Update the permissions on a base URI.
        api_response = api_instance.admin_permission_update_on_base_uri_post(uri_permission)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PermissionsApi->admin_permission_update_on_base_uri_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri_permission** | [**UriPermission**](UriPermission.md)|  | 

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

