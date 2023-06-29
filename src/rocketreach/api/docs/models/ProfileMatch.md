# openapi_client.model.profile_match.ProfileMatch

Specify the lookup criteria for up to 100 people.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specify the lookup criteria for up to 100 people. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | RocketReach internal person ID returned by searches. | [optional] 
**name** | str,  | str,  | Must specify along with &#x60;current_employer&#x60;. | [optional] 
**current_employer** | str,  | str,  | Must specify along with &#x60;name&#x60;. | [optional] 
**title** | str,  | str,  | Desired prospect&#x27;s job title. May improve match rate. | [optional] 
**linkedin_ext_url** | str,  | str,  | Deprecated: Use &#x60;linkedin_url&#x60;. | [optional] 
**linkedin_url** | str,  | str,  | LinkedIn URL of prospect to lookup. | [optional] 
**email** | str,  | str,  | A known email address of the prospect. May improve match rate. | [optional] 
**lookup_type** | None, str,  | NoneClass, str,  | Specify an alternative lookup type to use (if available). | [optional] must be one of ["standard", "premium", "premium (feeds disabled)", "bulk", "phone", "enrich", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

