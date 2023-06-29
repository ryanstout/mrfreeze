# openapi_client.model.api_bulk_lookup_query.APIBulkLookupQuery

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[queries](#queries)** | list, tuple,  | tuple,  | Specify the lookup criteria for up to 100 people. | 
**profile_list** | str,  | str,  | Add specified contacts to this profile list. | [optional] if omitted the server will use the default value of "API Bulk Lookup"
**webhook_id** | decimal.Decimal, int,  | decimal.Decimal,  | ID of the webhook to post lookup results upon completion. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# queries

Specify the lookup criteria for up to 100 people.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Specify the lookup criteria for up to 100 people. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProfileMatch**](ProfileMatch.md) | [**ProfileMatch**](ProfileMatch.md) | [**ProfileMatch**](ProfileMatch.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

