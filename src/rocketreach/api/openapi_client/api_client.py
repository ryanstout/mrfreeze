# coding: utf-8
"""
    RocketReach API

    # Getting Started The RocketReach API allows you to programmatically search & lookup contact info for over 700 million professionals, and 35 million companies. We constantly work on improving functionality and accuracy of our data. RocketReach is free to try for individual use.  You can always visit the [account page](/account?section=nav_gen_api) to view API usage, manage RocketReach API settings, and view your unique API key. All calls to the RocketReach API are authenticated with an API key.  ## Need Help? Have feedback, questions about usage, or pricing? Talk to us live or Email us at sales@rocketreach.co.  ## Troubleshooting  ### Handling Errors Normal responses are returned with HTTP status `HTTP: 200`. Error responses return `HTTP: 4xx/5xx` error codes. For example, if the profile being searched for cannot be found, we will return a `404`.  ### Rate Limits If we start receiving unusually heavy call volumes on your API key, you may receive responses with `HTTP: 429 \"Too Many Requests\"`. In general, do not make more than 5 calls per second using your API key.  Throttled API responses will contain a `Retry-After` header that contains the number of seconds to wait until the endpoint becomes available again. To ensure your client accesses the API fairly, it should parse this value and waits the appropriate amount of time.   Repeated instances of unexpected throttled requests should be addressed one of the following ways: 1. If you are not on a paid plan, you will generally need to upgrade to a paid API plan. Please email sales@rocketreach.co to setup an API plan. 2. If you are already on a paid API plan, please slow down and retry your requests. Contact sales@rocketreach.co or our live support if you continue to have problems.  You can visit the [account page](/account?section=api_section_gen_api) to review your RocketReach API limits and daily usage.  ## Webhooks We offer a webhook solution for person lookups so clients do not need to poll the check status endpoint until their results are available.  ### Set Up To set up a webhook, go to your [API settings](/account?section=nav_gen_api). Enter your server's callback URL into the field, and hit \"Create\".  ### Configuration Options For each URL created, you can perform some basic maintenance tasks:  - Test the webhook - we will attempt to send a basic JSON payload to the URL. - Disable/enable - if you may use this URL in the future, this is an option to temporarily disable it. - Delete - if you no longer plan using this URL, it can be deleted.  ### Usage Currently, only profile lookup and bulk lookup have webhook functionality, but we anticipate supporting more in the future! Once you call a webhook-enabled endpoint with a webhook set up in your settings, we will send back results to the provided URL. The results returned to you should look the same as if they were queried through the REST API. In addition, the API will still respond to your REST call as normal.  ### Errors If any errors occur, they will show up in the [API settings](/account?section=nav_gen_api) page in the \"Web Hook\" section. If the callback to the provided URL is unsuccessful after several attempts, the URL will be automatically disabled and will need to manually be re-enabled.  ## FAQ  **How Do I Know if RocketReach Has Data For a Profile?** - 87% of lookups return profiles  - \"teaser\" in search returns some indication of data; however, the final lookup may discover results even if the teaser is empty - if no data is found, credits are not deducted  **Do I Get Charged a Credit if No Data is Returned?** - for lookups, no - searches are metered, but usually the first ~10,000/day are free on paid API plans  **Why doesn't the data in a Profile match data from the API?** - this should almost never happen, please contact support - on the other hand, search results and sorting may be different depending on how the search is executed - the UI uses NLP for search facets  **Why don't the search results in the UI match data returned from the API?** - search results and sorting may be different depending on how the search is executed - this also uses NLP for search facets - try changing the facet and adjusting the `order_by` param  **Why does the teaser only contain phone numbers, and no emails?** - teaser information is only populated if data is cached  **Why am I getting rate limited?** - rate limits depend on product, contact us to get on an API plan - See our troubleshooting guide for more info.   ## SDKs  ### Python SDK The [Python SDK](https://www.github.com/rocketreach/rocketreach_python) allows you to find anyone's emails, social media and complete contact data, using only a few lines of code.  ### Installation The rocketreach python package can be installed from pip or from source into your project's virtual environment.  Install with pip:  ```bash pip install rocketreach ```  Install from source:  ```bash # The requests v2.2 or higher is a required dependency wget https://pypi.python.org/packages/source/r/requests/requests-2.2.1.tar.gz tar xzvf requests-2.2.1.tar.gz cd requests-2.2.1 python setup.py install  # Install the rocketreach SDK wget https://files.pythonhosted.org/packages/20/9d/5ba988d0b2f94a19fb8f86ae87ef1a2eb79b3fd7da7cce00998b7051d57f/rocketreach-2.1.0.tar.gz tar xzvf rocketreach-2.1.0.tar.gz cd rocketreach-2.1.0 python setup.py install ```  ### Usage  Initialization is the first step to use the SDK. You will need your API key for this step.  ```python import rocketreach import os rr = rocketreach.Gateway(api_key=os.environ.get('API_KEY'))  # Check that the SDK is working result = rr.account.get() if result.is_success:     print(f'Success: {result.account}') else:     print(f'Error: {result.message}!') ```  You can call any of our methods once the Gateway class is constructed. In this next example we will call lookup() using a name and current employer. Then, we'll do the same lookup using a LinkedIn URL.  ```python lookup_result = rr.person.lookup(name='Marc Benioff', current_employer='Salesforce') if lookup_result.is_success:     print(lookup_result.person) lookup_result = rr.person.lookup(linkedin_url='https://www.linkedin.com/in/marcbenioff') if lookup_result.is_success:     print(lookup_result.person) ```  By default, the lookup method blocks until /checkStatus returns complete. The caller can override this behavior and call lookup in a non-blocking context.  ```python import time # Lookup 2 profiles, non-blocking and checkStatus ourself. lookup1 = rr.person.lookup(linkedin_url='https://www.linkedin.com/in/marcbenioff', block=False) lookup2 = rr.person.lookup(linkedin_url='https://www.linkedin.com/in/reidhoffman', block=False) # Check if the lookups are complete. while True:     lookup_ids = [lookup1.person.id, lookup2.person.id]     cs_result = rr.person.check_status(lookup_ids)     num_complete = 0     for p in cs_result.people:         if p.status == 'complete':             num_complete += 1     if num_complete == len(lookups):         break     time.sleep(10)  # Wait a few seconds before checking status again # All the lookups are 'complete'. ```  `check_status()` can take either a single argument, or an array containing multiple IDs to lookup. Regardless of the number of arguments, the return value will always contain a person collection as an array (with 1 or more elements).  ```python result = rr.person.check_status(5244) assert(len(result.people) == 1) result = rr.person.check_status([5244, 5234]) assert(len(result.people) == 2) ```  ### Reference Calls are wrapped in a Result object. If the call was successful the Result object will encapsulate the return value.  Result object attributes  Name Description Type request Request object sent to the server. requests.Request response Response object received from the server. requests.Response is_success Indicates if the call succeeded. bool data (optional) Any data retrieved from the server response. dict error (optional) Any error data retrieved from the server response. Returned if is_success is False dict message (optional) A human readable message that explains what went wrong. str  | Name      | Description | Type | |-----------| ----------- | -----| | request    | Request object sent to the server. | `requests.Request` | | response | Response object received from the server. | `requests.Response` | | is_success | Indicates if the call succeeded. | `bool` | | data | Any data retrieved from the server response. | `dict` (optional) | | error | Any error data retrieved from the server response. Returned if `is_success = False` | `dict` (optional) |        | | message | A human readable message that explains what went wrong. | `str` (optional) |  ### Pagination  Searches will only return 10 results at a time, but the API provides a pagination method that can be accessed through the Python SDK.  ```python search = rr.person.search() # Add filters to your search start = 1 size = 10 result = search.execute() people = [] while result.is_success and result.people:     start += size     people.extend(result.people)     search = search.params(start=start, size=size)     result = search.execute() ```  The Python SDK provides iterators to handle paginating through results for you. These convenience iterators are accessed through the .iterator() method.  ```python search = rr.person.search() # Add filters to your search for person in search.iterator():     print(person) ```  The search object also supports indexing and slicing to limit the range of results. ```python search = rr.person.search() # Add filters to your search list(search[:100])  # Retrieve the first 100 results list(search[10:20])  # Retrieve results 11 - 19 person = search[0]  # Retrieve only the first result ```  Note: - Indexing causes the search to be immediately executed with the desired result returned. - Search object slices cannot contain steps.  ## Examples  ### Lookup by Name If you are calling the RocketReach API endpoints directly, you will essentially need to use 2 calls. First call `person/lookup` with 2 parameters: `name` and `current_employer`.  ```bash curl -G -L 'http://api.rocketreach.co/api/v2/person/lookup'\\      --header 'Api-Key: <INSERT API KEY>'\\      --data-urlencode 'name=Marc Benioff'\\      --data-urlencode 'current_employer=Salesforce' ```  If the status returned by the call is not `complete` or `failed`, then you will need to poll `person/checkStatus` untill it returns either `complete` or `failed`. If the status is `complete`, then the response will also contain contact info data.  ```bash curl --request 'GET' --location 'https://api.rocketreach.co/api/v2/person/checkStatus'\\      --header 'Api-Key: <INSERT API KEY>'\\      --data-urlencode 'ids=5262' ```  **Putting it all together** The following example demonstrates a fully functional application, using the RocketReach API. Here, we lookup contact info of a person, by name and current_employer.  The source code shown below uses the RocketReach Python SDK. We start by calling initializing the client. This checks to make sure that the `api_key` is valid, and that the user has sufficient credits to perform lookups. Under the covers, the SDK is simply calling the `/account` endpoint. If everything looks good, we now call `person/lookup` to lookup contact info. The library also polls `person/checkStatus` for you, when necessary.  ```python import rocketreach import os rr = rocketreach.Gateway(api_key=os.environ.get('API_KEY')) lookup = rr.person.lookup(extras={'name': 'Marc Benioff', 'current_employer': 'Salesforce'}) if lookup.is_success:     print(repr(lookup.person)) ```  Output ```python     {'current_employer': 'Salesforce',      'current_personal_email': 'benioff@gmail.com',      'current_title': 'Chairman and Co-CEO',      'current_work_email': 'marcb@salesforce.com',      'emails': [{'email': 'm.benioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'mbenioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'benioff@comcast.net',                  'smtp_valid': 'valid',                  'type': 'personal'},                 {'email': 'marc@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marc_benioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'benioff@gmail.com',                  'smtp_valid': 'valid',                  'type': 'personal'},                 {'email': 'benioff@aol.com',                  'smtp_valid': 'valid',                  'type': 'personal'},                 {'email': 'ceo@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marcb@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marc.benioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marcbenioff@salesforce.com',                  'smtp_valid': 'invalid',                  'type': 'professional'},                 {'email': 'benioff@frontiernet.net',                  'smtp_valid': 'invalid',                  'type': 'personal'},                 {'email': 'cooldwj@chinaren.com',                  'smtp_valid': 'invalid',                  'type': 'professional'},                 {'email': 'benioff@rcn.com',                  'smtp_valid': 'invalid',                  'type': 'professional'}],      'id': 5244,      'linkedin_url': 'https://www.linkedin.com/in/marcbenioff',      'links': {'aboutme': 'http://www.about.me/marcbenioff',                'amazon': 'http://www.amazon.com/gp/pdp/profile/AZGYQG724J6ON//190-5748375-2756131',                'angel': 'https://angel.co/benioff',                'angellist': 'http://www.angel.co/benioff',                'crunchbase': 'https://www.crunchbase.com/person/marc-benioff',                'facebook': 'http://www.facebook.com/benioff',                'google': 'https://plus.google.com/109586918294369333764',                'google+': 'https://plus.google.com/108172009599607363531/about',                'googleplus': 'https://plus.google.com/108172009599607363531',                'gravatar': 'http://www.gravatar.com/crmmaster',                'gravatar.com': 'http://gravatar.com/crmmaster',                'hi5': 'http://www.hi5.com/friend/p45336146--profile--html',                'instagram': 'http://www.instagram.com/benioff',                'klout': 'http://www.klout.com/benioff',                'linkedin': 'https://www.linkedin.com/in/marcbenioff',                'meetup': 'http://www.meetup.com/members/15867891',                'pinterest': 'http://www.pinterest.com/benioff',                'quora': 'http://www.quora.com/marc-benioff',                'salesforce.com': 'http://www.salesforce.com/company/leadership/executive-team/index.jsp#benioff',                'twicsy': 'http://twicsy.com/u/%40Benioff',                'twitter': 'http://www.twitter.com/benioff'},      'location': 'San Francisco, California, United States',      'name': 'Marc Benioff',      'phones': [],      'profile_pic': 'https://d1hbpr09pwz0sk.cloudfront.net/profile_pic/marc-benioff-4492e698',      'status': 'complete'}  ```  ### Lookup by LinkedIn URL  This is very similar to the previous example, but calls `person/lookup` with the `li_url` parameter.  ```bash  curl -G --location 'https://api.rocketreach.co/v2/api/person/lookup'\\      --header 'Api-Key: <INSERT API KEY>'\\      --data-urlencode 'li_url=https://www.linkedin.com/in/marcbenioff/' ```  **Putting it all together** The following example demonstrates a fully functional application, using the RocketReach API. Here, we lookup contact info of a person, by `name` and `current_employer`.  The source code shown below uses the RocketReach Python SDK. We start by calling initializing the client. This checks to make sure that the `api_key` is valid, and that the user has sufficient credits to perform lookups. Under the covers, the SDK is simply calling the `/account` endpoint. If everything looks good, we now call `person/lookup` to lookup contact info. The library also polls `person/checkStatus` for you, when necessary.  Code:  ```python import rocketreach import os rr = rocketreach.Gateway(api_key=os.environ.get('API_KEY')) lookup = rr.person.lookup(linkedin_url='https://www.linkedin.com/in/marcbenioff') if lookup.is_success:     print(repr(lookup.person)) ```  Output:  ```python      {'current_employer': 'Salesforce',      'current_personal_email': 'benioff@gmail.com',      'current_title': 'Chairman and Co-CEO',      'current_work_email': 'marcb@salesforce.com',      'emails': [{'email': 'm.benioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'mbenioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'benioff@comcast.net',                  'smtp_valid': 'valid',                  'type': 'personal'},                 {'email': 'marc@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marc_benioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'benioff@gmail.com',                  'smtp_valid': 'valid',                  'type': 'personal'},                 {'email': 'benioff@aol.com',                  'smtp_valid': 'valid',                  'type': 'personal'},                 {'email': 'ceo@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marcb@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marc.benioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marcbenioff@salesforce.com',                  'smtp_valid': 'invalid',                  'type': 'professional'},                 {'email': 'benioff@frontiernet.net',                  'smtp_valid': 'invalid',                  'type': 'personal'},                 {'email': 'cooldwj@chinaren.com',                  'smtp_valid': 'invalid',                  'type': 'professional'},                 {'email': 'benioff@rcn.com',                  'smtp_valid': 'invalid',                  'type': 'professional'}],      'id': 5244,      'linkedin_url': 'https://www.linkedin.com/in/marcbenioff',      'links': {'aboutme': 'http://www.about.me/marcbenioff',                'amazon': 'http://www.amazon.com/gp/pdp/profile/AZGYQG724J6ON//190-5748375-2756131',                'angel': 'https://angel.co/benioff',                'angellist': 'http://www.angel.co/benioff',                 'crunchbase': 'https://www.crunchbase.com/person/marc-benioff',                'facebook': 'http://www.facebook.com/benioff',                'google': 'https://plus.google.com/109586918294369333764',                'google+': 'https://plus.google.com/108172009599607363531/about',                'googleplus': 'https://plus.google.com/108172009599607363531',                'gravatar': 'http://www.gravatar.com/crmmaster',                'gravatar.com': 'http://gravatar.com/crmmaster',                'hi5': 'http://www.hi5.com/friend/p45336146--profile--html',                'instagram': 'http://www.instagram.com/benioff',                'klout': 'http://www.klout.com/benioff',                'linkedin': 'https://www.linkedin.com/in/marcbenioff',                'meetup': 'http://www.meetup.com/members/15867891',                'pinterest': 'http://www.pinterest.com/benioff',                'quora': 'http://www.quora.com/marc-benioff',                'salesforce.com': 'http://www.salesforce.com/company/leadership/executive-team/index.jsp#benioff',                'twicsy': 'http://twicsy.com/u/%40Benioff',                'twitter': 'http://www.twitter.com/benioff'},      'location': 'San Francisco, California, United States',      'name': 'Marc Benioff',      'phones': [],      'profile_pic': 'https://d1hbpr09pwz0sk.cloudfront.net/profile_pic/marc-benioff-4492e698',      'status': 'complete'} ```   ### Search People by Role at Company  If you are calling the RocketReach API endpoints directly, you will essentially need to use 3 calls. First call the `person/search` endpoint.  ```bash curl --request 'POST' --location 'https://api.rocketreach.co/api/v2/search'\\      --header 'Api-Key: <INSERT API KEY>'\\      --header 'Content-Type: application/json'\\      --data '{\"query\":{\"name\":[\"Marc Benioff\"],\"current_employer\":[\"Salesforce\"],\"current_title\":[\"CEO\"]}}' ```  Assuming that the `id` for Marc's profile is `5262`, you then call `person/lookup`.  ```bash curl --request 'GET' --location 'https://api.rocketreach.co/api/v2/lookupProfile'\\      --header 'Api-Key: <INSERT API KEY>'\\      --data-urlencode 'id=5262' ```  If the status returned by the call is not `complete` or `failed`, then you will need to poll `person/checkStatus` untill it returns either `complete` or `failed`.  ```bash curl --request 'GET' --location 'https://api.rocketreach.co/api/v2/checkStatus'\\      --header 'Api-Key: <INSERT API KEY>'\\      --data-urlencode 'ids=5262' ```  **Putting it all together** In this example, we will search for people with a specific name and title, at a company. We will then lookup contact info for one of the search results.  Code: ```python     import rocketreach     import os     rr = rocketreach.Gateway(api_key=os.environ.get('API_KEY'))     search = rr.person.search()     # Build up our search query     search = search.filter(name='Marc Benioff', current_title='CEO', current_employer='Salesforce')     # Call the search endpoint with our query     result = search.execute()     if result.is_success:         lookup = rr.person.lookup(result.people[0].id)         if lookup.is_success:             print(repr(lookup.person)) ```  Output: ```python {     'current_employer': 'Salesforce',     'current_personal_email': 'benioff@gmail.com',     'current_title': 'Chairman and Co-CEO',     'current_work_email': 'marcb@salesforce.com',     'emails': [{'email': 'm.benioff@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'mbenioff@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'benioff@comcast.net',              'smtp_valid': 'valid',              'type': 'personal'},             {'email': 'marc@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'marc_benioff@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'benioff@gmail.com',              'smtp_valid': 'valid',              'type': 'personal'},             {'email': 'benioff@aol.com',              'smtp_valid': 'valid',              'type': 'personal'},             {'email': 'ceo@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'marcb@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'marc.benioff@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'marcbenioff@salesforce.com',              'smtp_valid': 'invalid',              'type': 'professional'},             {'email': 'benioff@frontiernet.net',              'smtp_valid': 'invalid',              'type': 'personal'},             {'email': 'cooldwj@chinaren.com',              'smtp_valid': 'invalid',              'type': 'professional'},             {'email': 'benioff@rcn.com',              'smtp_valid': 'invalid',              'type': 'professional'}],     'id': 5244,     'linkedin_url': 'https://www.linkedin.com/in/marcbenioff',     'links': {'aboutme': 'http://www.about.me/marcbenioff',            'amazon': 'http://www.amazon.com/gp/pdp/profile/AZGYQG724J6ON//190-5748375-2756131',            'angel': 'https://angel.co/benioff',            'angellist': 'http://www.angel.co/benioff',            'crunchbase': 'https://www.crunchbase.com/person/marc-benioff',            'facebook': 'http://www.facebook.com/benioff',            'google': 'https://plus.google.com/109586918294369333764',            'google+': 'https://plus.google.com/108172009599607363531/about',            'googleplus': 'https://plus.google.com/108172009599607363531',            'gravatar': 'http://www.gravatar.com/crmmaster',            'gravatar.com': 'http://gravatar.com/crmmaster',            'hi5': 'http://www.hi5.com/friend/p45336146--profile--html',            'instagram': 'http://www.instagram.com/benioff',            'klout': 'http://www.klout.com/benioff',            'linkedin': 'https://www.linkedin.com/in/marcbenioff',            'meetup': 'http://www.meetup.com/members/15867891',            'pinterest': 'http://www.pinterest.com/benioff',            'quora': 'http://www.quora.com/marc-benioff',            'salesforce.com': 'http://www.salesforce.com/company/leadership/executive-team/index.jsp#benioff',            'twicsy': 'http://twicsy.com/u/%40Benioff',            'twitter': 'http://www.twitter.com/benioff'},     'location': 'San Francisco, California, United States',     'name': 'Marc Benioff',     'phones': [],     'profile_pic': 'https://d1hbpr09pwz0sk.cloudfront.net/profile_pic/marc-benioff-4492e698',     'status': 'complete' }  ```  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@rocketreach.co
    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
from decimal import Decimal
import enum
import email
import json
import os
import io
import atexit
from multiprocessing.pool import ThreadPool
import re
import tempfile
import typing
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict
from urllib.parse import urlparse, quote
from urllib3.fields import RequestField as RequestFieldBase

import frozendict

from openapi_client import rest
from openapi_client.configuration import Configuration
from openapi_client.exceptions import ApiTypeError, ApiValueError
from openapi_client.schemas import (
    NoneClass,
    BoolClass,
    Schema,
    FileIO,
    BinarySchema,
    date,
    datetime,
    none_type,
    Unset,
    unset,
)


class RequestField(RequestFieldBase):
    def __eq__(self, other):
        if not isinstance(other, RequestField):
            return False
        return self.__dict__ == other.__dict__


class JSONEncoder(json.JSONEncoder):
    compact_separators = (',', ':')

    def default(self, obj):
        if isinstance(obj, str):
            return str(obj)
        elif isinstance(obj, float):
            return float(obj)
        elif isinstance(obj, int):
            return int(obj)
        elif isinstance(obj, Decimal):
            if obj.as_tuple().exponent >= 0:
                return int(obj)
            return float(obj)
        elif isinstance(obj, NoneClass):
            return None
        elif isinstance(obj, BoolClass):
            return bool(obj)
        elif isinstance(obj, (dict, frozendict.frozendict)):
            return {key: self.default(val) for key, val in obj.items()}
        elif isinstance(obj, (list, tuple)):
            return [self.default(item) for item in obj]
        raise ApiValueError('Unable to prepare type {} for serialization'.format(obj.__class__.__name__))


class ParameterInType(enum.Enum):
    QUERY = 'query'
    HEADER = 'header'
    PATH = 'path'
    COOKIE = 'cookie'


class ParameterStyle(enum.Enum):
    MATRIX = 'matrix'
    LABEL = 'label'
    FORM = 'form'
    SIMPLE = 'simple'
    SPACE_DELIMITED = 'spaceDelimited'
    PIPE_DELIMITED = 'pipeDelimited'
    DEEP_OBJECT = 'deepObject'


class PrefixSeparatorIterator:
    # A class to store prefixes and separators for rfc6570 expansions

    def __init__(self, prefix: str, separator: str):
        self.prefix = prefix
        self.separator = separator
        self.first = True
        if separator in {'.', '|', '%20'}:
            item_separator = separator
        else:
            item_separator = ','
        self.item_separator = item_separator

    def __iter__(self):
        return self

    def __next__(self):
        if self.first:
            self.first = False
            return self.prefix
        return self.separator


class ParameterSerializerBase:
    @classmethod
    def _get_default_explode(cls, style: ParameterStyle) -> bool:
        return False

    @staticmethod
    def __ref6570_item_value(in_data: typing.Any, percent_encode: bool):
        """
        Get representation if str/float/int/None/items in list/ values in dict
        None is returned if an item is undefined, use cases are value=
        - None
        - []
        - {}
        - [None, None None]
        - {'a': None, 'b': None}
        """
        if type(in_data) in {str, float, int}:
            if percent_encode:
                return quote(str(in_data))
            return str(in_data)
        elif isinstance(in_data, none_type):
            # ignored by the expansion process https://datatracker.ietf.org/doc/html/rfc6570#section-3.2.1
            return None
        elif isinstance(in_data, list) and not in_data:
            # ignored by the expansion process https://datatracker.ietf.org/doc/html/rfc6570#section-3.2.1
            return None
        elif isinstance(in_data, dict) and not in_data:
            # ignored by the expansion process https://datatracker.ietf.org/doc/html/rfc6570#section-3.2.1
            return None
        raise ApiValueError('Unable to generate a ref6570 item representation of {}'.format(in_data))

    @staticmethod
    def _to_dict(name: str, value: str):
        return {name: value}

    @classmethod
    def __ref6570_str_float_int_expansion(
        cls,
        variable_name: str,
        in_data: typing.Any,
        explode: bool,
        percent_encode: bool,
        prefix_separator_iterator: PrefixSeparatorIterator,
        var_name_piece: str,
        named_parameter_expansion: bool
    ) -> str:
        item_value = cls.__ref6570_item_value(in_data, percent_encode)
        if item_value is None or (item_value == '' and prefix_separator_iterator.separator == ';'):
            return next(prefix_separator_iterator) + var_name_piece
        value_pair_equals = '=' if named_parameter_expansion else ''
        return next(prefix_separator_iterator) + var_name_piece + value_pair_equals + item_value

    @classmethod
    def __ref6570_list_expansion(
        cls,
        variable_name: str,
        in_data: typing.Any,
        explode: bool,
        percent_encode: bool,
        prefix_separator_iterator: PrefixSeparatorIterator,
        var_name_piece: str,
        named_parameter_expansion: bool
    ) -> str:
        item_values = [cls.__ref6570_item_value(v, percent_encode) for v in in_data]
        item_values = [v for v in item_values if v is not None]
        if not item_values:
            # ignored by the expansion process https://datatracker.ietf.org/doc/html/rfc6570#section-3.2.1
            return ""
        value_pair_equals = '=' if named_parameter_expansion else ''
        if not explode:
            return (
                next(prefix_separator_iterator) +
                var_name_piece +
                value_pair_equals +
                prefix_separator_iterator.item_separator.join(item_values)
            )
        # exploded
        return next(prefix_separator_iterator) + next(prefix_separator_iterator).join(
            [var_name_piece + value_pair_equals + val for val in item_values]
        )

    @classmethod
    def __ref6570_dict_expansion(
        cls,
        variable_name: str,
        in_data: typing.Any,
        explode: bool,
        percent_encode: bool,
        prefix_separator_iterator: PrefixSeparatorIterator,
        var_name_piece: str,
        named_parameter_expansion: bool
    ) -> str:
        in_data_transformed = {key: cls.__ref6570_item_value(val, percent_encode) for key, val in in_data.items()}
        in_data_transformed = {key: val for key, val in in_data_transformed.items() if val is not None}
        if not in_data_transformed:
            # ignored by the expansion process https://datatracker.ietf.org/doc/html/rfc6570#section-3.2.1
            return ""
        value_pair_equals = '=' if named_parameter_expansion else ''
        if not explode:
            return (
                next(prefix_separator_iterator) +
                var_name_piece + value_pair_equals +
                prefix_separator_iterator.item_separator.join(
                    prefix_separator_iterator.item_separator.join(
                        item_pair
                    ) for item_pair in in_data_transformed.items()
                )
            )
        # exploded
        return next(prefix_separator_iterator) + next(prefix_separator_iterator).join(
            [key + '=' + val for key, val in in_data_transformed.items()]
        )

    @classmethod
    def _ref6570_expansion(
        cls,
        variable_name: str,
        in_data: typing.Any,
        explode: bool,
        percent_encode: bool,
        prefix_separator_iterator: PrefixSeparatorIterator
    ) -> str:
        """
        Separator is for separate variables like dict with explode true, not for array item separation
        """
        named_parameter_expansion = prefix_separator_iterator.separator in {'&', ';'}
        var_name_piece = variable_name if named_parameter_expansion else ''
        if type(in_data) in {str, float, int}:
            return cls.__ref6570_str_float_int_expansion(
                variable_name,
                in_data,
                explode,
                percent_encode,
                prefix_separator_iterator,
                var_name_piece,
                named_parameter_expansion
            )
        elif isinstance(in_data, none_type):
            # ignored by the expansion process https://datatracker.ietf.org/doc/html/rfc6570#section-3.2.1
            return ""
        elif isinstance(in_data, list):
            return cls.__ref6570_list_expansion(
                variable_name,
                in_data,
                explode,
                percent_encode,
                prefix_separator_iterator,
                var_name_piece,
                named_parameter_expansion
            )
        elif isinstance(in_data, dict):
            return cls.__ref6570_dict_expansion(
                variable_name,
                in_data,
                explode,
                percent_encode,
                prefix_separator_iterator,
                var_name_piece,
                named_parameter_expansion
            )
        # bool, bytes, etc
        raise ApiValueError('Unable to generate a ref6570 representation of {}'.format(in_data))


class StyleFormSerializer(ParameterSerializerBase):
    @classmethod
    def _get_default_explode(cls, style: ParameterStyle) -> bool:
        if style is ParameterStyle.FORM:
            return True
        return super()._get_default_explode(style)

    def _serialize_form(
        self,
        in_data: typing.Union[None, int, float, str, bool, dict, list],
        name: str,
        explode: bool,
        percent_encode: bool,
        prefix_separator_iterator: typing.Optional[PrefixSeparatorIterator] = None
    ) -> str:
        if prefix_separator_iterator is None:
            prefix_separator_iterator = PrefixSeparatorIterator('', '&')
        return self._ref6570_expansion(
            variable_name=name,
            in_data=in_data,
            explode=explode,
            percent_encode=percent_encode,
            prefix_separator_iterator=prefix_separator_iterator
        )


class StyleSimpleSerializer(ParameterSerializerBase):

    def _serialize_simple(
        self,
        in_data: typing.Union[None, int, float, str, bool, dict, list],
        name: str,
        explode: bool,
        percent_encode: bool
    ) -> str:
        prefix_separator_iterator = PrefixSeparatorIterator('', ',')
        return self._ref6570_expansion(
            variable_name=name,
            in_data=in_data,
            explode=explode,
            percent_encode=percent_encode,
            prefix_separator_iterator=prefix_separator_iterator
        )


class JSONDetector:
    """
    Works for:
    application/json
    application/json; charset=UTF-8
    application/json-patch+json
    application/geo+json
    """
    __json_content_type_pattern = re.compile("application/[^+]*[+]?(json);?.*")

    @classmethod
    def _content_type_is_json(cls, content_type: str) -> bool:
        if cls.__json_content_type_pattern.match(content_type):
            return True
        return False


@dataclass
class ParameterBase(JSONDetector):
    name: str
    in_type: ParameterInType
    required: bool
    style: typing.Optional[ParameterStyle]
    explode: typing.Optional[bool]
    allow_reserved: typing.Optional[bool]
    schema: typing.Optional[typing.Type[Schema]]
    content: typing.Optional[typing.Dict[str, typing.Type[Schema]]]

    __style_to_in_type = {
        ParameterStyle.MATRIX: {ParameterInType.PATH},
        ParameterStyle.LABEL: {ParameterInType.PATH},
        ParameterStyle.FORM: {ParameterInType.QUERY, ParameterInType.COOKIE},
        ParameterStyle.SIMPLE: {ParameterInType.PATH, ParameterInType.HEADER},
        ParameterStyle.SPACE_DELIMITED: {ParameterInType.QUERY},
        ParameterStyle.PIPE_DELIMITED: {ParameterInType.QUERY},
        ParameterStyle.DEEP_OBJECT: {ParameterInType.QUERY},
    }
    __in_type_to_default_style = {
        ParameterInType.QUERY: ParameterStyle.FORM,
        ParameterInType.PATH: ParameterStyle.SIMPLE,
        ParameterInType.HEADER: ParameterStyle.SIMPLE,
        ParameterInType.COOKIE: ParameterStyle.FORM,
    }
    __disallowed_header_names = {'Accept', 'Content-Type', 'Authorization'}
    _json_encoder = JSONEncoder()

    @classmethod
    def __verify_style_to_in_type(cls, style: typing.Optional[ParameterStyle], in_type: ParameterInType):
        if style is None:
            return
        in_type_set = cls.__style_to_in_type[style]
        if in_type not in in_type_set:
            raise ValueError(
                'Invalid style and in_type combination. For style={} only in_type={} are allowed'.format(
                    style, in_type_set
                )
            )

    def __init__(
        self,
        name: str,
        in_type: ParameterInType,
        required: bool = False,
        style: typing.Optional[ParameterStyle] = None,
        explode: bool = False,
        allow_reserved: typing.Optional[bool] = None,
        schema: typing.Optional[typing.Type[Schema]] = None,
        content: typing.Optional[typing.Dict[str, typing.Type[Schema]]] = None
    ):
        if schema is None and content is None:
            raise ValueError('Value missing; Pass in either schema or content')
        if schema and content:
            raise ValueError('Too many values provided. Both schema and content were provided. Only one may be input')
        if name in self.__disallowed_header_names and in_type is ParameterInType.HEADER:
            raise ValueError('Invalid name, name may not be one of {}'.format(self.__disallowed_header_names))
        self.__verify_style_to_in_type(style, in_type)
        if content is None and style is None:
            style = self.__in_type_to_default_style[in_type]
        if content is not None and in_type in self.__in_type_to_default_style and len(content) != 1:
            raise ValueError('Invalid content length, content length must equal 1')
        self.in_type = in_type
        self.name = name
        self.required = required
        self.style = style
        self.explode = explode
        self.allow_reserved = allow_reserved
        self.schema = schema
        self.content = content

    def _serialize_json(
        self,
        in_data: typing.Union[None, int, float, str, bool, dict, list],
        eliminate_whitespace: bool = False
    ) -> str:
        if eliminate_whitespace:
            return json.dumps(in_data, separators=self._json_encoder.compact_separators)
        return json.dumps(in_data)


class PathParameter(ParameterBase, StyleSimpleSerializer):

    def __init__(
        self,
        name: str,
        required: bool = False,
        style: typing.Optional[ParameterStyle] = None,
        explode: bool = False,
        allow_reserved: typing.Optional[bool] = None,
        schema: typing.Optional[typing.Type[Schema]] = None,
        content: typing.Optional[typing.Dict[str, typing.Type[Schema]]] = None
    ):
        super().__init__(
            name,
            in_type=ParameterInType.PATH,
            required=required,
            style=style,
            explode=explode,
            allow_reserved=allow_reserved,
            schema=schema,
            content=content
        )

    def __serialize_label(
        self,
        in_data: typing.Union[None, int, float, str, bool, dict, list]
    ) -> typing.Dict[str, str]:
        prefix_separator_iterator = PrefixSeparatorIterator('.', '.')
        value = self._ref6570_expansion(
            variable_name=self.name,
            in_data=in_data,
            explode=self.explode,
            percent_encode=True,
            prefix_separator_iterator=prefix_separator_iterator
        )
        return self._to_dict(self.name, value)

    def __serialize_matrix(
        self,
        in_data: typing.Union[None, int, float, str, bool, dict, list]
    ) -> typing.Dict[str, str]:
        prefix_separator_iterator = PrefixSeparatorIterator(';', ';')
        value = self._ref6570_expansion(
            variable_name=self.name,
            in_data=in_data,
            explode=self.explode,
            percent_encode=True,
            prefix_separator_iterator=prefix_separator_iterator
        )
        return self._to_dict(self.name, value)

    def __serialize_simple(
        self,
        in_data: typing.Union[None, int, float, str, bool, dict, list],
    ) -> typing.Dict[str, str]:
        value = self._serialize_simple(
            in_data=in_data,
            name=self.name,
            explode=self.explode,
            percent_encode=True
        )
        return self._to_dict(self.name, value)

    def serialize(
        self,
        in_data: typing.Union[
            Schema, Decimal, int, float, str, date, datetime, None, bool, list, tuple, dict, frozendict.frozendict]
    ) -> typing.Dict[str, str]:
        if self.schema:
            cast_in_data = self.schema(in_data)
            cast_in_data = self._json_encoder.default(cast_in_data)
            """
            simple -> path
                path:
                    returns path_params: dict
            label -> path
                returns path_params
            matrix -> path
                returns path_params
            """
            if self.style:
                if self.style is ParameterStyle.SIMPLE:
                    return self.__serialize_simple(cast_in_data)
                elif self.style is ParameterStyle.LABEL:
                    return self.__serialize_label(cast_in_data)
                elif self.style is ParameterStyle.MATRIX:
                    return self.__serialize_matrix(cast_in_data)
        # self.content will be length one
        for content_type, schema in self.content.items():
            cast_in_data = schema(in_data)
            cast_in_data = self._json_encoder.default(cast_in_data)
            if self._content_type_is_json(content_type):
                value = self._serialize_json(cast_in_data)
                return self._to_dict(self.name, value)
            raise NotImplementedError('Serialization of {} has not yet been implemented'.format(content_type))


class QueryParameter(ParameterBase, StyleFormSerializer):

    def __init__(
        self,
        name: str,
        required: bool = False,
        style: typing.Optional[ParameterStyle] = None,
        explode: typing.Optional[bool] = None,
        allow_reserved: typing.Optional[bool] = None,
        schema: typing.Optional[typing.Type[Schema]] = None,
        content: typing.Optional[typing.Dict[str, typing.Type[Schema]]] = None
    ):
        used_style = ParameterStyle.FORM if style is None else style
        used_explode = self._get_default_explode(used_style) if explode is None else explode

        super().__init__(
            name,
            in_type=ParameterInType.QUERY,
            required=required,
            style=used_style,
            explode=used_explode,
            allow_reserved=allow_reserved,
            schema=schema,
            content=content
        )

    def __serialize_space_delimited(
        self,
        in_data: typing.Union[None, int, float, str, bool, dict, list],
        prefix_separator_iterator: typing.Optional[PrefixSeparatorIterator]
    ) -> typing.Dict[str, str]:
        if prefix_separator_iterator is None:
            prefix_separator_iterator = self.get_prefix_separator_iterator()
        value = self._ref6570_expansion(
            variable_name=self.name,
            in_data=in_data,
            explode=self.explode,
            percent_encode=True,
            prefix_separator_iterator=prefix_separator_iterator
        )
        return self._to_dict(self.name, value)

    def __serialize_pipe_delimited(
        self,
        in_data: typing.Union[None, int, float, str, bool, dict, list],
        prefix_separator_iterator: typing.Optional[PrefixSeparatorIterator]
    ) -> typing.Dict[str, str]:
        if prefix_separator_iterator is None:
            prefix_separator_iterator = self.get_prefix_separator_iterator()
        value = self._ref6570_expansion(
            variable_name=self.name,
            in_data=in_data,
            explode=self.explode,
            percent_encode=True,
            prefix_separator_iterator=prefix_separator_iterator
        )
        return self._to_dict(self.name, value)

    def __serialize_form(
        self,
        in_data: typing.Union[None, int, float, str, bool, dict, list],
        prefix_separator_iterator: typing.Optional[PrefixSeparatorIterator]
    ) -> typing.Dict[str, str]:
        if prefix_separator_iterator is None:
            prefix_separator_iterator = self.get_prefix_separator_iterator()
        value = self._serialize_form(
            in_data,
            name=self.name,
            explode=self.explode,
            percent_encode=True,
            prefix_separator_iterator=prefix_separator_iterator
        )
        return self._to_dict(self.name, value)

    def get_prefix_separator_iterator(self) -> typing.Optional[PrefixSeparatorIterator]:
        if self.style is ParameterStyle.FORM:
            return PrefixSeparatorIterator('?', '&')
        elif self.style is ParameterStyle.SPACE_DELIMITED:
            return PrefixSeparatorIterator('', '%20')
        elif self.style is ParameterStyle.PIPE_DELIMITED:
            return PrefixSeparatorIterator('', '|')

    def serialize(
        self,
        in_data: typing.Union[
            Schema, Decimal, int, float, str, date, datetime, None, bool, list, tuple, dict, frozendict.frozendict],
        prefix_separator_iterator: typing.Optional[PrefixSeparatorIterator] = None
    ) -> typing.Dict[str, str]:
        if self.schema:
            cast_in_data = self.schema(in_data)
            cast_in_data = self._json_encoder.default(cast_in_data)
            """
            form -> query
                query:
                    - GET/HEAD/DELETE: could use fields
                    - PUT/POST: must use urlencode to send parameters
                    returns fields: tuple
            spaceDelimited -> query
                returns fields
            pipeDelimited -> query
                returns fields
            deepObject -> query, https://github.com/OAI/OpenAPI-Specification/issues/1706
                returns fields
            """
            if self.style:
                # TODO update query ones to omit setting values when [] {} or None is input
                if self.style is ParameterStyle.FORM:
                    return self.__serialize_form(cast_in_data, prefix_separator_iterator)
                elif self.style is ParameterStyle.SPACE_DELIMITED:
                    return self.__serialize_space_delimited(cast_in_data, prefix_separator_iterator)
                elif self.style is ParameterStyle.PIPE_DELIMITED:
                    return self.__serialize_pipe_delimited(cast_in_data, prefix_separator_iterator)
        # self.content will be length one
        if prefix_separator_iterator is None:
            prefix_separator_iterator = self.get_prefix_separator_iterator()
        for content_type, schema in self.content.items():
            cast_in_data = schema(in_data)
            cast_in_data = self._json_encoder.default(cast_in_data)
            if self._content_type_is_json(content_type):
                value = self._serialize_json(cast_in_data, eliminate_whitespace=True)
                return self._to_dict(
                    self.name,
                    next(prefix_separator_iterator) + self.name + '=' + quote(value)
                )
            raise NotImplementedError('Serialization of {} has not yet been implemented'.format(content_type))


class CookieParameter(ParameterBase, StyleFormSerializer):

    def __init__(
        self,
        name: str,
        required: bool = False,
        style: typing.Optional[ParameterStyle] = None,
        explode: typing.Optional[bool] = None,
        allow_reserved: typing.Optional[bool] = None,
        schema: typing.Optional[typing.Type[Schema]] = None,
        content: typing.Optional[typing.Dict[str, typing.Type[Schema]]] = None
    ):
        used_style = ParameterStyle.FORM if style is None and content is None and schema else style
        used_explode = self._get_default_explode(used_style) if explode is None else explode

        super().__init__(
            name,
            in_type=ParameterInType.COOKIE,
            required=required,
            style=used_style,
            explode=used_explode,
            allow_reserved=allow_reserved,
            schema=schema,
            content=content
        )

    def serialize(
        self,
        in_data: typing.Union[
            Schema, Decimal, int, float, str, date, datetime, None, bool, list, tuple, dict, frozendict.frozendict]
    ) -> typing.Dict[str, str]:
        if self.schema:
            cast_in_data = self.schema(in_data)
            cast_in_data = self._json_encoder.default(cast_in_data)
            """
            form -> cookie
                returns fields: tuple
            """
            if self.style:
                """
                TODO add escaping of comma, space, equals
                or turn encoding on
                """
                value = self._serialize_form(
                    cast_in_data,
                    explode=self.explode,
                    name=self.name,
                    percent_encode=False,
                    prefix_separator_iterator=PrefixSeparatorIterator('', '&')
                )
                return self._to_dict(self.name, value)
        # self.content will be length one
        for content_type, schema in self.content.items():
            cast_in_data = schema(in_data)
            cast_in_data = self._json_encoder.default(cast_in_data)
            if self._content_type_is_json(content_type):
                value = self._serialize_json(cast_in_data)
                return self._to_dict(self.name, value)
            raise NotImplementedError('Serialization of {} has not yet been implemented'.format(content_type))


class HeaderParameter(ParameterBase, StyleSimpleSerializer):
    def __init__(
        self,
        name: str,
        required: bool = False,
        style: typing.Optional[ParameterStyle] = None,
        explode: bool = False,
        allow_reserved: typing.Optional[bool] = None,
        schema: typing.Optional[typing.Type[Schema]] = None,
        content: typing.Optional[typing.Dict[str, typing.Type[Schema]]] = None
    ):
        super().__init__(
            name,
            in_type=ParameterInType.HEADER,
            required=required,
            style=style,
            explode=explode,
            allow_reserved=allow_reserved,
            schema=schema,
            content=content
        )

    @staticmethod
    def __to_headers(in_data: typing.Tuple[typing.Tuple[str, str], ...]) -> HTTPHeaderDict:
        data = tuple(t for t in in_data if t)
        headers = HTTPHeaderDict()
        if not data:
            return headers
        headers.extend(data)
        return headers

    def serialize(
        self,
        in_data: typing.Union[
            Schema, Decimal, int, float, str, date, datetime, None, bool, list, tuple, dict, frozendict.frozendict]
    ) -> HTTPHeaderDict:
        if self.schema:
            cast_in_data = self.schema(in_data)
            cast_in_data = self._json_encoder.default(cast_in_data)
            """
            simple -> header
                headers: PoolManager needs a mapping, tuple is close
                    returns headers: dict
            """
            if self.style:
                value = self._serialize_simple(cast_in_data, self.name, self.explode, False)
                return self.__to_headers(((self.name, value),))
        # self.content will be length one
        for content_type, schema in self.content.items():
            cast_in_data = schema(in_data)
            cast_in_data = self._json_encoder.default(cast_in_data)
            if self._content_type_is_json(content_type):
                value = self._serialize_json(cast_in_data)
                return self.__to_headers(((self.name, value),))
            raise NotImplementedError('Serialization of {} has not yet been implemented'.format(content_type))


class Encoding:
    def __init__(
        self,
        content_type: str,
        headers: typing.Optional[typing.Dict[str, HeaderParameter]] = None,
        style: typing.Optional[ParameterStyle] = None,
        explode: bool = False,
        allow_reserved: bool = False,
    ):
        self.content_type = content_type
        self.headers = headers
        self.style = style
        self.explode = explode
        self.allow_reserved = allow_reserved


@dataclass
class MediaType:
    """
    Used to store request and response body schema information
    encoding:
        A map between a property name and its encoding information.
        The key, being the property name, MUST exist in the schema as a property.
        The encoding object SHALL only apply to requestBody objects when the media type is
        multipart or application/x-www-form-urlencoded.
    """
    schema: typing.Optional[typing.Type[Schema]] = None
    encoding: typing.Optional[typing.Dict[str, Encoding]] = None


@dataclass
class ApiResponse:
    response: urllib3.HTTPResponse
    body: typing.Union[Unset, Schema] = unset
    headers: typing.Union[Unset, typing.Dict[str, Schema]] = unset

    def __init__(
        self,
        response: urllib3.HTTPResponse,
        body: typing.Union[Unset, Schema] = unset,
        headers: typing.Union[Unset, typing.Dict[str, Schema]] = unset
    ):
        """
        pycharm needs this to prevent 'Unexpected argument' warnings
        """
        self.response = response
        self.body = body
        self.headers = headers


@dataclass
class ApiResponseWithoutDeserialization(ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[Unset, typing.Type[Schema]] = unset
    headers: typing.Union[Unset, typing.List[HeaderParameter]] = unset


class OpenApiResponse(JSONDetector):
    __filename_content_disposition_pattern = re.compile('filename="(.+?)"')

    def __init__(
        self,
        response_cls: typing.Type[ApiResponse] = ApiResponse,
        content: typing.Optional[typing.Dict[str, MediaType]] = None,
        headers: typing.Optional[typing.List[HeaderParameter]] = None,
    ):
        self.headers = headers
        if content is not None and len(content) == 0:
            raise ValueError('Invalid value for content, the content dict must have >= 1 entry')
        self.content = content
        self.response_cls = response_cls

    @staticmethod
    def __deserialize_json(response: urllib3.HTTPResponse) -> typing.Any:
        # python must be >= 3.9 so we can pass in bytes into json.loads
        return json.loads(response.data)

    @staticmethod
    def __file_name_from_response_url(response_url: typing.Optional[str]) -> typing.Optional[str]:
        if response_url is None:
            return None
        url_path = urlparse(response_url).path
        if url_path:
            path_basename = os.path.basename(url_path)
            if path_basename:
                _filename, ext = os.path.splitext(path_basename)
                if ext:
                    return path_basename
        return None

    @classmethod
    def __file_name_from_content_disposition(cls, content_disposition: typing.Optional[str]) -> typing.Optional[str]:
        if content_disposition is None:
            return None
        match = cls.__filename_content_disposition_pattern.search(content_disposition)
        if not match:
            return None
        return match.group(1)

    def __deserialize_application_octet_stream(
        self, response: urllib3.HTTPResponse
    ) -> typing.Union[bytes, io.BufferedReader]:
        """
        urllib3 use cases:
        1. when preload_content=True (stream=False) then supports_chunked_reads is False and bytes are returned
        2. when preload_content=False (stream=True) then supports_chunked_reads is True and
            a file will be written and returned
        """
        if response.supports_chunked_reads():
            file_name = (
                self.__file_name_from_content_disposition(response.headers.get('content-disposition'))
                or self.__file_name_from_response_url(response.geturl())
            )

            if file_name is None:
                _fd, path = tempfile.mkstemp()
            else:
                path = os.path.join(tempfile.gettempdir(), file_name)

            with open(path, 'wb') as new_file:
                chunk_size = 1024
                while True:
                    data = response.read(chunk_size)
                    if not data:
                        break
                    new_file.write(data)
            # release_conn is needed for streaming connections only
            response.release_conn()
            new_file = open(path, 'rb')
            return new_file
        else:
            return response.data

    @staticmethod
    def __deserialize_multipart_form_data(
        response: urllib3.HTTPResponse
    ) -> typing.Dict[str, typing.Any]:
        msg = email.message_from_bytes(response.data)
        return {
            part.get_param("name", header="Content-Disposition"): part.get_payload(
                decode=True
            ).decode(part.get_content_charset())
            if part.get_content_charset()
            else part.get_payload()
            for part in msg.get_payload()
        }

    def deserialize(self, response: urllib3.HTTPResponse, configuration: Configuration) -> ApiResponse:
        content_type = response.getheader('content-type')
        deserialized_body = unset
        streamed = response.supports_chunked_reads()

        deserialized_headers = unset
        if self.headers is not None:
            # TODO add header deserialiation here
            pass

        if self.content is not None:
            if content_type not in self.content:
                raise ApiValueError(
                    f"Invalid content_type returned. Content_type='{content_type}' was returned "
                    f"when only {str(set(self.content))} are defined for status_code={str(response.status)}"
                )
            body_schema = self.content[content_type].schema
            if body_schema is None:
                # some specs do not define response content media type schemas
                return self.response_cls(
                    response=response,
                    headers=deserialized_headers,
                    body=unset
                )

            if self._content_type_is_json(content_type):
                body_data = self.__deserialize_json(response)
            elif content_type == 'application/octet-stream':
                body_data = self.__deserialize_application_octet_stream(response)
            elif content_type.startswith('multipart/form-data'):
                body_data = self.__deserialize_multipart_form_data(response)
                content_type = 'multipart/form-data'
            else:
                raise NotImplementedError('Deserialization of {} has not yet been implemented'.format(content_type))
            deserialized_body = body_schema.from_openapi_data_oapg(
                body_data, _configuration=configuration)
        elif streamed:
            response.release_conn()

        return self.response_cls(
            response=response,
            headers=deserialized_headers,
            body=deserialized_body
        )


class ApiClient:
    """Generic API client for OpenAPI client library builds.

    OpenAPI generic API client. This client handles the client-
    server communication, and is invariant across implementations. Specifics of
    the methods and models for each application are generated from the OpenAPI
    templates.

    NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech
    Do not edit the class manually.

    :param configuration: .Configuration object for this client
    :param header_name: a header to pass when making calls to the API.
    :param header_value: a header value to pass when making calls to
        the API.
    :param cookie: a cookie to include in the header when making calls
        to the API
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    _pool = None

    def __init__(
        self,
        configuration: typing.Optional[Configuration] = None,
        header_name: typing.Optional[str] = None,
        header_value: typing.Optional[str] = None,
        cookie: typing.Optional[str] = None,
        pool_threads: int = 1
    ):
        if configuration is None:
            configuration = Configuration()
        self.configuration = configuration
        self.pool_threads = pool_threads

        self.rest_client = rest.RESTClientObject(configuration)
        self.default_headers = HTTPHeaderDict()
        if header_name is not None:
            self.default_headers[header_name] = header_value
        self.cookie = cookie
        # Set default User-Agent.
        self.user_agent = 'OpenAPI-Generator/1.0.0/python'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        if self._pool:
            self._pool.close()
            self._pool.join()
            self._pool = None
            if hasattr(atexit, 'unregister'):
                atexit.unregister(self.close)

    @property
    def pool(self):
        """Create thread pool on first request
         avoids instantiating unused threadpool for blocking clients.
        """
        if self._pool is None:
            atexit.register(self.close)
            self._pool = ThreadPool(self.pool_threads)
        return self._pool

    @property
    def user_agent(self):
        """User agent for this API client"""
        return self.default_headers['User-Agent']

    @user_agent.setter
    def user_agent(self, value):
        self.default_headers['User-Agent'] = value

    def set_default_header(self, header_name, header_value):
        self.default_headers[header_name] = header_value

    def __call_api(
        self,
        resource_path: str,
        method: str,
        headers: typing.Optional[HTTPHeaderDict] = None,
        body: typing.Optional[typing.Union[str, bytes]] = None,
        fields: typing.Optional[typing.Tuple[typing.Tuple[str, str], ...]] = None,
        auth_settings: typing.Optional[typing.List[str]] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        host: typing.Optional[str] = None,
    ) -> urllib3.HTTPResponse:

        # header parameters
        used_headers = HTTPHeaderDict(self.default_headers)
        if self.cookie:
            headers['Cookie'] = self.cookie

        # auth setting
        self.update_params_for_auth(used_headers,
                                    auth_settings, resource_path, method, body)

        # must happen after cookie setting and auth setting in case user is overriding those
        if headers:
            used_headers.update(headers)

        # request url
        if host is None:
            url = self.configuration.host + resource_path
        else:
            # use server/host defined in path or operation instead
            url = host + resource_path

        # perform request and return response
        response = self.request(
            method,
            url,
            headers=used_headers,
            fields=fields,
            body=body,
            stream=stream,
            timeout=timeout,
        )
        return response

    def call_api(
        self,
        resource_path: str,
        method: str,
        headers: typing.Optional[HTTPHeaderDict] = None,
        body: typing.Optional[typing.Union[str, bytes]] = None,
        fields: typing.Optional[typing.Tuple[typing.Tuple[str, str], ...]] = None,
        auth_settings: typing.Optional[typing.List[str]] = None,
        async_req: typing.Optional[bool] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        host: typing.Optional[str] = None,
    ) -> urllib3.HTTPResponse:
        """Makes the HTTP request (synchronous) and returns deserialized data.

        To make an async_req request, set the async_req parameter.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param headers: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param fields: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings: Auth Settings names for the request.
        :param async_req: execute request asynchronously
        :type async_req: bool, optional TODO remove, unused
        :param stream: if True, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Also when True, if the openapi spec describes a file download,
                                 the data will be written to a local filesystme file and the BinarySchema
                                 instance will also inherit from FileSchema and FileIO
                                 Default is False.
        :type stream: bool, optional
        :param timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param host: api endpoint host
        :return:
            If async_req parameter is True,
            the request will be called asynchronously.
            The method will return the request thread.
            If parameter async_req is False or missing,
            then the method will return the response directly.
        """

        if not async_req:
            return self.__call_api(
                resource_path,
                method,
                headers,
                body,
                fields,
                auth_settings,
                stream,
                timeout,
                host,
            )

        return self.pool.apply_async(
            self.__call_api,
            (
                resource_path,
                method,
                headers,
                body,
                json,
                fields,
                auth_settings,
                stream,
                timeout,
                host,
            )
        )

    def request(
        self,
        method: str,
        url: str,
        headers: typing.Optional[HTTPHeaderDict] = None,
        fields: typing.Optional[typing.Tuple[typing.Tuple[str, str], ...]] = None,
        body: typing.Optional[typing.Union[str, bytes]] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> urllib3.HTTPResponse:
        """Makes the HTTP request using RESTClient."""
        if method == "GET":
            return self.rest_client.GET(url,
                                        stream=stream,
                                        timeout=timeout,
                                        headers=headers)
        elif method == "HEAD":
            return self.rest_client.HEAD(url,
                                         stream=stream,
                                         timeout=timeout,
                                         headers=headers)
        elif method == "OPTIONS":
            return self.rest_client.OPTIONS(url,
                                            headers=headers,
                                            fields=fields,
                                            stream=stream,
                                            timeout=timeout,
                                            body=body)
        elif method == "POST":
            return self.rest_client.POST(url,
                                         headers=headers,
                                         fields=fields,
                                         stream=stream,
                                         timeout=timeout,
                                         body=body)
        elif method == "PUT":
            return self.rest_client.PUT(url,
                                        headers=headers,
                                        fields=fields,
                                        stream=stream,
                                        timeout=timeout,
                                        body=body)
        elif method == "PATCH":
            return self.rest_client.PATCH(url,
                                          headers=headers,
                                          fields=fields,
                                          stream=stream,
                                          timeout=timeout,
                                          body=body)
        elif method == "DELETE":
            return self.rest_client.DELETE(url,
                                           headers=headers,
                                           stream=stream,
                                           timeout=timeout,
                                           body=body)
        else:
            raise ApiValueError(
                "http method must be `GET`, `HEAD`, `OPTIONS`,"
                " `POST`, `PATCH`, `PUT` or `DELETE`."
            )

    def update_params_for_auth(self, headers, auth_settings,
                               resource_path, method, body):
        """Updates header and query params based on authentication setting.

        :param headers: Header parameters dict to be updated.
        :param auth_settings: Authentication setting identifiers list.
        :param resource_path: A string representation of the HTTP request resource path.
        :param method: A string representation of the HTTP request method.
        :param body: A object representing the body of the HTTP request.
            The object type is the return value of _encoder.default().
        """
        if not auth_settings:
            return

        for auth in auth_settings:
            auth_setting = self.configuration.auth_settings().get(auth)
            if not auth_setting:
                continue
            if auth_setting['in'] == 'cookie':
                headers.add('Cookie', auth_setting['value'])
            elif auth_setting['in'] == 'header':
                if auth_setting['type'] != 'http-signature':
                    headers.add(auth_setting['key'], auth_setting['value'])
            elif auth_setting['in'] == 'query':
                """ TODO implement auth in query
                need to pass in prefix_separator_iterator
                and need to output resource_path with query params added
                """
                raise ApiValueError("Auth in query not yet implemented")
            else:
                raise ApiValueError(
                    'Authentication token must be in `query` or `header`'
                )


class Api:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client: typing.Optional[ApiClient] = None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    @staticmethod
    def _verify_typed_dict_inputs_oapg(cls: typing.Type[typing_extensions.TypedDict], data: typing.Dict[str, typing.Any]):
        """
        Ensures that:
        - required keys are present
        - additional properties are not input
        - value stored under required keys do not have the value unset
        Note: detailed value checking is done in schema classes
        """
        missing_required_keys = []
        required_keys_with_unset_values = []
        for required_key in cls.__required_keys__:
            if required_key not in data:
                missing_required_keys.append(required_key)
                continue
            value = data[required_key]
            if value is unset:
                required_keys_with_unset_values.append(required_key)
        if missing_required_keys:
            raise ApiTypeError(
                '{} missing {} required arguments: {}'.format(
                    cls.__name__, len(missing_required_keys), missing_required_keys
                 )
             )
        if required_keys_with_unset_values:
            raise ApiValueError(
                '{} contains invalid unset values for {} required keys: {}'.format(
                    cls.__name__, len(required_keys_with_unset_values), required_keys_with_unset_values
                )
            )

        disallowed_additional_keys = []
        for key in data:
            if key in cls.__required_keys__ or key in cls.__optional_keys__:
                continue
            disallowed_additional_keys.append(key)
        if disallowed_additional_keys:
            raise ApiTypeError(
                '{} got {} unexpected keyword arguments: {}'.format(
                    cls.__name__, len(disallowed_additional_keys), disallowed_additional_keys
                )
            )

    def _get_host_oapg(
        self,
        operation_id: str,
        servers: typing.Tuple[typing.Dict[str, str], ...] = tuple(),
        host_index: typing.Optional[int] = None
    ) -> typing.Optional[str]:
        configuration = self.api_client.configuration
        try:
            if host_index is None:
                index = configuration.server_operation_index.get(
                    operation_id, configuration.server_index
                )
            else:
                index = host_index
            server_variables = configuration.server_operation_variables.get(
                operation_id, configuration.server_variables
            )
            host = configuration.get_host_from_settings(
                index, variables=server_variables, servers=servers
            )
        except IndexError:
            if servers:
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s" %
                    len(servers)
                )
            host = None
        return host


