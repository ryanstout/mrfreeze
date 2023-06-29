import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.account_ import Account
from openapi_client.apis.paths.bulk_lookup import BulkLookup
from openapi_client.apis.paths.check_status import CheckStatus
from openapi_client.apis.paths.company_lookup_ import CompanyLookup
from openapi_client.apis.paths.lookup_company import LookupCompany
from openapi_client.apis.paths.lookup_profile import LookupProfile
from openapi_client.apis.paths.person_check_status import PersonCheckStatus
from openapi_client.apis.paths.person_lookup import PersonLookup
from openapi_client.apis.paths.person_search import PersonSearch
from openapi_client.apis.paths.profile_company_lookup import ProfileCompanyLookup
from openapi_client.apis.paths.search import Search
from openapi_client.apis.paths.search_company import SearchCompany

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACCOUNT_: Account,
        PathValues.BULK_LOOKUP: BulkLookup,
        PathValues.CHECK_STATUS: CheckStatus,
        PathValues.COMPANY_LOOKUP_: CompanyLookup,
        PathValues.LOOKUP_COMPANY: LookupCompany,
        PathValues.LOOKUP_PROFILE: LookupProfile,
        PathValues.PERSON_CHECK_STATUS: PersonCheckStatus,
        PathValues.PERSON_LOOKUP: PersonLookup,
        PathValues.PERSON_SEARCH: PersonSearch,
        PathValues.PROFILECOMPANY_LOOKUP: ProfileCompanyLookup,
        PathValues.SEARCH: Search,
        PathValues.SEARCH_COMPANY: SearchCompany,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACCOUNT_: Account,
        PathValues.BULK_LOOKUP: BulkLookup,
        PathValues.CHECK_STATUS: CheckStatus,
        PathValues.COMPANY_LOOKUP_: CompanyLookup,
        PathValues.LOOKUP_COMPANY: LookupCompany,
        PathValues.LOOKUP_PROFILE: LookupProfile,
        PathValues.PERSON_CHECK_STATUS: PersonCheckStatus,
        PathValues.PERSON_LOOKUP: PersonLookup,
        PathValues.PERSON_SEARCH: PersonSearch,
        PathValues.PROFILECOMPANY_LOOKUP: ProfileCompanyLookup,
        PathValues.SEARCH: Search,
        PathValues.SEARCH_COMPANY: SearchCompany,
    }
)
