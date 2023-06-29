# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ACCOUNT_ = "/account/"
    BULK_LOOKUP = "/bulkLookup"
    CHECK_STATUS = "/checkStatus"
    COMPANY_LOOKUP_ = "/company/lookup/"
    LOOKUP_COMPANY = "/lookupCompany"
    LOOKUP_PROFILE = "/lookupProfile"
    PERSON_CHECK_STATUS = "/person/checkStatus"
    PERSON_LOOKUP = "/person/lookup"
    PERSON_SEARCH = "/person/search"
    PROFILECOMPANY_LOOKUP = "/profile-company/lookup"
    SEARCH = "/search"
    SEARCH_COMPANY = "/searchCompany"
