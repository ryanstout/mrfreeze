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


class CompanyQuery(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class keyword(
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
                ) -> 'keyword':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_keyword(
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
                ) -> 'exclude_keyword':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class growth(
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
                ) -> 'growth':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_growth(
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
                ) -> 'exclude_growth':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class name(
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
                ) -> 'name':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_name(
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
                ) -> 'exclude_name':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class extended_keyword(
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
                ) -> 'extended_keyword':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_extended_keyword(
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
                ) -> 'exclude_extended_keyword':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class employees(
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
                ) -> 'employees':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_employees(
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
                ) -> 'exclude_employees':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class location(
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
                ) -> 'location':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_location(
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
                ) -> 'exclude_location':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class naics_code(
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
                ) -> 'naics_code':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_naics_code(
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
                ) -> 'exclude_naics_code':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class industry_tags(
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
                ) -> 'industry_tags':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_industry_tags(
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
                ) -> 'exclude_industry_tags':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class all_industries(
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
                ) -> 'all_industries':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_all_industries(
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
                ) -> 'exclude_all_industries':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class total_funding(
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
                ) -> 'total_funding':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_total_funding(
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
                ) -> 'exclude_total_funding':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class description(
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
                ) -> 'description':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_description(
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
                ) -> 'exclude_description':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class primary_industry(
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
                ) -> 'primary_industry':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_primary_industry(
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
                ) -> 'exclude_primary_industry':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class website_url(
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
                ) -> 'website_url':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_website_url(
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
                ) -> 'exclude_website_url':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class email_domain(
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
                ) -> 'email_domain':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_email_domain(
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
                ) -> 'exclude_email_domain':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class domain(
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
                ) -> 'domain':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_domain(
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
                ) -> 'exclude_domain':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class insight(
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
                ) -> 'insight':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_insight(
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
                ) -> 'exclude_insight':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class geo(
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
                ) -> 'geo':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_geo(
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
                ) -> 'exclude_geo':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class simplified_keyword(
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
                ) -> 'simplified_keyword':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_simplified_keyword(
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
                ) -> 'exclude_simplified_keyword':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class link(
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
                ) -> 'link':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_link(
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
                ) -> 'exclude_link':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class industry(
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
                ) -> 'industry':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_industry(
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
                ) -> 'exclude_industry':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class publicly_traded(
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
                ) -> 'publicly_traded':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_publicly_traded(
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
                ) -> 'exclude_publicly_traded':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class revenue(
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
                ) -> 'revenue':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_revenue(
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
                ) -> 'exclude_revenue':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class id(
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
                ) -> 'id':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_id(
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
                ) -> 'exclude_id':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class techstack(
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
                ) -> 'techstack':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_techstack(
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
                ) -> 'exclude_techstack':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class website_category(
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
                ) -> 'website_category':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_website_category(
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
                ) -> 'exclude_website_category':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class is_primary(
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
                ) -> 'is_primary':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_is_primary(
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
                ) -> 'exclude_is_primary':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class sic_code(
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
                ) -> 'sic_code':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_sic_code(
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
                ) -> 'exclude_sic_code':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "keyword": keyword,
                "exclude_keyword": exclude_keyword,
                "growth": growth,
                "exclude_growth": exclude_growth,
                "name": name,
                "exclude_name": exclude_name,
                "extended_keyword": extended_keyword,
                "exclude_extended_keyword": exclude_extended_keyword,
                "employees": employees,
                "exclude_employees": exclude_employees,
                "location": location,
                "exclude_location": exclude_location,
                "naics_code": naics_code,
                "exclude_naics_code": exclude_naics_code,
                "industry_tags": industry_tags,
                "exclude_industry_tags": exclude_industry_tags,
                "all_industries": all_industries,
                "exclude_all_industries": exclude_all_industries,
                "total_funding": total_funding,
                "exclude_total_funding": exclude_total_funding,
                "description": description,
                "exclude_description": exclude_description,
                "primary_industry": primary_industry,
                "exclude_primary_industry": exclude_primary_industry,
                "website_url": website_url,
                "exclude_website_url": exclude_website_url,
                "email_domain": email_domain,
                "exclude_email_domain": exclude_email_domain,
                "domain": domain,
                "exclude_domain": exclude_domain,
                "insight": insight,
                "exclude_insight": exclude_insight,
                "geo": geo,
                "exclude_geo": exclude_geo,
                "simplified_keyword": simplified_keyword,
                "exclude_simplified_keyword": exclude_simplified_keyword,
                "link": link,
                "exclude_link": exclude_link,
                "industry": industry,
                "exclude_industry": exclude_industry,
                "publicly_traded": publicly_traded,
                "exclude_publicly_traded": exclude_publicly_traded,
                "revenue": revenue,
                "exclude_revenue": exclude_revenue,
                "id": id,
                "exclude_id": exclude_id,
                "techstack": techstack,
                "exclude_techstack": exclude_techstack,
                "website_category": website_category,
                "exclude_website_category": exclude_website_category,
                "is_primary": is_primary,
                "exclude_is_primary": exclude_is_primary,
                "sic_code": sic_code,
                "exclude_sic_code": exclude_sic_code,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["keyword"]) -> MetaOapg.properties.keyword: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_keyword"]) -> MetaOapg.properties.exclude_keyword: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["growth"]) -> MetaOapg.properties.growth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_growth"]) -> MetaOapg.properties.exclude_growth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_name"]) -> MetaOapg.properties.exclude_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extended_keyword"]) -> MetaOapg.properties.extended_keyword: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_extended_keyword"]) -> MetaOapg.properties.exclude_extended_keyword: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employees"]) -> MetaOapg.properties.employees: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_employees"]) -> MetaOapg.properties.exclude_employees: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location"]) -> MetaOapg.properties.location: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_location"]) -> MetaOapg.properties.exclude_location: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["naics_code"]) -> MetaOapg.properties.naics_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_naics_code"]) -> MetaOapg.properties.exclude_naics_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["industry_tags"]) -> MetaOapg.properties.industry_tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_industry_tags"]) -> MetaOapg.properties.exclude_industry_tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["all_industries"]) -> MetaOapg.properties.all_industries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_all_industries"]) -> MetaOapg.properties.exclude_all_industries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_funding"]) -> MetaOapg.properties.total_funding: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_total_funding"]) -> MetaOapg.properties.exclude_total_funding: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_description"]) -> MetaOapg.properties.exclude_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary_industry"]) -> MetaOapg.properties.primary_industry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_primary_industry"]) -> MetaOapg.properties.exclude_primary_industry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["website_url"]) -> MetaOapg.properties.website_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_website_url"]) -> MetaOapg.properties.exclude_website_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_domain"]) -> MetaOapg.properties.email_domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_email_domain"]) -> MetaOapg.properties.exclude_email_domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domain"]) -> MetaOapg.properties.domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_domain"]) -> MetaOapg.properties.exclude_domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["insight"]) -> MetaOapg.properties.insight: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_insight"]) -> MetaOapg.properties.exclude_insight: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["geo"]) -> MetaOapg.properties.geo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_geo"]) -> MetaOapg.properties.exclude_geo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["simplified_keyword"]) -> MetaOapg.properties.simplified_keyword: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_simplified_keyword"]) -> MetaOapg.properties.exclude_simplified_keyword: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_link"]) -> MetaOapg.properties.exclude_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["industry"]) -> MetaOapg.properties.industry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_industry"]) -> MetaOapg.properties.exclude_industry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publicly_traded"]) -> MetaOapg.properties.publicly_traded: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_publicly_traded"]) -> MetaOapg.properties.exclude_publicly_traded: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["revenue"]) -> MetaOapg.properties.revenue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_revenue"]) -> MetaOapg.properties.exclude_revenue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_id"]) -> MetaOapg.properties.exclude_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["techstack"]) -> MetaOapg.properties.techstack: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_techstack"]) -> MetaOapg.properties.exclude_techstack: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["website_category"]) -> MetaOapg.properties.website_category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_website_category"]) -> MetaOapg.properties.exclude_website_category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_primary"]) -> MetaOapg.properties.is_primary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_is_primary"]) -> MetaOapg.properties.exclude_is_primary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sic_code"]) -> MetaOapg.properties.sic_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_sic_code"]) -> MetaOapg.properties.exclude_sic_code: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["keyword", "exclude_keyword", "growth", "exclude_growth", "name", "exclude_name", "extended_keyword", "exclude_extended_keyword", "employees", "exclude_employees", "location", "exclude_location", "naics_code", "exclude_naics_code", "industry_tags", "exclude_industry_tags", "all_industries", "exclude_all_industries", "total_funding", "exclude_total_funding", "description", "exclude_description", "primary_industry", "exclude_primary_industry", "website_url", "exclude_website_url", "email_domain", "exclude_email_domain", "domain", "exclude_domain", "insight", "exclude_insight", "geo", "exclude_geo", "simplified_keyword", "exclude_simplified_keyword", "link", "exclude_link", "industry", "exclude_industry", "publicly_traded", "exclude_publicly_traded", "revenue", "exclude_revenue", "id", "exclude_id", "techstack", "exclude_techstack", "website_category", "exclude_website_category", "is_primary", "exclude_is_primary", "sic_code", "exclude_sic_code", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["keyword"]) -> typing.Union[MetaOapg.properties.keyword, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_keyword"]) -> typing.Union[MetaOapg.properties.exclude_keyword, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["growth"]) -> typing.Union[MetaOapg.properties.growth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_growth"]) -> typing.Union[MetaOapg.properties.exclude_growth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_name"]) -> typing.Union[MetaOapg.properties.exclude_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extended_keyword"]) -> typing.Union[MetaOapg.properties.extended_keyword, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_extended_keyword"]) -> typing.Union[MetaOapg.properties.exclude_extended_keyword, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employees"]) -> typing.Union[MetaOapg.properties.employees, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_employees"]) -> typing.Union[MetaOapg.properties.exclude_employees, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> typing.Union[MetaOapg.properties.location, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_location"]) -> typing.Union[MetaOapg.properties.exclude_location, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["naics_code"]) -> typing.Union[MetaOapg.properties.naics_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_naics_code"]) -> typing.Union[MetaOapg.properties.exclude_naics_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["industry_tags"]) -> typing.Union[MetaOapg.properties.industry_tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_industry_tags"]) -> typing.Union[MetaOapg.properties.exclude_industry_tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["all_industries"]) -> typing.Union[MetaOapg.properties.all_industries, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_all_industries"]) -> typing.Union[MetaOapg.properties.exclude_all_industries, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_funding"]) -> typing.Union[MetaOapg.properties.total_funding, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_total_funding"]) -> typing.Union[MetaOapg.properties.exclude_total_funding, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_description"]) -> typing.Union[MetaOapg.properties.exclude_description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary_industry"]) -> typing.Union[MetaOapg.properties.primary_industry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_primary_industry"]) -> typing.Union[MetaOapg.properties.exclude_primary_industry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["website_url"]) -> typing.Union[MetaOapg.properties.website_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_website_url"]) -> typing.Union[MetaOapg.properties.exclude_website_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_domain"]) -> typing.Union[MetaOapg.properties.email_domain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_email_domain"]) -> typing.Union[MetaOapg.properties.exclude_email_domain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domain"]) -> typing.Union[MetaOapg.properties.domain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_domain"]) -> typing.Union[MetaOapg.properties.exclude_domain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["insight"]) -> typing.Union[MetaOapg.properties.insight, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_insight"]) -> typing.Union[MetaOapg.properties.exclude_insight, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["geo"]) -> typing.Union[MetaOapg.properties.geo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_geo"]) -> typing.Union[MetaOapg.properties.exclude_geo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["simplified_keyword"]) -> typing.Union[MetaOapg.properties.simplified_keyword, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_simplified_keyword"]) -> typing.Union[MetaOapg.properties.exclude_simplified_keyword, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> typing.Union[MetaOapg.properties.link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_link"]) -> typing.Union[MetaOapg.properties.exclude_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["industry"]) -> typing.Union[MetaOapg.properties.industry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_industry"]) -> typing.Union[MetaOapg.properties.exclude_industry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publicly_traded"]) -> typing.Union[MetaOapg.properties.publicly_traded, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_publicly_traded"]) -> typing.Union[MetaOapg.properties.exclude_publicly_traded, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["revenue"]) -> typing.Union[MetaOapg.properties.revenue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_revenue"]) -> typing.Union[MetaOapg.properties.exclude_revenue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_id"]) -> typing.Union[MetaOapg.properties.exclude_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["techstack"]) -> typing.Union[MetaOapg.properties.techstack, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_techstack"]) -> typing.Union[MetaOapg.properties.exclude_techstack, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["website_category"]) -> typing.Union[MetaOapg.properties.website_category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_website_category"]) -> typing.Union[MetaOapg.properties.exclude_website_category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_primary"]) -> typing.Union[MetaOapg.properties.is_primary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_is_primary"]) -> typing.Union[MetaOapg.properties.exclude_is_primary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sic_code"]) -> typing.Union[MetaOapg.properties.sic_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_sic_code"]) -> typing.Union[MetaOapg.properties.exclude_sic_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["keyword", "exclude_keyword", "growth", "exclude_growth", "name", "exclude_name", "extended_keyword", "exclude_extended_keyword", "employees", "exclude_employees", "location", "exclude_location", "naics_code", "exclude_naics_code", "industry_tags", "exclude_industry_tags", "all_industries", "exclude_all_industries", "total_funding", "exclude_total_funding", "description", "exclude_description", "primary_industry", "exclude_primary_industry", "website_url", "exclude_website_url", "email_domain", "exclude_email_domain", "domain", "exclude_domain", "insight", "exclude_insight", "geo", "exclude_geo", "simplified_keyword", "exclude_simplified_keyword", "link", "exclude_link", "industry", "exclude_industry", "publicly_traded", "exclude_publicly_traded", "revenue", "exclude_revenue", "id", "exclude_id", "techstack", "exclude_techstack", "website_category", "exclude_website_category", "is_primary", "exclude_is_primary", "sic_code", "exclude_sic_code", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        keyword: typing.Union[MetaOapg.properties.keyword, list, tuple, schemas.Unset] = schemas.unset,
        exclude_keyword: typing.Union[MetaOapg.properties.exclude_keyword, list, tuple, schemas.Unset] = schemas.unset,
        growth: typing.Union[MetaOapg.properties.growth, list, tuple, schemas.Unset] = schemas.unset,
        exclude_growth: typing.Union[MetaOapg.properties.exclude_growth, list, tuple, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, list, tuple, schemas.Unset] = schemas.unset,
        exclude_name: typing.Union[MetaOapg.properties.exclude_name, list, tuple, schemas.Unset] = schemas.unset,
        extended_keyword: typing.Union[MetaOapg.properties.extended_keyword, list, tuple, schemas.Unset] = schemas.unset,
        exclude_extended_keyword: typing.Union[MetaOapg.properties.exclude_extended_keyword, list, tuple, schemas.Unset] = schemas.unset,
        employees: typing.Union[MetaOapg.properties.employees, list, tuple, schemas.Unset] = schemas.unset,
        exclude_employees: typing.Union[MetaOapg.properties.exclude_employees, list, tuple, schemas.Unset] = schemas.unset,
        location: typing.Union[MetaOapg.properties.location, list, tuple, schemas.Unset] = schemas.unset,
        exclude_location: typing.Union[MetaOapg.properties.exclude_location, list, tuple, schemas.Unset] = schemas.unset,
        naics_code: typing.Union[MetaOapg.properties.naics_code, list, tuple, schemas.Unset] = schemas.unset,
        exclude_naics_code: typing.Union[MetaOapg.properties.exclude_naics_code, list, tuple, schemas.Unset] = schemas.unset,
        industry_tags: typing.Union[MetaOapg.properties.industry_tags, list, tuple, schemas.Unset] = schemas.unset,
        exclude_industry_tags: typing.Union[MetaOapg.properties.exclude_industry_tags, list, tuple, schemas.Unset] = schemas.unset,
        all_industries: typing.Union[MetaOapg.properties.all_industries, list, tuple, schemas.Unset] = schemas.unset,
        exclude_all_industries: typing.Union[MetaOapg.properties.exclude_all_industries, list, tuple, schemas.Unset] = schemas.unset,
        total_funding: typing.Union[MetaOapg.properties.total_funding, list, tuple, schemas.Unset] = schemas.unset,
        exclude_total_funding: typing.Union[MetaOapg.properties.exclude_total_funding, list, tuple, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, list, tuple, schemas.Unset] = schemas.unset,
        exclude_description: typing.Union[MetaOapg.properties.exclude_description, list, tuple, schemas.Unset] = schemas.unset,
        primary_industry: typing.Union[MetaOapg.properties.primary_industry, list, tuple, schemas.Unset] = schemas.unset,
        exclude_primary_industry: typing.Union[MetaOapg.properties.exclude_primary_industry, list, tuple, schemas.Unset] = schemas.unset,
        website_url: typing.Union[MetaOapg.properties.website_url, list, tuple, schemas.Unset] = schemas.unset,
        exclude_website_url: typing.Union[MetaOapg.properties.exclude_website_url, list, tuple, schemas.Unset] = schemas.unset,
        email_domain: typing.Union[MetaOapg.properties.email_domain, list, tuple, schemas.Unset] = schemas.unset,
        exclude_email_domain: typing.Union[MetaOapg.properties.exclude_email_domain, list, tuple, schemas.Unset] = schemas.unset,
        domain: typing.Union[MetaOapg.properties.domain, list, tuple, schemas.Unset] = schemas.unset,
        exclude_domain: typing.Union[MetaOapg.properties.exclude_domain, list, tuple, schemas.Unset] = schemas.unset,
        insight: typing.Union[MetaOapg.properties.insight, list, tuple, schemas.Unset] = schemas.unset,
        exclude_insight: typing.Union[MetaOapg.properties.exclude_insight, list, tuple, schemas.Unset] = schemas.unset,
        geo: typing.Union[MetaOapg.properties.geo, list, tuple, schemas.Unset] = schemas.unset,
        exclude_geo: typing.Union[MetaOapg.properties.exclude_geo, list, tuple, schemas.Unset] = schemas.unset,
        simplified_keyword: typing.Union[MetaOapg.properties.simplified_keyword, list, tuple, schemas.Unset] = schemas.unset,
        exclude_simplified_keyword: typing.Union[MetaOapg.properties.exclude_simplified_keyword, list, tuple, schemas.Unset] = schemas.unset,
        link: typing.Union[MetaOapg.properties.link, list, tuple, schemas.Unset] = schemas.unset,
        exclude_link: typing.Union[MetaOapg.properties.exclude_link, list, tuple, schemas.Unset] = schemas.unset,
        industry: typing.Union[MetaOapg.properties.industry, list, tuple, schemas.Unset] = schemas.unset,
        exclude_industry: typing.Union[MetaOapg.properties.exclude_industry, list, tuple, schemas.Unset] = schemas.unset,
        publicly_traded: typing.Union[MetaOapg.properties.publicly_traded, list, tuple, schemas.Unset] = schemas.unset,
        exclude_publicly_traded: typing.Union[MetaOapg.properties.exclude_publicly_traded, list, tuple, schemas.Unset] = schemas.unset,
        revenue: typing.Union[MetaOapg.properties.revenue, list, tuple, schemas.Unset] = schemas.unset,
        exclude_revenue: typing.Union[MetaOapg.properties.exclude_revenue, list, tuple, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, list, tuple, schemas.Unset] = schemas.unset,
        exclude_id: typing.Union[MetaOapg.properties.exclude_id, list, tuple, schemas.Unset] = schemas.unset,
        techstack: typing.Union[MetaOapg.properties.techstack, list, tuple, schemas.Unset] = schemas.unset,
        exclude_techstack: typing.Union[MetaOapg.properties.exclude_techstack, list, tuple, schemas.Unset] = schemas.unset,
        website_category: typing.Union[MetaOapg.properties.website_category, list, tuple, schemas.Unset] = schemas.unset,
        exclude_website_category: typing.Union[MetaOapg.properties.exclude_website_category, list, tuple, schemas.Unset] = schemas.unset,
        is_primary: typing.Union[MetaOapg.properties.is_primary, list, tuple, schemas.Unset] = schemas.unset,
        exclude_is_primary: typing.Union[MetaOapg.properties.exclude_is_primary, list, tuple, schemas.Unset] = schemas.unset,
        sic_code: typing.Union[MetaOapg.properties.sic_code, list, tuple, schemas.Unset] = schemas.unset,
        exclude_sic_code: typing.Union[MetaOapg.properties.exclude_sic_code, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CompanyQuery':
        return super().__new__(
            cls,
            *_args,
            keyword=keyword,
            exclude_keyword=exclude_keyword,
            growth=growth,
            exclude_growth=exclude_growth,
            name=name,
            exclude_name=exclude_name,
            extended_keyword=extended_keyword,
            exclude_extended_keyword=exclude_extended_keyword,
            employees=employees,
            exclude_employees=exclude_employees,
            location=location,
            exclude_location=exclude_location,
            naics_code=naics_code,
            exclude_naics_code=exclude_naics_code,
            industry_tags=industry_tags,
            exclude_industry_tags=exclude_industry_tags,
            all_industries=all_industries,
            exclude_all_industries=exclude_all_industries,
            total_funding=total_funding,
            exclude_total_funding=exclude_total_funding,
            description=description,
            exclude_description=exclude_description,
            primary_industry=primary_industry,
            exclude_primary_industry=exclude_primary_industry,
            website_url=website_url,
            exclude_website_url=exclude_website_url,
            email_domain=email_domain,
            exclude_email_domain=exclude_email_domain,
            domain=domain,
            exclude_domain=exclude_domain,
            insight=insight,
            exclude_insight=exclude_insight,
            geo=geo,
            exclude_geo=exclude_geo,
            simplified_keyword=simplified_keyword,
            exclude_simplified_keyword=exclude_simplified_keyword,
            link=link,
            exclude_link=exclude_link,
            industry=industry,
            exclude_industry=exclude_industry,
            publicly_traded=publicly_traded,
            exclude_publicly_traded=exclude_publicly_traded,
            revenue=revenue,
            exclude_revenue=exclude_revenue,
            id=id,
            exclude_id=exclude_id,
            techstack=techstack,
            exclude_techstack=exclude_techstack,
            website_category=website_category,
            exclude_website_category=exclude_website_category,
            is_primary=is_primary,
            exclude_is_primary=exclude_is_primary,
            sic_code=sic_code,
            exclude_sic_code=exclude_sic_code,
            _configuration=_configuration,
            **kwargs,
        )
