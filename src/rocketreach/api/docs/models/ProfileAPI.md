# openapi_client.model.profile_api.ProfileAPI

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**current_employer_linkedin_url** | None, str,  | NoneClass, str,  | This person&#x27;s company&#x27;s LinkedIn URL. | 
**[skills](#skills)** | list, tuple,  | tuple,  |  | 
**[education](#education)** | list, tuple,  | tuple,  |  | 
**region_latitude** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | 
**current_employer_domain** | None, str,  | NoneClass, str,  | This person&#x27;s company&#x27;s domain name. | 
**region_longitude** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | 
**current_employer_website** | None, str,  | NoneClass, str,  | This person&#x27;s company&#x27;s website. | 
**current_employer_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**[job_history](#job_history)** | list, tuple,  | tuple,  |  | 
**profile_list** | [**ProfileListAPI**](ProfileListAPI.md) | [**ProfileListAPI**](ProfileListAPI.md) |  | [optional] 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**status** | str,  | str,  | Either \&quot;complete\&quot;, \&quot;progress\&quot;, \&quot;searching\&quot; or \&quot;not queued\&quot;. A status other than \&quot;complete\&quot; indicates the lookup is not finished, and the contact info is not fully available yet. | [optional] 
**name** | None, str,  | NoneClass, str,  |  | [optional] 
**profile_pic** | str,  | str,  | URL containing this profile&#x27;s picture (if available). | [optional] 
**linkedin_url** | str,  | str,  |  | [optional] 
**[links](#links)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**location** | None, str,  | NoneClass, str,  |  | [optional] 
**current_title** | str,  | str,  |  | [optional] 
**normalized_title** | None, str,  | NoneClass, str,  |  | [optional] if omitted the server will use the default value of "unknown normalized title"
**current_employer** | str,  | str,  |  | [optional] 
**[emails](#emails)** | list, tuple,  | tuple,  |  | [optional] 
**[phones](#phones)** | list, tuple,  | tuple,  |  | [optional] 
**birth_year** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**recommended_email** | str,  | str,  |  | [optional] 
**recommended_personal_email** | str,  | str,  |  | [optional] 
**recommended_professional_email** | str,  | str,  |  | [optional] 
**current_work_email** | str,  | str,  |  | [optional] 
**current_personal_email** | str,  | str,  |  | [optional] 
**city** | None, str,  | NoneClass, str,  |  | [optional] 
**region** | None, str,  | NoneClass, str,  |  | [optional] 
**country** | str,  | str,  |  | [optional] 
**country_code** | None, str,  | NoneClass, str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# job_history

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**JobHistoryAPI**](JobHistoryAPI.md) | [**JobHistoryAPI**](JobHistoryAPI.md) | [**JobHistoryAPI**](JobHistoryAPI.md) |  | 

# education

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EducationAPI**](EducationAPI.md) | [**EducationAPI**](EducationAPI.md) | [**EducationAPI**](EducationAPI.md) |  | 

# skills

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# links

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | None, str,  | NoneClass, str,  | any string name can be used but the value must be the correct type | [optional] 

# emails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProfileEmailAPI**](ProfileEmailAPI.md) | [**ProfileEmailAPI**](ProfileEmailAPI.md) | [**ProfileEmailAPI**](ProfileEmailAPI.md) |  | 

# phones

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProfilePhoneAPI**](ProfilePhoneAPI.md) | [**ProfilePhoneAPI**](ProfilePhoneAPI.md) | [**ProfilePhoneAPI**](ProfilePhoneAPI.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

