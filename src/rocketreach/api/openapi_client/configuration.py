# coding: utf-8

"""
    RocketReach API

    # Getting Started The RocketReach API allows you to programmatically search & lookup contact info for over 700 million professionals, and 35 million companies. We constantly work on improving functionality and accuracy of our data. RocketReach is free to try for individual use.  You can always visit the [account page](/account?section=nav_gen_api) to view API usage, manage RocketReach API settings, and view your unique API key. All calls to the RocketReach API are authenticated with an API key.  ## Need Help? Have feedback, questions about usage, or pricing? Talk to us live or Email us at sales@rocketreach.co.  ## Troubleshooting  ### Handling Errors Normal responses are returned with HTTP status `HTTP: 200`. Error responses return `HTTP: 4xx/5xx` error codes. For example, if the profile being searched for cannot be found, we will return a `404`.  ### Rate Limits If we start receiving unusually heavy call volumes on your API key, you may receive responses with `HTTP: 429 \"Too Many Requests\"`. In general, do not make more than 5 calls per second using your API key.  Throttled API responses will contain a `Retry-After` header that contains the number of seconds to wait until the endpoint becomes available again. To ensure your client accesses the API fairly, it should parse this value and waits the appropriate amount of time.   Repeated instances of unexpected throttled requests should be addressed one of the following ways: 1. If you are not on a paid plan, you will generally need to upgrade to a paid API plan. Please email sales@rocketreach.co to setup an API plan. 2. If you are already on a paid API plan, please slow down and retry your requests. Contact sales@rocketreach.co or our live support if you continue to have problems.  You can visit the [account page](/account?section=api_section_gen_api) to review your RocketReach API limits and daily usage.  ## Webhooks We offer a webhook solution for person lookups so clients do not need to poll the check status endpoint until their results are available.  ### Set Up To set up a webhook, go to your [API settings](/account?section=nav_gen_api). Enter your server's callback URL into the field, and hit \"Create\".  ### Configuration Options For each URL created, you can perform some basic maintenance tasks:  - Test the webhook - we will attempt to send a basic JSON payload to the URL. - Disable/enable - if you may use this URL in the future, this is an option to temporarily disable it. - Delete - if you no longer plan using this URL, it can be deleted.  ### Usage Currently, only profile lookup and bulk lookup have webhook functionality, but we anticipate supporting more in the future! Once you call a webhook-enabled endpoint with a webhook set up in your settings, we will send back results to the provided URL. The results returned to you should look the same as if they were queried through the REST API. In addition, the API will still respond to your REST call as normal.  ### Errors If any errors occur, they will show up in the [API settings](/account?section=nav_gen_api) page in the \"Web Hook\" section. If the callback to the provided URL is unsuccessful after several attempts, the URL will be automatically disabled and will need to manually be re-enabled.  ## FAQ  **How Do I Know if RocketReach Has Data For a Profile?** - 87% of lookups return profiles  - \"teaser\" in search returns some indication of data; however, the final lookup may discover results even if the teaser is empty - if no data is found, credits are not deducted  **Do I Get Charged a Credit if No Data is Returned?** - for lookups, no - searches are metered, but usually the first ~10,000/day are free on paid API plans  **Why doesn't the data in a Profile match data from the API?** - this should almost never happen, please contact support - on the other hand, search results and sorting may be different depending on how the search is executed - the UI uses NLP for search facets  **Why don't the search results in the UI match data returned from the API?** - search results and sorting may be different depending on how the search is executed - this also uses NLP for search facets - try changing the facet and adjusting the `order_by` param  **Why does the teaser only contain phone numbers, and no emails?** - teaser information is only populated if data is cached  **Why am I getting rate limited?** - rate limits depend on product, contact us to get on an API plan - See our troubleshooting guide for more info.   ## SDKs  ### Python SDK The [Python SDK](https://www.github.com/rocketreach/rocketreach_python) allows you to find anyone's emails, social media and complete contact data, using only a few lines of code.  ### Installation The rocketreach python package can be installed from pip or from source into your project's virtual environment.  Install with pip:  ```bash pip install rocketreach ```  Install from source:  ```bash # The requests v2.2 or higher is a required dependency wget https://pypi.python.org/packages/source/r/requests/requests-2.2.1.tar.gz tar xzvf requests-2.2.1.tar.gz cd requests-2.2.1 python setup.py install  # Install the rocketreach SDK wget https://files.pythonhosted.org/packages/20/9d/5ba988d0b2f94a19fb8f86ae87ef1a2eb79b3fd7da7cce00998b7051d57f/rocketreach-2.1.0.tar.gz tar xzvf rocketreach-2.1.0.tar.gz cd rocketreach-2.1.0 python setup.py install ```  ### Usage  Initialization is the first step to use the SDK. You will need your API key for this step.  ```python import rocketreach import os rr = rocketreach.Gateway(api_key=os.environ.get('API_KEY'))  # Check that the SDK is working result = rr.account.get() if result.is_success:     print(f'Success: {result.account}') else:     print(f'Error: {result.message}!') ```  You can call any of our methods once the Gateway class is constructed. In this next example we will call lookup() using a name and current employer. Then, we'll do the same lookup using a LinkedIn URL.  ```python lookup_result = rr.person.lookup(name='Marc Benioff', current_employer='Salesforce') if lookup_result.is_success:     print(lookup_result.person) lookup_result = rr.person.lookup(linkedin_url='https://www.linkedin.com/in/marcbenioff') if lookup_result.is_success:     print(lookup_result.person) ```  By default, the lookup method blocks until /checkStatus returns complete. The caller can override this behavior and call lookup in a non-blocking context.  ```python import time # Lookup 2 profiles, non-blocking and checkStatus ourself. lookup1 = rr.person.lookup(linkedin_url='https://www.linkedin.com/in/marcbenioff', block=False) lookup2 = rr.person.lookup(linkedin_url='https://www.linkedin.com/in/reidhoffman', block=False) # Check if the lookups are complete. while True:     lookup_ids = [lookup1.person.id, lookup2.person.id]     cs_result = rr.person.check_status(lookup_ids)     num_complete = 0     for p in cs_result.people:         if p.status == 'complete':             num_complete += 1     if num_complete == len(lookups):         break     time.sleep(10)  # Wait a few seconds before checking status again # All the lookups are 'complete'. ```  `check_status()` can take either a single argument, or an array containing multiple IDs to lookup. Regardless of the number of arguments, the return value will always contain a person collection as an array (with 1 or more elements).  ```python result = rr.person.check_status(5244) assert(len(result.people) == 1) result = rr.person.check_status([5244, 5234]) assert(len(result.people) == 2) ```  ### Reference Calls are wrapped in a Result object. If the call was successful the Result object will encapsulate the return value.  Result object attributes  Name Description Type request Request object sent to the server. requests.Request response Response object received from the server. requests.Response is_success Indicates if the call succeeded. bool data (optional) Any data retrieved from the server response. dict error (optional) Any error data retrieved from the server response. Returned if is_success is False dict message (optional) A human readable message that explains what went wrong. str  | Name      | Description | Type | |-----------| ----------- | -----| | request    | Request object sent to the server. | `requests.Request` | | response | Response object received from the server. | `requests.Response` | | is_success | Indicates if the call succeeded. | `bool` | | data | Any data retrieved from the server response. | `dict` (optional) | | error | Any error data retrieved from the server response. Returned if `is_success = False` | `dict` (optional) |        | | message | A human readable message that explains what went wrong. | `str` (optional) |  ### Pagination  Searches will only return 10 results at a time, but the API provides a pagination method that can be accessed through the Python SDK.  ```python search = rr.person.search() # Add filters to your search start = 1 size = 10 result = search.execute() people = [] while result.is_success and result.people:     start += size     people.extend(result.people)     search = search.params(start=start, size=size)     result = search.execute() ```  The Python SDK provides iterators to handle paginating through results for you. These convenience iterators are accessed through the .iterator() method.  ```python search = rr.person.search() # Add filters to your search for person in search.iterator():     print(person) ```  The search object also supports indexing and slicing to limit the range of results. ```python search = rr.person.search() # Add filters to your search list(search[:100])  # Retrieve the first 100 results list(search[10:20])  # Retrieve results 11 - 19 person = search[0]  # Retrieve only the first result ```  Note: - Indexing causes the search to be immediately executed with the desired result returned. - Search object slices cannot contain steps.  ## Examples  ### Lookup by Name If you are calling the RocketReach API endpoints directly, you will essentially need to use 2 calls. First call `person/lookup` with 2 parameters: `name` and `current_employer`.  ```bash curl -G -L 'http://api.rocketreach.co/api/v2/person/lookup'\\      --header 'Api-Key: <INSERT API KEY>'\\      --data-urlencode 'name=Marc Benioff'\\      --data-urlencode 'current_employer=Salesforce' ```  If the status returned by the call is not `complete` or `failed`, then you will need to poll `person/checkStatus` untill it returns either `complete` or `failed`. If the status is `complete`, then the response will also contain contact info data.  ```bash curl --request 'GET' --location 'https://api.rocketreach.co/api/v2/person/checkStatus'\\      --header 'Api-Key: <INSERT API KEY>'\\      --data-urlencode 'ids=5262' ```  **Putting it all together** The following example demonstrates a fully functional application, using the RocketReach API. Here, we lookup contact info of a person, by name and current_employer.  The source code shown below uses the RocketReach Python SDK. We start by calling initializing the client. This checks to make sure that the `api_key` is valid, and that the user has sufficient credits to perform lookups. Under the covers, the SDK is simply calling the `/account` endpoint. If everything looks good, we now call `person/lookup` to lookup contact info. The library also polls `person/checkStatus` for you, when necessary.  ```python import rocketreach import os rr = rocketreach.Gateway(api_key=os.environ.get('API_KEY')) lookup = rr.person.lookup(extras={'name': 'Marc Benioff', 'current_employer': 'Salesforce'}) if lookup.is_success:     print(repr(lookup.person)) ```  Output ```python     {'current_employer': 'Salesforce',      'current_personal_email': 'benioff@gmail.com',      'current_title': 'Chairman and Co-CEO',      'current_work_email': 'marcb@salesforce.com',      'emails': [{'email': 'm.benioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'mbenioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'benioff@comcast.net',                  'smtp_valid': 'valid',                  'type': 'personal'},                 {'email': 'marc@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marc_benioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'benioff@gmail.com',                  'smtp_valid': 'valid',                  'type': 'personal'},                 {'email': 'benioff@aol.com',                  'smtp_valid': 'valid',                  'type': 'personal'},                 {'email': 'ceo@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marcb@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marc.benioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marcbenioff@salesforce.com',                  'smtp_valid': 'invalid',                  'type': 'professional'},                 {'email': 'benioff@frontiernet.net',                  'smtp_valid': 'invalid',                  'type': 'personal'},                 {'email': 'cooldwj@chinaren.com',                  'smtp_valid': 'invalid',                  'type': 'professional'},                 {'email': 'benioff@rcn.com',                  'smtp_valid': 'invalid',                  'type': 'professional'}],      'id': 5244,      'linkedin_url': 'https://www.linkedin.com/in/marcbenioff',      'links': {'aboutme': 'http://www.about.me/marcbenioff',                'amazon': 'http://www.amazon.com/gp/pdp/profile/AZGYQG724J6ON//190-5748375-2756131',                'angel': 'https://angel.co/benioff',                'angellist': 'http://www.angel.co/benioff',                'crunchbase': 'https://www.crunchbase.com/person/marc-benioff',                'facebook': 'http://www.facebook.com/benioff',                'google': 'https://plus.google.com/109586918294369333764',                'google+': 'https://plus.google.com/108172009599607363531/about',                'googleplus': 'https://plus.google.com/108172009599607363531',                'gravatar': 'http://www.gravatar.com/crmmaster',                'gravatar.com': 'http://gravatar.com/crmmaster',                'hi5': 'http://www.hi5.com/friend/p45336146--profile--html',                'instagram': 'http://www.instagram.com/benioff',                'klout': 'http://www.klout.com/benioff',                'linkedin': 'https://www.linkedin.com/in/marcbenioff',                'meetup': 'http://www.meetup.com/members/15867891',                'pinterest': 'http://www.pinterest.com/benioff',                'quora': 'http://www.quora.com/marc-benioff',                'salesforce.com': 'http://www.salesforce.com/company/leadership/executive-team/index.jsp#benioff',                'twicsy': 'http://twicsy.com/u/%40Benioff',                'twitter': 'http://www.twitter.com/benioff'},      'location': 'San Francisco, California, United States',      'name': 'Marc Benioff',      'phones': [],      'profile_pic': 'https://d1hbpr09pwz0sk.cloudfront.net/profile_pic/marc-benioff-4492e698',      'status': 'complete'}  ```  ### Lookup by LinkedIn URL  This is very similar to the previous example, but calls `person/lookup` with the `li_url` parameter.  ```bash  curl -G --location 'https://api.rocketreach.co/v2/api/person/lookup'\\      --header 'Api-Key: <INSERT API KEY>'\\      --data-urlencode 'li_url=https://www.linkedin.com/in/marcbenioff/' ```  **Putting it all together** The following example demonstrates a fully functional application, using the RocketReach API. Here, we lookup contact info of a person, by `name` and `current_employer`.  The source code shown below uses the RocketReach Python SDK. We start by calling initializing the client. This checks to make sure that the `api_key` is valid, and that the user has sufficient credits to perform lookups. Under the covers, the SDK is simply calling the `/account` endpoint. If everything looks good, we now call `person/lookup` to lookup contact info. The library also polls `person/checkStatus` for you, when necessary.  Code:  ```python import rocketreach import os rr = rocketreach.Gateway(api_key=os.environ.get('API_KEY')) lookup = rr.person.lookup(linkedin_url='https://www.linkedin.com/in/marcbenioff') if lookup.is_success:     print(repr(lookup.person)) ```  Output:  ```python      {'current_employer': 'Salesforce',      'current_personal_email': 'benioff@gmail.com',      'current_title': 'Chairman and Co-CEO',      'current_work_email': 'marcb@salesforce.com',      'emails': [{'email': 'm.benioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'mbenioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'benioff@comcast.net',                  'smtp_valid': 'valid',                  'type': 'personal'},                 {'email': 'marc@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marc_benioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'benioff@gmail.com',                  'smtp_valid': 'valid',                  'type': 'personal'},                 {'email': 'benioff@aol.com',                  'smtp_valid': 'valid',                  'type': 'personal'},                 {'email': 'ceo@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marcb@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marc.benioff@salesforce.com',                  'smtp_valid': 'valid',                  'type': 'professional'},                 {'email': 'marcbenioff@salesforce.com',                  'smtp_valid': 'invalid',                  'type': 'professional'},                 {'email': 'benioff@frontiernet.net',                  'smtp_valid': 'invalid',                  'type': 'personal'},                 {'email': 'cooldwj@chinaren.com',                  'smtp_valid': 'invalid',                  'type': 'professional'},                 {'email': 'benioff@rcn.com',                  'smtp_valid': 'invalid',                  'type': 'professional'}],      'id': 5244,      'linkedin_url': 'https://www.linkedin.com/in/marcbenioff',      'links': {'aboutme': 'http://www.about.me/marcbenioff',                'amazon': 'http://www.amazon.com/gp/pdp/profile/AZGYQG724J6ON//190-5748375-2756131',                'angel': 'https://angel.co/benioff',                'angellist': 'http://www.angel.co/benioff',                 'crunchbase': 'https://www.crunchbase.com/person/marc-benioff',                'facebook': 'http://www.facebook.com/benioff',                'google': 'https://plus.google.com/109586918294369333764',                'google+': 'https://plus.google.com/108172009599607363531/about',                'googleplus': 'https://plus.google.com/108172009599607363531',                'gravatar': 'http://www.gravatar.com/crmmaster',                'gravatar.com': 'http://gravatar.com/crmmaster',                'hi5': 'http://www.hi5.com/friend/p45336146--profile--html',                'instagram': 'http://www.instagram.com/benioff',                'klout': 'http://www.klout.com/benioff',                'linkedin': 'https://www.linkedin.com/in/marcbenioff',                'meetup': 'http://www.meetup.com/members/15867891',                'pinterest': 'http://www.pinterest.com/benioff',                'quora': 'http://www.quora.com/marc-benioff',                'salesforce.com': 'http://www.salesforce.com/company/leadership/executive-team/index.jsp#benioff',                'twicsy': 'http://twicsy.com/u/%40Benioff',                'twitter': 'http://www.twitter.com/benioff'},      'location': 'San Francisco, California, United States',      'name': 'Marc Benioff',      'phones': [],      'profile_pic': 'https://d1hbpr09pwz0sk.cloudfront.net/profile_pic/marc-benioff-4492e698',      'status': 'complete'} ```   ### Search People by Role at Company  If you are calling the RocketReach API endpoints directly, you will essentially need to use 3 calls. First call the `person/search` endpoint.  ```bash curl --request 'POST' --location 'https://api.rocketreach.co/api/v2/search'\\      --header 'Api-Key: <INSERT API KEY>'\\      --header 'Content-Type: application/json'\\      --data '{\"query\":{\"name\":[\"Marc Benioff\"],\"current_employer\":[\"Salesforce\"],\"current_title\":[\"CEO\"]}}' ```  Assuming that the `id` for Marc's profile is `5262`, you then call `person/lookup`.  ```bash curl --request 'GET' --location 'https://api.rocketreach.co/api/v2/lookupProfile'\\      --header 'Api-Key: <INSERT API KEY>'\\      --data-urlencode 'id=5262' ```  If the status returned by the call is not `complete` or `failed`, then you will need to poll `person/checkStatus` untill it returns either `complete` or `failed`.  ```bash curl --request 'GET' --location 'https://api.rocketreach.co/api/v2/checkStatus'\\      --header 'Api-Key: <INSERT API KEY>'\\      --data-urlencode 'ids=5262' ```  **Putting it all together** In this example, we will search for people with a specific name and title, at a company. We will then lookup contact info for one of the search results.  Code: ```python     import rocketreach     import os     rr = rocketreach.Gateway(api_key=os.environ.get('API_KEY'))     search = rr.person.search()     # Build up our search query     search = search.filter(name='Marc Benioff', current_title='CEO', current_employer='Salesforce')     # Call the search endpoint with our query     result = search.execute()     if result.is_success:         lookup = rr.person.lookup(result.people[0].id)         if lookup.is_success:             print(repr(lookup.person)) ```  Output: ```python {     'current_employer': 'Salesforce',     'current_personal_email': 'benioff@gmail.com',     'current_title': 'Chairman and Co-CEO',     'current_work_email': 'marcb@salesforce.com',     'emails': [{'email': 'm.benioff@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'mbenioff@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'benioff@comcast.net',              'smtp_valid': 'valid',              'type': 'personal'},             {'email': 'marc@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'marc_benioff@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'benioff@gmail.com',              'smtp_valid': 'valid',              'type': 'personal'},             {'email': 'benioff@aol.com',              'smtp_valid': 'valid',              'type': 'personal'},             {'email': 'ceo@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'marcb@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'marc.benioff@salesforce.com',              'smtp_valid': 'valid',              'type': 'professional'},             {'email': 'marcbenioff@salesforce.com',              'smtp_valid': 'invalid',              'type': 'professional'},             {'email': 'benioff@frontiernet.net',              'smtp_valid': 'invalid',              'type': 'personal'},             {'email': 'cooldwj@chinaren.com',              'smtp_valid': 'invalid',              'type': 'professional'},             {'email': 'benioff@rcn.com',              'smtp_valid': 'invalid',              'type': 'professional'}],     'id': 5244,     'linkedin_url': 'https://www.linkedin.com/in/marcbenioff',     'links': {'aboutme': 'http://www.about.me/marcbenioff',            'amazon': 'http://www.amazon.com/gp/pdp/profile/AZGYQG724J6ON//190-5748375-2756131',            'angel': 'https://angel.co/benioff',            'angellist': 'http://www.angel.co/benioff',            'crunchbase': 'https://www.crunchbase.com/person/marc-benioff',            'facebook': 'http://www.facebook.com/benioff',            'google': 'https://plus.google.com/109586918294369333764',            'google+': 'https://plus.google.com/108172009599607363531/about',            'googleplus': 'https://plus.google.com/108172009599607363531',            'gravatar': 'http://www.gravatar.com/crmmaster',            'gravatar.com': 'http://gravatar.com/crmmaster',            'hi5': 'http://www.hi5.com/friend/p45336146--profile--html',            'instagram': 'http://www.instagram.com/benioff',            'klout': 'http://www.klout.com/benioff',            'linkedin': 'https://www.linkedin.com/in/marcbenioff',            'meetup': 'http://www.meetup.com/members/15867891',            'pinterest': 'http://www.pinterest.com/benioff',            'quora': 'http://www.quora.com/marc-benioff',            'salesforce.com': 'http://www.salesforce.com/company/leadership/executive-team/index.jsp#benioff',            'twicsy': 'http://twicsy.com/u/%40Benioff',            'twitter': 'http://www.twitter.com/benioff'},     'location': 'San Francisco, California, United States',     'name': 'Marc Benioff',     'phones': [],     'profile_pic': 'https://d1hbpr09pwz0sk.cloudfront.net/profile_pic/marc-benioff-4492e698',     'status': 'complete' }  ```  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@rocketreach.co
    Generated by: https://openapi-generator.tech
"""

