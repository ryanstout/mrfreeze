# openapi_client.model.company_api.CompanyAPI

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[sic_codes](#sic_codes)** | list, tuple,  | tuple,  |  | 
**address** | [**CompanyAddress**](CompanyAddress.md) | [**CompanyAddress**](CompanyAddress.md) |  | 
**ticker_symbol** | None, str,  | NoneClass, str,  | Company ticker symbol, if available. | 
**num_employees** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Number of employees working at this company. | 
**[funding_investors](#funding_investors)** | list, tuple,  | tuple,  |  | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**name** | str,  | str,  |  | [optional] 
**domain** | None, str,  | NoneClass, str,  |  | [optional] 
**email_domain** | str,  | str,  |  | [optional] 
**website_domain** | None, str,  | NoneClass, str,  | Company&#x27;s website. | [optional] 
**[links](#links)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Company&#x27;s social links. | [optional] 
**year_founded** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Year company was founded. | [optional] 
**phone** | str,  | str,  |  | [optional] 
**fax** | str,  | str,  |  | [optional] 
**revenue** | str,  | str,  |  | [optional] 
**industry** | str,  | str,  |  | [optional] 
**rr_profile_url** | str,  | str,  | rocketreach.co URL where you can view more information about this company. | [optional] 
**description** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# funding_investors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# sic_codes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# links

Company's social links.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Company&#x27;s social links. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

