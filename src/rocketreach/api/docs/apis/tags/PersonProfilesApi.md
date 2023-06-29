<a id="__pageTop"></a>
# openapi_client.apis.tags.person_profiles_api.PersonProfilesApi

All URIs are relative to *https://rocketreach.co/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_lookup_create**](#bulk_lookup_create) | **post** /bulkLookup | Bulk People Lookup
[**check_status_list**](#check_status_list) | **get** /checkStatus | Check Person Lookup Status
[**lookup_profile_read**](#lookup_profile_read) | **get** /lookupProfile | Lookup Person
[**person_check_status_list**](#person_check_status_list) | **get** /person/checkStatus | Check Person Lookup Status
[**person_lookup_read**](#person_lookup_read) | **get** /person/lookup | Lookup Person
[**person_search_create**](#person_search_create) | **post** /person/search | Search People
[**profile_company_lookup_read**](#profile_company_lookup_read) | **get** /profile-company/lookup | Lookup Person and Company
[**search_create**](#search_create) | **post** /search | Search People

# **bulk_lookup_create**
<a id="bulk_lookup_create"></a>
> bulk_lookup_create(data)

Bulk People Lookup

This endpoint is suited for large numbers of simultaneous lookups. This endpoint requires for at least one webhook URL enabled for this endpoint, or a webhook ID specified. Up to 100 lookups can be performed per batch.  ## Bulk Lookup Queries Each query in the queries list has the following parameters. For each query, at least one of the following is required: - linkedin_url - profile_id - company and name - email (warning: lower success rate than other options)

### Example

* Api Key Authentication (RocketReach API Key):
```python
import openapi_client
from openapi_client.apis.tags import person_profiles_api
from openapi_client.model.api_bulk_lookup_query import APIBulkLookupQuery
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
    api_instance = person_profiles_api.PersonProfilesApi(api_client)

    # example passing only required values which don't have defaults set
    body = APIBulkLookupQuery(
        queries=[
            ProfileMatch(
                id=1,
                name="name_example",
                current_employer="current_employer_example",
                title="title_example",
                linkedin_ext_url="https://www.linkedin.com/in/benioff",
                linkedin_url="https://www.linkedin.com/in/benioff",
                email="email_example",
                lookup_type="standard",
            )
        ],
        profile_list="API Bulk Lookup",
        webhook_id=1,
    )
    try:
        # Bulk People Lookup
        api_response = api_instance.bulk_lookup_create(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PersonProfilesApi->bulk_lookup_create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APIBulkLookupQuery**](../../models/APIBulkLookupQuery.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#bulk_lookup_create.ApiResponseFor200) | 

#### bulk_lookup_create.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | ResponseHeadersFor200 |  |
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
RR-Request-ID | RRRequestIDSchema | | optional

# RRRequestIDSchema

Bulk lookup unique idenfifier, will also be sent in the header of webhook.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  | Bulk lookup unique idenfifier, will also be sent in the header of webhook. | value must be a uuid


### Authorization

[RocketReach API Key](../../../README.md#RocketReach API Key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **check_status_list**
<a id="check_status_list"></a>
> ProfileAPI check_status_list()

Check Person Lookup Status

**This path is deprecated. Please use /api/v2/person/checkStatus.**  Check the status/progress of a person after they have been looked up.  ## Changing to Webhook Usage  Moving forward, we would like to encourage our API users to work with webhooks instead of the checkStatus endpoint. This way, you will no longer need to poll this endpoint repeatedly, and we can send you the data as it becomes available.  ## Checking the Status of Active Lookups  The /checkStatus API call is used, primarily, to poll the status of active lookups initiated by the /lookupProfile endpoint. When you make a call to /lookupProfile, the response can contain one of the following 5 values: ```response  status:\"complete\" //The search for contact information finished successfully  status:\"failed\" //Search is complete, but there were errors.  status:\"waiting\" //The request is waiting in an internal queue.  status:\"searching\" //The search for contact information is in progress.  status:\"progress\" //In progress, and partial data may be available. ``` ## Example Usage Assume that you made a call to lookup contact info for 'Mark Benioff' and the response was ```response  [     {         \"id\": 5244,         \"status\": \"searching\",         \"name\": \"Mark Benioff\",         \"current_employer\": \"Salesforce\",         \"current_title\": \"CEO\"     }  ] ``` You can now poll the status for this profile by calling: ```bash  curl --request 'POST' --location 'https://api.rocketreach.co/v2/api/search'     --header 'Api-Key: <YOUR API KEY>'     --header 'Content-Type: application/json'     --data '{\"query\":{\"name\":[\"Marc Benioff\"]}}'  ``` Which in turn will initially return: ```response  [     {         \"id\": 5244,         \"status\": \"searching\"     }  ] ``` And after a while... will return status:\"complete\", along with the complete data. ```response [     {         \"id\": 5244,         \"status\": \"complete\",         \"profile_pic\": \"https://images.com/profile_images/....jpeg\",         \"name\": \"Mark Benioff\",         \"links\": [         \"...\"         ]     } ] ```

### Example

* Api Key Authentication (RocketReach API Key):
```python
import openapi_client
from openapi_client.apis.tags import person_profiles_api
from openapi_client.model.profile_api import ProfileAPI
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
    api_instance = person_profiles_api.PersonProfilesApi(api_client)

    # example passing only optional values
    query_params = {
        'ids': [
        1
    ],
    }
    try:
        # Check Person Lookup Status
        api_response = api_instance.check_status_list(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PersonProfilesApi->check_status_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ids | IdsSchema | | optional


# IdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#check_status_list.ApiResponseFor200) | 

#### check_status_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProfileAPI**](../../models/ProfileAPI.md) |  | 


### Authorization

[RocketReach API Key](../../../README.md#RocketReach API Key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **lookup_profile_read**
<a id="lookup_profile_read"></a>
> ProfileAPI lookup_profile_read()

Lookup Person

**This path is deprecated. Please use /api/v2/person/lookup.**  Starts a lookup to retrieve contact information for a prospect(profile). You can identify the profile using parameters like name, current employer, LinkedIn URL, or profile id (returned from search).  The call is pretty straightforward – you provide information about the person you are looking for i.e name, employer etc. and RocketReach searches for a person matching this information.

### Example

* Api Key Authentication (RocketReach API Key):
```python
import openapi_client
from openapi_client.apis.tags import person_profiles_api
from openapi_client.model.profile_api import ProfileAPI
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
    api_instance = person_profiles_api.PersonProfilesApi(api_client)

    # example passing only optional values
    query_params = {
        'id': 1,
        'name': "name_example",
        'current_employer': "current_employer_example",
        'title': "title_example",
        'linkedin_ext_url': "a",
        'linkedin_url': "a",
        'email': "email_example",
        'lookup_type': "standard",
    }
    try:
        # Lookup Person
        api_response = api_instance.lookup_profile_read(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PersonProfilesApi->lookup_profile_read: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | optional
name | NameSchema | | optional
current_employer | CurrentEmployerSchema | | optional
title | TitleSchema | | optional
linkedin_ext_url | LinkedinExtUrlSchema | | optional
linkedin_url | LinkedinUrlSchema | | optional
email | EmailSchema | | optional
lookup_type | LookupTypeSchema | | optional


# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CurrentEmployerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LinkedinExtUrlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LinkedinUrlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EmailSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LookupTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  |  | must be one of ["standard", "premium", "premium (feeds disabled)", "bulk", "phone", "enrich", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#lookup_profile_read.ApiResponseFor200) | 

#### lookup_profile_read.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProfileAPI**](../../models/ProfileAPI.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
RR-Request-ID | RRRequestIDSchema | | optional

# RRRequestIDSchema

Lookup unique identifier, will also be sent in the header of webhook.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  | Lookup unique identifier, will also be sent in the header of webhook. | value must be a uuid


### Authorization

[RocketReach API Key](../../../README.md#RocketReach API Key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **person_check_status_list**
<a id="person_check_status_list"></a>
> ProfileAPI person_check_status_list()

Check Person Lookup Status

Check the status/progress of a person after they have been looked up.  ## Changing to Webhook Usage  Moving forward, we would like to encourage our API users to work with webhooks instead of the checkStatus endpoint. This way, you will no longer need to poll this endpoint repeatedly, and we can send you the data as it becomes available.  ## Checking the Status of Active Lookups  The /checkStatus API call is used, primarily, to poll the status of active lookups initiated by the /lookupProfile endpoint. When you make a call to /lookupProfile, the response can contain one of the following 5 values: ```response  status:\"complete\" //The search for contact information finished successfully  status:\"failed\" //Search is complete, but there were errors.  status:\"waiting\" //The request is waiting in an internal queue.  status:\"searching\" //The search for contact information is in progress.  status:\"progress\" //In progress, and partial data may be available. ``` ## Example Usage Assume that you made a call to lookup contact info for 'Mark Benioff' and the response was ```response  [     {         \"id\": 5244,         \"status\": \"searching\",         \"name\": \"Mark Benioff\",         \"current_employer\": \"Salesforce\",         \"current_title\": \"CEO\"     }  ] ``` You can now poll the status for this profile by calling: ```bash  curl --request 'POST' --location 'https://api.rocketreach.co/v2/api/search'     --header 'Api-Key: <YOUR API KEY>'     --header 'Content-Type: application/json'     --data '{\"query\":{\"name\":[\"Marc Benioff\"]}}'  ``` Which in turn will initially return: ```response  [     {         \"id\": 5244,         \"status\": \"searching\"     }  ] ``` And after a while... will return status:\"complete\", along with the complete data. ```response [     {         \"id\": 5244,         \"status\": \"complete\",         \"profile_pic\": \"https://images.com/profile_images/....jpeg\",         \"name\": \"Mark Benioff\",         \"links\": [         \"...\"         ]     } ] ```

### Example

* Api Key Authentication (RocketReach API Key):
```python
import openapi_client
from openapi_client.apis.tags import person_profiles_api
from openapi_client.model.profile_api import ProfileAPI
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
    api_instance = person_profiles_api.PersonProfilesApi(api_client)

    # example passing only optional values
    query_params = {
        'ids': [
        1
    ],
    }
    try:
        # Check Person Lookup Status
        api_response = api_instance.person_check_status_list(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PersonProfilesApi->person_check_status_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ids | IdsSchema | | optional


# IdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#person_check_status_list.ApiResponseFor200) | 

#### person_check_status_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProfileAPI**](../../models/ProfileAPI.md) |  | 


### Authorization

[RocketReach API Key](../../../README.md#RocketReach API Key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **person_lookup_read**
<a id="person_lookup_read"></a>
> ProfileAPI person_lookup_read()

Lookup Person

Starts a lookup to retrieve contact information for a prospect(profile). You can identify the profile using parameters like name, current employer, LinkedIn URL, or profile id (returned from search).  The call is pretty straightforward – you provide information about the person you are looking for i.e name, employer etc. and RocketReach searches for a person matching this information.

### Example

* Api Key Authentication (RocketReach API Key):
```python
import openapi_client
from openapi_client.apis.tags import person_profiles_api
from openapi_client.model.profile_api import ProfileAPI
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
    api_instance = person_profiles_api.PersonProfilesApi(api_client)

    # example passing only optional values
    query_params = {
        'id': 1,
        'name': "name_example",
        'current_employer': "current_employer_example",
        'title': "title_example",
        'linkedin_ext_url': "a",
        'linkedin_url': "a",
        'email': "email_example",
        'lookup_type': "standard",
    }
    try:
        # Lookup Person
        api_response = api_instance.person_lookup_read(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PersonProfilesApi->person_lookup_read: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | optional
name | NameSchema | | optional
current_employer | CurrentEmployerSchema | | optional
title | TitleSchema | | optional
linkedin_ext_url | LinkedinExtUrlSchema | | optional
linkedin_url | LinkedinUrlSchema | | optional
email | EmailSchema | | optional
lookup_type | LookupTypeSchema | | optional


# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CurrentEmployerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LinkedinExtUrlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LinkedinUrlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EmailSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LookupTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  |  | must be one of ["standard", "premium", "premium (feeds disabled)", "bulk", "phone", "enrich", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#person_lookup_read.ApiResponseFor200) | 

#### person_lookup_read.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProfileAPI**](../../models/ProfileAPI.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
RR-Request-ID | RRRequestIDSchema | | optional

# RRRequestIDSchema

Lookup unique identifier, will also be sent in the header of webhook.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  | Lookup unique identifier, will also be sent in the header of webhook. | value must be a uuid


### Authorization

[RocketReach API Key](../../../README.md#RocketReach API Key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **person_search_create**
<a id="person_search_create"></a>
> [ProfileSearchResult] person_search_create(data)

Search People

The person search endpoint behaves similarly to the search in our UI. When you provide certain keywords, or facets as inputs, this endpoint returns a list of people. The result is always a list of possible matches, without any contact info. You can search by name, keyword, title, company or location, and more. See the full list of search parameters.  ## Retrieving Contact Information for Profiles Contact information is not returned in the result. In order to retrieve contact information for someone in the list, please make a separate call to lookup that person.  A detailed flowchart for this webservice call, is shown below. ![People Search and Lookup Flow](https://static.rocketreach.co/images/api/search_then_lookupProfile.svg \"People Search and Lookup\")  ## Specifying exact matches You can specify exact matches for all your search terms. E.g. The following query matches anyone with 'Marc Benioff' in their name. I.e it will match people named both “Marc Benioff”, “Benioff Marc” and also “Marc Anthony Benioff”. It will also ignore certain typos like “Marck benoiff” etc.  ```bash curl --request 'POST' --location 'https://api.rocketreach.co/v2/api/search'  --header 'Api-Key: <YOUR API KEY>'  --header 'Content-Type: application/json'  --data '{\"query\":{\"name\":[\"Marc Benioff\"]}}' ``` This query exact matches anyone with the exact name 'Marc Benioff'. To specify exact matches, add quotes around your search term  ```bash curl --request 'POST' --location 'https://api.rocketreach.co/v2/api/search'  --header 'Api-Key: <YOUR API KEY>'  --header 'Content-Type: application/json'  --data '{\"query\":{\"name\":[\"\"Marc Benioff\"\"]}}' ```  This approach works for all other parameters that accept strings. E.g. If you wish to exact match people with current employer: “IBM”, you can use the following query. Note that this will exclude people who work e.g. for \"IBM UK\".  ``` curl --request 'POST' --location 'https://api.rocketreach.co/v2/api/search'  --header 'Api-Key: <YOUR API KEY>'  --header 'Content-Type: application/json'  --data '{\"query\":{\"current_employer\":[\"\"IBM\"\"]}}' ```  ## Exclude Search Terms You can omit results matching any of the search terms listed in the table above. Prepend exclude_ before the field name to change the field parameter to exclude all matching documents. In this specific example, we will return the best results that match title: 'Software Engineer' and title: 'Software Developer' but not title: 'Senior' or title: 'Sr'.  Basically, this should match Software Engineers and Software Developers that don't have senior anywhere in their job title. ```bash curl --request 'POST' --location 'https://api.rocketreach.co/v2/api/search'  --header 'Api-Key: <YOUR API KEY>'  --header 'Content-Type: application/json'  --data '{\"query\":{\"current_title\":[\"Software Engineer\"],\"exclude_current_title\":[\"Senior\",\"Sr\"]}}' ```  ## Numbers with Operators Some fields, such as company_funding, take strings which are numbers with mathematical operators. For example, here are some valid values: - \"1000000+\" - \"<90000000\" - \"1000000>=\" - \"1000000-90000000\"  ## Normalized Titles A query should specify at most one of `current_title` and `normalized_title`. Normalized titles are a relatively new feature. They are intended to reduce the space of titles in a reliable way. As of 2022-04-21, half of person profiles have normalized titles. The full list of current normalized titles is available [here](https://static.rocketreach.co/job-titles/normalized_titles_display_names.txt). A normalized title must be specified exactly (see below) and will always be matched exactly.  ## US Diversity Fields US Diversity fields may be used only in addition to other fields for searches. To gain access to US diversity fields please contact sales.  ## Location With Radius With the location parameter, you can add a radius at the end of the location string, prepended by ::~. Here are a couple examples: - `\"location\": [\"\"San Francisco\"::~50mi\"]` - metric is also supported: `\"location\": [\"\"San Francisco\"::~50km\"]`  ## Ordering - `relevance`: return results most closely matching the search query. - `popularity`: decision makers, executives and managers matching the search criteria are closer to the top of the search results.

### Example

* Api Key Authentication (RocketReach API Key):
```python
import openapi_client
from openapi_client.apis.tags import person_profiles_api
from openapi_client.model.api_search_input import APISearchInput
from openapi_client.model.profile_search_result import ProfileSearchResult
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
    api_instance = person_profiles_api.PersonProfilesApi(api_client)

    # example passing only required values which don't have defaults set
    body = APISearchInput(
        start=1,
        page_size=1,
        query=PersonQuery(
            keyword=[
                "keyword_example"
            ],
            exclude_keyword=[
                "exclude_keyword_example"
            ],
            company_naics_code=[
                "company_naics_code_example"
            ],
            exclude_company_naics_code=[
                "exclude_company_naics_code_example"
            ],
            name=[
                "name_example"
            ],
            exclude_name=[
                "exclude_name_example"
            ],
            company_postal_code=[
                "company_postal_code_example"
            ],
            exclude_company_postal_code=[
                "exclude_company_postal_code_example"
            ],
            city=[
                "city_example"
            ],
            exclude_city=[
                "exclude_city_example"
            ],
            previous_employer=[
                "previous_employer_example"
            ],
            exclude_previous_employer=[
                "exclude_previous_employer_example"
            ],
            handle=[
                "handle_example"
            ],
            exclude_handle=[
                "exclude_handle_example"
            ],
            industry_tags=[
                "industry_tags_example"
            ],
            exclude_industry_tags=[
                "exclude_industry_tags_example"
            ],
            company_revenue_max=[
                "company_revenue_max_example"
            ],
            exclude_company_revenue_max=[
                "exclude_company_revenue_max_example"
            ],
            sic_code=[
                "sic_code_example"
            ],
            exclude_sic_code=[
                "exclude_sic_code_example"
            ],
            company_industry=[
                "company_industry_example"
            ],
            exclude_company_industry=[
                "exclude_company_industry_example"
            ],
            postal_code=[
                "postal_code_example"
            ],
            exclude_postal_code=[
                "exclude_postal_code_example"
            ],
            company_size_min=[
                "company_size_min_example"
            ],
            exclude_company_size_min=[
                "exclude_company_size_min_example"
            ],
            management_levels=[
                "management_levels_example"
            ],
            exclude_management_levels=[
                "exclude_management_levels_example"
            ],
            company_list_id=[
                "company_list_id_example"
            ],
            exclude_company_list_id=[
                "exclude_company_list_id_example"
            ],
            phone=[
                "phone_example"
            ],
            exclude_phone=[
                "exclude_phone_example"
            ],
            company_revenue=[
                "company_revenue_example"
            ],
            exclude_company_revenue=[
                "exclude_company_revenue_example"
            ],
            company_funding_max=[
                "company_funding_max_example"
            ],
            exclude_company_funding_max=[
                "exclude_company_funding_max_example"
            ],
            company_website_url=[
                "company_website_url_example"
            ],
            exclude_company_website_url=[
                "exclude_company_website_url_example"
            ],
            keywords=[
                "keywords_example"
            ],
            exclude_keywords=[
                "exclude_keywords_example"
            ],
            insight=[
                "insight_example"
            ],
            exclude_insight=[
                "exclude_insight_example"
            ],
            veteran_status=[
                "veteran_status_example"
            ],
            exclude_veteran_status=[
                "exclude_veteran_status_example"
            ],
            company_website_rank_min=[
                "company_website_rank_min_example"
            ],
            exclude_company_website_rank_min=[
                "exclude_company_website_rank_min_example"
            ],
            simplified_keyword=[
                "simplified_keyword_example"
            ],
            exclude_simplified_keyword=[
                "exclude_simplified_keyword_example"
            ],
            link=[
                "link_example"
            ],
            exclude_link=[
                "exclude_link_example"
            ],
            company_id=[
                "company_id_example"
            ],
            exclude_company_id=[
                "exclude_company_id_example"
            ],
            company_name=[
                "company_name_example"
            ],
            exclude_company_name=[
                "exclude_company_name_example"
            ],
            company_industry_tags=[
                "company_industry_tags_example"
            ],
            exclude_company_industry_tags=[
                "exclude_company_industry_tags_example"
            ],
            techstack=[
                "techstack_example"
            ],
            exclude_techstack=[
                "exclude_techstack_example"
            ],
            is_primary=[
                "is_primary_example"
            ],
            exclude_is_primary=[
                "exclude_is_primary_example"
            ],
            birth_year=[
                "birth_year_example"
            ],
            exclude_birth_year=[
                "exclude_birth_year_example"
            ],
            keyword_orig=[
                "keyword_orig_example"
            ],
            exclude_keyword_orig=[
                "exclude_keyword_orig_example"
            ],
            growth=[
                "growth_example"
            ],
            exclude_growth=[
                "exclude_growth_example"
            ],
            email=[
                "email_example"
            ],
            exclude_email=[
                "exclude_email_example"
            ],
            ethnicity=[
                "ethnicity_example"
            ],
            exclude_ethnicity=[
                "exclude_ethnicity_example"
            ],
            company_website_rank_max=[
                "company_website_rank_max_example"
            ],
            exclude_company_website_rank_max=[
                "exclude_company_website_rank_max_example"
            ],
            extended_keyword=[
                "extended_keyword_example"
            ],
            exclude_extended_keyword=[
                "exclude_extended_keyword_example"
            ],
            employees=[
                "employees_example"
            ],
            exclude_employees=[
                "exclude_employees_example"
            ],
            company_publicly_traded=[
                "company_publicly_traded_example"
            ],
            exclude_company_publicly_traded=[
                "exclude_company_publicly_traded_example"
            ],
            sic_codes=[
                "sic_codes_example"
            ],
            exclude_sic_codes=[
                "exclude_sic_codes_example"
            ],
            location=[
                "location_example"
            ],
            exclude_location=[
                "exclude_location_example"
            ],
            company_email=[
                "company_email_example"
            ],
            exclude_company_email=[
                "exclude_company_email_example"
            ],
            naics_code=[
                "naics_code_example"
            ],
            exclude_naics_code=[
                "exclude_naics_code_example"
            ],
            degree=[
                "degree_example"
            ],
            exclude_degree=[
                "exclude_degree_example"
            ],
            years_experience=[
                "years_experience_example"
            ],
            exclude_years_experience=[
                "exclude_years_experience_example"
            ],
            country=[
                "country_example"
            ],
            exclude_country=[
                "exclude_country_example"
            ],
            company_size_max=[
                "company_size_max_example"
            ],
            exclude_company_size_max=[
                "exclude_company_size_max_example"
            ],
            current_title=[
                "current_title_example"
            ],
            exclude_current_title=[
                "exclude_current_title_example"
            ],
            department=[
                "department_example"
            ],
            exclude_department=[
                "exclude_department_example"
            ],
            all_industries=[
                "all_industries_example"
            ],
            exclude_all_industries=[
                "exclude_all_industries_example"
            ],
            keyword_enhanced=[
                "keyword_enhanced_example"
            ],
            exclude_keyword_enhanced=[
                "exclude_keyword_enhanced_example"
            ],
            company_city=[
                "company_city_example"
            ],
            exclude_company_city=[
                "exclude_company_city_example"
            ],
            company_revenue_min=[
                "company_revenue_min_example"
            ],
            exclude_company_revenue_min=[
                "exclude_company_revenue_min_example"
            ],
            total_funding=[
                "total_funding_example"
            ],
            exclude_total_funding=[
                "exclude_total_funding_example"
            ],
            company_website_rank=[
                "company_website_rank_example"
            ],
            exclude_company_website_rank=[
                "exclude_company_website_rank_example"
            ],
            description=[
                "description_example"
            ],
            exclude_description=[
                "exclude_description_example"
            ],
            job_change_range_days=[
                "job_change_range_days_example"
            ],
            exclude_job_change_range_days=[
                "exclude_job_change_range_days_example"
            ],
            primary_industry=[
                "primary_industry_example"
            ],
            exclude_primary_industry=[
                "exclude_primary_industry_example"
            ],
            website_url=[
                "website_url_example"
            ],
            exclude_website_url=[
                "exclude_website_url_example"
            ],
            company_country_code=[
                "company_country_code_example"
            ],
            exclude_company_country_code=[
                "exclude_company_country_code_example"
            ],
            domain=[
                "domain_example"
            ],
            exclude_domain=[
                "exclude_domain_example"
            ],
            email_domain=[
                "email_domain_example"
            ],
            exclude_email_domain=[
                "exclude_email_domain_example"
            ],
            gender=[
                "gender_example"
            ],
            exclude_gender=[
                "exclude_gender_example"
            ],
            company_sic_code=[
                "company_sic_code_example"
            ],
            exclude_company_sic_code=[
                "exclude_company_sic_code_example"
            ],
            naics_codes=[
                "naics_codes_example"
            ],
            exclude_naics_codes=[
                "exclude_naics_codes_example"
            ],
            company_size=[
                "company_size_example"
            ],
            exclude_company_size=[
                "exclude_company_size_example"
            ],
            normalized_title=[
                "normalized_title_example"
            ],
            exclude_normalized_title=[
                "exclude_normalized_title_example"
            ],
            connections=[
                "connections_example"
            ],
            exclude_connections=[
                "exclude_connections_example"
            ],
            major=[
                "major_example"
            ],
            exclude_major=[
                "exclude_major_example"
            ],
            company_list=[
                "company_list_example"
            ],
            exclude_company_list=[
                "exclude_company_list_example"
            ],
            geo=[
                "geo_example"
            ],
            exclude_geo=[
                "exclude_geo_example"
            ],
            previous_company_id=[
                "previous_company_id_example"
            ],
            exclude_previous_company_id=[
                "exclude_previous_company_id_example"
            ],
            state=[
                "state_example"
            ],
            exclude_state=[
                "exclude_state_example"
            ],
            skills=[
                "skills_example"
            ],
            exclude_skills=[
                "exclude_skills_example"
            ],
            company_domain=[
                "company_domain_example"
            ],
            exclude_company_domain=[
                "exclude_company_domain_example"
            ],
            company_region=[
                "company_region_example"
            ],
            exclude_company_region=[
                "exclude_company_region_example"
            ],
            company_website_category=[
                "company_website_category_example"
            ],
            exclude_company_website_category=[
                "exclude_company_website_category_example"
            ],
            industry=[
                "industry_example"
            ],
            exclude_industry=[
                "exclude_industry_example"
            ],
            publicly_traded=[
                "publicly_traded_example"
            ],
            exclude_publicly_traded=[
                "exclude_publicly_traded_example"
            ],
            revenue=[
                "revenue_example"
            ],
            exclude_revenue=[
                "exclude_revenue_example"
            ],
            id=[
                "id_example"
            ],
            exclude_id=[
                "exclude_id_example"
            ],
            current_employer=[
                "current_employer_example"
            ],
            exclude_current_employer=[
                "exclude_current_employer_example"
            ],
            company_funding_min=[
                "company_funding_min_example"
            ],
            exclude_company_funding_min=[
                "exclude_company_funding_min_example"
            ],
            employer=[
                "employer_example"
            ],
            exclude_employer=[
                "exclude_employer_example"
            ],
            website_category=[
                "website_category_example"
            ],
            exclude_website_category=[
                "exclude_website_category_example"
            ],
            school=[
                "school_example"
            ],
            exclude_school=[
                "exclude_school_example"
            ],
        ),
        order_by="relevance",
    )
    try:
        # Search People
        api_response = api_instance.person_search_create(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PersonProfilesApi->person_search_create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APISearchInput**](../../models/APISearchInput.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#person_search_create.ApiResponseFor201) | 

#### person_search_create.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProfileSearchResult**]({{complexTypePrefix}}ProfileSearchResult.md) | [**ProfileSearchResult**]({{complexTypePrefix}}ProfileSearchResult.md) | [**ProfileSearchResult**]({{complexTypePrefix}}ProfileSearchResult.md) |  | 

### Authorization

[RocketReach API Key](../../../README.md#RocketReach API Key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **profile_company_lookup_read**
<a id="profile_company_lookup_read"></a>
> ProfileAPISerializerWithCompany profile_company_lookup_read()

Lookup Person and Company

Starts a lookup to retrieve contact information for a prospect(profile) and any associated company data. You can identify the profile using parameters like name, current employer, LinkedIn URL, or profile id (returned from search).  The call is pretty straightforward – you provide information about the person you are looking for i.e name, employer etc. and RocketReach searches for a person matching this information along with any matching company data.

### Example

* Api Key Authentication (RocketReach API Key):
```python
import openapi_client
from openapi_client.apis.tags import person_profiles_api
from openapi_client.model.profile_api_serializer_with_company import ProfileAPISerializerWithCompany
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
    api_instance = person_profiles_api.PersonProfilesApi(api_client)

    # example passing only optional values
    query_params = {
        'id': 1,
        'name': "name_example",
        'current_employer': "current_employer_example",
        'title': "title_example",
        'linkedin_ext_url': "a",
        'linkedin_url': "a",
        'email': "email_example",
        'lookup_type': "standard",
    }
    try:
        # Lookup Person and Company
        api_response = api_instance.profile_company_lookup_read(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PersonProfilesApi->profile_company_lookup_read: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
id | IdSchema | | optional
name | NameSchema | | optional
current_employer | CurrentEmployerSchema | | optional
title | TitleSchema | | optional
linkedin_ext_url | LinkedinExtUrlSchema | | optional
linkedin_url | LinkedinUrlSchema | | optional
email | EmailSchema | | optional
lookup_type | LookupTypeSchema | | optional


# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CurrentEmployerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TitleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LinkedinExtUrlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LinkedinUrlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EmailSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LookupTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  |  | must be one of ["standard", "premium", "premium (feeds disabled)", "bulk", "phone", "enrich", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#profile_company_lookup_read.ApiResponseFor200) | 

#### profile_company_lookup_read.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ProfileAPISerializerWithCompany**](../../models/ProfileAPISerializerWithCompany.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
RR-Request-ID | RRRequestIDSchema | | optional

# RRRequestIDSchema

Lookup unique identifier, will also be sent in the header of webhook.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, uuid.UUID,  | str,  | Lookup unique identifier, will also be sent in the header of webhook. | value must be a uuid


### Authorization

[RocketReach API Key](../../../README.md#RocketReach API Key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_create**
<a id="search_create"></a>
> [ProfileSearchResult] search_create(data)

Search People

**This path is deprecated. Please use /api/v2/person/search.**  The person search endpoint behaves similarly to the search in our UI. When you provide certain keywords, or facets as inputs, this endpoint returns a list of people. The result is always a list of possible matches, without any contact info. You can search by name, keyword, title, company or location, and more. See the full list of search parameters.  ## Retrieving Contact Information for Profiles Contact information is not returned in the result. In order to retrieve contact information for someone in the list, please make a separate call to lookup that person.  A detailed flowchart for this webservice call, is shown below. ![People Search and Lookup Flow](https://static.rocketreach.co/images/api/search_then_lookupProfile.svg \"People Search and Lookup\")  ## Specifying exact matches You can specify exact matches for all your search terms. E.g. The following query matches anyone with 'Marc Benioff' in their name. I.e it will match people named both “Marc Benioff”, “Benioff Marc” and also “Marc Anthony Benioff”. It will also ignore certain typos like “Marck benoiff” etc.  ```bash curl --request 'POST' --location 'https://api.rocketreach.co/v2/api/search'  --header 'Api-Key: <YOUR API KEY>'  --header 'Content-Type: application/json'  --data '{\"query\":{\"name\":[\"Marc Benioff\"]}}' ``` This query exact matches anyone with the exact name 'Marc Benioff'. To specify exact matches, add quotes around your search term  ```bash curl --request 'POST' --location 'https://api.rocketreach.co/v2/api/search'  --header 'Api-Key: <YOUR API KEY>'  --header 'Content-Type: application/json'  --data '{\"query\":{\"name\":[\"\"Marc Benioff\"\"]}}' ```  This approach works for all other parameters that accept strings. E.g. If you wish to exact match people with current employer: “IBM”, you can use the following query. Note that this will exclude people who work e.g. for \"IBM UK\".  ``` curl --request 'POST' --location 'https://api.rocketreach.co/v2/api/search'  --header 'Api-Key: <YOUR API KEY>'  --header 'Content-Type: application/json'  --data '{\"query\":{\"current_employer\":[\"\"IBM\"\"]}}' ```  ## Exclude Search Terms You can omit results matching any of the search terms listed in the table above. Prepend exclude_ before the field name to change the field parameter to exclude all matching documents. In this specific example, we will return the best results that match title: 'Software Engineer' and title: 'Software Developer' but not title: 'Senior' or title: 'Sr'.  Basically, this should match Software Engineers and Software Developers that don't have senior anywhere in their job title. ```bash curl --request 'POST' --location 'https://api.rocketreach.co/v2/api/search'  --header 'Api-Key: <YOUR API KEY>'  --header 'Content-Type: application/json'  --data '{\"query\":{\"current_title\":[\"Software Engineer\"],\"exclude_current_title\":[\"Senior\",\"Sr\"]}}' ```  ## Numbers with Operators Some fields, such as company_funding, take strings which are numbers with mathematical operators. For example, here are some valid values: - \"1000000+\" - \"<90000000\" - \"1000000>=\" - \"1000000-90000000\"  ## Normalized Titles A query should specify at most one of `current_title` and `normalized_title`. Normalized titles are a relatively new feature. They are intended to reduce the space of titles in a reliable way. As of 2022-04-21, half of person profiles have normalized titles. The full list of current normalized titles is available [here](https://static.rocketreach.co/job-titles/normalized_titles_display_names.txt). A normalized title must be specified exactly (see below) and will always be matched exactly.  ## US Diversity Fields US Diversity fields may be used only in addition to other fields for searches. To gain access to US diversity fields please contact sales.  ## Location With Radius With the location parameter, you can add a radius at the end of the location string, prepended by ::~. Here are a couple examples: - `\"location\": [\"\"San Francisco\"::~50mi\"]` - metric is also supported: `\"location\": [\"\"San Francisco\"::~50km\"]`  ## Ordering - `relevance`: return results most closely matching the search query. - `popularity`: decision makers, executives and managers matching the search criteria are closer to the top of the search results.

### Example

* Api Key Authentication (RocketReach API Key):
```python
import openapi_client
from openapi_client.apis.tags import person_profiles_api
from openapi_client.model.api_search_input import APISearchInput
from openapi_client.model.profile_search_result import ProfileSearchResult
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
    api_instance = person_profiles_api.PersonProfilesApi(api_client)

    # example passing only required values which don't have defaults set
    body = APISearchInput(
        start=1,
        page_size=1,
        query=PersonQuery(
            keyword=[
                "keyword_example"
            ],
            exclude_keyword=[
                "exclude_keyword_example"
            ],
            company_naics_code=[
                "company_naics_code_example"
            ],
            exclude_company_naics_code=[
                "exclude_company_naics_code_example"
            ],
            name=[
                "name_example"
            ],
            exclude_name=[
                "exclude_name_example"
            ],
            company_postal_code=[
                "company_postal_code_example"
            ],
            exclude_company_postal_code=[
                "exclude_company_postal_code_example"
            ],
            city=[
                "city_example"
            ],
            exclude_city=[
                "exclude_city_example"
            ],
            previous_employer=[
                "previous_employer_example"
            ],
            exclude_previous_employer=[
                "exclude_previous_employer_example"
            ],
            handle=[
                "handle_example"
            ],
            exclude_handle=[
                "exclude_handle_example"
            ],
            industry_tags=[
                "industry_tags_example"
            ],
            exclude_industry_tags=[
                "exclude_industry_tags_example"
            ],
            company_revenue_max=[
                "company_revenue_max_example"
            ],
            exclude_company_revenue_max=[
                "exclude_company_revenue_max_example"
            ],
            sic_code=[
                "sic_code_example"
            ],
            exclude_sic_code=[
                "exclude_sic_code_example"
            ],
            company_industry=[
                "company_industry_example"
            ],
            exclude_company_industry=[
                "exclude_company_industry_example"
            ],
            postal_code=[
                "postal_code_example"
            ],
            exclude_postal_code=[
                "exclude_postal_code_example"
            ],
            company_size_min=[
                "company_size_min_example"
            ],
            exclude_company_size_min=[
                "exclude_company_size_min_example"
            ],
            management_levels=[
                "management_levels_example"
            ],
            exclude_management_levels=[
                "exclude_management_levels_example"
            ],
            company_list_id=[
                "company_list_id_example"
            ],
            exclude_company_list_id=[
                "exclude_company_list_id_example"
            ],
            phone=[
                "phone_example"
            ],
            exclude_phone=[
                "exclude_phone_example"
            ],
            company_revenue=[
                "company_revenue_example"
            ],
            exclude_company_revenue=[
                "exclude_company_revenue_example"
            ],
            company_funding_max=[
                "company_funding_max_example"
            ],
            exclude_company_funding_max=[
                "exclude_company_funding_max_example"
            ],
            company_website_url=[
                "company_website_url_example"
            ],
            exclude_company_website_url=[
                "exclude_company_website_url_example"
            ],
            keywords=[
                "keywords_example"
            ],
            exclude_keywords=[
                "exclude_keywords_example"
            ],
            insight=[
                "insight_example"
            ],
            exclude_insight=[
                "exclude_insight_example"
            ],
            veteran_status=[
                "veteran_status_example"
            ],
            exclude_veteran_status=[
                "exclude_veteran_status_example"
            ],
            company_website_rank_min=[
                "company_website_rank_min_example"
            ],
            exclude_company_website_rank_min=[
                "exclude_company_website_rank_min_example"
            ],
            simplified_keyword=[
                "simplified_keyword_example"
            ],
            exclude_simplified_keyword=[
                "exclude_simplified_keyword_example"
            ],
            link=[
                "link_example"
            ],
            exclude_link=[
                "exclude_link_example"
            ],
            company_id=[
                "company_id_example"
            ],
            exclude_company_id=[
                "exclude_company_id_example"
            ],
            company_name=[
                "company_name_example"
            ],
            exclude_company_name=[
                "exclude_company_name_example"
            ],
            company_industry_tags=[
                "company_industry_tags_example"
            ],
            exclude_company_industry_tags=[
                "exclude_company_industry_tags_example"
            ],
            techstack=[
                "techstack_example"
            ],
            exclude_techstack=[
                "exclude_techstack_example"
            ],
            is_primary=[
                "is_primary_example"
            ],
            exclude_is_primary=[
                "exclude_is_primary_example"
            ],
            birth_year=[
                "birth_year_example"
            ],
            exclude_birth_year=[
                "exclude_birth_year_example"
            ],
            keyword_orig=[
                "keyword_orig_example"
            ],
            exclude_keyword_orig=[
                "exclude_keyword_orig_example"
            ],
            growth=[
                "growth_example"
            ],
            exclude_growth=[
                "exclude_growth_example"
            ],
            email=[
                "email_example"
            ],
            exclude_email=[
                "exclude_email_example"
            ],
            ethnicity=[
                "ethnicity_example"
            ],
            exclude_ethnicity=[
                "exclude_ethnicity_example"
            ],
            company_website_rank_max=[
                "company_website_rank_max_example"
            ],
            exclude_company_website_rank_max=[
                "exclude_company_website_rank_max_example"
            ],
            extended_keyword=[
                "extended_keyword_example"
            ],
            exclude_extended_keyword=[
                "exclude_extended_keyword_example"
            ],
            employees=[
                "employees_example"
            ],
            exclude_employees=[
                "exclude_employees_example"
            ],
            company_publicly_traded=[
                "company_publicly_traded_example"
            ],
            exclude_company_publicly_traded=[
                "exclude_company_publicly_traded_example"
            ],
            sic_codes=[
                "sic_codes_example"
            ],
            exclude_sic_codes=[
                "exclude_sic_codes_example"
            ],
            location=[
                "location_example"
            ],
            exclude_location=[
                "exclude_location_example"
            ],
            company_email=[
                "company_email_example"
            ],
            exclude_company_email=[
                "exclude_company_email_example"
            ],
            naics_code=[
                "naics_code_example"
            ],
            exclude_naics_code=[
                "exclude_naics_code_example"
            ],
            degree=[
                "degree_example"
            ],
            exclude_degree=[
                "exclude_degree_example"
            ],
            years_experience=[
                "years_experience_example"
            ],
            exclude_years_experience=[
                "exclude_years_experience_example"
            ],
            country=[
                "country_example"
            ],
            exclude_country=[
                "exclude_country_example"
            ],
            company_size_max=[
                "company_size_max_example"
            ],
            exclude_company_size_max=[
                "exclude_company_size_max_example"
            ],
            current_title=[
                "current_title_example"
            ],
            exclude_current_title=[
                "exclude_current_title_example"
            ],
            department=[
                "department_example"
            ],
            exclude_department=[
                "exclude_department_example"
            ],
            all_industries=[
                "all_industries_example"
            ],
            exclude_all_industries=[
                "exclude_all_industries_example"
            ],
            keyword_enhanced=[
                "keyword_enhanced_example"
            ],
            exclude_keyword_enhanced=[
                "exclude_keyword_enhanced_example"
            ],
            company_city=[
                "company_city_example"
            ],
            exclude_company_city=[
                "exclude_company_city_example"
            ],
            company_revenue_min=[
                "company_revenue_min_example"
            ],
            exclude_company_revenue_min=[
                "exclude_company_revenue_min_example"
            ],
            total_funding=[
                "total_funding_example"
            ],
            exclude_total_funding=[
                "exclude_total_funding_example"
            ],
            company_website_rank=[
                "company_website_rank_example"
            ],
            exclude_company_website_rank=[
                "exclude_company_website_rank_example"
            ],
            description=[
                "description_example"
            ],
            exclude_description=[
                "exclude_description_example"
            ],
            job_change_range_days=[
                "job_change_range_days_example"
            ],
            exclude_job_change_range_days=[
                "exclude_job_change_range_days_example"
            ],
            primary_industry=[
                "primary_industry_example"
            ],
            exclude_primary_industry=[
                "exclude_primary_industry_example"
            ],
            website_url=[
                "website_url_example"
            ],
            exclude_website_url=[
                "exclude_website_url_example"
            ],
            company_country_code=[
                "company_country_code_example"
            ],
            exclude_company_country_code=[
                "exclude_company_country_code_example"
            ],
            domain=[
                "domain_example"
            ],
            exclude_domain=[
                "exclude_domain_example"
            ],
            email_domain=[
                "email_domain_example"
            ],
            exclude_email_domain=[
                "exclude_email_domain_example"
            ],
            gender=[
                "gender_example"
            ],
            exclude_gender=[
                "exclude_gender_example"
            ],
            company_sic_code=[
                "company_sic_code_example"
            ],
            exclude_company_sic_code=[
                "exclude_company_sic_code_example"
            ],
            naics_codes=[
                "naics_codes_example"
            ],
            exclude_naics_codes=[
                "exclude_naics_codes_example"
            ],
            company_size=[
                "company_size_example"
            ],
            exclude_company_size=[
                "exclude_company_size_example"
            ],
            normalized_title=[
                "normalized_title_example"
            ],
            exclude_normalized_title=[
                "exclude_normalized_title_example"
            ],
            connections=[
                "connections_example"
            ],
            exclude_connections=[
                "exclude_connections_example"
            ],
            major=[
                "major_example"
            ],
            exclude_major=[
                "exclude_major_example"
            ],
            company_list=[
                "company_list_example"
            ],
            exclude_company_list=[
                "exclude_company_list_example"
            ],
            geo=[
                "geo_example"
            ],
            exclude_geo=[
                "exclude_geo_example"
            ],
            previous_company_id=[
                "previous_company_id_example"
            ],
            exclude_previous_company_id=[
                "exclude_previous_company_id_example"
            ],
            state=[
                "state_example"
            ],
            exclude_state=[
                "exclude_state_example"
            ],
            skills=[
                "skills_example"
            ],
            exclude_skills=[
                "exclude_skills_example"
            ],
            company_domain=[
                "company_domain_example"
            ],
            exclude_company_domain=[
                "exclude_company_domain_example"
            ],
            company_region=[
                "company_region_example"
            ],
            exclude_company_region=[
                "exclude_company_region_example"
            ],
            company_website_category=[
                "company_website_category_example"
            ],
            exclude_company_website_category=[
                "exclude_company_website_category_example"
            ],
            industry=[
                "industry_example"
            ],
            exclude_industry=[
                "exclude_industry_example"
            ],
            publicly_traded=[
                "publicly_traded_example"
            ],
            exclude_publicly_traded=[
                "exclude_publicly_traded_example"
            ],
            revenue=[
                "revenue_example"
            ],
            exclude_revenue=[
                "exclude_revenue_example"
            ],
            id=[
                "id_example"
            ],
            exclude_id=[
                "exclude_id_example"
            ],
            current_employer=[
                "current_employer_example"
            ],
            exclude_current_employer=[
                "exclude_current_employer_example"
            ],
            company_funding_min=[
                "company_funding_min_example"
            ],
            exclude_company_funding_min=[
                "exclude_company_funding_min_example"
            ],
            employer=[
                "employer_example"
            ],
            exclude_employer=[
                "exclude_employer_example"
            ],
            website_category=[
                "website_category_example"
            ],
            exclude_website_category=[
                "exclude_website_category_example"
            ],
            school=[
                "school_example"
            ],
            exclude_school=[
                "exclude_school_example"
            ],
        ),
        order_by="relevance",
    )
    try:
        # Search People
        api_response = api_instance.search_create(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PersonProfilesApi->search_create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**APISearchInput**](../../models/APISearchInput.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#search_create.ApiResponseFor201) | 

#### search_create.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProfileSearchResult**]({{complexTypePrefix}}ProfileSearchResult.md) | [**ProfileSearchResult**]({{complexTypePrefix}}ProfileSearchResult.md) | [**ProfileSearchResult**]({{complexTypePrefix}}ProfileSearchResult.md) |  | 

### Authorization

[RocketReach API Key](../../../README.md#RocketReach API Key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

