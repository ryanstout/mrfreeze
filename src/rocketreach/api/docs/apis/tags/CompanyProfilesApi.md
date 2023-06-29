<a id="__pageTop"></a>
# openapi_client.apis.tags.company_profiles_api.CompanyProfilesApi

All URIs are relative to *https://rocketreach.co/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**company_lookup_read**](#company_lookup_read) | **get** /company/lookup/ | Lookup Company Information
[**lookup_company_read**](#lookup_company_read) | **get** /lookupCompany | Lookup Company Information
[**profile_company_lookup_read**](#profile_company_lookup_read) | **get** /profile-company/lookup | Lookup Person and Company
[**search_company_create**](#search_company_create) | **post** /searchCompany | Search Companies

# **company_lookup_read**
<a id="company_lookup_read"></a>
> CompanyAPI company_lookup_read()

Lookup Company Information

Retrieves metadata information for an account(company). You can identify the company using domain, name, or LinkedIn URL. Provide information about the company you are looking for and RocketReach searches for a company matching that information.  Company exports are required for this endpoint. Talk to sales@rocketreach.co to purchase access.

### Example

* Api Key Authentication (RocketReach API Key):
```python
import openapi_client
from openapi_client.apis.tags import company_profiles_api
from openapi_client.model.company_api import CompanyAPI
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
    api_instance = company_profiles_api.CompanyProfilesApi(api_client)

    # example passing only optional values
    query_params = {
        'id': 1,
        'name': "name_example",
        'domain': "domain_example",
        'ticker': "ticker_example",
        'linkedin_url': "a",
    }
    try:
        # Lookup Company Information
        api_response = api_instance.company_lookup_read(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CompanyProfilesApi->company_lookup_read: %s\n" % e)
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
domain | DomainSchema | | optional
ticker | TickerSchema | | optional
linkedin_url | LinkedinUrlSchema | | optional


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

# DomainSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TickerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LinkedinUrlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#company_lookup_read.ApiResponseFor200) | 

#### company_lookup_read.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CompanyAPI**](../../models/CompanyAPI.md) |  | 


### Authorization

[RocketReach API Key](../../../README.md#RocketReach API Key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **lookup_company_read**
<a id="lookup_company_read"></a>
> CompanyAPI lookup_company_read()

Lookup Company Information

**This path is deprecated. Please use /api/v2/company/lookup.**  Retrieves metadata information for an account(company). You can identify the company using domain, name, or LinkedIn URL. Provide information about the company you are looking for and RocketReach searches for a company matching that information.  Company exports are required for this endpoint. Talk to sales@rocketreach.co to purchase access.

### Example

* Api Key Authentication (RocketReach API Key):
```python
import openapi_client
from openapi_client.apis.tags import company_profiles_api
from openapi_client.model.company_api import CompanyAPI
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
    api_instance = company_profiles_api.CompanyProfilesApi(api_client)

    # example passing only optional values
    query_params = {
        'id': 1,
        'name': "name_example",
        'domain': "domain_example",
        'ticker': "ticker_example",
        'linkedin_url': "a",
    }
    try:
        # Lookup Company Information
        api_response = api_instance.lookup_company_read(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CompanyProfilesApi->lookup_company_read: %s\n" % e)
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
domain | DomainSchema | | optional
ticker | TickerSchema | | optional
linkedin_url | LinkedinUrlSchema | | optional


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

# DomainSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TickerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LinkedinUrlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#lookup_company_read.ApiResponseFor200) | 

#### lookup_company_read.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CompanyAPI**](../../models/CompanyAPI.md) |  | 


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
from openapi_client.apis.tags import company_profiles_api
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
    api_instance = company_profiles_api.CompanyProfilesApi(api_client)

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
        print("Exception when calling CompanyProfilesApi->profile_company_lookup_read: %s\n" % e)
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

# **search_company_create**
<a id="search_company_create"></a>
> [CompanyPublicDetails] search_company_create(data)

Search Companies

Find companies based on certain criteria. This endpoint operates similarly to the search API for people. Once companies matching criteria have been found, you can lookup more details on that company using the Company Lookup API.

### Example

* Api Key Authentication (RocketReach API Key):
```python
import openapi_client
from openapi_client.apis.tags import company_profiles_api
from openapi_client.model.api_public_company_search_input import APIPublicCompanySearchInput
from openapi_client.model.company_public_details import CompanyPublicDetails
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
    api_instance = company_profiles_api.CompanyProfilesApi(api_client)

    # example passing only required values which don't have defaults set
    body = APIPublicCompanySearchInput(
        start=1,
        page_size=1,
        query=CompanyQuery(
            keyword=[
                "keyword_example"
            ],
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
,
        ),
        order_by="relevance",
    )
    try:
        # Search Companies
        api_response = api_instance.search_company_create(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CompanyProfilesApi->search_company_create: %s\n" % e)
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
[**APIPublicCompanySearchInput**](../../models/APIPublicCompanySearchInput.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#search_company_create.ApiResponseFor201) | 

#### search_company_create.ApiResponseFor201
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
[**CompanyPublicDetails**]({{complexTypePrefix}}CompanyPublicDetails.md) | [**CompanyPublicDetails**]({{complexTypePrefix}}CompanyPublicDetails.md) | [**CompanyPublicDetails**]({{complexTypePrefix}}CompanyPublicDetails.md) |  | 

### Authorization

[RocketReach API Key](../../../README.md#RocketReach API Key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

