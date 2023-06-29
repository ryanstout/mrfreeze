# openapi-client
# Getting Started
The RocketReach API allows you to programmatically search & lookup contact info for over 700 million professionals, and 35 million companies. We constantly work on improving functionality and accuracy of our data. RocketReach is free to try for individual use.

You can always visit the [account page](/account?section=nav_gen_api) to view API usage, manage RocketReach API settings, and view your unique API key. All calls to the RocketReach API are authenticated with an API key.

## Need Help?
Have feedback, questions about usage, or pricing? Talk to us live or Email us at sales@rocketreach.co.

## Troubleshooting

### Handling Errors
Normal responses are returned with HTTP status `HTTP: 200`. Error responses return `HTTP: 4xx/5xx` error codes. For example, if the profile being searched for cannot be found, we will return a `404`.

### Rate Limits
If we start receiving unusually heavy call volumes on your API key, you may receive responses with `HTTP: 429 \"Too Many Requests\"`. In general, do not make more than 5 calls per second using your API key.

Throttled API responses will contain a `Retry-After` header that contains the number of seconds to wait until the endpoint becomes available again. To ensure your client accesses the API fairly, it should parse this value and waits the appropriate amount of time. 

Repeated instances of unexpected throttled requests should be addressed one of the following ways:
1. If you are not on a paid plan, you will generally need to upgrade to a paid API plan. Please email sales@rocketreach.co to setup an API plan.
2. If you are already on a paid API plan, please slow down and retry your requests. Contact sales@rocketreach.co or our live support if you continue to have problems.

You can visit the [account page](/account?section=api_section_gen_api) to review your RocketReach API limits and daily usage.

## Webhooks
We offer a webhook solution for person lookups so clients do not need to poll the check status endpoint until their results are available.

### Set Up
To set up a webhook, go to your [API settings](/account?section=nav_gen_api). Enter your server's callback URL into the field, and hit \"Create\".

### Configuration Options
For each URL created, you can perform some basic maintenance tasks:

- Test the webhook - we will attempt to send a basic JSON payload to the URL.
- Disable/enable - if you may use this URL in the future, this is an option to temporarily disable it.
- Delete - if you no longer plan using this URL, it can be deleted.

### Usage
Currently, only profile lookup and bulk lookup have webhook functionality, but we anticipate supporting more in the future!
Once you call a webhook-enabled endpoint with a webhook set up in your settings, we will send back results to the provided URL.
The results returned to you should look the same as if they were queried through the REST API. In addition, the API will still respond to your REST call as normal.

### Errors
If any errors occur, they will show up in the [API settings](/account?section=nav_gen_api) page in the \"Web Hook\" section.
If the callback to the provided URL is unsuccessful after several attempts, the URL will be automatically disabled and will need to manually be re-enabled.

## FAQ

**How Do I Know if RocketReach Has Data For a Profile?**
- 87% of lookups return profiles 
- \"teaser\" in search returns some indication of data; however, the final lookup may discover results even if the teaser is empty
- if no data is found, credits are not deducted

**Do I Get Charged a Credit if No Data is Returned?**
- for lookups, no
- searches are metered, but usually the first ~10,000/day are free on paid API plans

**Why doesn't the data in a Profile match data from the API?**
- this should almost never happen, please contact support
- on the other hand, search results and sorting may be different depending on how the search is executed
- the UI uses NLP for search facets

**Why don't the search results in the UI match data returned from the API?**
- search results and sorting may be different depending on how the search is executed
- this also uses NLP for search facets
- try changing the facet and adjusting the `order_by` param

**Why does the teaser only contain phone numbers, and no emails?**
- teaser information is only populated if data is cached

**Why am I getting rate limited?**
- rate limits depend on product, contact us to get on an API plan
- See our troubleshooting guide for more info.


## SDKs

