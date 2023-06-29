# openapi_client.model.profile_phone_api.ProfilePhoneAPI

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**number** | str,  | str,  |  | 
**type** | str,  | str,  |  | [optional] if omitted the server will use the default value of "unknown"
**validity** | str,  | str,  |  | [optional] if omitted the server will use the default value of "unknown"
**recommended** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**premium** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**last_checked** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

