# openapi_client.model.job_history_api.JobHistoryAPI

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**highest_level** | str,  | str,  |  | 
**last_updated** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**company_name** | str,  | str,  |  | 
**description** | str,  | str,  |  | 
**department** | str,  | str,  |  | 
**title** | str,  | str,  |  | 
**start_date** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time
**end_date** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time
**company** | None, str,  | NoneClass, str,  |  | [optional] 
**company_id** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] 
**company_linkedin_url** | None, str,  | NoneClass, str,  |  | [optional] 
**sub_department** | None, str,  | NoneClass, str,  |  | [optional] 
**is_current** | None, bool,  | NoneClass, BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

