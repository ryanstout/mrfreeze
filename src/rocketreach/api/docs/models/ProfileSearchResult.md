# openapi_client.model.profile_search_result.ProfileSearchResult

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**current_employer_linkedin_url** | None, str,  | NoneClass, str,  | This person&#x27;s company&#x27;s LinkedIn URL. | 
**region_latitude** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | 
**current_employer_domain** | None, str,  | NoneClass, str,  | This person&#x27;s company&#x27;s domain name. | 
**region_longitude** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | 
**[links](#links)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**current_employer_website** | None, str,  | NoneClass, str,  | This person&#x27;s company&#x27;s website. | 
**current_employer_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**birth_year** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**status** | str,  | str,  |  | [optional] 
**name** | None, str,  | NoneClass, str,  |  | [optional] 
**profile_pic** | str,  | str,  |  | [optional] 
**linkedin_url** | str,  | str,  |  | [optional] 
**location** | None, str,  | NoneClass, str,  |  | [optional] 
**city** | None, str,  | NoneClass, str,  |  | [optional] 
**region** | None, str,  | NoneClass, str,  |  | [optional] 
**country** | str,  | str,  |  | [optional] 
**country_code** | None, str,  | NoneClass, str,  |  | [optional] 
**current_title** | str,  | str,  |  | [optional] 
**normalized_title** | None, str,  | NoneClass, str,  |  | [optional] if omitted the server will use the default value of "unknown normalized title"
**current_employer** | str,  | str,  |  | [optional] 
**teaser** | str,  | str,  |  | [optional] 
**suppressed** | str,  | str,  | Returns True if this profile is blocked by a suppression list filter | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# links

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | None, str,  | NoneClass, str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

