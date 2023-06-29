import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.account_api import AccountApi
from openapi_client.apis.tags.company_profiles_api import CompanyProfilesApi
from openapi_client.apis.tags.person_profiles_api import PersonProfilesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACCOUNT: AccountApi,
        TagValues.COMPANY_PROFILES: CompanyProfilesApi,
        TagValues.PERSON_PROFILES: PersonProfilesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACCOUNT: AccountApi,
        TagValues.COMPANY_PROFILES: CompanyProfilesApi,
        TagValues.PERSON_PROFILES: PersonProfilesApi,
    }
)
