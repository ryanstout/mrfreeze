# openapi_client.model.person_query.PersonQuery

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[keyword](#keyword)** | list, tuple,  | tuple,  | Include results matching keyword. | [optional] 
**[exclude_keyword](#exclude_keyword)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching keyword. Use \&quot;-example\&quot;. | [optional] 
**[company_naics_code](#company_naics_code)** | list, tuple,  | tuple,  | Include results matching company_naics_code. | [optional] 
**[exclude_company_naics_code](#exclude_company_naics_code)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_naics_code. Use \&quot;-example\&quot;. | [optional] 
**[name](#name)** | list, tuple,  | tuple,  | Include results matching name. | [optional] 
**[exclude_name](#exclude_name)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching name. Use \&quot;-example\&quot;. | [optional] 
**[company_postal_code](#company_postal_code)** | list, tuple,  | tuple,  | Include results matching company_postal_code. | [optional] 
**[exclude_company_postal_code](#exclude_company_postal_code)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_postal_code. Use \&quot;-example\&quot;. | [optional] 
**[city](#city)** | list, tuple,  | tuple,  | Include results matching city. | [optional] 
**[exclude_city](#exclude_city)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching city. Use \&quot;-example\&quot;. | [optional] 
**[previous_employer](#previous_employer)** | list, tuple,  | tuple,  | Include results matching previous_employer. | [optional] 
**[exclude_previous_employer](#exclude_previous_employer)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching previous_employer. Use \&quot;-example\&quot;. | [optional] 
**[handle](#handle)** | list, tuple,  | tuple,  | Include results matching handle. | [optional] 
**[exclude_handle](#exclude_handle)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching handle. Use \&quot;-example\&quot;. | [optional] 
**[industry_tags](#industry_tags)** | list, tuple,  | tuple,  | DEPRECATED: use &#x60;industry&#x60;. | [optional] 
**[exclude_industry_tags](#exclude_industry_tags)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching industry_tags. Use \&quot;-example\&quot;. | [optional] 
**[company_revenue_max](#company_revenue_max)** | list, tuple,  | tuple,  | Include results matching company_revenue_max. | [optional] 
**[exclude_company_revenue_max](#exclude_company_revenue_max)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_revenue_max. Use \&quot;-example\&quot;. | [optional] 
**[sic_code](#sic_code)** | list, tuple,  | tuple,  | Include results matching sic_code. | [optional] 
**[exclude_sic_code](#exclude_sic_code)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching sic_code. Use \&quot;-example\&quot;. | [optional] 
**[company_industry](#company_industry)** | list, tuple,  | tuple,  | Include results matching company_industry. | [optional] 
**[exclude_company_industry](#exclude_company_industry)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_industry. Use \&quot;-example\&quot;. | [optional] 
**[postal_code](#postal_code)** | list, tuple,  | tuple,  | Include results matching postal_code. | [optional] 
**[exclude_postal_code](#exclude_postal_code)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching postal_code. Use \&quot;-example\&quot;. | [optional] 
**[company_size_min](#company_size_min)** | list, tuple,  | tuple,  | Include results matching company_size_min. | [optional] 
**[exclude_company_size_min](#exclude_company_size_min)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_size_min. Use \&quot;-example\&quot;. | [optional] 
**[management_levels](#management_levels)** | list, tuple,  | tuple,  | Include results matching management_levels. | [optional] 
**[exclude_management_levels](#exclude_management_levels)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching management_levels. Use \&quot;-example\&quot;. | [optional] 
**[company_list_id](#company_list_id)** | list, tuple,  | tuple,  | Include results matching company_list_id. | [optional] 
**[exclude_company_list_id](#exclude_company_list_id)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_list_id. Use \&quot;-example\&quot;. | [optional] 
**[phone](#phone)** | list, tuple,  | tuple,  | Include results matching phone. | [optional] 
**[exclude_phone](#exclude_phone)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching phone. Use \&quot;-example\&quot;. | [optional] 
**[company_revenue](#company_revenue)** | list, tuple,  | tuple,  | Include results matching company_revenue. | [optional] 
**[exclude_company_revenue](#exclude_company_revenue)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_revenue. Use \&quot;-example\&quot;. | [optional] 
**[company_funding_max](#company_funding_max)** | list, tuple,  | tuple,  | Include results matching company_funding_max. | [optional] 
**[exclude_company_funding_max](#exclude_company_funding_max)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_funding_max. Use \&quot;-example\&quot;. | [optional] 
**[company_website_url](#company_website_url)** | list, tuple,  | tuple,  | Include results matching company_website_url. | [optional] 
**[exclude_company_website_url](#exclude_company_website_url)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_website_url. Use \&quot;-example\&quot;. | [optional] 
**[keywords](#keywords)** | list, tuple,  | tuple,  | Include results matching keywords. | [optional] 
**[exclude_keywords](#exclude_keywords)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching keywords. Use \&quot;-example\&quot;. | [optional] 
**[insight](#insight)** | list, tuple,  | tuple,  | Include results matching insight. | [optional] 
**[exclude_insight](#exclude_insight)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching insight. Use \&quot;-example\&quot;. | [optional] 
**[veteran_status](#veteran_status)** | list, tuple,  | tuple,  | veteran_status is a boolean and we only accept True values | [optional] 
**[exclude_veteran_status](#exclude_veteran_status)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching veteran_status. Use \&quot;-example\&quot;. | [optional] 
**[company_website_rank_min](#company_website_rank_min)** | list, tuple,  | tuple,  | Include results matching company_website_rank_min. | [optional] 
**[exclude_company_website_rank_min](#exclude_company_website_rank_min)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_website_rank_min. Use \&quot;-example\&quot;. | [optional] 
**[simplified_keyword](#simplified_keyword)** | list, tuple,  | tuple,  | Include results matching simplified_keyword. | [optional] 
**[exclude_simplified_keyword](#exclude_simplified_keyword)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching simplified_keyword. Use \&quot;-example\&quot;. | [optional] 
**[link](#link)** | list, tuple,  | tuple,  | Include results matching link. | [optional] 
**[exclude_link](#exclude_link)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching link. Use \&quot;-example\&quot;. | [optional] 
**[company_id](#company_id)** | list, tuple,  | tuple,  | Include results matching company_id. | [optional] 
**[exclude_company_id](#exclude_company_id)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_id. Use \&quot;-example\&quot;. | [optional] 
**[company_name](#company_name)** | list, tuple,  | tuple,  | Include results matching company_name. | [optional] 
**[exclude_company_name](#exclude_company_name)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_name. Use \&quot;-example\&quot;. | [optional] 
**[company_industry_tags](#company_industry_tags)** | list, tuple,  | tuple,  | DEPRECATED: use &#x60;company_industry&#x60;. | [optional] 
**[exclude_company_industry_tags](#exclude_company_industry_tags)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_industry_tags. Use \&quot;-example\&quot;. | [optional] 
**[techstack](#techstack)** | list, tuple,  | tuple,  | Include results matching techstack. | [optional] 
**[exclude_techstack](#exclude_techstack)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching techstack. Use \&quot;-example\&quot;. | [optional] 
**[is_primary](#is_primary)** | list, tuple,  | tuple,  | Include results matching is_primary. | [optional] 
**[exclude_is_primary](#exclude_is_primary)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching is_primary. Use \&quot;-example\&quot;. | [optional] 
**[birth_year](#birth_year)** | list, tuple,  | tuple,  | Range query on birth year using the index on birth_date  Translates the original query on year to a query on birth date. | [optional] 
**[exclude_birth_year](#exclude_birth_year)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching birth_year. Use \&quot;-example\&quot;. | [optional] 
**[keyword_orig](#keyword_orig)** | list, tuple,  | tuple,  | Include results matching keyword_orig. | [optional] 
**[exclude_keyword_orig](#exclude_keyword_orig)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching keyword_orig. Use \&quot;-example\&quot;. | [optional] 
**[growth](#growth)** | list, tuple,  | tuple,  | Include results matching growth. | [optional] 
**[exclude_growth](#exclude_growth)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching growth. Use \&quot;-example\&quot;. | [optional] 
**[email](#email)** | list, tuple,  | tuple,  | Include results matching email. | [optional] 
**[exclude_email](#exclude_email)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching email. Use \&quot;-example\&quot;. | [optional] 
**[ethnicity](#ethnicity)** | list, tuple,  | tuple,  | Similar to normalized title, we require exact &#x27;display name&#x27; searches including capitalization. | [optional] 
**[exclude_ethnicity](#exclude_ethnicity)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching ethnicity. Use \&quot;-example\&quot;. | [optional] 
**[company_website_rank_max](#company_website_rank_max)** | list, tuple,  | tuple,  | Include results matching company_website_rank_max. | [optional] 
**[exclude_company_website_rank_max](#exclude_company_website_rank_max)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_website_rank_max. Use \&quot;-example\&quot;. | [optional] 
**[extended_keyword](#extended_keyword)** | list, tuple,  | tuple,  | Include results matching extended_keyword. | [optional] 
**[exclude_extended_keyword](#exclude_extended_keyword)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching extended_keyword. Use \&quot;-example\&quot;. | [optional] 
**[employees](#employees)** | list, tuple,  | tuple,  | Include results matching employees. | [optional] 
**[exclude_employees](#exclude_employees)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching employees. Use \&quot;-example\&quot;. | [optional] 
**[company_publicly_traded](#company_publicly_traded)** | list, tuple,  | tuple,  | Include results matching company_publicly_traded. | [optional] 
**[exclude_company_publicly_traded](#exclude_company_publicly_traded)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_publicly_traded. Use \&quot;-example\&quot;. | [optional] 
**[sic_codes](#sic_codes)** | list, tuple,  | tuple,  | Include results matching sic_codes. | [optional] 
**[exclude_sic_codes](#exclude_sic_codes)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching sic_codes. Use \&quot;-example\&quot;. | [optional] 
**[location](#location)** | list, tuple,  | tuple,  | Include results matching location. | [optional] 
**[exclude_location](#exclude_location)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching location. Use \&quot;-example\&quot;. | [optional] 
**[company_email](#company_email)** | list, tuple,  | tuple,  | Include results matching company_email. | [optional] 
**[exclude_company_email](#exclude_company_email)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_email. Use \&quot;-example\&quot;. | [optional] 
**[naics_code](#naics_code)** | list, tuple,  | tuple,  | Include results matching naics_code. | [optional] 
**[exclude_naics_code](#exclude_naics_code)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching naics_code. Use \&quot;-example\&quot;. | [optional] 
**[degree](#degree)** | list, tuple,  | tuple,  | Include results matching degree. | [optional] 
**[exclude_degree](#exclude_degree)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching degree. Use \&quot;-example\&quot;. | [optional] 
**[years_experience](#years_experience)** | list, tuple,  | tuple,  | Include results matching years_experience. | [optional] 
**[exclude_years_experience](#exclude_years_experience)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching years_experience. Use \&quot;-example\&quot;. | [optional] 
**[country](#country)** | list, tuple,  | tuple,  | Include results matching country. | [optional] 
**[exclude_country](#exclude_country)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching country. Use \&quot;-example\&quot;. | [optional] 
**[company_size_max](#company_size_max)** | list, tuple,  | tuple,  | Include results matching company_size_max. | [optional] 
**[exclude_company_size_max](#exclude_company_size_max)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_size_max. Use \&quot;-example\&quot;. | [optional] 
**[current_title](#current_title)** | list, tuple,  | tuple,  | Include results matching current_title. | [optional] 
**[exclude_current_title](#exclude_current_title)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching current_title. Use \&quot;-example\&quot;. | [optional] 
**[department](#department)** | list, tuple,  | tuple,  | Include results matching department. | [optional] 
**[exclude_department](#exclude_department)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching department. Use \&quot;-example\&quot;. | [optional] 
**[all_industries](#all_industries)** | list, tuple,  | tuple,  | Include results matching all_industries. | [optional] 
**[exclude_all_industries](#exclude_all_industries)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching all_industries. Use \&quot;-example\&quot;. | [optional] 
**[keyword_enhanced](#keyword_enhanced)** | list, tuple,  | tuple,  | Include results matching keyword_enhanced. | [optional] 
**[exclude_keyword_enhanced](#exclude_keyword_enhanced)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching keyword_enhanced. Use \&quot;-example\&quot;. | [optional] 
**[company_city](#company_city)** | list, tuple,  | tuple,  | Include results matching company_city. | [optional] 
**[exclude_company_city](#exclude_company_city)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_city. Use \&quot;-example\&quot;. | [optional] 
**[company_revenue_min](#company_revenue_min)** | list, tuple,  | tuple,  | Include results matching company_revenue_min. | [optional] 
**[exclude_company_revenue_min](#exclude_company_revenue_min)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_revenue_min. Use \&quot;-example\&quot;. | [optional] 
**[total_funding](#total_funding)** | list, tuple,  | tuple,  | Include results matching total_funding. | [optional] 
**[exclude_total_funding](#exclude_total_funding)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching total_funding. Use \&quot;-example\&quot;. | [optional] 
**[company_website_rank](#company_website_rank)** | list, tuple,  | tuple,  | Include results matching company_website_rank. | [optional] 
**[exclude_company_website_rank](#exclude_company_website_rank)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_website_rank. Use \&quot;-example\&quot;. | [optional] 
**[description](#description)** | list, tuple,  | tuple,  | Include results matching description. | [optional] 
**[exclude_description](#exclude_description)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching description. Use \&quot;-example\&quot;. | [optional] 
**[job_change_range_days](#job_change_range_days)** | list, tuple,  | tuple,  | Include results matching job_change_range_days. | [optional] 
**[exclude_job_change_range_days](#exclude_job_change_range_days)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching job_change_range_days. Use \&quot;-example\&quot;. | [optional] 
**[primary_industry](#primary_industry)** | list, tuple,  | tuple,  | Include results matching primary_industry. | [optional] 
**[exclude_primary_industry](#exclude_primary_industry)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching primary_industry. Use \&quot;-example\&quot;. | [optional] 
**[website_url](#website_url)** | list, tuple,  | tuple,  | Include results matching website_url. | [optional] 
**[exclude_website_url](#exclude_website_url)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching website_url. Use \&quot;-example\&quot;. | [optional] 
**[company_country_code](#company_country_code)** | list, tuple,  | tuple,  | Include results matching company_country_code. | [optional] 
**[exclude_company_country_code](#exclude_company_country_code)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_country_code. Use \&quot;-example\&quot;. | [optional] 
**[domain](#domain)** | list, tuple,  | tuple,  | Include results matching domain. | [optional] 
**[exclude_domain](#exclude_domain)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching domain. Use \&quot;-example\&quot;. | [optional] 
**[email_domain](#email_domain)** | list, tuple,  | tuple,  | Include results matching email_domain. | [optional] 
**[exclude_email_domain](#exclude_email_domain)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching email_domain. Use \&quot;-example\&quot;. | [optional] 
**[gender](#gender)** | list, tuple,  | tuple,  | Include results matching gender. | [optional] 
**[exclude_gender](#exclude_gender)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching gender. Use \&quot;-example\&quot;. | [optional] 
**[company_sic_code](#company_sic_code)** | list, tuple,  | tuple,  | Include results matching company_sic_code. | [optional] 
**[exclude_company_sic_code](#exclude_company_sic_code)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_sic_code. Use \&quot;-example\&quot;. | [optional] 
**[naics_codes](#naics_codes)** | list, tuple,  | tuple,  | Include results matching naics_codes. | [optional] 
**[exclude_naics_codes](#exclude_naics_codes)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching naics_codes. Use \&quot;-example\&quot;. | [optional] 
**[company_size](#company_size)** | list, tuple,  | tuple,  | Include results matching company_size. | [optional] 
**[exclude_company_size](#exclude_company_size)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_size. Use \&quot;-example\&quot;. | [optional] 
**[normalized_title](#normalized_title)** | list, tuple,  | tuple,  | Matches against a known normalized title exactly, after title-normalization | [optional] 
**[exclude_normalized_title](#exclude_normalized_title)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching normalized_title. Use \&quot;-example\&quot;. | [optional] 
**[connections](#connections)** | list, tuple,  | tuple,  | Include results matching connections. | [optional] 
**[exclude_connections](#exclude_connections)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching connections. Use \&quot;-example\&quot;. | [optional] 
**[major](#major)** | list, tuple,  | tuple,  | Include results matching major. | [optional] 
**[exclude_major](#exclude_major)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching major. Use \&quot;-example\&quot;. | [optional] 
**[company_list](#company_list)** | list, tuple,  | tuple,  | Transforms [ company_list ] search terms into a list of [ company_id ] search terms. | [optional] 
**[exclude_company_list](#exclude_company_list)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_list. Use \&quot;-example\&quot;. | [optional] 
**[geo](#geo)** | list, tuple,  | tuple,  | Include results matching geo. | [optional] 
**[exclude_geo](#exclude_geo)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching geo. Use \&quot;-example\&quot;. | [optional] 
**[previous_company_id](#previous_company_id)** | list, tuple,  | tuple,  | Include results matching previous_company_id. | [optional] 
**[exclude_previous_company_id](#exclude_previous_company_id)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching previous_company_id. Use \&quot;-example\&quot;. | [optional] 
**[state](#state)** | list, tuple,  | tuple,  | Include results matching state. | [optional] 
**[exclude_state](#exclude_state)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching state. Use \&quot;-example\&quot;. | [optional] 
**[skills](#skills)** | list, tuple,  | tuple,  | Include results matching skills. | [optional] 
**[exclude_skills](#exclude_skills)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching skills. Use \&quot;-example\&quot;. | [optional] 
**[company_domain](#company_domain)** | list, tuple,  | tuple,  | Include results matching company_domain. | [optional] 
**[exclude_company_domain](#exclude_company_domain)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_domain. Use \&quot;-example\&quot;. | [optional] 
**[company_region](#company_region)** | list, tuple,  | tuple,  | Include results matching company_region. | [optional] 
**[exclude_company_region](#exclude_company_region)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_region. Use \&quot;-example\&quot;. | [optional] 
**[company_website_category](#company_website_category)** | list, tuple,  | tuple,  | Include results matching company_website_category. | [optional] 
**[exclude_company_website_category](#exclude_company_website_category)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_website_category. Use \&quot;-example\&quot;. | [optional] 
**[industry](#industry)** | list, tuple,  | tuple,  | Include results matching industry. | [optional] 
**[exclude_industry](#exclude_industry)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching industry. Use \&quot;-example\&quot;. | [optional] 
**[publicly_traded](#publicly_traded)** | list, tuple,  | tuple,  | Include results matching publicly_traded. | [optional] 
**[exclude_publicly_traded](#exclude_publicly_traded)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching publicly_traded. Use \&quot;-example\&quot;. | [optional] 
**[revenue](#revenue)** | list, tuple,  | tuple,  | Include results matching revenue. | [optional] 
**[exclude_revenue](#exclude_revenue)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching revenue. Use \&quot;-example\&quot;. | [optional] 
**[id](#id)** | list, tuple,  | tuple,  | Include results matching id. | [optional] 
**[exclude_id](#exclude_id)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching id. Use \&quot;-example\&quot;. | [optional] 
**[current_employer](#current_employer)** | list, tuple,  | tuple,  | Include results matching current_employer. | [optional] 
**[exclude_current_employer](#exclude_current_employer)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching current_employer. Use \&quot;-example\&quot;. | [optional] 
**[company_funding_min](#company_funding_min)** | list, tuple,  | tuple,  | Include results matching company_funding_min. | [optional] 
**[exclude_company_funding_min](#exclude_company_funding_min)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_funding_min. Use \&quot;-example\&quot;. | [optional] 
**[employer](#employer)** | list, tuple,  | tuple,  | Include results matching employer. | [optional] 
**[exclude_employer](#exclude_employer)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching employer. Use \&quot;-example\&quot;. | [optional] 
**[website_category](#website_category)** | list, tuple,  | tuple,  | Include results matching website_category. | [optional] 
**[exclude_website_category](#exclude_website_category)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching website_category. Use \&quot;-example\&quot;. | [optional] 
**[school](#school)** | list, tuple,  | tuple,  | Include results matching school. | [optional] 
**[exclude_school](#exclude_school)** | list, tuple,  | tuple,  | DEPRECATED: Exclude results matching school. Use \&quot;-example\&quot;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# keyword

Include results matching keyword.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching keyword. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_keyword

DEPRECATED: Exclude results matching keyword. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching keyword. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_naics_code

Include results matching company_naics_code.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_naics_code. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_naics_code

DEPRECATED: Exclude results matching company_naics_code. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_naics_code. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# name

Include results matching name.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching name. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_name

DEPRECATED: Exclude results matching name. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching name. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_postal_code

Include results matching company_postal_code.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_postal_code. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_postal_code

DEPRECATED: Exclude results matching company_postal_code. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_postal_code. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# city

Include results matching city.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching city. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_city

DEPRECATED: Exclude results matching city. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching city. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# previous_employer

Include results matching previous_employer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching previous_employer. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_previous_employer

DEPRECATED: Exclude results matching previous_employer. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching previous_employer. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# handle

Include results matching handle.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching handle. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_handle

DEPRECATED: Exclude results matching handle. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching handle. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# industry_tags

DEPRECATED: use `industry`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: use &#x60;industry&#x60;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_industry_tags

DEPRECATED: Exclude results matching industry_tags. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching industry_tags. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_revenue_max

Include results matching company_revenue_max.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_revenue_max. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_revenue_max

DEPRECATED: Exclude results matching company_revenue_max. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_revenue_max. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# sic_code

Include results matching sic_code.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching sic_code. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_sic_code

DEPRECATED: Exclude results matching sic_code. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching sic_code. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_industry

Include results matching company_industry.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_industry. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_industry

DEPRECATED: Exclude results matching company_industry. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_industry. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# postal_code

Include results matching postal_code.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching postal_code. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_postal_code

DEPRECATED: Exclude results matching postal_code. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching postal_code. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_size_min

Include results matching company_size_min.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_size_min. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_size_min

DEPRECATED: Exclude results matching company_size_min. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_size_min. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# management_levels

Include results matching management_levels.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching management_levels. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_management_levels

DEPRECATED: Exclude results matching management_levels. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching management_levels. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_list_id

Include results matching company_list_id.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_list_id. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_list_id

DEPRECATED: Exclude results matching company_list_id. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_list_id. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# phone

Include results matching phone.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching phone. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_phone

DEPRECATED: Exclude results matching phone. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching phone. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_revenue

Include results matching company_revenue.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_revenue. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_revenue

DEPRECATED: Exclude results matching company_revenue. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_revenue. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_funding_max

Include results matching company_funding_max.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_funding_max. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_funding_max

DEPRECATED: Exclude results matching company_funding_max. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_funding_max. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_website_url

Include results matching company_website_url.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_website_url. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_website_url

DEPRECATED: Exclude results matching company_website_url. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_website_url. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# keywords

Include results matching keywords.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching keywords. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_keywords

DEPRECATED: Exclude results matching keywords. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching keywords. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# insight

Include results matching insight.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching insight. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_insight

DEPRECATED: Exclude results matching insight. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching insight. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# veteran_status

veteran_status is a boolean and we only accept True values

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | veteran_status is a boolean and we only accept True values | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_veteran_status

DEPRECATED: Exclude results matching veteran_status. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching veteran_status. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_website_rank_min

Include results matching company_website_rank_min.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_website_rank_min. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_website_rank_min

DEPRECATED: Exclude results matching company_website_rank_min. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_website_rank_min. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# simplified_keyword

Include results matching simplified_keyword.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching simplified_keyword. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_simplified_keyword

DEPRECATED: Exclude results matching simplified_keyword. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching simplified_keyword. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# link

Include results matching link.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching link. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_link

DEPRECATED: Exclude results matching link. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching link. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_id

Include results matching company_id.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_id. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_id

DEPRECATED: Exclude results matching company_id. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_id. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_name

Include results matching company_name.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_name. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_name

DEPRECATED: Exclude results matching company_name. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_name. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_industry_tags

DEPRECATED: use `company_industry`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: use &#x60;company_industry&#x60;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_industry_tags

DEPRECATED: Exclude results matching company_industry_tags. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_industry_tags. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# techstack

Include results matching techstack.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching techstack. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_techstack

DEPRECATED: Exclude results matching techstack. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching techstack. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# is_primary

Include results matching is_primary.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching is_primary. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_is_primary

DEPRECATED: Exclude results matching is_primary. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching is_primary. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# birth_year

Range query on birth year using the index on birth_date  Translates the original query on year to a query on birth date.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Range query on birth year using the index on birth_date  Translates the original query on year to a query on birth date. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_birth_year

DEPRECATED: Exclude results matching birth_year. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching birth_year. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# keyword_orig

Include results matching keyword_orig.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching keyword_orig. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_keyword_orig

DEPRECATED: Exclude results matching keyword_orig. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching keyword_orig. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# growth

Include results matching growth.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching growth. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_growth

DEPRECATED: Exclude results matching growth. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching growth. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# email

Include results matching email.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching email. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_email

DEPRECATED: Exclude results matching email. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching email. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# ethnicity

Similar to normalized title, we require exact 'display name' searches including capitalization.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Similar to normalized title, we require exact &#x27;display name&#x27; searches including capitalization. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_ethnicity

DEPRECATED: Exclude results matching ethnicity. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching ethnicity. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_website_rank_max

Include results matching company_website_rank_max.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_website_rank_max. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_website_rank_max

DEPRECATED: Exclude results matching company_website_rank_max. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_website_rank_max. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# extended_keyword

Include results matching extended_keyword.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching extended_keyword. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_extended_keyword

DEPRECATED: Exclude results matching extended_keyword. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching extended_keyword. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# employees

Include results matching employees.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching employees. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_employees

DEPRECATED: Exclude results matching employees. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching employees. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_publicly_traded

Include results matching company_publicly_traded.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_publicly_traded. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_publicly_traded

DEPRECATED: Exclude results matching company_publicly_traded. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_publicly_traded. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# sic_codes

Include results matching sic_codes.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching sic_codes. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_sic_codes

DEPRECATED: Exclude results matching sic_codes. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching sic_codes. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# location

Include results matching location.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching location. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_location

DEPRECATED: Exclude results matching location. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching location. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_email

Include results matching company_email.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_email. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_email

DEPRECATED: Exclude results matching company_email. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_email. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# naics_code

Include results matching naics_code.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching naics_code. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_naics_code

DEPRECATED: Exclude results matching naics_code. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching naics_code. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# degree

Include results matching degree.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching degree. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_degree

DEPRECATED: Exclude results matching degree. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching degree. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# years_experience

Include results matching years_experience.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching years_experience. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_years_experience

DEPRECATED: Exclude results matching years_experience. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching years_experience. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# country

Include results matching country.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching country. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_country

DEPRECATED: Exclude results matching country. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching country. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_size_max

Include results matching company_size_max.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_size_max. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_size_max

DEPRECATED: Exclude results matching company_size_max. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_size_max. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# current_title

Include results matching current_title.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching current_title. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_current_title

DEPRECATED: Exclude results matching current_title. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching current_title. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# department

Include results matching department.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching department. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_department

DEPRECATED: Exclude results matching department. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching department. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# all_industries

Include results matching all_industries.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching all_industries. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_all_industries

DEPRECATED: Exclude results matching all_industries. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching all_industries. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# keyword_enhanced

Include results matching keyword_enhanced.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching keyword_enhanced. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_keyword_enhanced

DEPRECATED: Exclude results matching keyword_enhanced. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching keyword_enhanced. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_city

Include results matching company_city.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_city. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_city

DEPRECATED: Exclude results matching company_city. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_city. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_revenue_min

Include results matching company_revenue_min.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_revenue_min. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_revenue_min

DEPRECATED: Exclude results matching company_revenue_min. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_revenue_min. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# total_funding

Include results matching total_funding.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching total_funding. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_total_funding

DEPRECATED: Exclude results matching total_funding. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching total_funding. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_website_rank

Include results matching company_website_rank.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_website_rank. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_website_rank

DEPRECATED: Exclude results matching company_website_rank. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_website_rank. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# description

Include results matching description.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching description. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_description

DEPRECATED: Exclude results matching description. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching description. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# job_change_range_days

Include results matching job_change_range_days.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching job_change_range_days. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_job_change_range_days

DEPRECATED: Exclude results matching job_change_range_days. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching job_change_range_days. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# primary_industry

Include results matching primary_industry.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching primary_industry. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_primary_industry

DEPRECATED: Exclude results matching primary_industry. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching primary_industry. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# website_url

Include results matching website_url.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching website_url. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_website_url

DEPRECATED: Exclude results matching website_url. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching website_url. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_country_code

Include results matching company_country_code.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_country_code. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_country_code

DEPRECATED: Exclude results matching company_country_code. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_country_code. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# domain

Include results matching domain.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching domain. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_domain

DEPRECATED: Exclude results matching domain. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching domain. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# email_domain

Include results matching email_domain.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching email_domain. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_email_domain

DEPRECATED: Exclude results matching email_domain. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching email_domain. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# gender

Include results matching gender.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching gender. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_gender

DEPRECATED: Exclude results matching gender. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching gender. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_sic_code

Include results matching company_sic_code.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_sic_code. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_sic_code

DEPRECATED: Exclude results matching company_sic_code. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_sic_code. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# naics_codes

Include results matching naics_codes.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching naics_codes. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_naics_codes

DEPRECATED: Exclude results matching naics_codes. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching naics_codes. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_size

Include results matching company_size.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_size. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_size

DEPRECATED: Exclude results matching company_size. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_size. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# normalized_title

Matches against a known normalized title exactly, after title-normalization

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Matches against a known normalized title exactly, after title-normalization | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_normalized_title

DEPRECATED: Exclude results matching normalized_title. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching normalized_title. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# connections

Include results matching connections.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching connections. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_connections

DEPRECATED: Exclude results matching connections. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching connections. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# major

Include results matching major.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching major. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_major

DEPRECATED: Exclude results matching major. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching major. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_list

Transforms [ company_list ] search terms into a list of [ company_id ] search terms.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Transforms [ company_list ] search terms into a list of [ company_id ] search terms. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_list

DEPRECATED: Exclude results matching company_list. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_list. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# geo

Include results matching geo.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching geo. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_geo

DEPRECATED: Exclude results matching geo. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching geo. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# previous_company_id

Include results matching previous_company_id.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching previous_company_id. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_previous_company_id

DEPRECATED: Exclude results matching previous_company_id. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching previous_company_id. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# state

Include results matching state.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching state. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_state

DEPRECATED: Exclude results matching state. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching state. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# skills

Include results matching skills.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching skills. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_skills

DEPRECATED: Exclude results matching skills. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching skills. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_domain

Include results matching company_domain.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_domain. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_domain

DEPRECATED: Exclude results matching company_domain. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_domain. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_region

Include results matching company_region.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_region. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_region

DEPRECATED: Exclude results matching company_region. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_region. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_website_category

Include results matching company_website_category.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_website_category. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_website_category

DEPRECATED: Exclude results matching company_website_category. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_website_category. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# industry

Include results matching industry.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching industry. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_industry

DEPRECATED: Exclude results matching industry. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching industry. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# publicly_traded

Include results matching publicly_traded.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching publicly_traded. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_publicly_traded

DEPRECATED: Exclude results matching publicly_traded. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching publicly_traded. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# revenue

Include results matching revenue.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching revenue. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_revenue

DEPRECATED: Exclude results matching revenue. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching revenue. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# id

Include results matching id.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching id. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_id

DEPRECATED: Exclude results matching id. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching id. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# current_employer

Include results matching current_employer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching current_employer. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_current_employer

DEPRECATED: Exclude results matching current_employer. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching current_employer. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# company_funding_min

Include results matching company_funding_min.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching company_funding_min. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_company_funding_min

DEPRECATED: Exclude results matching company_funding_min. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching company_funding_min. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# employer

Include results matching employer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching employer. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_employer

DEPRECATED: Exclude results matching employer. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching employer. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# website_category

Include results matching website_category.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching website_category. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_website_category

DEPRECATED: Exclude results matching website_category. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching website_category. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# school

Include results matching school.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Include results matching school. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

# exclude_school

DEPRECATED: Exclude results matching school. Use \"-example\".

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: Exclude results matching school. Use \&quot;-example\&quot;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | None, str,  | NoneClass, str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