### Python SDK
The [Python SDK](https://www.github.com/rocketreach/rocketreach_python) allows you to find anyone's emails, social media and complete contact data, using only a few lines of code.

### Installation
The rocketreach python package can be installed from pip or from source into your project's virtual environment.

Install with pip:

```bash
pip install rocketreach
```

Install from source:

```bash
# The requests v2.2 or higher is a required dependency
wget https://pypi.python.org/packages/source/r/requests/requests-2.2.1.tar.gz
tar xzvf requests-2.2.1.tar.gz
cd requests-2.2.1
python setup.py install

# Install the rocketreach SDK
wget https://files.pythonhosted.org/packages/20/9d/5ba988d0b2f94a19fb8f86ae87ef1a2eb79b3fd7da7cce00998b7051d57f/rocketreach-2.1.0.tar.gz
tar xzvf rocketreach-2.1.0.tar.gz
cd rocketreach-2.1.0
python setup.py install
```

### Usage

Initialization is the first step to use the SDK. You will need your API key for this step.

```python
import rocketreach
import os
rr = rocketreach.Gateway(api_key=os.environ.get('API_KEY'))

# Check that the SDK is working
result = rr.account.get()
if result.is_success:
    print(f'Success: {result.account}')
else:
    print(f'Error: {result.message}!')
```

You can call any of our methods once the Gateway class is constructed. In this next example we will call lookup() using a name and current employer. Then, we'll do the same lookup using a LinkedIn URL.

```python
lookup_result = rr.person.lookup(name='Marc Benioff', current_employer='Salesforce')
if lookup_result.is_success:
    print(lookup_result.person)
lookup_result = rr.person.lookup(linkedin_url='https://www.linkedin.com/in/marcbenioff')
if lookup_result.is_success:
    print(lookup_result.person)
```

By default, the lookup method blocks until /checkStatus returns complete. The caller can override this behavior and call lookup in a non-blocking context.

```python
import time
# Lookup 2 profiles, non-blocking and checkStatus ourself.
lookup1 = rr.person.lookup(linkedin_url='https://www.linkedin.com/in/marcbenioff', block=False)
lookup2 = rr.person.lookup(linkedin_url='https://www.linkedin.com/in/reidhoffman', block=False)
# Check if the lookups are complete.
while True:
    lookup_ids = [lookup1.person.id, lookup2.person.id]
    cs_result = rr.person.check_status(lookup_ids)
    num_complete = 0
    for p in cs_result.people:
        if p.status == 'complete':
            num_complete += 1
    if num_complete == len(lookups):
        break
    time.sleep(10)  # Wait a few seconds before checking status again
# All the lookups are 'complete'.
```

`check_status()` can take either a single argument, or an array containing multiple IDs to lookup. Regardless of the number of arguments, the return value will always contain a person collection as an array (with 1 or more elements).

```python
result = rr.person.check_status(5244)
assert(len(result.people) == 1)
result = rr.person.check_status([5244, 5234])
assert(len(result.people) == 2)
```

### Reference
Calls are wrapped in a Result object. If the call was successful the Result object will encapsulate the return value.

Result object attributes

Name Description Type
request Request object sent to the server. requests.Request
response Response object received from the server. requests.Response
is_success Indicates if the call succeeded. bool
data (optional) Any data retrieved from the server response. dict
error (optional) Any error data retrieved from the server response. Returned if is_success is False dict
message (optional) A human readable message that explains what went wrong. str

| Name      | Description | Type |
|-----------| ----------- | -----|
| request    | Request object sent to the server. | `requests.Request` |
| response | Response object received from the server. | `requests.Response` |
| is_success | Indicates if the call succeeded. | `bool` |
| data | Any data retrieved from the server response. | `dict` (optional) |
| error | Any error data retrieved from the server response. Returned if `is_success = False` | `dict` (optional) |        |
| message | A human readable message that explains what went wrong. | `str` (optional) |

### Pagination

Searches will only return 10 results at a time, but the API provides a pagination method that can be accessed through the Python SDK.

```python
search = rr.person.search()
# Add filters to your search
start = 1
size = 10
result = search.execute()
people = []
while result.is_success and result.people:
    start += size
    people.extend(result.people)
    search = search.params(start=start, size=size)
    result = search.execute()
```

The Python SDK provides iterators to handle paginating through results for you. These convenience iterators are accessed through the .iterator() method.

```python
search = rr.person.search()
# Add filters to your search
for person in search.iterator():
    print(person)
```

The search object also supports indexing and slicing to limit the range of results.
```python
search = rr.person.search()
# Add filters to your search
list(search[:100])  # Retrieve the first 100 results
list(search[10:20])  # Retrieve results 11 - 19
person = search[0]  # Retrieve only the first result
```

Note:
- Indexing causes the search to be immediately executed with the desired result returned.
- Search object slices cannot contain steps.

## Examples

### Lookup by Name
If you are calling the RocketReach API endpoints directly, you will essentially need to use 2 calls. First call `person/lookup` with 2 parameters: `name` and `current_employer`.

```bash
curl -G -L 'http://api.rocketreach.co/api/v2/person/lookup'\\
     --header 'Api-Key: <INSERT API KEY>'\\
     --data-urlencode 'name=Marc Benioff'\\
     --data-urlencode 'current_employer=Salesforce'
```

If the status returned by the call is not `complete` or `failed`, then you will need to poll `person/checkStatus` untill it returns either `complete` or `failed`. If the status is `complete`, then the response will also contain contact info data.

```bash
curl --request 'GET' --location 'https://api.rocketreach.co/api/v2/person/checkStatus'\\
     --header 'Api-Key: <INSERT API KEY>'\\
     --data-urlencode 'ids=5262'
```

**Putting it all together**
The following example demonstrates a fully functional application, using the RocketReach API. Here, we lookup contact info of a person, by name and current_employer.

The source code shown below uses the RocketReach Python SDK. We start by calling initializing the client. This checks to make sure that the `api_key` is valid, and that the user has sufficient credits to perform lookups. Under the covers, the SDK is simply calling the `/account` endpoint.
If everything looks good, we now call `person/lookup` to lookup contact info. The library also polls `person/checkStatus` for you, when necessary.

```python
import rocketreach
import os
rr = rocketreach.Gateway(api_key=os.environ.get('API_KEY'))
lookup = rr.person.lookup(extras={'name': 'Marc Benioff', 'current_employer': 'Salesforce'})
if lookup.is_success:
    print(repr(lookup.person))
```

Output
```python
    {'current_employer': 'Salesforce',
     'current_personal_email': 'benioff@gmail.com',
     'current_title': 'Chairman and Co-CEO',
     'current_work_email': 'marcb@salesforce.com',
     'emails': [{'email': 'm.benioff@salesforce.com',
                 'smtp_valid': 'valid',
                 'type': 'professional'},
                {'email': 'mbenioff@salesforce.com',
                 'smtp_valid': 'valid',
                 'type': 'professional'},
                {'email': 'benioff@comcast.net',
                 'smtp_valid': 'valid',
                 'type': 'personal'},
                {'email': 'marc@salesforce.com',
                 'smtp_valid': 'valid',
                 'type': 'professional'},
                {'email': 'marc_benioff@salesforce.com',
                 'smtp_valid': 'valid',
                 'type': 'professional'},
                {'email': 'benioff@gmail.com',
                 'smtp_valid': 'valid',
                 'type': 'personal'},
                {'email': 'benioff@aol.com',
                 'smtp_valid': 'valid',
                 'type': 'personal'},
                {'email': 'ceo@salesforce.com',
                 'smtp_valid': 'valid',
                 'type': 'professional'},
                {'email': 'marcb@salesforce.com',
                 'smtp_valid': 'valid',
                 'type': 'professional'},
                {'email': 'marc.benioff@salesforce.com',
                 'smtp_valid': 'valid',
                 'type': 'professional'},
                {'email': 'marcbenioff@salesforce.com',
                 'smtp_valid': 'invalid',
                 'type': 'professional'},
                {'email': 'benioff@frontiernet.net',
                 'smtp_valid': 'invalid',
                 'type': 'personal'},
                {'email': 'cooldwj@chinaren.com',
                 'smtp_valid': 'invalid',
                 'type': 'professional'},
                {'email': 'benioff@rcn.com',
                 'smtp_valid': 'invalid',
                 'type': 'professional'}],
     'id': 5244,
     'linkedin_url': 'https://www.linkedin.com/in/marcbenioff',
     'links': {'aboutme': 'http://www.about.me/marcbenioff',
               'amazon': 'http://www.amazon.com/gp/pdp/profile/AZGYQG724J6ON//190-5748375-2756131',
               'angel': 'https://angel.co/benioff',
               'angellist': 'http://www.angel.co/benioff',
               'crunchbase': 'https://www.crunchbase.com/person/marc-benioff',
               'facebook': 'http://www.facebook.com/benioff',
               'google': 'https://plus.google.com/109586918294369333764',
               'google+': 'https://plus.google.com/108172009599607363531/about',
               'googleplus': 'https://plus.google.com/108172009599607363531',
               'gravatar': 'http://www.gravatar.com/crmmaster',
               'gravatar.com': 'http://gravatar.com/crmmaster',
               'hi5': 'http://www.hi5.com/friend/p45336146--profile--html',
               'instagram': 'http://www.instagram.com/benioff',
               'klout': 'http://www.klout.com/benioff',
               'linkedin': 'https://www.linkedin.com/in/marcbenioff',
               'meetup': 'http://www.meetup.com/members/15867891',
               'pinterest': 'http://www.pinterest.com/benioff',
               'quora': 'http://www.quora.com/marc-benioff',
               'salesforce.com': 'http://www.salesforce.com/company/leadership/executive-team/index.jsp#benioff',
               'twicsy': 'http://twicsy.com/u/%40Benioff',
               'twitter': 'http://www.twitter.com/benioff'},
     'location': 'San Francisco, California, United States',
     'name': 'Marc Benioff',
     'phones': [],
     'profile_pic': 'https://d1hbpr09pwz0sk.cloudfront.net/profile_pic/marc-benioff-4492e698',
     'status': 'complete'}

```

### Lookup by LinkedIn URL

This is very similar to the previous example, but calls `person/lookup` with the `li_url` parameter.

```bash

curl -G --location 'https://api.rocketreach.co/v2/api/person/lookup'\\
     --header 'Api-Key: <INSERT API KEY>'\\
     --data-urlencode 'li_url=https://www.linkedin.com/in/marcbenioff/'
```

**Putting it all together**
The following example demonstrates a fully functional application, using the RocketReach API. Here, we lookup contact info of a person, by `name` and `current_employer`.

The source code shown below uses the RocketReach Python SDK. We start by calling initializing the client. This checks to make sure that the `api_key` is valid, and that the user has sufficient credits to perform lookups. Under the covers, the SDK is simply calling the `/account` endpoint.
If everything looks good, we now call `person/lookup` to lookup contact info. The library also polls `person/checkStatus` for you, when necessary.

Code:

```python
import rocketreach
import os
rr = rocketreach.Gateway(api_key=os.environ.get('API_KEY'))
lookup = rr.person.lookup(linkedin_url='https://www.linkedin.com/in/marcbenioff')
if lookup.is_success:
    print(repr(lookup.person))
```

Output:

```python

    {'current_employer': 'Salesforce',
     'current_personal_email': 'benioff@gmail.com',
     'current_title': 'Chairman and Co-CEO',
     'current_work_email': 'marcb@salesforce.com',
     'emails': [{'email': 'm.benioff@salesforce.com',
                 'smtp_valid': 'valid',
                 'type': 'professional'},
                {'email': 'mbenioff@salesforce.com',
                 'smtp_valid': 'valid',
                 'type': 'professional'},
                {'email': 'benioff@comcast.net',
                 'smtp_valid': 'valid',
                 'type': 'personal'},
                {'email': 'marc@salesforce.com',
                 'smtp_valid': 'valid',
                 'type': 'professional'},
                {'email': 'marc_benioff@salesforce.com',
                 'smtp_valid': 'valid',
                 'type': 'professional'},
                {'email': 'benioff@gmail.com',
                 'smtp_valid': 'valid',
                 'type': 'personal'},
                {'email': 'benioff@aol.com',
                 'smtp_valid': 'valid',
                 'type': 'personal'},
                {'email': 'ceo@salesforce.com',
                 'smtp_valid': 'valid',
                 'type': 'professional'},
                {'email': 'marcb@salesforce.com',
                 'smtp_valid': 'valid',
                 'type': 'professional'},
                {'email': 'marc.benioff@salesforce.com',
                 'smtp_valid': 'valid',
                 'type': 'professional'},
                {'email': 'marcbenioff@salesforce.com',
                 'smtp_valid': 'invalid',
                 'type': 'professional'},
                {'email': 'benioff@frontiernet.net',
                 'smtp_valid': 'invalid',
                 'type': 'personal'},
                {'email': 'cooldwj@chinaren.com',
                 'smtp_valid': 'invalid',
                 'type': 'professional'},
                {'email': 'benioff@rcn.com',
                 'smtp_valid': 'invalid',
                 'type': 'professional'}],
     'id': 5244,
     'linkedin_url': 'https://www.linkedin.com/in/marcbenioff',
     'links': {'aboutme': 'http://www.about.me/marcbenioff',
               'amazon': 'http://www.amazon.com/gp/pdp/profile/AZGYQG724J6ON//190-5748375-2756131',
               'angel': 'https://angel.co/benioff',
               'angellist': 'http://www.angel.co/benioff',

               'crunchbase': 'https://www.crunchbase.com/person/marc-benioff',
               'facebook': 'http://www.facebook.com/benioff',
               'google': 'https://plus.google.com/109586918294369333764',
               'google+': 'https://plus.google.com/108172009599607363531/about',
               'googleplus': 'https://plus.google.com/108172009599607363531',
               'gravatar': 'http://www.gravatar.com/crmmaster',
               'gravatar.com': 'http://gravatar.com/crmmaster',
               'hi5': 'http://www.hi5.com/friend/p45336146--profile--html',
               'instagram': 'http://www.instagram.com/benioff',
               'klout': 'http://www.klout.com/benioff',
               'linkedin': 'https://www.linkedin.com/in/marcbenioff',
               'meetup': 'http://www.meetup.com/members/15867891',
               'pinterest': 'http://www.pinterest.com/benioff',
               'quora': 'http://www.quora.com/marc-benioff',
               'salesforce.com': 'http://www.salesforce.com/company/leadership/executive-team/index.jsp#benioff',
               'twicsy': 'http://twicsy.com/u/%40Benioff',
               'twitter': 'http://www.twitter.com/benioff'},
     'location': 'San Francisco, California, United States',
     'name': 'Marc Benioff',
     'phones': [],
     'profile_pic': 'https://d1hbpr09pwz0sk.cloudfront.net/profile_pic/marc-benioff-4492e698',
     'status': 'complete'}
```


### Search People by Role at Company

If you are calling the RocketReach API endpoints directly, you will essentially need to use 3 calls. First call the `person/search` endpoint.

```bash
curl --request 'POST' --location 'https://api.rocketreach.co/api/v2/search'\\
     --header 'Api-Key: <INSERT API KEY>'\\
     --header 'Content-Type: application/json'\\
     --data '{\"query\":{\"name\":[\"Marc Benioff\"],\"current_employer\":[\"Salesforce\"],\"current_title\":[\"CEO\"]}}'
```

Assuming that the `id` for Marc's profile is `5262`, you then call `person/lookup`.

```bash
curl --request 'GET' --location 'https://api.rocketreach.co/api/v2/lookupProfile'\\
     --header 'Api-Key: <INSERT API KEY>'\\
     --data-urlencode 'id=5262'
```

If the status returned by the call is not `complete` or `failed`, then you will need to poll `person/checkStatus` untill it returns either `complete` or `failed`.

```bash
curl --request 'GET' --location 'https://api.rocketreach.co/api/v2/checkStatus'\\
     --header 'Api-Key: <INSERT API KEY>'\\
     --data-urlencode 'ids=5262'
```

**Putting it all together**
In this example, we will search for people with a specific name and title, at a company. We will then lookup contact info for one of the search results.

Code:
```python
    import rocketreach
    import os
    rr = rocketreach.Gateway(api_key=os.environ.get('API_KEY'))
    search = rr.person.search()
    # Build up our search query
    search = search.filter(name='Marc Benioff', current_title='CEO', current_employer='Salesforce')
    # Call the search endpoint with our query
    result = search.execute()
    if result.is_success:
        lookup = rr.person.lookup(result.people[0].id)
        if lookup.is_success:
            print(repr(lookup.person))
```

Output:
```python
{
    'current_employer': 'Salesforce',
    'current_personal_email': 'benioff@gmail.com',
    'current_title': 'Chairman and Co-CEO',
    'current_work_email': 'marcb@salesforce.com',
    'emails': [{'email': 'm.benioff@salesforce.com',
             'smtp_valid': 'valid',
             'type': 'professional'},
            {'email': 'mbenioff@salesforce.com',
             'smtp_valid': 'valid',
             'type': 'professional'},
            {'email': 'benioff@comcast.net',
             'smtp_valid': 'valid',
             'type': 'personal'},
            {'email': 'marc@salesforce.com',
             'smtp_valid': 'valid',
             'type': 'professional'},
            {'email': 'marc_benioff@salesforce.com',
             'smtp_valid': 'valid',
             'type': 'professional'},
            {'email': 'benioff@gmail.com',
             'smtp_valid': 'valid',
             'type': 'personal'},
            {'email': 'benioff@aol.com',
             'smtp_valid': 'valid',
             'type': 'personal'},
            {'email': 'ceo@salesforce.com',
             'smtp_valid': 'valid',
             'type': 'professional'},
            {'email': 'marcb@salesforce.com',
             'smtp_valid': 'valid',
             'type': 'professional'},
            {'email': 'marc.benioff@salesforce.com',
             'smtp_valid': 'valid',
             'type': 'professional'},
            {'email': 'marcbenioff@salesforce.com',
             'smtp_valid': 'invalid',
             'type': 'professional'},
            {'email': 'benioff@frontiernet.net',
             'smtp_valid': 'invalid',
             'type': 'personal'},
            {'email': 'cooldwj@chinaren.com',
             'smtp_valid': 'invalid',
             'type': 'professional'},
            {'email': 'benioff@rcn.com',
             'smtp_valid': 'invalid',
             'type': 'professional'}],
    'id': 5244,
    'linkedin_url': 'https://www.linkedin.com/in/marcbenioff',
    'links': {'aboutme': 'http://www.about.me/marcbenioff',
           'amazon': 'http://www.amazon.com/gp/pdp/profile/AZGYQG724J6ON//190-5748375-2756131',
           'angel': 'https://angel.co/benioff',
           'angellist': 'http://www.angel.co/benioff',
           'crunchbase': 'https://www.crunchbase.com/person/marc-benioff',
           'facebook': 'http://www.facebook.com/benioff',
           'google': 'https://plus.google.com/109586918294369333764',
           'google+': 'https://plus.google.com/108172009599607363531/about',
           'googleplus': 'https://plus.google.com/108172009599607363531',
           'gravatar': 'http://www.gravatar.com/crmmaster',
           'gravatar.com': 'http://gravatar.com/crmmaster',
           'hi5': 'http://www.hi5.com/friend/p45336146--profile--html',
           'instagram': 'http://www.instagram.com/benioff',
           'klout': 'http://www.klout.com/benioff',
           'linkedin': 'https://www.linkedin.com/in/marcbenioff',
           'meetup': 'http://www.meetup.com/members/15867891',
           'pinterest': 'http://www.pinterest.com/benioff',
           'quora': 'http://www.quora.com/marc-benioff',
           'salesforce.com': 'http://www.salesforce.com/company/leadership/executive-team/index.jsp#benioff',
           'twicsy': 'http://twicsy.com/u/%40Benioff',
           'twitter': 'http://www.twitter.com/benioff'},
    'location': 'San Francisco, California, United States',
    'name': 'Marc Benioff',
    'phones': [],
    'profile_pic': 'https://d1hbpr09pwz0sk.cloudfront.net/profile_pic/marc-benioff-4492e698',
    'status': 'complete'
}
 ```

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v2
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from pprint import pprint
from openapi_client.apis.tags import account_api
from openapi_client.model.user_model import UserModel
# Defining the host is optional and defaults to https://rocketreach.co/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://rocketreach.co/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: RocketReach API Key
configuration.api_key['RocketReach API Key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['RocketReach API Key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    
    try:
        # Retrieve Account
        api_response = api_instance.account_read()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountApi->account_read: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://rocketreach.co/api/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**account_read**](docs/apis/tags/AccountApi.md#account_read) | **get** /account/ | Retrieve Account
*CompanyProfilesApi* | [**company_lookup_read**](docs/apis/tags/CompanyProfilesApi.md#company_lookup_read) | **get** /company/lookup/ | Lookup Company Information
*CompanyProfilesApi* | [**lookup_company_read**](docs/apis/tags/CompanyProfilesApi.md#lookup_company_read) | **get** /lookupCompany | Lookup Company Information
*CompanyProfilesApi* | [**profile_company_lookup_read**](docs/apis/tags/CompanyProfilesApi.md#profile_company_lookup_read) | **get** /profile-company/lookup | Lookup Person and Company
*CompanyProfilesApi* | [**search_company_create**](docs/apis/tags/CompanyProfilesApi.md#search_company_create) | **post** /searchCompany | Search Companies
*PersonProfilesApi* | [**bulk_lookup_create**](docs/apis/tags/PersonProfilesApi.md#bulk_lookup_create) | **post** /bulkLookup | Bulk People Lookup
*PersonProfilesApi* | [**check_status_list**](docs/apis/tags/PersonProfilesApi.md#check_status_list) | **get** /checkStatus | Check Person Lookup Status
*PersonProfilesApi* | [**lookup_profile_read**](docs/apis/tags/PersonProfilesApi.md#lookup_profile_read) | **get** /lookupProfile | Lookup Person
*PersonProfilesApi* | [**person_check_status_list**](docs/apis/tags/PersonProfilesApi.md#person_check_status_list) | **get** /person/checkStatus | Check Person Lookup Status
*PersonProfilesApi* | [**person_lookup_read**](docs/apis/tags/PersonProfilesApi.md#person_lookup_read) | **get** /person/lookup | Lookup Person
*PersonProfilesApi* | [**person_search_create**](docs/apis/tags/PersonProfilesApi.md#person_search_create) | **post** /person/search | Search People
*PersonProfilesApi* | [**profile_company_lookup_read**](docs/apis/tags/PersonProfilesApi.md#profile_company_lookup_read) | **get** /profile-company/lookup | Lookup Person and Company
*PersonProfilesApi* | [**search_create**](docs/apis/tags/PersonProfilesApi.md#search_create) | **post** /search | Search People

## Documentation For Models

 - [APIBulkLookupQuery](docs/models/APIBulkLookupQuery.md)
 - [APIPublicCompanySearchInput](docs/models/APIPublicCompanySearchInput.md)
 - [APISearchInput](docs/models/APISearchInput.md)
 - [CompanyAPI](docs/models/CompanyAPI.md)
 - [CompanyAddress](docs/models/CompanyAddress.md)
 - [CompanyPublicDetails](docs/models/CompanyPublicDetails.md)
 - [CompanyQuery](docs/models/CompanyQuery.md)
 - [EducationAPI](docs/models/EducationAPI.md)
 - [JobHistoryAPI](docs/models/JobHistoryAPI.md)
 - [PersonQuery](docs/models/PersonQuery.md)
 - [Plan](docs/models/Plan.md)
 - [ProfileAPI](docs/models/ProfileAPI.md)
 - [ProfileAPISerializerWithCompany](docs/models/ProfileAPISerializerWithCompany.md)
 - [ProfileEmailAPI](docs/models/ProfileEmailAPI.md)
 - [ProfileListAPI](docs/models/ProfileListAPI.md)
 - [ProfileMatch](docs/models/ProfileMatch.md)
 - [ProfilePhoneAPI](docs/models/ProfilePhoneAPI.md)
 - [ProfileSearchResult](docs/models/ProfileSearchResult.md)
 - [UserModel](docs/models/UserModel.md)

## Documentation For Authorization

Authentication schemes defined for the API:
<a id="RocketReach API Key"></a>
### RocketReach API Key

- **Type**: API key
- **API key parameter name**: Api-Key
- **Location**: HTTP header


## Author

support@rocketreach.co
support@rocketreach.co
support@rocketreach.co

## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in openapi_client.apis and openapi_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from openapi_client.apis.default_api import DefaultApi`
- `from openapi_client.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import openapi_client
from openapi_client.apis import *
from openapi_client.models import *
```