import copy
import logging
import multiprocessing
import sys
import urllib3

from http import client as http_client
from openapi_client.exceptions import ApiValueError


JSON_SCHEMA_VALIDATION_KEYWORDS = {
    'multipleOf', 'maximum', 'exclusiveMaximum',
    'minimum', 'exclusiveMinimum', 'maxLength',
    'minLength', 'pattern', 'maxItems', 'minItems',
    'uniqueItems', 'maxProperties', 'minProperties',
}

class Configuration(object):
    """NOTE: This class is auto generated by OpenAPI Generator

    Ref: https://openapi-generator.tech
    Do not edit the class manually.

    :param host: Base url
    :param api_key: Dict to store API key(s).
      Each entry in the dict specifies an API key.
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is the API key secret.
    :param api_key_prefix: Dict to store API prefix (e.g. Bearer)
      The dict key is the name of the security scheme in the OAS specification.
      The dict value is an API key prefix when generating the auth data.
    :param username: Username for HTTP basic authentication
    :param password: Password for HTTP basic authentication
    :param discard_unknown_keys: Boolean value indicating whether to discard
      unknown properties. A server may send a response that includes additional
      properties that are not known by the client in the following scenarios:
      1. The OpenAPI document is incomplete, i.e. it does not match the server
         implementation.
      2. The client was generated using an older version of the OpenAPI document
         and the server has been upgraded since then.
      If a schema in the OpenAPI document defines the additionalProperties attribute,
      then all undeclared properties received by the server are injected into the
      additional properties map. In that case, there are undeclared properties, and
      nothing to discard.
    :param disabled_client_side_validations (string): Comma-separated list of
      JSON schema validation keywords to disable JSON schema structural validation
      rules. The following keywords may be specified: multipleOf, maximum,
      exclusiveMaximum, minimum, exclusiveMinimum, maxLength, minLength, pattern,
      maxItems, minItems.
      By default, the validation is performed for data generated locally by the client
      and data received from the server, independent of any validation performed by
      the server side. If the input data does not satisfy the JSON schema validation
      rules specified in the OpenAPI document, an exception is raised.
      If disabled_client_side_validations is set, structural validation is
      disabled. This can be useful to troubleshoot data validation problem, such as
      when the OpenAPI document validation rules do not match the actual API data
      received by the server.
    :param server_index: Index to servers configuration.
    :param server_variables: Mapping with string values to replace variables in
      templated server configuration. The validation of enums is performed for
      variables with defined enum values before.
    :param server_operation_index: Mapping from operation ID to an index to server
      configuration.
    :param server_operation_variables: Mapping from operation ID to a mapping with
      string values to replace variables in templated server configuration.
      The validation of enums is performed for variables with defined enum values before.

    :Example:

    API Key Authentication Example.
    Given the following security scheme in the OpenAPI specification:
      components:
        securitySchemes:
          cookieAuth:         # name for the security scheme
            type: apiKey
            in: cookie
            name: JSESSIONID  # cookie name

    You can programmatically set the cookie:

conf = openapi_client.Configuration(
    api_key={'cookieAuth': 'abc123'}
    api_key_prefix={'cookieAuth': 'JSESSIONID'}
)

    The following cookie will be added to the HTTP request:
       Cookie: JSESSIONID abc123
    """

    _default = None

    def __init__(
        self,
        host=None,
        api_key=None,
        api_key_prefix=None,
        discard_unknown_keys=False,
        disabled_client_side_validations="",
        server_index=None,
        server_variables=None,
        server_operation_index=None,
        server_operation_variables=None,
    ):
        """Constructor
        """
        self._base_path = "https://rocketreach.co/api/v2" if host is None else host
        """Default Base url
        """
        self.server_index = 0 if server_index is None and host is None else server_index
        self.server_operation_index = server_operation_index or {}
        """Default server index
        """
        self.server_variables = server_variables or {}
        self.server_operation_variables = server_operation_variables or {}
        """Default server variables
        """
        self.temp_folder_path = None
        """Temp file folder for downloading files
        """
        # Authentication Settings
        self.api_key = {}
        if api_key:
            self.api_key = api_key
        """dict to store API key(s)
        """
        self.api_key_prefix = {}
        if api_key_prefix:
            self.api_key_prefix = api_key_prefix
        """dict to store API prefix (e.g. Bearer)
        """
        self.refresh_api_key_hook = None
        """function hook to refresh API key if expired
        """
        self.disabled_client_side_validations = disabled_client_side_validations
        self.logger = {}
        """Logging Settings
        """
        self.logger["package_logger"] = logging.getLogger("openapi_client")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        """Log format
        """
        self.logger_stream_handler = None
        """Log stream handler
        """
        self.logger_file_handler = None
        """Log file handler
        """
        self.logger_file = None
        """Debug file location
        """
        self.debug = False
        """Debug switch
        """

        self.verify_ssl = True
        """SSL/TLS verification
           Set this to false to skip verifying SSL certificate when calling API
           from https server.
        """
        self.ssl_ca_cert = None
        """Set this to customize the certificate file to verify the peer.
        """
        self.cert_file = None
        """client certificate file
        """
        self.key_file = None
        """client key file
        """
        self.assert_hostname = None
        """Set this to True/False to enable/disable SSL hostname verification.
        """
        self.tls_server_name = None
        """SSL/TLS Server Name Indication (SNI)
           Set this to the SNI value expected by the server.
        """

        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5
        """urllib3 connection pool's maximum number of connections saved
           per pool. urllib3 uses 1 connection as default value, but this is
           not the best value when you are making a lot of possibly parallel
           requests to the same host, which is often the case here.
           cpu_count * 5 is used as default value to increase performance.
        """

        self.proxy = None
        """Proxy URL
        """
        self.proxy_headers = None
        """Proxy headers
        """
        self.safe_chars_for_path_param = ''
        """Safe chars for path_param
        """
        self.retries = None
        """Adding retries to override urllib3 default value 3
        """
        # Enable client side validation
        self.client_side_validation = True

        # Options to pass down to the underlying urllib3 socket
        self.socket_options = None

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in ('logger', 'logger_file_handler'):
                setattr(result, k, copy.deepcopy(v, memo))
        # shallow copy of loggers
        result.logger = copy.copy(self.logger)
        # use setters to configure loggers
        result.logger_file = self.logger_file
        result.debug = self.debug
        return result

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        if name == 'disabled_client_side_validations':
            s = set(filter(None, value.split(',')))
            for v in s:
                if v not in JSON_SCHEMA_VALIDATION_KEYWORDS:
                    raise ApiValueError(
                        "Invalid keyword: '{0}''".format(v))
            self._disabled_client_side_validations = s

    @classmethod
    def set_default(cls, default):
        """Set default instance of configuration.

        It stores default configuration, which can be
        returned by get_default_copy method.

        :param default: object of Configuration
        """
        cls._default = copy.deepcopy(default)

    @classmethod
    def get_default_copy(cls):
        """Return new instance of configuration.

        This method returns newly created, based on default constructor,
        object of Configuration class or returns a copy of default
        configuration passed by the set_default method.

        :return: The configuration object.
        """
        if cls._default is not None:
            return copy.deepcopy(cls._default)
        return Configuration()

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in self.logger.items():
                logger.addHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in self.logger.items():
                logger.setLevel(logging.DEBUG)
            # turn on http_client debug
            http_client.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in self.logger.items():
                logger.setLevel(logging.WARNING)
            # turn off http_client debug
            http_client.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_api_key_with_prefix(self, identifier, alias=None):
        """Gets API key (with prefix if set).

        :param identifier: The identifier of apiKey.
        :param alias: The alternative identifier of apiKey.
        :return: The token for api key authentication.
        """
        if self.refresh_api_key_hook is not None:
            self.refresh_api_key_hook(self)
        key = self.api_key.get(identifier, self.api_key.get(alias) if alias is not None else None)
        if key:
            prefix = self.api_key_prefix.get(identifier)
            if prefix:
                return "%s %s" % (prefix, key)
            else:
                return key

    def get_basic_auth_token(self):
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        username = ""
        if self.username is not None:
            username = self.username
        password = ""
        if self.password is not None:
            password = self.password
        return urllib3.util.make_headers(
            basic_auth=username + ':' + password
        ).get('authorization')

    def auth_settings(self):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        auth = {}
        if 'RocketReach API Key' in self.api_key:
            auth['RocketReach API Key'] = {
                'type': 'api_key',
                'in': 'header',
                'key': 'Api-Key',
                'value': self.get_api_key_with_prefix(
                    'RocketReach API Key',
                ),
            }
        return auth

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: v2\n"\
               "SDK Package Version: 1.0.0".\
               format(env=sys.platform, pyversion=sys.version)

    def get_host_settings(self):
        """Gets an array of host settings

        :return: An array of host settings
        """
        return [
            {
                'url': "https://rocketreach.co/api/v2",
                'description': "No description provided",
            }
        ]

    def get_host_from_settings(self, index, variables=None, servers=None):
        """Gets host URL based on the index and variables
        :param index: array index of the host settings
        :param variables: hash of variable and the corresponding value
        :param servers: an array of host settings or None
        :return: URL based on host settings
        """
        if index is None:
            return self._base_path

        variables = {} if variables is None else variables
        servers = self.get_host_settings() if servers is None else servers

        try:
            server = servers[index]
        except IndexError:
            raise ValueError(
                "Invalid index {0} when selecting the host settings. "
                "Must be less than {1}".format(index, len(servers)))

        url = server['url']

        # go through variables and replace placeholders
        for variable_name, variable in server.get('variables', {}).items():
            used_value = variables.get(
                variable_name, variable['default_value'])

            if 'enum_values' in variable \
                    and used_value not in variable['enum_values']:
                raise ValueError(
                    "The variable `{0}` in the host URL has invalid value "
                    "{1}. Must be {2}.".format(
                        variable_name, variables[variable_name],
                        variable['enum_values']))

            url = url.replace("{" + variable_name + "}", used_value)

        return url

    @property
    def host(self):
        """Return generated host."""
        return self.get_host_from_settings(self.server_index, variables=self.server_variables)

    @host.setter
    def host(self, value):
        """Fix base path."""
        self._base_path = value
        self.server_index = None