class SerializedRequestBody(typing_extensions.TypedDict, total=False):
    body: typing.Union[str, bytes]
    fields: typing.Tuple[typing.Union[RequestField, typing.Tuple[str, str]], ...]


class RequestBody(StyleFormSerializer, JSONDetector):
    """
    A request body parameter
    content: content_type to MediaType Schema info
    """
    __json_encoder = JSONEncoder()

    def __init__(
        self,
        content: typing.Dict[str, MediaType],
        required: bool = False,
    ):
        self.required = required
        if len(content) == 0:
            raise ValueError('Invalid value for content, the content dict must have >= 1 entry')
        self.content = content

    def __serialize_json(
        self,
        in_data: typing.Any
    ) -> typing.Dict[str, bytes]:
        in_data = self.__json_encoder.default(in_data)
        json_str = json.dumps(in_data, separators=(",", ":"), ensure_ascii=False).encode(
            "utf-8"
        )
        return dict(body=json_str)

    @staticmethod
    def __serialize_text_plain(in_data: typing.Any) -> typing.Dict[str, str]:
        if isinstance(in_data, frozendict.frozendict):
            raise ValueError('Unable to serialize type frozendict.frozendict to text/plain')
        elif isinstance(in_data, tuple):
            raise ValueError('Unable to serialize type tuple to text/plain')
        elif isinstance(in_data, NoneClass):
            raise ValueError('Unable to serialize type NoneClass to text/plain')
        elif isinstance(in_data, BoolClass):
            raise ValueError('Unable to serialize type BoolClass to text/plain')
        return dict(body=str(in_data))

    def __multipart_json_item(self, key: str, value: Schema) -> RequestField:
        json_value = self.__json_encoder.default(value)
        request_field = RequestField(name=key, data=json.dumps(json_value))
        request_field.make_multipart(content_type='application/json')
        return request_field

    def __multipart_form_item(self, key: str, value: Schema) -> RequestField:
        if isinstance(value, str):
            request_field = RequestField(name=key, data=str(value))
            request_field.make_multipart(content_type='text/plain')
        elif isinstance(value, bytes):
            request_field = RequestField(name=key, data=value)
            request_field.make_multipart(content_type='application/octet-stream')
        elif isinstance(value, FileIO):
            # TODO use content.encoding to limit allowed content types if they are present
            request_field = RequestField.from_tuples(key, (os.path.basename(value.name), value.read()))
            value.close()
        else:
            request_field = self.__multipart_json_item(key=key, value=value)
        return request_field

    def __serialize_multipart_form_data(
        self, in_data: Schema
    ) -> typing.Dict[str, typing.Tuple[RequestField, ...]]:
        if not isinstance(in_data, frozendict.frozendict):
            raise ValueError(f'Unable to serialize {in_data} to multipart/form-data because it is not a dict of data')
        """
        In a multipart/form-data request body, each schema property, or each element of a schema array property,
        takes a section in the payload with an internal header as defined by RFC7578. The serialization strategy
        for each property of a multipart/form-data request body can be specified in an associated Encoding Object.

        When passing in multipart types, boundaries MAY be used to separate sections of the content being
        transferred – thus, the following default Content-Types are defined for multipart:

        If the (object) property is a primitive, or an array of primitive values, the default Content-Type is text/plain
        If the property is complex, or an array of complex values, the default Content-Type is application/json
            Question: how is the array of primitives encoded?
        If the property is a type: string with a contentEncoding, the default Content-Type is application/octet-stream
        """
        fields = []
        for key, value in in_data.items():
            if isinstance(value, tuple):
                if value:
                    # values use explode = True, so the code makes a RequestField for each item with name=key
                    for item in value:
                        request_field = self.__multipart_form_item(key=key, value=item)
                        fields.append(request_field)
                else:
                    # send an empty array as json because exploding will not send it
                    request_field = self.__multipart_json_item(key=key, value=value)
                    fields.append(request_field)
            else:
                request_field = self.__multipart_form_item(key=key, value=value)
                fields.append(request_field)

        return dict(fields=tuple(fields))

    def __serialize_application_octet_stream(self, in_data: BinarySchema) -> typing.Dict[str, bytes]:
        if isinstance(in_data, bytes):
            return dict(body=in_data)
        # FileIO type
        result = dict(body=in_data.read())
        in_data.close()
        return result

    def __serialize_application_x_www_form_data(
        self, in_data: typing.Any
    ) -> SerializedRequestBody:
        """
        POST submission of form data in body
        """
        if not isinstance(in_data, frozendict.frozendict):
            raise ValueError(
                f'Unable to serialize {in_data} to application/x-www-form-urlencoded because it is not a dict of data')
        cast_in_data = self.__json_encoder.default(in_data)
        value = self._serialize_form(cast_in_data, name='', explode=True, percent_encode=True)
        return dict(body=value)

    def serialize(
        self, in_data: typing.Any, content_type: str
    ) -> SerializedRequestBody:
        """
        If a str is returned then the result will be assigned to data when making the request
        If a tuple is returned then the result will be used as fields input in encode_multipart_formdata
        Return a tuple of

        The key of the return dict is
        - body for application/json
        - encode_multipart and fields for multipart/form-data
        """
        media_type = self.content[content_type]
        if isinstance(in_data, media_type.schema):
            cast_in_data = in_data
        elif isinstance(in_data, (dict, frozendict.frozendict)) and in_data:
            cast_in_data = media_type.schema(**in_data)
        else:
            cast_in_data = media_type.schema(in_data)
        # TODO check for and use encoding if it exists
        # and content_type is multipart or application/x-www-form-urlencoded
        if self._content_type_is_json(content_type):
            return self.__serialize_json(cast_in_data)
        elif content_type == 'text/plain':
            return self.__serialize_text_plain(cast_in_data)
        elif content_type == 'multipart/form-data':
            return self.__serialize_multipart_form_data(cast_in_data)
        elif content_type == 'application/x-www-form-urlencoded':
            return self.__serialize_application_x_www_form_data(cast_in_data)
        elif content_type == 'application/octet-stream':
            return self.__serialize_application_octet_stream(cast_in_data)
        raise NotImplementedError('Serialization has not yet been implemented for {}'.format(content_type))