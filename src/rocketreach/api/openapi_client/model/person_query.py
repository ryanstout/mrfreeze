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


class PersonQuery(
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
            
            
            class company_naics_code(
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
                ) -> 'company_naics_code':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_naics_code(
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
                ) -> 'exclude_company_naics_code':
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
            
            
            class company_postal_code(
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
                ) -> 'company_postal_code':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_postal_code(
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
                ) -> 'exclude_company_postal_code':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class city(
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
                ) -> 'city':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_city(
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
                ) -> 'exclude_city':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class previous_employer(
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
                ) -> 'previous_employer':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_previous_employer(
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
                ) -> 'exclude_previous_employer':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class handle(
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
                ) -> 'handle':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_handle(
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
                ) -> 'exclude_handle':
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
            
            
            class company_revenue_max(
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
                ) -> 'company_revenue_max':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_revenue_max(
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
                ) -> 'exclude_company_revenue_max':
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
            
            
            class company_industry(
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
                ) -> 'company_industry':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_industry(
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
                ) -> 'exclude_company_industry':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class postal_code(
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
                ) -> 'postal_code':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_postal_code(
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
                ) -> 'exclude_postal_code':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class company_size_min(
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
                ) -> 'company_size_min':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_size_min(
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
                ) -> 'exclude_company_size_min':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class management_levels(
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
                ) -> 'management_levels':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_management_levels(
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
                ) -> 'exclude_management_levels':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class company_list_id(
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
                ) -> 'company_list_id':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_list_id(
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
                ) -> 'exclude_company_list_id':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class phone(
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
                ) -> 'phone':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_phone(
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
                ) -> 'exclude_phone':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class company_revenue(
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
                ) -> 'company_revenue':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_revenue(
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
                ) -> 'exclude_company_revenue':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class company_funding_max(
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
                ) -> 'company_funding_max':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_funding_max(
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
                ) -> 'exclude_company_funding_max':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class company_website_url(
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
                ) -> 'company_website_url':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_website_url(
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
                ) -> 'exclude_company_website_url':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class keywords(
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
                ) -> 'keywords':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_keywords(
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
                ) -> 'exclude_keywords':
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
            
            
            class veteran_status(
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
                ) -> 'veteran_status':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_veteran_status(
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
                ) -> 'exclude_veteran_status':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class company_website_rank_min(
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
                ) -> 'company_website_rank_min':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_website_rank_min(
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
                ) -> 'exclude_company_website_rank_min':
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
            
            
            class company_id(
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
                ) -> 'company_id':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_id(
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
                ) -> 'exclude_company_id':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class company_name(
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
                ) -> 'company_name':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_name(
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
                ) -> 'exclude_company_name':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class company_industry_tags(
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
                ) -> 'company_industry_tags':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_industry_tags(
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
                ) -> 'exclude_company_industry_tags':
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
            
            
            class birth_year(
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
                ) -> 'birth_year':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_birth_year(
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
                ) -> 'exclude_birth_year':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class keyword_orig(
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
                ) -> 'keyword_orig':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_keyword_orig(
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
                ) -> 'exclude_keyword_orig':
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
            
            
            class email(
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
                ) -> 'email':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_email(
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
                ) -> 'exclude_email':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class ethnicity(
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
                ) -> 'ethnicity':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_ethnicity(
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
                ) -> 'exclude_ethnicity':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class company_website_rank_max(
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
                ) -> 'company_website_rank_max':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_website_rank_max(
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
                ) -> 'exclude_company_website_rank_max':
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
            
            
            class company_publicly_traded(
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
                ) -> 'company_publicly_traded':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_publicly_traded(
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
                ) -> 'exclude_company_publicly_traded':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class sic_codes(
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
                ) -> 'sic_codes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_sic_codes(
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
                ) -> 'exclude_sic_codes':
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
            
            
            class company_email(
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
                ) -> 'company_email':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_email(
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
                ) -> 'exclude_company_email':
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
            
            
            class degree(
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
                ) -> 'degree':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_degree(
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
                ) -> 'exclude_degree':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class years_experience(
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
                ) -> 'years_experience':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_years_experience(
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
                ) -> 'exclude_years_experience':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class country(
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
                ) -> 'country':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_country(
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
                ) -> 'exclude_country':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class company_size_max(
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
                ) -> 'company_size_max':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_size_max(
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
                ) -> 'exclude_company_size_max':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class current_title(
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
                ) -> 'current_title':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_current_title(
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
                ) -> 'exclude_current_title':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class department(
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
                ) -> 'department':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_department(
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
                ) -> 'exclude_department':
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
            
            
            class keyword_enhanced(
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
                ) -> 'keyword_enhanced':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_keyword_enhanced(
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
                ) -> 'exclude_keyword_enhanced':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class company_city(
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
                ) -> 'company_city':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_city(
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
                ) -> 'exclude_company_city':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class company_revenue_min(
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
                ) -> 'company_revenue_min':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_revenue_min(
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
                ) -> 'exclude_company_revenue_min':
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
            
            
            class company_website_rank(
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
                ) -> 'company_website_rank':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_website_rank(
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
                ) -> 'exclude_company_website_rank':
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
            
            
            class job_change_range_days(
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
                ) -> 'job_change_range_days':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_job_change_range_days(
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
                ) -> 'exclude_job_change_range_days':
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
            
            
            class company_country_code(
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
                ) -> 'company_country_code':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_country_code(
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
                ) -> 'exclude_company_country_code':
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
            
            
            class gender(
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
                ) -> 'gender':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_gender(
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
                ) -> 'exclude_gender':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class company_sic_code(
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
                ) -> 'company_sic_code':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_sic_code(
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
                ) -> 'exclude_company_sic_code':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class naics_codes(
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
                ) -> 'naics_codes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_naics_codes(
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
                ) -> 'exclude_naics_codes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class company_size(
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
                ) -> 'company_size':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_size(
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
                ) -> 'exclude_company_size':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class normalized_title(
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
                ) -> 'normalized_title':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_normalized_title(
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
                ) -> 'exclude_normalized_title':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class connections(
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
                ) -> 'connections':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_connections(
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
                ) -> 'exclude_connections':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class major(
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
                ) -> 'major':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_major(
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
                ) -> 'exclude_major':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class company_list(
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
                ) -> 'company_list':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_list(
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
                ) -> 'exclude_company_list':
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
            
            
            class previous_company_id(
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
                ) -> 'previous_company_id':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_previous_company_id(
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
                ) -> 'exclude_previous_company_id':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class state(
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
                ) -> 'state':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_state(
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
                ) -> 'exclude_state':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
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
            
            
            class exclude_skills(
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
                ) -> 'exclude_skills':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class company_domain(
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
                ) -> 'company_domain':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_domain(
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
                ) -> 'exclude_company_domain':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class company_region(
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
                ) -> 'company_region':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_region(
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
                ) -> 'exclude_company_region':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class company_website_category(
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
                ) -> 'company_website_category':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_website_category(
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
                ) -> 'exclude_company_website_category':
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
            
            
            class current_employer(
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
                ) -> 'current_employer':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_current_employer(
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
                ) -> 'exclude_current_employer':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class company_funding_min(
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
                ) -> 'company_funding_min':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_company_funding_min(
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
                ) -> 'exclude_company_funding_min':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class employer(
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
                ) -> 'employer':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_employer(
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
                ) -> 'exclude_employer':
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
            
            
            class school(
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
                ) -> 'school':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class exclude_school(
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
                ) -> 'exclude_school':
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
                "company_naics_code": company_naics_code,
                "exclude_company_naics_code": exclude_company_naics_code,
                "name": name,
                "exclude_name": exclude_name,
                "company_postal_code": company_postal_code,
                "exclude_company_postal_code": exclude_company_postal_code,
                "city": city,
                "exclude_city": exclude_city,
                "previous_employer": previous_employer,
                "exclude_previous_employer": exclude_previous_employer,
                "handle": handle,
                "exclude_handle": exclude_handle,
                "industry_tags": industry_tags,
                "exclude_industry_tags": exclude_industry_tags,
                "company_revenue_max": company_revenue_max,
                "exclude_company_revenue_max": exclude_company_revenue_max,
                "sic_code": sic_code,
                "exclude_sic_code": exclude_sic_code,
                "company_industry": company_industry,
                "exclude_company_industry": exclude_company_industry,
                "postal_code": postal_code,
                "exclude_postal_code": exclude_postal_code,
                "company_size_min": company_size_min,
                "exclude_company_size_min": exclude_company_size_min,
                "management_levels": management_levels,
                "exclude_management_levels": exclude_management_levels,
                "company_list_id": company_list_id,
                "exclude_company_list_id": exclude_company_list_id,
                "phone": phone,
                "exclude_phone": exclude_phone,
                "company_revenue": company_revenue,
                "exclude_company_revenue": exclude_company_revenue,
                "company_funding_max": company_funding_max,
                "exclude_company_funding_max": exclude_company_funding_max,
                "company_website_url": company_website_url,
                "exclude_company_website_url": exclude_company_website_url,
                "keywords": keywords,
                "exclude_keywords": exclude_keywords,
                "insight": insight,
                "exclude_insight": exclude_insight,
                "veteran_status": veteran_status,
                "exclude_veteran_status": exclude_veteran_status,
                "company_website_rank_min": company_website_rank_min,
                "exclude_company_website_rank_min": exclude_company_website_rank_min,
                "simplified_keyword": simplified_keyword,
                "exclude_simplified_keyword": exclude_simplified_keyword,
                "link": link,
                "exclude_link": exclude_link,
                "company_id": company_id,
                "exclude_company_id": exclude_company_id,
                "company_name": company_name,
                "exclude_company_name": exclude_company_name,
                "company_industry_tags": company_industry_tags,
                "exclude_company_industry_tags": exclude_company_industry_tags,
                "techstack": techstack,
                "exclude_techstack": exclude_techstack,
                "is_primary": is_primary,
                "exclude_is_primary": exclude_is_primary,
                "birth_year": birth_year,
                "exclude_birth_year": exclude_birth_year,
                "keyword_orig": keyword_orig,
                "exclude_keyword_orig": exclude_keyword_orig,
                "growth": growth,
                "exclude_growth": exclude_growth,
                "email": email,
                "exclude_email": exclude_email,
                "ethnicity": ethnicity,
                "exclude_ethnicity": exclude_ethnicity,
                "company_website_rank_max": company_website_rank_max,
                "exclude_company_website_rank_max": exclude_company_website_rank_max,
                "extended_keyword": extended_keyword,
                "exclude_extended_keyword": exclude_extended_keyword,
                "employees": employees,
                "exclude_employees": exclude_employees,
                "company_publicly_traded": company_publicly_traded,
                "exclude_company_publicly_traded": exclude_company_publicly_traded,
                "sic_codes": sic_codes,
                "exclude_sic_codes": exclude_sic_codes,
                "location": location,
                "exclude_location": exclude_location,
                "company_email": company_email,
                "exclude_company_email": exclude_company_email,
                "naics_code": naics_code,
                "exclude_naics_code": exclude_naics_code,
                "degree": degree,
                "exclude_degree": exclude_degree,
                "years_experience": years_experience,
                "exclude_years_experience": exclude_years_experience,
                "country": country,
                "exclude_country": exclude_country,
                "company_size_max": company_size_max,
                "exclude_company_size_max": exclude_company_size_max,
                "current_title": current_title,
                "exclude_current_title": exclude_current_title,
                "department": department,
                "exclude_department": exclude_department,
                "all_industries": all_industries,
                "exclude_all_industries": exclude_all_industries,
                "keyword_enhanced": keyword_enhanced,
                "exclude_keyword_enhanced": exclude_keyword_enhanced,
                "company_city": company_city,
                "exclude_company_city": exclude_company_city,
                "company_revenue_min": company_revenue_min,
                "exclude_company_revenue_min": exclude_company_revenue_min,
                "total_funding": total_funding,
                "exclude_total_funding": exclude_total_funding,
                "company_website_rank": company_website_rank,
                "exclude_company_website_rank": exclude_company_website_rank,
                "description": description,
                "exclude_description": exclude_description,
                "job_change_range_days": job_change_range_days,
                "exclude_job_change_range_days": exclude_job_change_range_days,
                "primary_industry": primary_industry,
                "exclude_primary_industry": exclude_primary_industry,
                "website_url": website_url,
                "exclude_website_url": exclude_website_url,
                "company_country_code": company_country_code,
                "exclude_company_country_code": exclude_company_country_code,
                "domain": domain,
                "exclude_domain": exclude_domain,
                "email_domain": email_domain,
                "exclude_email_domain": exclude_email_domain,
                "gender": gender,
                "exclude_gender": exclude_gender,
                "company_sic_code": company_sic_code,
                "exclude_company_sic_code": exclude_company_sic_code,
                "naics_codes": naics_codes,
                "exclude_naics_codes": exclude_naics_codes,
                "company_size": company_size,
                "exclude_company_size": exclude_company_size,
                "normalized_title": normalized_title,
                "exclude_normalized_title": exclude_normalized_title,
                "connections": connections,
                "exclude_connections": exclude_connections,
                "major": major,
                "exclude_major": exclude_major,
                "company_list": company_list,
                "exclude_company_list": exclude_company_list,
                "geo": geo,
                "exclude_geo": exclude_geo,
                "previous_company_id": previous_company_id,
                "exclude_previous_company_id": exclude_previous_company_id,
                "state": state,
                "exclude_state": exclude_state,
                "skills": skills,
                "exclude_skills": exclude_skills,
                "company_domain": company_domain,
                "exclude_company_domain": exclude_company_domain,
                "company_region": company_region,
                "exclude_company_region": exclude_company_region,
                "company_website_category": company_website_category,
                "exclude_company_website_category": exclude_company_website_category,
                "industry": industry,
                "exclude_industry": exclude_industry,
                "publicly_traded": publicly_traded,
                "exclude_publicly_traded": exclude_publicly_traded,
                "revenue": revenue,
                "exclude_revenue": exclude_revenue,
                "id": id,
                "exclude_id": exclude_id,
                "current_employer": current_employer,
                "exclude_current_employer": exclude_current_employer,
                "company_funding_min": company_funding_min,
                "exclude_company_funding_min": exclude_company_funding_min,
                "employer": employer,
                "exclude_employer": exclude_employer,
                "website_category": website_category,
                "exclude_website_category": exclude_website_category,
                "school": school,
                "exclude_school": exclude_school,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["keyword"]) -> MetaOapg.properties.keyword: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_keyword"]) -> MetaOapg.properties.exclude_keyword: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_naics_code"]) -> MetaOapg.properties.company_naics_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_naics_code"]) -> MetaOapg.properties.exclude_company_naics_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_name"]) -> MetaOapg.properties.exclude_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_postal_code"]) -> MetaOapg.properties.company_postal_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_postal_code"]) -> MetaOapg.properties.exclude_company_postal_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_city"]) -> MetaOapg.properties.exclude_city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["previous_employer"]) -> MetaOapg.properties.previous_employer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_previous_employer"]) -> MetaOapg.properties.exclude_previous_employer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["handle"]) -> MetaOapg.properties.handle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_handle"]) -> MetaOapg.properties.exclude_handle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["industry_tags"]) -> MetaOapg.properties.industry_tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_industry_tags"]) -> MetaOapg.properties.exclude_industry_tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_revenue_max"]) -> MetaOapg.properties.company_revenue_max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_revenue_max"]) -> MetaOapg.properties.exclude_company_revenue_max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sic_code"]) -> MetaOapg.properties.sic_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_sic_code"]) -> MetaOapg.properties.exclude_sic_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_industry"]) -> MetaOapg.properties.company_industry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_industry"]) -> MetaOapg.properties.exclude_company_industry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postal_code"]) -> MetaOapg.properties.postal_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_postal_code"]) -> MetaOapg.properties.exclude_postal_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_size_min"]) -> MetaOapg.properties.company_size_min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_size_min"]) -> MetaOapg.properties.exclude_company_size_min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["management_levels"]) -> MetaOapg.properties.management_levels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_management_levels"]) -> MetaOapg.properties.exclude_management_levels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_list_id"]) -> MetaOapg.properties.company_list_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_list_id"]) -> MetaOapg.properties.exclude_company_list_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_phone"]) -> MetaOapg.properties.exclude_phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_revenue"]) -> MetaOapg.properties.company_revenue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_revenue"]) -> MetaOapg.properties.exclude_company_revenue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_funding_max"]) -> MetaOapg.properties.company_funding_max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_funding_max"]) -> MetaOapg.properties.exclude_company_funding_max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_website_url"]) -> MetaOapg.properties.company_website_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_website_url"]) -> MetaOapg.properties.exclude_company_website_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["keywords"]) -> MetaOapg.properties.keywords: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_keywords"]) -> MetaOapg.properties.exclude_keywords: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["insight"]) -> MetaOapg.properties.insight: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_insight"]) -> MetaOapg.properties.exclude_insight: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["veteran_status"]) -> MetaOapg.properties.veteran_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_veteran_status"]) -> MetaOapg.properties.exclude_veteran_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_website_rank_min"]) -> MetaOapg.properties.company_website_rank_min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_website_rank_min"]) -> MetaOapg.properties.exclude_company_website_rank_min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["simplified_keyword"]) -> MetaOapg.properties.simplified_keyword: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_simplified_keyword"]) -> MetaOapg.properties.exclude_simplified_keyword: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["link"]) -> MetaOapg.properties.link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_link"]) -> MetaOapg.properties.exclude_link: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_id"]) -> MetaOapg.properties.company_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_id"]) -> MetaOapg.properties.exclude_company_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_name"]) -> MetaOapg.properties.company_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_name"]) -> MetaOapg.properties.exclude_company_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_industry_tags"]) -> MetaOapg.properties.company_industry_tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_industry_tags"]) -> MetaOapg.properties.exclude_company_industry_tags: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["techstack"]) -> MetaOapg.properties.techstack: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_techstack"]) -> MetaOapg.properties.exclude_techstack: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_primary"]) -> MetaOapg.properties.is_primary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_is_primary"]) -> MetaOapg.properties.exclude_is_primary: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["birth_year"]) -> MetaOapg.properties.birth_year: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_birth_year"]) -> MetaOapg.properties.exclude_birth_year: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["keyword_orig"]) -> MetaOapg.properties.keyword_orig: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_keyword_orig"]) -> MetaOapg.properties.exclude_keyword_orig: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["growth"]) -> MetaOapg.properties.growth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_growth"]) -> MetaOapg.properties.exclude_growth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_email"]) -> MetaOapg.properties.exclude_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ethnicity"]) -> MetaOapg.properties.ethnicity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_ethnicity"]) -> MetaOapg.properties.exclude_ethnicity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_website_rank_max"]) -> MetaOapg.properties.company_website_rank_max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_website_rank_max"]) -> MetaOapg.properties.exclude_company_website_rank_max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extended_keyword"]) -> MetaOapg.properties.extended_keyword: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_extended_keyword"]) -> MetaOapg.properties.exclude_extended_keyword: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employees"]) -> MetaOapg.properties.employees: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_employees"]) -> MetaOapg.properties.exclude_employees: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_publicly_traded"]) -> MetaOapg.properties.company_publicly_traded: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_publicly_traded"]) -> MetaOapg.properties.exclude_company_publicly_traded: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sic_codes"]) -> MetaOapg.properties.sic_codes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_sic_codes"]) -> MetaOapg.properties.exclude_sic_codes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location"]) -> MetaOapg.properties.location: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_location"]) -> MetaOapg.properties.exclude_location: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_email"]) -> MetaOapg.properties.company_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_email"]) -> MetaOapg.properties.exclude_company_email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["naics_code"]) -> MetaOapg.properties.naics_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_naics_code"]) -> MetaOapg.properties.exclude_naics_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["degree"]) -> MetaOapg.properties.degree: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_degree"]) -> MetaOapg.properties.exclude_degree: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["years_experience"]) -> MetaOapg.properties.years_experience: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_years_experience"]) -> MetaOapg.properties.exclude_years_experience: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_country"]) -> MetaOapg.properties.exclude_country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_size_max"]) -> MetaOapg.properties.company_size_max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_size_max"]) -> MetaOapg.properties.exclude_company_size_max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["current_title"]) -> MetaOapg.properties.current_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_current_title"]) -> MetaOapg.properties.exclude_current_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department"]) -> MetaOapg.properties.department: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_department"]) -> MetaOapg.properties.exclude_department: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["all_industries"]) -> MetaOapg.properties.all_industries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_all_industries"]) -> MetaOapg.properties.exclude_all_industries: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["keyword_enhanced"]) -> MetaOapg.properties.keyword_enhanced: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_keyword_enhanced"]) -> MetaOapg.properties.exclude_keyword_enhanced: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_city"]) -> MetaOapg.properties.company_city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_city"]) -> MetaOapg.properties.exclude_company_city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_revenue_min"]) -> MetaOapg.properties.company_revenue_min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_revenue_min"]) -> MetaOapg.properties.exclude_company_revenue_min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_funding"]) -> MetaOapg.properties.total_funding: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_total_funding"]) -> MetaOapg.properties.exclude_total_funding: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_website_rank"]) -> MetaOapg.properties.company_website_rank: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_website_rank"]) -> MetaOapg.properties.exclude_company_website_rank: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_description"]) -> MetaOapg.properties.exclude_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job_change_range_days"]) -> MetaOapg.properties.job_change_range_days: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_job_change_range_days"]) -> MetaOapg.properties.exclude_job_change_range_days: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary_industry"]) -> MetaOapg.properties.primary_industry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_primary_industry"]) -> MetaOapg.properties.exclude_primary_industry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["website_url"]) -> MetaOapg.properties.website_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_website_url"]) -> MetaOapg.properties.exclude_website_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_country_code"]) -> MetaOapg.properties.company_country_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_country_code"]) -> MetaOapg.properties.exclude_company_country_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domain"]) -> MetaOapg.properties.domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_domain"]) -> MetaOapg.properties.exclude_domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email_domain"]) -> MetaOapg.properties.email_domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_email_domain"]) -> MetaOapg.properties.exclude_email_domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gender"]) -> MetaOapg.properties.gender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_gender"]) -> MetaOapg.properties.exclude_gender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_sic_code"]) -> MetaOapg.properties.company_sic_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_sic_code"]) -> MetaOapg.properties.exclude_company_sic_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["naics_codes"]) -> MetaOapg.properties.naics_codes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_naics_codes"]) -> MetaOapg.properties.exclude_naics_codes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_size"]) -> MetaOapg.properties.company_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_size"]) -> MetaOapg.properties.exclude_company_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["normalized_title"]) -> MetaOapg.properties.normalized_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_normalized_title"]) -> MetaOapg.properties.exclude_normalized_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connections"]) -> MetaOapg.properties.connections: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_connections"]) -> MetaOapg.properties.exclude_connections: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["major"]) -> MetaOapg.properties.major: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_major"]) -> MetaOapg.properties.exclude_major: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_list"]) -> MetaOapg.properties.company_list: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_list"]) -> MetaOapg.properties.exclude_company_list: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["geo"]) -> MetaOapg.properties.geo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_geo"]) -> MetaOapg.properties.exclude_geo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["previous_company_id"]) -> MetaOapg.properties.previous_company_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_previous_company_id"]) -> MetaOapg.properties.exclude_previous_company_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_state"]) -> MetaOapg.properties.exclude_state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["skills"]) -> MetaOapg.properties.skills: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_skills"]) -> MetaOapg.properties.exclude_skills: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_domain"]) -> MetaOapg.properties.company_domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_domain"]) -> MetaOapg.properties.exclude_company_domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_region"]) -> MetaOapg.properties.company_region: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_region"]) -> MetaOapg.properties.exclude_company_region: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_website_category"]) -> MetaOapg.properties.company_website_category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_website_category"]) -> MetaOapg.properties.exclude_company_website_category: ...
    
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
    def __getitem__(self, name: typing_extensions.Literal["current_employer"]) -> MetaOapg.properties.current_employer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_current_employer"]) -> MetaOapg.properties.exclude_current_employer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_funding_min"]) -> MetaOapg.properties.company_funding_min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_company_funding_min"]) -> MetaOapg.properties.exclude_company_funding_min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employer"]) -> MetaOapg.properties.employer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_employer"]) -> MetaOapg.properties.exclude_employer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["website_category"]) -> MetaOapg.properties.website_category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_website_category"]) -> MetaOapg.properties.exclude_website_category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["school"]) -> MetaOapg.properties.school: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_school"]) -> MetaOapg.properties.exclude_school: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["keyword", "exclude_keyword", "company_naics_code", "exclude_company_naics_code", "name", "exclude_name", "company_postal_code", "exclude_company_postal_code", "city", "exclude_city", "previous_employer", "exclude_previous_employer", "handle", "exclude_handle", "industry_tags", "exclude_industry_tags", "company_revenue_max", "exclude_company_revenue_max", "sic_code", "exclude_sic_code", "company_industry", "exclude_company_industry", "postal_code", "exclude_postal_code", "company_size_min", "exclude_company_size_min", "management_levels", "exclude_management_levels", "company_list_id", "exclude_company_list_id", "phone", "exclude_phone", "company_revenue", "exclude_company_revenue", "company_funding_max", "exclude_company_funding_max", "company_website_url", "exclude_company_website_url", "keywords", "exclude_keywords", "insight", "exclude_insight", "veteran_status", "exclude_veteran_status", "company_website_rank_min", "exclude_company_website_rank_min", "simplified_keyword", "exclude_simplified_keyword", "link", "exclude_link", "company_id", "exclude_company_id", "company_name", "exclude_company_name", "company_industry_tags", "exclude_company_industry_tags", "techstack", "exclude_techstack", "is_primary", "exclude_is_primary", "birth_year", "exclude_birth_year", "keyword_orig", "exclude_keyword_orig", "growth", "exclude_growth", "email", "exclude_email", "ethnicity", "exclude_ethnicity", "company_website_rank_max", "exclude_company_website_rank_max", "extended_keyword", "exclude_extended_keyword", "employees", "exclude_employees", "company_publicly_traded", "exclude_company_publicly_traded", "sic_codes", "exclude_sic_codes", "location", "exclude_location", "company_email", "exclude_company_email", "naics_code", "exclude_naics_code", "degree", "exclude_degree", "years_experience", "exclude_years_experience", "country", "exclude_country", "company_size_max", "exclude_company_size_max", "current_title", "exclude_current_title", "department", "exclude_department", "all_industries", "exclude_all_industries", "keyword_enhanced", "exclude_keyword_enhanced", "company_city", "exclude_company_city", "company_revenue_min", "exclude_company_revenue_min", "total_funding", "exclude_total_funding", "company_website_rank", "exclude_company_website_rank", "description", "exclude_description", "job_change_range_days", "exclude_job_change_range_days", "primary_industry", "exclude_primary_industry", "website_url", "exclude_website_url", "company_country_code", "exclude_company_country_code", "domain", "exclude_domain", "email_domain", "exclude_email_domain", "gender", "exclude_gender", "company_sic_code", "exclude_company_sic_code", "naics_codes", "exclude_naics_codes", "company_size", "exclude_company_size", "normalized_title", "exclude_normalized_title", "connections", "exclude_connections", "major", "exclude_major", "company_list", "exclude_company_list", "geo", "exclude_geo", "previous_company_id", "exclude_previous_company_id", "state", "exclude_state", "skills", "exclude_skills", "company_domain", "exclude_company_domain", "company_region", "exclude_company_region", "company_website_category", "exclude_company_website_category", "industry", "exclude_industry", "publicly_traded", "exclude_publicly_traded", "revenue", "exclude_revenue", "id", "exclude_id", "current_employer", "exclude_current_employer", "company_funding_min", "exclude_company_funding_min", "employer", "exclude_employer", "website_category", "exclude_website_category", "school", "exclude_school", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["keyword"]) -> typing.Union[MetaOapg.properties.keyword, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_keyword"]) -> typing.Union[MetaOapg.properties.exclude_keyword, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_naics_code"]) -> typing.Union[MetaOapg.properties.company_naics_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_naics_code"]) -> typing.Union[MetaOapg.properties.exclude_company_naics_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_name"]) -> typing.Union[MetaOapg.properties.exclude_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_postal_code"]) -> typing.Union[MetaOapg.properties.company_postal_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_postal_code"]) -> typing.Union[MetaOapg.properties.exclude_company_postal_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_city"]) -> typing.Union[MetaOapg.properties.exclude_city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["previous_employer"]) -> typing.Union[MetaOapg.properties.previous_employer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_previous_employer"]) -> typing.Union[MetaOapg.properties.exclude_previous_employer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["handle"]) -> typing.Union[MetaOapg.properties.handle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_handle"]) -> typing.Union[MetaOapg.properties.exclude_handle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["industry_tags"]) -> typing.Union[MetaOapg.properties.industry_tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_industry_tags"]) -> typing.Union[MetaOapg.properties.exclude_industry_tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_revenue_max"]) -> typing.Union[MetaOapg.properties.company_revenue_max, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_revenue_max"]) -> typing.Union[MetaOapg.properties.exclude_company_revenue_max, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sic_code"]) -> typing.Union[MetaOapg.properties.sic_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_sic_code"]) -> typing.Union[MetaOapg.properties.exclude_sic_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_industry"]) -> typing.Union[MetaOapg.properties.company_industry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_industry"]) -> typing.Union[MetaOapg.properties.exclude_company_industry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postal_code"]) -> typing.Union[MetaOapg.properties.postal_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_postal_code"]) -> typing.Union[MetaOapg.properties.exclude_postal_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_size_min"]) -> typing.Union[MetaOapg.properties.company_size_min, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_size_min"]) -> typing.Union[MetaOapg.properties.exclude_company_size_min, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["management_levels"]) -> typing.Union[MetaOapg.properties.management_levels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_management_levels"]) -> typing.Union[MetaOapg.properties.exclude_management_levels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_list_id"]) -> typing.Union[MetaOapg.properties.company_list_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_list_id"]) -> typing.Union[MetaOapg.properties.exclude_company_list_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_phone"]) -> typing.Union[MetaOapg.properties.exclude_phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_revenue"]) -> typing.Union[MetaOapg.properties.company_revenue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_revenue"]) -> typing.Union[MetaOapg.properties.exclude_company_revenue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_funding_max"]) -> typing.Union[MetaOapg.properties.company_funding_max, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_funding_max"]) -> typing.Union[MetaOapg.properties.exclude_company_funding_max, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_website_url"]) -> typing.Union[MetaOapg.properties.company_website_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_website_url"]) -> typing.Union[MetaOapg.properties.exclude_company_website_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["keywords"]) -> typing.Union[MetaOapg.properties.keywords, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_keywords"]) -> typing.Union[MetaOapg.properties.exclude_keywords, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["insight"]) -> typing.Union[MetaOapg.properties.insight, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_insight"]) -> typing.Union[MetaOapg.properties.exclude_insight, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["veteran_status"]) -> typing.Union[MetaOapg.properties.veteran_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_veteran_status"]) -> typing.Union[MetaOapg.properties.exclude_veteran_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_website_rank_min"]) -> typing.Union[MetaOapg.properties.company_website_rank_min, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_website_rank_min"]) -> typing.Union[MetaOapg.properties.exclude_company_website_rank_min, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["simplified_keyword"]) -> typing.Union[MetaOapg.properties.simplified_keyword, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_simplified_keyword"]) -> typing.Union[MetaOapg.properties.exclude_simplified_keyword, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["link"]) -> typing.Union[MetaOapg.properties.link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_link"]) -> typing.Union[MetaOapg.properties.exclude_link, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_id"]) -> typing.Union[MetaOapg.properties.company_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_id"]) -> typing.Union[MetaOapg.properties.exclude_company_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_name"]) -> typing.Union[MetaOapg.properties.company_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_name"]) -> typing.Union[MetaOapg.properties.exclude_company_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_industry_tags"]) -> typing.Union[MetaOapg.properties.company_industry_tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_industry_tags"]) -> typing.Union[MetaOapg.properties.exclude_company_industry_tags, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["techstack"]) -> typing.Union[MetaOapg.properties.techstack, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_techstack"]) -> typing.Union[MetaOapg.properties.exclude_techstack, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_primary"]) -> typing.Union[MetaOapg.properties.is_primary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_is_primary"]) -> typing.Union[MetaOapg.properties.exclude_is_primary, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["birth_year"]) -> typing.Union[MetaOapg.properties.birth_year, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_birth_year"]) -> typing.Union[MetaOapg.properties.exclude_birth_year, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["keyword_orig"]) -> typing.Union[MetaOapg.properties.keyword_orig, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_keyword_orig"]) -> typing.Union[MetaOapg.properties.exclude_keyword_orig, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["growth"]) -> typing.Union[MetaOapg.properties.growth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_growth"]) -> typing.Union[MetaOapg.properties.exclude_growth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_email"]) -> typing.Union[MetaOapg.properties.exclude_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ethnicity"]) -> typing.Union[MetaOapg.properties.ethnicity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_ethnicity"]) -> typing.Union[MetaOapg.properties.exclude_ethnicity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_website_rank_max"]) -> typing.Union[MetaOapg.properties.company_website_rank_max, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_website_rank_max"]) -> typing.Union[MetaOapg.properties.exclude_company_website_rank_max, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extended_keyword"]) -> typing.Union[MetaOapg.properties.extended_keyword, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_extended_keyword"]) -> typing.Union[MetaOapg.properties.exclude_extended_keyword, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employees"]) -> typing.Union[MetaOapg.properties.employees, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_employees"]) -> typing.Union[MetaOapg.properties.exclude_employees, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_publicly_traded"]) -> typing.Union[MetaOapg.properties.company_publicly_traded, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_publicly_traded"]) -> typing.Union[MetaOapg.properties.exclude_company_publicly_traded, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sic_codes"]) -> typing.Union[MetaOapg.properties.sic_codes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_sic_codes"]) -> typing.Union[MetaOapg.properties.exclude_sic_codes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location"]) -> typing.Union[MetaOapg.properties.location, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_location"]) -> typing.Union[MetaOapg.properties.exclude_location, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_email"]) -> typing.Union[MetaOapg.properties.company_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_email"]) -> typing.Union[MetaOapg.properties.exclude_company_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["naics_code"]) -> typing.Union[MetaOapg.properties.naics_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_naics_code"]) -> typing.Union[MetaOapg.properties.exclude_naics_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["degree"]) -> typing.Union[MetaOapg.properties.degree, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_degree"]) -> typing.Union[MetaOapg.properties.exclude_degree, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["years_experience"]) -> typing.Union[MetaOapg.properties.years_experience, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_years_experience"]) -> typing.Union[MetaOapg.properties.exclude_years_experience, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_country"]) -> typing.Union[MetaOapg.properties.exclude_country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_size_max"]) -> typing.Union[MetaOapg.properties.company_size_max, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_size_max"]) -> typing.Union[MetaOapg.properties.exclude_company_size_max, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["current_title"]) -> typing.Union[MetaOapg.properties.current_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_current_title"]) -> typing.Union[MetaOapg.properties.exclude_current_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department"]) -> typing.Union[MetaOapg.properties.department, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_department"]) -> typing.Union[MetaOapg.properties.exclude_department, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["all_industries"]) -> typing.Union[MetaOapg.properties.all_industries, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_all_industries"]) -> typing.Union[MetaOapg.properties.exclude_all_industries, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["keyword_enhanced"]) -> typing.Union[MetaOapg.properties.keyword_enhanced, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_keyword_enhanced"]) -> typing.Union[MetaOapg.properties.exclude_keyword_enhanced, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_city"]) -> typing.Union[MetaOapg.properties.company_city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_city"]) -> typing.Union[MetaOapg.properties.exclude_company_city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_revenue_min"]) -> typing.Union[MetaOapg.properties.company_revenue_min, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_revenue_min"]) -> typing.Union[MetaOapg.properties.exclude_company_revenue_min, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_funding"]) -> typing.Union[MetaOapg.properties.total_funding, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_total_funding"]) -> typing.Union[MetaOapg.properties.exclude_total_funding, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_website_rank"]) -> typing.Union[MetaOapg.properties.company_website_rank, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_website_rank"]) -> typing.Union[MetaOapg.properties.exclude_company_website_rank, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_description"]) -> typing.Union[MetaOapg.properties.exclude_description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job_change_range_days"]) -> typing.Union[MetaOapg.properties.job_change_range_days, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_job_change_range_days"]) -> typing.Union[MetaOapg.properties.exclude_job_change_range_days, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary_industry"]) -> typing.Union[MetaOapg.properties.primary_industry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_primary_industry"]) -> typing.Union[MetaOapg.properties.exclude_primary_industry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["website_url"]) -> typing.Union[MetaOapg.properties.website_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_website_url"]) -> typing.Union[MetaOapg.properties.exclude_website_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_country_code"]) -> typing.Union[MetaOapg.properties.company_country_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_country_code"]) -> typing.Union[MetaOapg.properties.exclude_company_country_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domain"]) -> typing.Union[MetaOapg.properties.domain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_domain"]) -> typing.Union[MetaOapg.properties.exclude_domain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email_domain"]) -> typing.Union[MetaOapg.properties.email_domain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_email_domain"]) -> typing.Union[MetaOapg.properties.exclude_email_domain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gender"]) -> typing.Union[MetaOapg.properties.gender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_gender"]) -> typing.Union[MetaOapg.properties.exclude_gender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_sic_code"]) -> typing.Union[MetaOapg.properties.company_sic_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_sic_code"]) -> typing.Union[MetaOapg.properties.exclude_company_sic_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["naics_codes"]) -> typing.Union[MetaOapg.properties.naics_codes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_naics_codes"]) -> typing.Union[MetaOapg.properties.exclude_naics_codes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_size"]) -> typing.Union[MetaOapg.properties.company_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_size"]) -> typing.Union[MetaOapg.properties.exclude_company_size, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["normalized_title"]) -> typing.Union[MetaOapg.properties.normalized_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_normalized_title"]) -> typing.Union[MetaOapg.properties.exclude_normalized_title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connections"]) -> typing.Union[MetaOapg.properties.connections, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_connections"]) -> typing.Union[MetaOapg.properties.exclude_connections, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["major"]) -> typing.Union[MetaOapg.properties.major, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_major"]) -> typing.Union[MetaOapg.properties.exclude_major, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_list"]) -> typing.Union[MetaOapg.properties.company_list, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_list"]) -> typing.Union[MetaOapg.properties.exclude_company_list, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["geo"]) -> typing.Union[MetaOapg.properties.geo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_geo"]) -> typing.Union[MetaOapg.properties.exclude_geo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["previous_company_id"]) -> typing.Union[MetaOapg.properties.previous_company_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_previous_company_id"]) -> typing.Union[MetaOapg.properties.exclude_previous_company_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_state"]) -> typing.Union[MetaOapg.properties.exclude_state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["skills"]) -> typing.Union[MetaOapg.properties.skills, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_skills"]) -> typing.Union[MetaOapg.properties.exclude_skills, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_domain"]) -> typing.Union[MetaOapg.properties.company_domain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_domain"]) -> typing.Union[MetaOapg.properties.exclude_company_domain, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_region"]) -> typing.Union[MetaOapg.properties.company_region, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_region"]) -> typing.Union[MetaOapg.properties.exclude_company_region, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_website_category"]) -> typing.Union[MetaOapg.properties.company_website_category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_website_category"]) -> typing.Union[MetaOapg.properties.exclude_company_website_category, schemas.Unset]: ...
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["current_employer"]) -> typing.Union[MetaOapg.properties.current_employer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_current_employer"]) -> typing.Union[MetaOapg.properties.exclude_current_employer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_funding_min"]) -> typing.Union[MetaOapg.properties.company_funding_min, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_company_funding_min"]) -> typing.Union[MetaOapg.properties.exclude_company_funding_min, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employer"]) -> typing.Union[MetaOapg.properties.employer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_employer"]) -> typing.Union[MetaOapg.properties.exclude_employer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["website_category"]) -> typing.Union[MetaOapg.properties.website_category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_website_category"]) -> typing.Union[MetaOapg.properties.exclude_website_category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["school"]) -> typing.Union[MetaOapg.properties.school, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_school"]) -> typing.Union[MetaOapg.properties.exclude_school, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["keyword", "exclude_keyword", "company_naics_code", "exclude_company_naics_code", "name", "exclude_name", "company_postal_code", "exclude_company_postal_code", "city", "exclude_city", "previous_employer", "exclude_previous_employer", "handle", "exclude_handle", "industry_tags", "exclude_industry_tags", "company_revenue_max", "exclude_company_revenue_max", "sic_code", "exclude_sic_code", "company_industry", "exclude_company_industry", "postal_code", "exclude_postal_code", "company_size_min", "exclude_company_size_min", "management_levels", "exclude_management_levels", "company_list_id", "exclude_company_list_id", "phone", "exclude_phone", "company_revenue", "exclude_company_revenue", "company_funding_max", "exclude_company_funding_max", "company_website_url", "exclude_company_website_url", "keywords", "exclude_keywords", "insight", "exclude_insight", "veteran_status", "exclude_veteran_status", "company_website_rank_min", "exclude_company_website_rank_min", "simplified_keyword", "exclude_simplified_keyword", "link", "exclude_link", "company_id", "exclude_company_id", "company_name", "exclude_company_name", "company_industry_tags", "exclude_company_industry_tags", "techstack", "exclude_techstack", "is_primary", "exclude_is_primary", "birth_year", "exclude_birth_year", "keyword_orig", "exclude_keyword_orig", "growth", "exclude_growth", "email", "exclude_email", "ethnicity", "exclude_ethnicity", "company_website_rank_max", "exclude_company_website_rank_max", "extended_keyword", "exclude_extended_keyword", "employees", "exclude_employees", "company_publicly_traded", "exclude_company_publicly_traded", "sic_codes", "exclude_sic_codes", "location", "exclude_location", "company_email", "exclude_company_email", "naics_code", "exclude_naics_code", "degree", "exclude_degree", "years_experience", "exclude_years_experience", "country", "exclude_country", "company_size_max", "exclude_company_size_max", "current_title", "exclude_current_title", "department", "exclude_department", "all_industries", "exclude_all_industries", "keyword_enhanced", "exclude_keyword_enhanced", "company_city", "exclude_company_city", "company_revenue_min", "exclude_company_revenue_min", "total_funding", "exclude_total_funding", "company_website_rank", "exclude_company_website_rank", "description", "exclude_description", "job_change_range_days", "exclude_job_change_range_days", "primary_industry", "exclude_primary_industry", "website_url", "exclude_website_url", "company_country_code", "exclude_company_country_code", "domain", "exclude_domain", "email_domain", "exclude_email_domain", "gender", "exclude_gender", "company_sic_code", "exclude_company_sic_code", "naics_codes", "exclude_naics_codes", "company_size", "exclude_company_size", "normalized_title", "exclude_normalized_title", "connections", "exclude_connections", "major", "exclude_major", "company_list", "exclude_company_list", "geo", "exclude_geo", "previous_company_id", "exclude_previous_company_id", "state", "exclude_state", "skills", "exclude_skills", "company_domain", "exclude_company_domain", "company_region", "exclude_company_region", "company_website_category", "exclude_company_website_category", "industry", "exclude_industry", "publicly_traded", "exclude_publicly_traded", "revenue", "exclude_revenue", "id", "exclude_id", "current_employer", "exclude_current_employer", "company_funding_min", "exclude_company_funding_min", "employer", "exclude_employer", "website_category", "exclude_website_category", "school", "exclude_school", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        keyword: typing.Union[MetaOapg.properties.keyword, list, tuple, schemas.Unset] = schemas.unset,
        exclude_keyword: typing.Union[MetaOapg.properties.exclude_keyword, list, tuple, schemas.Unset] = schemas.unset,
        company_naics_code: typing.Union[MetaOapg.properties.company_naics_code, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_naics_code: typing.Union[MetaOapg.properties.exclude_company_naics_code, list, tuple, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, list, tuple, schemas.Unset] = schemas.unset,
        exclude_name: typing.Union[MetaOapg.properties.exclude_name, list, tuple, schemas.Unset] = schemas.unset,
        company_postal_code: typing.Union[MetaOapg.properties.company_postal_code, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_postal_code: typing.Union[MetaOapg.properties.exclude_company_postal_code, list, tuple, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, list, tuple, schemas.Unset] = schemas.unset,
        exclude_city: typing.Union[MetaOapg.properties.exclude_city, list, tuple, schemas.Unset] = schemas.unset,
        previous_employer: typing.Union[MetaOapg.properties.previous_employer, list, tuple, schemas.Unset] = schemas.unset,
        exclude_previous_employer: typing.Union[MetaOapg.properties.exclude_previous_employer, list, tuple, schemas.Unset] = schemas.unset,
        handle: typing.Union[MetaOapg.properties.handle, list, tuple, schemas.Unset] = schemas.unset,
        exclude_handle: typing.Union[MetaOapg.properties.exclude_handle, list, tuple, schemas.Unset] = schemas.unset,
        industry_tags: typing.Union[MetaOapg.properties.industry_tags, list, tuple, schemas.Unset] = schemas.unset,
        exclude_industry_tags: typing.Union[MetaOapg.properties.exclude_industry_tags, list, tuple, schemas.Unset] = schemas.unset,
        company_revenue_max: typing.Union[MetaOapg.properties.company_revenue_max, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_revenue_max: typing.Union[MetaOapg.properties.exclude_company_revenue_max, list, tuple, schemas.Unset] = schemas.unset,
        sic_code: typing.Union[MetaOapg.properties.sic_code, list, tuple, schemas.Unset] = schemas.unset,
        exclude_sic_code: typing.Union[MetaOapg.properties.exclude_sic_code, list, tuple, schemas.Unset] = schemas.unset,
        company_industry: typing.Union[MetaOapg.properties.company_industry, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_industry: typing.Union[MetaOapg.properties.exclude_company_industry, list, tuple, schemas.Unset] = schemas.unset,
        postal_code: typing.Union[MetaOapg.properties.postal_code, list, tuple, schemas.Unset] = schemas.unset,
        exclude_postal_code: typing.Union[MetaOapg.properties.exclude_postal_code, list, tuple, schemas.Unset] = schemas.unset,
        company_size_min: typing.Union[MetaOapg.properties.company_size_min, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_size_min: typing.Union[MetaOapg.properties.exclude_company_size_min, list, tuple, schemas.Unset] = schemas.unset,
        management_levels: typing.Union[MetaOapg.properties.management_levels, list, tuple, schemas.Unset] = schemas.unset,
        exclude_management_levels: typing.Union[MetaOapg.properties.exclude_management_levels, list, tuple, schemas.Unset] = schemas.unset,
        company_list_id: typing.Union[MetaOapg.properties.company_list_id, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_list_id: typing.Union[MetaOapg.properties.exclude_company_list_id, list, tuple, schemas.Unset] = schemas.unset,
        phone: typing.Union[MetaOapg.properties.phone, list, tuple, schemas.Unset] = schemas.unset,
        exclude_phone: typing.Union[MetaOapg.properties.exclude_phone, list, tuple, schemas.Unset] = schemas.unset,
        company_revenue: typing.Union[MetaOapg.properties.company_revenue, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_revenue: typing.Union[MetaOapg.properties.exclude_company_revenue, list, tuple, schemas.Unset] = schemas.unset,
        company_funding_max: typing.Union[MetaOapg.properties.company_funding_max, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_funding_max: typing.Union[MetaOapg.properties.exclude_company_funding_max, list, tuple, schemas.Unset] = schemas.unset,
        company_website_url: typing.Union[MetaOapg.properties.company_website_url, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_website_url: typing.Union[MetaOapg.properties.exclude_company_website_url, list, tuple, schemas.Unset] = schemas.unset,
        keywords: typing.Union[MetaOapg.properties.keywords, list, tuple, schemas.Unset] = schemas.unset,
        exclude_keywords: typing.Union[MetaOapg.properties.exclude_keywords, list, tuple, schemas.Unset] = schemas.unset,
        insight: typing.Union[MetaOapg.properties.insight, list, tuple, schemas.Unset] = schemas.unset,
        exclude_insight: typing.Union[MetaOapg.properties.exclude_insight, list, tuple, schemas.Unset] = schemas.unset,
        veteran_status: typing.Union[MetaOapg.properties.veteran_status, list, tuple, schemas.Unset] = schemas.unset,
        exclude_veteran_status: typing.Union[MetaOapg.properties.exclude_veteran_status, list, tuple, schemas.Unset] = schemas.unset,
        company_website_rank_min: typing.Union[MetaOapg.properties.company_website_rank_min, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_website_rank_min: typing.Union[MetaOapg.properties.exclude_company_website_rank_min, list, tuple, schemas.Unset] = schemas.unset,
        simplified_keyword: typing.Union[MetaOapg.properties.simplified_keyword, list, tuple, schemas.Unset] = schemas.unset,
        exclude_simplified_keyword: typing.Union[MetaOapg.properties.exclude_simplified_keyword, list, tuple, schemas.Unset] = schemas.unset,
        link: typing.Union[MetaOapg.properties.link, list, tuple, schemas.Unset] = schemas.unset,
        exclude_link: typing.Union[MetaOapg.properties.exclude_link, list, tuple, schemas.Unset] = schemas.unset,
        company_id: typing.Union[MetaOapg.properties.company_id, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_id: typing.Union[MetaOapg.properties.exclude_company_id, list, tuple, schemas.Unset] = schemas.unset,
        company_name: typing.Union[MetaOapg.properties.company_name, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_name: typing.Union[MetaOapg.properties.exclude_company_name, list, tuple, schemas.Unset] = schemas.unset,
        company_industry_tags: typing.Union[MetaOapg.properties.company_industry_tags, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_industry_tags: typing.Union[MetaOapg.properties.exclude_company_industry_tags, list, tuple, schemas.Unset] = schemas.unset,
        techstack: typing.Union[MetaOapg.properties.techstack, list, tuple, schemas.Unset] = schemas.unset,
        exclude_techstack: typing.Union[MetaOapg.properties.exclude_techstack, list, tuple, schemas.Unset] = schemas.unset,
        is_primary: typing.Union[MetaOapg.properties.is_primary, list, tuple, schemas.Unset] = schemas.unset,
        exclude_is_primary: typing.Union[MetaOapg.properties.exclude_is_primary, list, tuple, schemas.Unset] = schemas.unset,
        birth_year: typing.Union[MetaOapg.properties.birth_year, list, tuple, schemas.Unset] = schemas.unset,
        exclude_birth_year: typing.Union[MetaOapg.properties.exclude_birth_year, list, tuple, schemas.Unset] = schemas.unset,
        keyword_orig: typing.Union[MetaOapg.properties.keyword_orig, list, tuple, schemas.Unset] = schemas.unset,
        exclude_keyword_orig: typing.Union[MetaOapg.properties.exclude_keyword_orig, list, tuple, schemas.Unset] = schemas.unset,
        growth: typing.Union[MetaOapg.properties.growth, list, tuple, schemas.Unset] = schemas.unset,
        exclude_growth: typing.Union[MetaOapg.properties.exclude_growth, list, tuple, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, list, tuple, schemas.Unset] = schemas.unset,
        exclude_email: typing.Union[MetaOapg.properties.exclude_email, list, tuple, schemas.Unset] = schemas.unset,
        ethnicity: typing.Union[MetaOapg.properties.ethnicity, list, tuple, schemas.Unset] = schemas.unset,
        exclude_ethnicity: typing.Union[MetaOapg.properties.exclude_ethnicity, list, tuple, schemas.Unset] = schemas.unset,
        company_website_rank_max: typing.Union[MetaOapg.properties.company_website_rank_max, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_website_rank_max: typing.Union[MetaOapg.properties.exclude_company_website_rank_max, list, tuple, schemas.Unset] = schemas.unset,
        extended_keyword: typing.Union[MetaOapg.properties.extended_keyword, list, tuple, schemas.Unset] = schemas.unset,
        exclude_extended_keyword: typing.Union[MetaOapg.properties.exclude_extended_keyword, list, tuple, schemas.Unset] = schemas.unset,
        employees: typing.Union[MetaOapg.properties.employees, list, tuple, schemas.Unset] = schemas.unset,
        exclude_employees: typing.Union[MetaOapg.properties.exclude_employees, list, tuple, schemas.Unset] = schemas.unset,
        company_publicly_traded: typing.Union[MetaOapg.properties.company_publicly_traded, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_publicly_traded: typing.Union[MetaOapg.properties.exclude_company_publicly_traded, list, tuple, schemas.Unset] = schemas.unset,
        sic_codes: typing.Union[MetaOapg.properties.sic_codes, list, tuple, schemas.Unset] = schemas.unset,
        exclude_sic_codes: typing.Union[MetaOapg.properties.exclude_sic_codes, list, tuple, schemas.Unset] = schemas.unset,
        location: typing.Union[MetaOapg.properties.location, list, tuple, schemas.Unset] = schemas.unset,
        exclude_location: typing.Union[MetaOapg.properties.exclude_location, list, tuple, schemas.Unset] = schemas.unset,
        company_email: typing.Union[MetaOapg.properties.company_email, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_email: typing.Union[MetaOapg.properties.exclude_company_email, list, tuple, schemas.Unset] = schemas.unset,
        naics_code: typing.Union[MetaOapg.properties.naics_code, list, tuple, schemas.Unset] = schemas.unset,
        exclude_naics_code: typing.Union[MetaOapg.properties.exclude_naics_code, list, tuple, schemas.Unset] = schemas.unset,
        degree: typing.Union[MetaOapg.properties.degree, list, tuple, schemas.Unset] = schemas.unset,
        exclude_degree: typing.Union[MetaOapg.properties.exclude_degree, list, tuple, schemas.Unset] = schemas.unset,
        years_experience: typing.Union[MetaOapg.properties.years_experience, list, tuple, schemas.Unset] = schemas.unset,
        exclude_years_experience: typing.Union[MetaOapg.properties.exclude_years_experience, list, tuple, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, list, tuple, schemas.Unset] = schemas.unset,
        exclude_country: typing.Union[MetaOapg.properties.exclude_country, list, tuple, schemas.Unset] = schemas.unset,
        company_size_max: typing.Union[MetaOapg.properties.company_size_max, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_size_max: typing.Union[MetaOapg.properties.exclude_company_size_max, list, tuple, schemas.Unset] = schemas.unset,
        current_title: typing.Union[MetaOapg.properties.current_title, list, tuple, schemas.Unset] = schemas.unset,
        exclude_current_title: typing.Union[MetaOapg.properties.exclude_current_title, list, tuple, schemas.Unset] = schemas.unset,
        department: typing.Union[MetaOapg.properties.department, list, tuple, schemas.Unset] = schemas.unset,
        exclude_department: typing.Union[MetaOapg.properties.exclude_department, list, tuple, schemas.Unset] = schemas.unset,
        all_industries: typing.Union[MetaOapg.properties.all_industries, list, tuple, schemas.Unset] = schemas.unset,
        exclude_all_industries: typing.Union[MetaOapg.properties.exclude_all_industries, list, tuple, schemas.Unset] = schemas.unset,
        keyword_enhanced: typing.Union[MetaOapg.properties.keyword_enhanced, list, tuple, schemas.Unset] = schemas.unset,
        exclude_keyword_enhanced: typing.Union[MetaOapg.properties.exclude_keyword_enhanced, list, tuple, schemas.Unset] = schemas.unset,
        company_city: typing.Union[MetaOapg.properties.company_city, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_city: typing.Union[MetaOapg.properties.exclude_company_city, list, tuple, schemas.Unset] = schemas.unset,
        company_revenue_min: typing.Union[MetaOapg.properties.company_revenue_min, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_revenue_min: typing.Union[MetaOapg.properties.exclude_company_revenue_min, list, tuple, schemas.Unset] = schemas.unset,
        total_funding: typing.Union[MetaOapg.properties.total_funding, list, tuple, schemas.Unset] = schemas.unset,
        exclude_total_funding: typing.Union[MetaOapg.properties.exclude_total_funding, list, tuple, schemas.Unset] = schemas.unset,
        company_website_rank: typing.Union[MetaOapg.properties.company_website_rank, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_website_rank: typing.Union[MetaOapg.properties.exclude_company_website_rank, list, tuple, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, list, tuple, schemas.Unset] = schemas.unset,
        exclude_description: typing.Union[MetaOapg.properties.exclude_description, list, tuple, schemas.Unset] = schemas.unset,
        job_change_range_days: typing.Union[MetaOapg.properties.job_change_range_days, list, tuple, schemas.Unset] = schemas.unset,
        exclude_job_change_range_days: typing.Union[MetaOapg.properties.exclude_job_change_range_days, list, tuple, schemas.Unset] = schemas.unset,
        primary_industry: typing.Union[MetaOapg.properties.primary_industry, list, tuple, schemas.Unset] = schemas.unset,
        exclude_primary_industry: typing.Union[MetaOapg.properties.exclude_primary_industry, list, tuple, schemas.Unset] = schemas.unset,
        website_url: typing.Union[MetaOapg.properties.website_url, list, tuple, schemas.Unset] = schemas.unset,
        exclude_website_url: typing.Union[MetaOapg.properties.exclude_website_url, list, tuple, schemas.Unset] = schemas.unset,
        company_country_code: typing.Union[MetaOapg.properties.company_country_code, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_country_code: typing.Union[MetaOapg.properties.exclude_company_country_code, list, tuple, schemas.Unset] = schemas.unset,
        domain: typing.Union[MetaOapg.properties.domain, list, tuple, schemas.Unset] = schemas.unset,
        exclude_domain: typing.Union[MetaOapg.properties.exclude_domain, list, tuple, schemas.Unset] = schemas.unset,
        email_domain: typing.Union[MetaOapg.properties.email_domain, list, tuple, schemas.Unset] = schemas.unset,
        exclude_email_domain: typing.Union[MetaOapg.properties.exclude_email_domain, list, tuple, schemas.Unset] = schemas.unset,
        gender: typing.Union[MetaOapg.properties.gender, list, tuple, schemas.Unset] = schemas.unset,
        exclude_gender: typing.Union[MetaOapg.properties.exclude_gender, list, tuple, schemas.Unset] = schemas.unset,
        company_sic_code: typing.Union[MetaOapg.properties.company_sic_code, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_sic_code: typing.Union[MetaOapg.properties.exclude_company_sic_code, list, tuple, schemas.Unset] = schemas.unset,
        naics_codes: typing.Union[MetaOapg.properties.naics_codes, list, tuple, schemas.Unset] = schemas.unset,
        exclude_naics_codes: typing.Union[MetaOapg.properties.exclude_naics_codes, list, tuple, schemas.Unset] = schemas.unset,
        company_size: typing.Union[MetaOapg.properties.company_size, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_size: typing.Union[MetaOapg.properties.exclude_company_size, list, tuple, schemas.Unset] = schemas.unset,
        normalized_title: typing.Union[MetaOapg.properties.normalized_title, list, tuple, schemas.Unset] = schemas.unset,
        exclude_normalized_title: typing.Union[MetaOapg.properties.exclude_normalized_title, list, tuple, schemas.Unset] = schemas.unset,
        connections: typing.Union[MetaOapg.properties.connections, list, tuple, schemas.Unset] = schemas.unset,
        exclude_connections: typing.Union[MetaOapg.properties.exclude_connections, list, tuple, schemas.Unset] = schemas.unset,
        major: typing.Union[MetaOapg.properties.major, list, tuple, schemas.Unset] = schemas.unset,
        exclude_major: typing.Union[MetaOapg.properties.exclude_major, list, tuple, schemas.Unset] = schemas.unset,
        company_list: typing.Union[MetaOapg.properties.company_list, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_list: typing.Union[MetaOapg.properties.exclude_company_list, list, tuple, schemas.Unset] = schemas.unset,
        geo: typing.Union[MetaOapg.properties.geo, list, tuple, schemas.Unset] = schemas.unset,
        exclude_geo: typing.Union[MetaOapg.properties.exclude_geo, list, tuple, schemas.Unset] = schemas.unset,
        previous_company_id: typing.Union[MetaOapg.properties.previous_company_id, list, tuple, schemas.Unset] = schemas.unset,
        exclude_previous_company_id: typing.Union[MetaOapg.properties.exclude_previous_company_id, list, tuple, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, list, tuple, schemas.Unset] = schemas.unset,
        exclude_state: typing.Union[MetaOapg.properties.exclude_state, list, tuple, schemas.Unset] = schemas.unset,
        skills: typing.Union[MetaOapg.properties.skills, list, tuple, schemas.Unset] = schemas.unset,
        exclude_skills: typing.Union[MetaOapg.properties.exclude_skills, list, tuple, schemas.Unset] = schemas.unset,
        company_domain: typing.Union[MetaOapg.properties.company_domain, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_domain: typing.Union[MetaOapg.properties.exclude_company_domain, list, tuple, schemas.Unset] = schemas.unset,
        company_region: typing.Union[MetaOapg.properties.company_region, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_region: typing.Union[MetaOapg.properties.exclude_company_region, list, tuple, schemas.Unset] = schemas.unset,
        company_website_category: typing.Union[MetaOapg.properties.company_website_category, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_website_category: typing.Union[MetaOapg.properties.exclude_company_website_category, list, tuple, schemas.Unset] = schemas.unset,
        industry: typing.Union[MetaOapg.properties.industry, list, tuple, schemas.Unset] = schemas.unset,
        exclude_industry: typing.Union[MetaOapg.properties.exclude_industry, list, tuple, schemas.Unset] = schemas.unset,
        publicly_traded: typing.Union[MetaOapg.properties.publicly_traded, list, tuple, schemas.Unset] = schemas.unset,
        exclude_publicly_traded: typing.Union[MetaOapg.properties.exclude_publicly_traded, list, tuple, schemas.Unset] = schemas.unset,
        revenue: typing.Union[MetaOapg.properties.revenue, list, tuple, schemas.Unset] = schemas.unset,
        exclude_revenue: typing.Union[MetaOapg.properties.exclude_revenue, list, tuple, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, list, tuple, schemas.Unset] = schemas.unset,
        exclude_id: typing.Union[MetaOapg.properties.exclude_id, list, tuple, schemas.Unset] = schemas.unset,
        current_employer: typing.Union[MetaOapg.properties.current_employer, list, tuple, schemas.Unset] = schemas.unset,
        exclude_current_employer: typing.Union[MetaOapg.properties.exclude_current_employer, list, tuple, schemas.Unset] = schemas.unset,
        company_funding_min: typing.Union[MetaOapg.properties.company_funding_min, list, tuple, schemas.Unset] = schemas.unset,
        exclude_company_funding_min: typing.Union[MetaOapg.properties.exclude_company_funding_min, list, tuple, schemas.Unset] = schemas.unset,
        employer: typing.Union[MetaOapg.properties.employer, list, tuple, schemas.Unset] = schemas.unset,
        exclude_employer: typing.Union[MetaOapg.properties.exclude_employer, list, tuple, schemas.Unset] = schemas.unset,
        website_category: typing.Union[MetaOapg.properties.website_category, list, tuple, schemas.Unset] = schemas.unset,
        exclude_website_category: typing.Union[MetaOapg.properties.exclude_website_category, list, tuple, schemas.Unset] = schemas.unset,
        school: typing.Union[MetaOapg.properties.school, list, tuple, schemas.Unset] = schemas.unset,
        exclude_school: typing.Union[MetaOapg.properties.exclude_school, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PersonQuery':
        return super().__new__(
            cls,
            *_args,
            keyword=keyword,
            exclude_keyword=exclude_keyword,
            company_naics_code=company_naics_code,
            exclude_company_naics_code=exclude_company_naics_code,
            name=name,
            exclude_name=exclude_name,
            company_postal_code=company_postal_code,
            exclude_company_postal_code=exclude_company_postal_code,
            city=city,
            exclude_city=exclude_city,
            previous_employer=previous_employer,
            exclude_previous_employer=exclude_previous_employer,
            handle=handle,
            exclude_handle=exclude_handle,
            industry_tags=industry_tags,
            exclude_industry_tags=exclude_industry_tags,
            company_revenue_max=company_revenue_max,
            exclude_company_revenue_max=exclude_company_revenue_max,
            sic_code=sic_code,
            exclude_sic_code=exclude_sic_code,
            company_industry=company_industry,
            exclude_company_industry=exclude_company_industry,
            postal_code=postal_code,
            exclude_postal_code=exclude_postal_code,
            company_size_min=company_size_min,
            exclude_company_size_min=exclude_company_size_min,
            management_levels=management_levels,
            exclude_management_levels=exclude_management_levels,
            company_list_id=company_list_id,
            exclude_company_list_id=exclude_company_list_id,
            phone=phone,
            exclude_phone=exclude_phone,
            company_revenue=company_revenue,
            exclude_company_revenue=exclude_company_revenue,
            company_funding_max=company_funding_max,
            exclude_company_funding_max=exclude_company_funding_max,
            company_website_url=company_website_url,
            exclude_company_website_url=exclude_company_website_url,
            keywords=keywords,
            exclude_keywords=exclude_keywords,
            insight=insight,
            exclude_insight=exclude_insight,
            veteran_status=veteran_status,
            exclude_veteran_status=exclude_veteran_status,
            company_website_rank_min=company_website_rank_min,
            exclude_company_website_rank_min=exclude_company_website_rank_min,
            simplified_keyword=simplified_keyword,
            exclude_simplified_keyword=exclude_simplified_keyword,
            link=link,
            exclude_link=exclude_link,
            company_id=company_id,
            exclude_company_id=exclude_company_id,
            company_name=company_name,
            exclude_company_name=exclude_company_name,
            company_industry_tags=company_industry_tags,
            exclude_company_industry_tags=exclude_company_industry_tags,
            techstack=techstack,
            exclude_techstack=exclude_techstack,
            is_primary=is_primary,
            exclude_is_primary=exclude_is_primary,
            birth_year=birth_year,
            exclude_birth_year=exclude_birth_year,
            keyword_orig=keyword_orig,
            exclude_keyword_orig=exclude_keyword_orig,
            growth=growth,
            exclude_growth=exclude_growth,
            email=email,
            exclude_email=exclude_email,
            ethnicity=ethnicity,
            exclude_ethnicity=exclude_ethnicity,
            company_website_rank_max=company_website_rank_max,
            exclude_company_website_rank_max=exclude_company_website_rank_max,
            extended_keyword=extended_keyword,
            exclude_extended_keyword=exclude_extended_keyword,
            employees=employees,
            exclude_employees=exclude_employees,
            company_publicly_traded=company_publicly_traded,
            exclude_company_publicly_traded=exclude_company_publicly_traded,
            sic_codes=sic_codes,
            exclude_sic_codes=exclude_sic_codes,
            location=location,
            exclude_location=exclude_location,
            company_email=company_email,
            exclude_company_email=exclude_company_email,
            naics_code=naics_code,
            exclude_naics_code=exclude_naics_code,
            degree=degree,
            exclude_degree=exclude_degree,
            years_experience=years_experience,
            exclude_years_experience=exclude_years_experience,
            country=country,
            exclude_country=exclude_country,
            company_size_max=company_size_max,
            exclude_company_size_max=exclude_company_size_max,
            current_title=current_title,
            exclude_current_title=exclude_current_title,
            department=department,
            exclude_department=exclude_department,
            all_industries=all_industries,
            exclude_all_industries=exclude_all_industries,
            keyword_enhanced=keyword_enhanced,
            exclude_keyword_enhanced=exclude_keyword_enhanced,
            company_city=company_city,
            exclude_company_city=exclude_company_city,
            company_revenue_min=company_revenue_min,
            exclude_company_revenue_min=exclude_company_revenue_min,
            total_funding=total_funding,
            exclude_total_funding=exclude_total_funding,
            company_website_rank=company_website_rank,
            exclude_company_website_rank=exclude_company_website_rank,
            description=description,
            exclude_description=exclude_description,
            job_change_range_days=job_change_range_days,
            exclude_job_change_range_days=exclude_job_change_range_days,
            primary_industry=primary_industry,
            exclude_primary_industry=exclude_primary_industry,
            website_url=website_url,
            exclude_website_url=exclude_website_url,
            company_country_code=company_country_code,
            exclude_company_country_code=exclude_company_country_code,
            domain=domain,
            exclude_domain=exclude_domain,
            email_domain=email_domain,
            exclude_email_domain=exclude_email_domain,
            gender=gender,
            exclude_gender=exclude_gender,
            company_sic_code=company_sic_code,
            exclude_company_sic_code=exclude_company_sic_code,
            naics_codes=naics_codes,
            exclude_naics_codes=exclude_naics_codes,
            company_size=company_size,
            exclude_company_size=exclude_company_size,
            normalized_title=normalized_title,
            exclude_normalized_title=exclude_normalized_title,
            connections=connections,
            exclude_connections=exclude_connections,
            major=major,
            exclude_major=exclude_major,
            company_list=company_list,
            exclude_company_list=exclude_company_list,
            geo=geo,
            exclude_geo=exclude_geo,
            previous_company_id=previous_company_id,
            exclude_previous_company_id=exclude_previous_company_id,
            state=state,
            exclude_state=exclude_state,
            skills=skills,
            exclude_skills=exclude_skills,
            company_domain=company_domain,
            exclude_company_domain=exclude_company_domain,
            company_region=company_region,
            exclude_company_region=exclude_company_region,
            company_website_category=company_website_category,
            exclude_company_website_category=exclude_company_website_category,
            industry=industry,
            exclude_industry=exclude_industry,
            publicly_traded=publicly_traded,
            exclude_publicly_traded=exclude_publicly_traded,
            revenue=revenue,
            exclude_revenue=exclude_revenue,
            id=id,
            exclude_id=exclude_id,
            current_employer=current_employer,
            exclude_current_employer=exclude_current_employer,
            company_funding_min=company_funding_min,
            exclude_company_funding_min=exclude_company_funding_min,
            employer=employer,
            exclude_employer=exclude_employer,
            website_category=website_category,
            exclude_website_category=exclude_website_category,
            school=school,
            exclude_school=exclude_school,
            _configuration=_configuration,
            **kwargs,
        )
