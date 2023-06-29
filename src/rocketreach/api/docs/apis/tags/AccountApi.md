<a id="__pageTop"></a>
# openapi_client.apis.tags.account_api.AccountApi

All URIs are relative to *https://rocketreach.co/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_read**](#account_read) | **get** /account/ | Retrieve Account

# **account_read**
<a id="account_read"></a>
> UserModel account_read()

Retrieve Account

The account object contains information about your RocketReach account. Visit https://rocketreach.co/account to update this information.

### Example

* Api Key Authentication (RocketReach API Key):
```python
import openapi_client
from openapi_client.apis.tags import account_api
from openapi_client.model.user_model import UserModel
from pprint import pprint
# Defining the host is optional and defaults to https://rocketreach.co/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rocketreach.co/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: RocketReach API Key
configuration.api_key['RocketReach API Key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['RocketReach API Key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve Account
        api_response = api_instance.account_read()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountApi->account_read: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#account_read.ApiResponseFor200) | 

#### account_read.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserModel**](../../models/UserModel.md) |  | 


### Authorization

[RocketReach API Key](../../../README.md#RocketReach API Key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

