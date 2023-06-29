# coding: utf-8

"""
    RocketReach API

    # Getting Started The RocketReach API allows you to programmatically search & lookup contact info for over 700 million professionals, and 35 million companies. We constantly work on improving functionality and accuracy of our data. RocketReach is free to try for individual use.  You can always visit the [account page](/account?section=nav_gen_api) to view API usage, manage RocketReach API settings, and view your unique API key. All calls to the RocketReach API are authenticated with an API key.  ## Need Help? Have feedback, questions about usage, or pricing? Talk to us live or Email us at sales@rocketreach.co.  ## Troubleshooting  ### Handling Errors Normal responses are returned with HTTP status `HTTP: 200`. Error responses return `HTTP: 4xx/5xx` error codes. For example, if the profile being searched for cannot be found, we will return a `404`.  ### Rate Limits If we start receiving unusually heavy call volumes on your API key, you may receive responses with `HTTP: 429 \"Too Many Requests\"`. In general, do not make more than 5 calls per second using your API key.  Throttled API responses will contain a `Retry-After` header that contains the number of seconds to wait until the endpoint becomes available again. To ensure your client accesses the API fairly, it should parse this value and waits the appropriate amount of time.   Repeated instances of unexpected throttled requests should be addressed one of the following ways: 1. If you are not on a paid plan, you will generally need to upgrade to a paid API plan. Please email sales@rocketreach.co to setup an API plan. 2. If you are already on a paid API plan, please slow down and retry your requests. Contact sales@rocketreach.co or our live support if you continue to have problems.  You can visit the [account page](/account?section=api_section_gen_api) to review your RocketReach API limits and daily usage.  ## Webhooks We offer a webhook solution for person lookups so clients do not need to poll the check status endpoint until their results are available.  ### Set Up To set up a webhook, go to your [API settings](/account?section=nav_gen_api). Enter your server's callback URL into the field, and hit \"Create\".  ### Configuration Options For each URL created, you can perform some basic maintenance tasks:  - Test the webhook - we will attempt to send a basic JSON payload to the URL. - Disable/enable - if you may use this URL in the future, this is an option to temporarily disable it. - Delete - if you no longer plan using this URL, it can be deleted.  ### Usage Currently, only profile lookup and bulk lookup have webhook functionality, but we anticipate supporting more in the future! Once you call a webhook-enabled endpoint with a webhook set up in your settings, we will send back results to the provided URL. The results returned to you should look the same as if they were queried through the REST API. In addition, the API will still respond to your REST call as normal.  ### Errors If any errors occur, they will show up in the [API settings](/account?section=nav_gen_api) page in the \"Web Hook\" section. If the callback to the provided URL is unsuccessful after several attempts, the URL will be automatically disabled and will need to manually be re-enabled.  ## FAQ  **How Do I Know if RocketReach Has Data For a Profile?** - 87% of lookups return profiles  - \"teaser\" in search returns some indication of data; however, the final lookup may discover results even if the teaser is empty - if no data is found, credits are not deducted  **Do I Get Charged a Credit if No Data is Returned?** - for lookups, no - searches are metered, but usually the first ~10,000/day are free on paid API plans  **Why doesn't the data in a Profile match data from the API?** - this should almost never happen, please contact support - on the other hand, search results and sorting may be different depending on how the search is executed - the UI uses NLP for search facets  **Why don't the search results in the UI match data returned from the API?** - search results and sorting may be different depending on how the search is executed - this also uses NLP for search facets - try changing the facet and adjusting the `order_by` param  **Why does the teaser only contain phone numbers, and no emails?** - teaser information is only populated if data is cached  **Why am I getting rate limited?** - rate limits depend on product, contact us to get on an API plan - See our troubleshooting guide for more info.   ## SDKs  ### Python SDK The [Python SDK](https://www.github.com/rocketreach/rocketreach_python) allows you to find anyone's emails, social media and complete contact data, using only a few lines of code.  ### Installation The rocketreach python package can be installed from pip or from source into your project's virtual environment.  Install with pip:  ```bash pip install rocketreach ```  Install from source:  ```bash # The requests v2.2 or higher is a required dependency wget https://pypi.python.org/packages/source/r/requests/requests-2.2.1.tar.gz tar xzvf requests-2.2.1.tar.gz cd requests-2.2.1 python setup.py install  # Install the rocketreach SDK wget https://files.pythonhosted.org/packages/20/9d/5ba988d0b2f94a19fb8f86ae87ef1a2eb79b3fd7da7cce00998b7051d57f/rocketreach-2.1.0.tar.gz tar xzvf rocketreach-2.1.0.tar.gz cd rocketreach-2.1.0 python setup.py install ```  ### Usage  Initialization is the first step to use the SDK. You will need your API key for this step.  ```python import rocketreach import os rr = rocketreach.Gateway(api_key=os.environ.get('API_KEY'))  # Check that the SDK is working result = rr.account.get() if result.is_success:     print(f'Success: {result.account}') else:     print(f'Error: {result.message}!') ```  You can call any of our methods once the Gateway class is constructed. In this next example we will call lookup() using a name and current employer. Then, we'll do the same lookup using a LinkedIn URL.  ```python lookup_result = rr.person.lookup(name='Marc Benioff', current_employer='Salesforce') if lookup_result.is_success:     print(lookup_result.person) lookup_result = rr.person.lookup(linkedin_url='https://www.linkedin.com/in/marcbenioff') if lookup_result.is_success:     print(lookup_result.person) ```  By default, the lookup method blocks until /checkStatus returns complete. The caller can override this behavior and call lookup in a non-blocking context.  ```python import time # Lookup 2 profiles, non-blocking and checkStatus ourself. lookup1 = rr.person.lookup(linkedin_url='https://www.linkedin.com/in/marcbenioff', block=False) lookup2 = rr.person.lookup(linkedin_url='https://www.linkedin.com/in/reidhoffman', block=False) # Check if the lookups are complete. while True:     lookup_ids = [lookup1.person.id, lookup2.person.id]     cs_result = rr.person.check_status(lookup_ids)     num_complete = 0     for p in cs_result.people:         if p.status == 'complete':             num_complete += 1     if num_complete == len(lookups):         break     time.sleep(10)  # Wait a few seconds before checking status again # All the lookups are 'complete'. ```  `check_status()` can take either a single argument, or an array containing multiple IDs to lookup. Regardless of the number of arguments, the return value will always contain a person collection as an array (with 1 or more elements).  ```python result = rr.person.check_status(5244) assert(len(result.people) == 1) result = rr.person.check_status([5244, 5234]) assert(len(result.people) == 2) ```  ### Reference Calls are wrapped in a Result object. If the call was successful the Result object will encapsulate the return value.  Result object attributes  Name Description Type request Request object sent to the server. requests.Request response Response object received from the server. requests.Response is_success Indicates if the call succeeded. bool data (optional) Any data retrieved from the server response. dict error (optional) Any error data retrieved from the server response. Returned if is_success is False dict message (optional) A human readable message that explains what went wrong. str  | Name      | Description | Type | |-----------| ----------- | -----| | request    | Request object sent to the server. | `requests.Request` | | response | Response object received from the server. | `requests.Response` | | is_success | Indicates if the call succeeded. | `bool` | | data | Any data retrieved from the server response. | `dict` (optional) | | error | Any error data retrieved from the server response. Returned if `is_success = False` | `dict` (optional) |        | | message | A human readable message that explains what went wrong. | `str` (optional) |  ### Pagination  Searches will only return 10 results at a time, but the API provides a pagination method that can be accessed through the Python SDK.  ```python search = rr.person.search() # Add filters to your search start = 1 size = 10 result = search.execute() people = [] while result.is_success and result.people:     start += size     people.extend(result.people)     search = search.params(start=start, size=size)     result = search.execute() ```  The Python SDK provides iterators to handle paginating through results for you. These convenience iterators are accessed through the .iterator() method.  ```python search = rr.person.search() # Add filters to your search for person in search.iterator():     print(person) ```  The search object also supports indexing and slicing to limit the range of results. ```python search = rr.person.search() # Add filters to your search list(search[:100])  # Retrieve the first 100 results list(search[10:20])  # Retrieve results 11 - 19 person = search[0]  # Retrieve only the first result ```  Note: - Indexing causes the search to be immediately executed with the desired result returned. - Search object slices cannot contain steps.  ## Examples  ### Lookup by Name If you are calling the RocketReach API endpoints directly, you will essentially need to use 2 calls. First call `person/lookup` with 2 parameters: `name` and `current_employer`.  ```bash curl -G -L 'http://api.rocketreach.co/api/v2/person/lookup'\\      --header 'Api-Key: <INSERT API KEY>'\\      --data-urlencode 'name=Marc Benioff'\\      --data-urlencode 'current_employer=Salesforce' ```  If the status returned by the call is not `complete` or `failed`, then you will need to poll `person/checkStatus` untill it returns either `complete` or `failed`. If the status is `complete`, then the response will also contain contact info data.  ```bash curl --request 'GET' --location 'https://api.rocketreach.co/api/v2/person/checkStatus'\\      --header 'Api-Key: <INSERT API KEY>'\\      --data-urlencode 'ids=5262' ```  **Putting it all together** The following example demonstrates a fully functional application, using the RocketReach API. Here, we lookup contact info of a person, by name and current_employer.  The source code shown below uses the RocketReach Python SDK. We start by calling initializing the client. This checks to make sure that the `api_key` is valid, and that the user has sufficient credits to perform lookups. Under the covers, the SDK is simply calling the `/account` endpoint. If everything looks good, we now call `person/lookup` to lookup contact info. The library also polls `person/checkStatus` for you, when necessary.  ```python import rocketreach import os rr = rocketreach.Gateway(api_key=os.environ.get('API_KEY')) lookup = rr.person.lookup(extras={'name': 'Marc Benioff', 'current_employer': 'Salesforce'}) if lookup.is_success:     print(repr(lookup.person)) ```  Output ```python     {'current_employer': 'Salesforce',      'current_personal_email': 'benioff@gmail.com',      'current_title': 'Chairman and Co-CEO',      'current_work_email': 'marcb@salesforce.com',      'emails': [{'email': 'm.benioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'mbenioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'benioff@comcast.net',                  'smtp_valid': 'valid',                  'type': 'personal'},                 {'email': 'marc@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marc_benioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'benioff@gmail.com',                  'smtp_valid': 'valid',                  'type': 'personal'},                 {'email': 'benioff@aol.com',                  'smtp_valid': 'valid',                  'type': 'personal'},                 {'email': 'ceo@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marcb@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marc.benioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marcbenioff@salesforce.com',                  'smtp_valid': 'invalid',                  'type': 'professional'},                 {'email': 'benioff@frontiernet.net',                  'smtp_valid': 'invalid',                  'type': 'personal'},                 {'email': 'cooldwj@chinaren.com',                  'smtp_valid': 'invalid',                  'type': 'professional'},                 {'email': 'benioff@rcn.com',                  'smtp_valid': 'invalid',                  'type': 'professional'}],      'id': 5244,      'linkedin_url': 'https://www.linkedin.com/in/marcbenioff',      'links': {'aboutme': 'http://www.about.me/marcbenioff',                'amazon': 'http://www.amazon.com/gp/pdp/profile/AZGYQG724J6ON//190-5748375-2756131',                'angel': 'https://angel.co/benioff',                'angellist': 'http://www.angel.co/benioff',                'crunchbase': 'https://www.crunchbase.com/person/marc-benioff',                'facebook': 'http://www.facebook.com/benioff',                'google': 'https://plus.google.com/109586918294369333764',                'google+': 'https://plus.google.com/108172009599607363531/about',                'googleplus': 'https://plus.google.com/108172009599607363531',                'gravatar': 'http://www.gravatar.com/crmmaster',                'gravatar.com': 'http://gravatar.com/crmmaster',                'hi5': 'http://www.hi5.com/friend/p45336146--profile--html',                'instagram': 'http://www.instagram.com/benioff',                'klout': 'http://www.klout.com/benioff',                'linkedin': 'https://www.linkedin.com/in/marcbenioff',                'meetup': 'http://www.meetup.com/members/15867891',                'pinterest': 'http://www.pinterest.com/benioff',                'quora': 'http://www.quora.com/marc-benioff',                'salesforce.com': 'http://www.salesforce.com/company/leadership/executive-team/index.jsp#benioff',                'twicsy': 'http://twicsy.com/u/%40Benioff',                'twitter': 'http://www.twitter.com/benioff'},      'location': 'San Francisco, California, United States',      'name': 'Marc Benioff',      'phones': [],      'profile_pic': 'https://d1hbpr09pwz0sk.cloudfront.net/profile_pic/marc-benioff-4492e698',      'status': 'complete'}  ```  ### Lookup by LinkedIn URL  This is very similar to the previous example, but calls `person/lookup` with the `li_url` parameter.  ```bash  curl -G --location 'https://api.rocketreach.co/v2/api/person/lookup'\\      --header 'Api-Key: <INSERT API KEY>'\\      --data-urlencode 'li_url=https://www.linkedin.com/in/marcbenioff/' ```  **Putting it all together** The following example demonstrates a fully functional application, using the RocketReach API. Here, we lookup contact info of a person, by `name` and `current_employer`.  The source code shown below uses the RocketReach Python SDK. We start by calling initializing the client. This checks to make sure that the `api_key` is valid, and that the user has sufficient credits to perform lookups. Under the covers, the SDK is simply calling the `/account` endpoint. If everything looks good, we now call `person/lookup` to lookup contact info. The library also polls `person/checkStatus` for you, when necessary.  Code:  ```python import rocketreach import os rr = rocketreach.Gateway(api_key=os.environ.get('API_KEY')) lookup = rr.person.lookup(linkedin_url='https://www.linkedin.com/in/marcbenioff') if lookup.is_success:     print(repr(lookup.person)) ```  Output:  ```python      {'current_employer': 'Salesforce',      'current_personal_email': 'benioff@gmail.com',      'current_title': 'Chairman and Co-CEO',      'current_work_email': 'marcb@salesforce.com',      'emails': [{'email': 'm.benioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'mbenioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'benioff@comcast.net',                  'smtp_valid': 'valid',                  'type': 'personal'},                 {'email': 'marc@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marc_benioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'benioff@gmail.com',                  'smtp_valid': 'valid',                  'type': 'personal'},                 {'email': 'benioff@aol.com',                  'smtp_valid': 'valid',                  'type': 'personal'},                 {'email': 'ceo@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marcb@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marc.benioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marcbenioff@salesforce.com',                  'smtp_valid': 'invalid',                  'type': 'professional'},                 {'email': 'benioff@frontiernet.net',                  'smtp_valid': 'invalid',                  'type': 'personal'},                 {'email': 'cooldwj@chinaren.com',                  'smtp_valid': 'invalid',                  'type': 'professional'},                 {'email': 'benioff@rcn.com',                  'smtp_valid': 'invalid',                  'type': 'professional'}],      'id': 5244,      'linkedin_url': 'https://www.linkedin.com/in/marcbenioff',      'links': {'aboutme': 'http://www.about.me/marcbenioff',                'amazon': 'http://www.amazon.com/gp/pdp/profile/AZGYQG724J6ON//190-5748375-2756131',                'angel': 'https://angel.co/benioff',                'angellist': 'http://www.angel.co/benioff',                 'crunchbase': 'https://www.crunchbase.com/person/marc-benioff',                'facebook': 'http://www.facebook.com/benioff',                'google': 'https://plus.google.com/109586918294369333764',                'google+': 'https://plus.google.com/108172009599607363531/about',                'googleplus': 'https://plus.google.com/108172009599607363531',                'gravatar': 'http://www.gravatar.com/crmmaster',                'gravatar.com': 'http://gravatar.com/crmmaster',                'hi5': 'http://www.hi5.com/friend/p45336146--profile--html',                'instagram': 'http://www.instagram.com/benioff',                'klout': 'http://www.klout.com/benioff',                'linkedin': 'https://www.linkedin.com/in/marcbenioff',                'meetup': 'http://www.meetup.com/members/15867891',                'pinterest': 'http://www.pinterest.com/benioff',                'quora': 'http://www.quora.com/marc-benioff',                'salesforce.com': 'http://www.salesforce.com/company/leadership/executive-team/index.jsp#benioff',                'twicsy': 'http://twicsy.com/u/%40Benioff',                'twitter': 'http://www.twitter.com/benioff'},      'location': 'San Francisco, California, United States',      'name': 'Marc Benioff',      'phones': [],      'profile_pic': 'https://d1hbpr09pwz0sk.cloudfront.net/profile_pic/marc-benioff-4492e698',      'status': 'complete'} ```   ### Search People by Role at Company  If you are calling the RocketReach API endpoints directly, you will essentially need to use 3 calls. First call the `person/search` endpoint.  ```bash curl --request 'POST' --location 'https://api.rocketreach.co/api/v2/search'\\      --header 'Api-Key: <INSERT API KEY>'\\      --header 'Content-Type: application/json'\\      --data '{\"query\":{\"name\":[\"Marc Benioff\"],\"current_employer\":[\"Salesforce\"],\"current_title\":[\"CEO\"]}}' ```  Assuming that the `id` for Marc's profile is `5262`, you then call `person/lookup`.  ```bash curl --request 'GET' --location 'https://api.rocketreach.co/api/v2/lookupProfile'\\      --header 'Api-Key: <INSERT API KEY>'\\      --data-urlencode 'id=5262' ```  If the status returned by the call is not `complete` or `failed`, then you will need to poll `person/checkStatus` untill it returns either `complete` or `failed`.  ```bash curl --request 'GET' --location 'https://api.rocketreach.co/api/v2/checkStatus'\\      --header 'Api-Key: <INSERT API KEY>'\\      --data-urlencode 'ids=5262' ```  **Putting it all together** In this example, we will search for people with a specific name and title, at a company. We will then lookup contact info for one of the search results.  Code: ```python     import rocketreach     import os     rr = rocketreach.Gateway(api_key=os.environ.get('API_KEY'))     search = rr.person.search()     # Build up our search query     search = search.filter(name='Marc Benioff', current_title='CEO', current_employer='Salesforce')     # Call the search endpoint with our query     result = search.execute()     if result.is_success:         lookup = rr.person.lookup(result.people[0].id)         if lookup.is_success:             print(repr(lookup.person)) ```  Output: ```python {     'current_employer': 'Salesforce',     'current_personal_email': 'benioff@gmail.com',     'current_title': 'Chairman and Co-CEO',     'current_work_email': 'marcb@salesforce.com',     'emails': [{'email': 'm.benioff@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'mbenioff@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'benioff@comcast.net',              'smtp_valid': 'valid',              'type': 'personal'},             {'email': 'marc@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'marc_benioff@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'benioff@gmail.com',              'smtp_valid': 'valid',              'type': 'personal'},             {'email': 'benioff@aol.com',              'smtp_valid': 'valid',              'type': 'personal'},             {'email': 'ceo@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'marcb@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'marc.benioff@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'marcbenioff@salesforce.com',              'smtp_valid': 'invalid',              'type': 'professional'},             {'email': 'benioff@frontiernet.net',              'smtp_valid': 'invalid',              'type': 'personal'},             {'email': 'cooldwj@chinaren.com',              'smtp_valid': 'invalid',              'type': 'professional'},             {'email': 'benioff@rcn.com',              'smtp_valid': 'invalid',              'type': 'professional'}],     'id': 5244,     'linkedin_url': 'https://www.linkedin.com/in/marcbenioff',     'links': {'aboutme': 'http://www.about.me/marcbenioff',            'amazon': 'http://www.amazon.com/gp/pdp/profile/AZGYQG724J6ON//190-5748375-2756131',            'angel': 'https://angel.co/benioff',            'angellist': 'http://www.angel.co/benioff',            'crunchbase': 'https://www.crunchbase.com/person/marc-benioff',            'facebook': 'http://www.facebook.com/benioff',            'google': 'https://plus.google.com/109586918294369333764',            'google+': 'https://plus.google.com/108172009599607363531/about',            'googleplus': 'https://plus.google.com/108172009599607363531',            'gravatar': 'http://www.gravatar.com/crmmaster',            'gravatar.com': 'http://gravatar.com/crmmaster',            'hi5': 'http://www.hi5.com/friend/p45336146--profile--html',            'instagram': 'http://www.instagram.com/benioff',            'klout': 'http://www.klout.com/benioff',            'linkedin': 'https://www.linkedin.com/in/marcbenioff',            'meetup': 'http://www.meetup.com/members/15867891',            'pinterest': 'http://www.pinterest.com/benioff',            'quora': 'http://www.quora.com/marc-benioff',            'salesforce.com': 'http://www.salesforce.com/company/leadership/executive-team/index.jsp#benioff',            'twicsy': 'http://twicsy.com/u/%40Benioff',            'twitter': 'http://www.twitter.com/benioff'},     'location': 'San Francisco, California, United States',     'name': 'Marc Benioff',     'phones': [],     'profile_pic': 'https://d1hbpr09pwz0sk.cloudfront.net/profile_pic/marc-benioff-4492e698',     'status': 'complete' }  ```  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@rocketreach.co
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class ProfileAPISerializerWithCompany(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "current_employer_linkedin_url",
            "skills",
            "education",
            "region_latitude",
            "current_employer_domain",
            "region_longitude",
            "company",
            "current_employer_website",
            "current_employer_id",
            "job_history",
        }
        
        class properties:
            
            
            class current_employer_domain(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'current_employer_domain':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class current_employer_website(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'current_employer_website':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class job_history(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['JobHistoryAPI']:
                        return JobHistoryAPI
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['JobHistoryAPI'], typing.List['JobHistoryAPI']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'job_history':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'JobHistoryAPI':
                    return super().__getitem__(i)
            
            
            class education(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EducationAPI']:
                        return EducationAPI
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['EducationAPI'], typing.List['EducationAPI']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'education':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EducationAPI':
                    return super().__getitem__(i)
            
            
            class skills(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, None, str, ]], typing.List[typing.Union[MetaOapg.items, None, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'skills':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            current_employer_id = schemas.IntSchema
            
            
            class current_employer_linkedin_url(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'current_employer_linkedin_url':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class region_latitude(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'region_latitude':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class region_longitude(
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'region_longitude':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def company() -> typing.Type['CompanyAPI']:
                return CompanyAPI
        
            @staticmethod
            def profile_list() -> typing.Type['ProfileListAPI']:
                return ProfileListAPI
            id = schemas.IntSchema
            
            
            class status(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 128
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'name':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            profile_pic = schemas.StrSchema
            linkedin_url = schemas.StrSchema
            
            
            class links(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class additional_properties(
                        schemas.StrBase,
                        schemas.NoneBase,
                        schemas.Schema,
                        schemas.NoneStrMixin
                    ):
                    
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[None, str, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'additional_properties':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                            )
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, None, str, ],
                ) -> 'links':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class location(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 256
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'location':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            current_title = schemas.StrSchema
            
            
            class normalized_title(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'normalized_title':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            current_employer = schemas.StrSchema
            
            
            class emails(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ProfileEmailAPI']:
                        return ProfileEmailAPI
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ProfileEmailAPI'], typing.List['ProfileEmailAPI']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'emails':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ProfileEmailAPI':
                    return super().__getitem__(i)
            
            
            class phones(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ProfilePhoneAPI']:
                        return ProfilePhoneAPI
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ProfilePhoneAPI'], typing.List['ProfilePhoneAPI']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'phones':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ProfilePhoneAPI':
                    return super().__getitem__(i)
            birth_year = schemas.IntSchema
            recommended_email = schemas.StrSchema
            recommended_personal_email = schemas.StrSchema
            recommended_professional_email = schemas.StrSchema
            current_work_email = schemas.StrSchema
            current_personal_email = schemas.StrSchema
            
            
            class city(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 128
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'city':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class region(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 3
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'region':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            country = schemas.StrSchema
            
            
            class country_code(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 2
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'country_code':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "current_employer_domain": current_employer_domain,
                "current_employer_website": current_employer_website,
                "job_history": job_history,
                "education": education,
                "skills": skills,
                "current_employer_id": current_employer_id,
                "current_employer_linkedin_url": current_employer_linkedin_url,
                "region_latitude": region_latitude,
                "region_longitude": region_longitude,
                "company": company,
                "profile_list": profile_list,
                "id": id,
                "status": status,
                "name": name,
                "profile_pic": profile_pic,
                "linkedin_url": linkedin_url,
                "links": links,
                "location": location,
                "current_title": current_title,
                "normalized_title": normalized_title,
                "current_employer": current_employer,
                "emails": emails,
                "phones": phones,
                "birth_year": birth_year,
                "recommended_email": recommended_email,
                "recommended_personal_email": recommended_personal_email,
                "recommended_professional_email": recommended_professional_email,
                "current_work_email": current_work_email,
                "current_personal_email": current_personal_email,
                "city": city,
                "region": region,
                "country": country,
                "country_code": country_code,
            }
    
    current_employer_linkedin_url: MetaOapg.properties.current_employer_linkedin_url
    skills: MetaOapg.properties.skills
    education: MetaOapg.properties.education
    region_latitude: MetaOapg.properties.region_latitude
    current_employer_domain: MetaOapg.properties.current_employer_domain
    region_longitude: MetaOapg.properties.region_longitude
    company: 'CompanyAPI'
    current_employer_website: MetaOapg.properties.current_employer_website
    current_employer_id: MetaOapg.properties.current_employer_id
    job_history: MetaOapg.properties.job_history
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_employer_domain"]) -> MetaOapg.properties.current_employer_domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_employer_website"]) -> MetaOapg.properties.current_employer_website: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job_history"]) -> MetaOapg.properties.job_history: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["education"]) -> MetaOapg.properties.education: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skills"]) -> MetaOapg.properties.skills: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_employer_id"]) -> MetaOapg.properties.current_employer_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_employer_linkedin_url"]) -> MetaOapg.properties.current_employer_linkedin_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["region_latitude"]) -> MetaOapg.properties.region_latitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["region_longitude"]) -> MetaOapg.properties.region_longitude: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company"]) -> 'CompanyAPI': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profile_list"]) -> 'ProfileListAPI': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profile_pic"]) -> MetaOapg.properties.profile_pic: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linkedin_url"]) -> MetaOapg.properties.linkedin_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location"]) -> MetaOapg.properties.location: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_title"]) -> MetaOapg.properties.current_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normalized_title"]) -> MetaOapg.properties.normalized_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_employer"]) -> MetaOapg.properties.current_employer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emails"]) -> MetaOapg.properties.emails: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phones"]) -> MetaOapg.properties.phones: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["birth_year"]) -> MetaOapg.properties.birth_year: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recommended_email"]) -> MetaOapg.properties.recommended_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recommended_personal_email"]) -> MetaOapg.properties.recommended_personal_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recommended_professional_email"]) -> MetaOapg.properties.recommended_professional_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_work_email"]) -> MetaOapg.properties.current_work_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_personal_email"]) -> MetaOapg.properties.current_personal_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["region"]) -> MetaOapg.properties.region: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country_code"]) -> MetaOapg.properties.country_code: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["current_employer_domain", "current_employer_website", "job_history", "education", "skills", "current_employer_id", "current_employer_linkedin_url", "region_latitude", "region_longitude", "company", "profile_list", "id", "status", "name", "profile_pic", "linkedin_url", "links", "location", "current_title", "normalized_title", "current_employer", "emails", "phones", "birth_year", "recommended_email", "recommended_personal_email", "recommended_professional_email", "current_work_email", "current_personal_email", "city", "region", "country", "country_code", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_employer_domain"]) -> MetaOapg.properties.current_employer_domain: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_employer_website"]) -> MetaOapg.properties.current_employer_website: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job_history"]) -> MetaOapg.properties.job_history: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["education"]) -> MetaOapg.properties.education: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skills"]) -> MetaOapg.properties.skills: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_employer_id"]) -> MetaOapg.properties.current_employer_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_employer_linkedin_url"]) -> MetaOapg.properties.current_employer_linkedin_url: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["region_latitude"]) -> MetaOapg.properties.region_latitude: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["region_longitude"]) -> MetaOapg.properties.region_longitude: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company"]) -> 'CompanyAPI': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profile_list"]) -> typing.Union['ProfileListAPI', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profile_pic"]) -> typing.Union[MetaOapg.properties.profile_pic, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linkedin_url"]) -> typing.Union[MetaOapg.properties.linkedin_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> typing.Union[MetaOapg.properties.location, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_title"]) -> typing.Union[MetaOapg.properties.current_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normalized_title"]) -> typing.Union[MetaOapg.properties.normalized_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_employer"]) -> typing.Union[MetaOapg.properties.current_employer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emails"]) -> typing.Union[MetaOapg.properties.emails, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phones"]) -> typing.Union[MetaOapg.properties.phones, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["birth_year"]) -> typing.Union[MetaOapg.properties.birth_year, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recommended_email"]) -> typing.Union[MetaOapg.properties.recommended_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recommended_personal_email"]) -> typing.Union[MetaOapg.properties.recommended_personal_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recommended_professional_email"]) -> typing.Union[MetaOapg.properties.recommended_professional_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_work_email"]) -> typing.Union[MetaOapg.properties.current_work_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_personal_email"]) -> typing.Union[MetaOapg.properties.current_personal_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["region"]) -> typing.Union[MetaOapg.properties.region, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country_code"]) -> typing.Union[MetaOapg.properties.country_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["current_employer_domain", "current_employer_website", "job_history", "education", "skills", "current_employer_id", "current_employer_linkedin_url", "region_latitude", "region_longitude", "company", "profile_list", "id", "status", "name", "profile_pic", "linkedin_url", "links", "location", "current_title", "normalized_title", "current_employer", "emails", "phones", "birth_year", "recommended_email", "recommended_personal_email", "recommended_professional_email", "current_work_email", "current_personal_email", "city", "region", "country", "country_code", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        current_employer_linkedin_url: typing.Union[MetaOapg.properties.current_employer_linkedin_url, None, str, ],
        skills: typing.Union[MetaOapg.properties.skills, list, tuple, ],
        education: typing.Union[MetaOapg.properties.education, list, tuple, ],
        region_latitude: typing.Union[MetaOapg.properties.region_latitude, None, decimal.Decimal, int, float, ],
        current_employer_domain: typing.Union[MetaOapg.properties.current_employer_domain, None, str, ],
        region_longitude: typing.Union[MetaOapg.properties.region_longitude, None, decimal.Decimal, int, float, ],
        company: 'CompanyAPI',
        current_employer_website: typing.Union[MetaOapg.properties.current_employer_website, None, str, ],
        current_employer_id: typing.Union[MetaOapg.properties.current_employer_id, decimal.Decimal, int, ],
        job_history: typing.Union[MetaOapg.properties.job_history, list, tuple, ],
        profile_list: typing.Union['ProfileListAPI', schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
        profile_pic: typing.Union[MetaOapg.properties.profile_pic, str, schemas.Unset] = schemas.unset,
        linkedin_url: typing.Union[MetaOapg.properties.linkedin_url, str, schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        location: typing.Union[MetaOapg.properties.location, None, str, schemas.Unset] = schemas.unset,
        current_title: typing.Union[MetaOapg.properties.current_title, str, schemas.Unset] = schemas.unset,
        normalized_title: typing.Union[MetaOapg.properties.normalized_title, None, str, schemas.Unset] = schemas.unset,
        current_employer: typing.Union[MetaOapg.properties.current_employer, str, schemas.Unset] = schemas.unset,
        emails: typing.Union[MetaOapg.properties.emails, list, tuple, schemas.Unset] = schemas.unset,
        phones: typing.Union[MetaOapg.properties.phones, list, tuple, schemas.Unset] = schemas.unset,
        birth_year: typing.Union[MetaOapg.properties.birth_year, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        recommended_email: typing.Union[MetaOapg.properties.recommended_email, str, schemas.Unset] = schemas.unset,
        recommended_personal_email: typing.Union[MetaOapg.properties.recommended_personal_email, str, schemas.Unset] = schemas.unset,
        recommended_professional_email: typing.Union[MetaOapg.properties.recommended_professional_email, str, schemas.Unset] = schemas.unset,
        current_work_email: typing.Union[MetaOapg.properties.current_work_email, str, schemas.Unset] = schemas.unset,
        current_personal_email: typing.Union[MetaOapg.properties.current_personal_email, str, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, None, str, schemas.Unset] = schemas.unset,
        region: typing.Union[MetaOapg.properties.region, None, str, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        country_code: typing.Union[MetaOapg.properties.country_code, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProfileAPISerializerWithCompany':
        return super().__new__(
            cls,
            *_args,
            current_employer_linkedin_url=current_employer_linkedin_url,
            skills=skills,
            education=education,
            region_latitude=region_latitude,
            current_employer_domain=current_employer_domain,
            region_longitude=region_longitude,
            company=company,
            current_employer_website=current_employer_website,
            current_employer_id=current_employer_id,
            job_history=job_history,
            profile_list=profile_list,
            id=id,
            status=status,
            name=name,
            profile_pic=profile_pic,
            linkedin_url=linkedin_url,
            links=links,
            location=location,
            current_title=current_title,
            normalized_title=normalized_title,
            current_employer=current_employer,
            emails=emails,
            phones=phones,
            birth_year=birth_year,
            recommended_email=recommended_email,
            recommended_personal_email=recommended_personal_email,
            recommended_professional_email=recommended_professional_email,
            current_work_email=current_work_email,
            current_personal_email=current_personal_email,
            city=city,
            region=region,
            country=country,
            country_code=country_code,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.company_api import CompanyAPI
from openapi_client.model.education_api import EducationAPI
from openapi_client.model.job_history_api import JobHistoryAPI
from openapi_client.model.profile_email_api import ProfileEmailAPI
from openapi_client.model.profile_list_api import ProfileListAPI
from openapi_client.model.profile_phone_api import ProfilePhoneAPI
