# openapi_client.StatusAndInformationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appdef_get**](StatusAndInformationApi.md#appdef_get) | **GET** /jarvice/appdef | Returns the Application Definition (AppDef) for a given application.
[**apps_get**](StatusAndInformationApi.md#apps_get) | **GET** /jarvice/apps | Returns the Application Definition (AppDef) for a given application.
[**billing_get**](StatusAndInformationApi.md#billing_get) | **GET** /jarvice/billing | (JXE/System Admins only) Returns billing report for JARVICE users
[**connect_get**](StatusAndInformationApi.md#connect_get) | **GET** /jarvice/connect | Requests the network address and user nimbix password (if set), for an interactive job.
[**events_get**](StatusAndInformationApi.md#events_get) | **GET** /jarvice/events | (JXE/System Admins only) Retrieves event logs for a running job that are related to the cluster infrastructure
[**info_get**](StatusAndInformationApi.md#info_get) | **GET** /jarvice/info | Get info from job
[**jobs_get**](StatusAndInformationApi.md#jobs_get) | **GET** /jarvice/jobs | Returns job information and status for all queued and running jobs.
[**license_get**](StatusAndInformationApi.md#license_get) | **GET** /jarvice/license | (JXE/System Admins only) Retrieves Jarvice license
[**live_get**](StatusAndInformationApi.md#live_get) | **GET** /jarvice/live | Get info is API is alive
[**machines_get**](StatusAndInformationApi.md#machines_get) | **GET** /jarvice/machines | Returns information about available machine type(s).
[**metrics_get**](StatusAndInformationApi.md#metrics_get) | **GET** /jarvice/metrics | Returns the last known CPU and memory utilization metrics for a given job.
[**output_get**](StatusAndInformationApi.md#output_get) | **GET** /jarvice/output | Returns a tail (or optionally all) of the output of a completed job.
[**projects_get**](StatusAndInformationApi.md#projects_get) | **GET** /jarvice/projects | (JXE/System Admins only) Returns all JARVICE projects and members
[**queues_get**](StatusAndInformationApi.md#queues_get) | **GET** /jarvice/queues | (JXE only) Returns information about available queue(s).
[**ready_get**](StatusAndInformationApi.md#ready_get) | **GET** /jarvice/ready | Get info if DAL is ready
[**screenshot_get**](StatusAndInformationApi.md#screenshot_get) | **GET** /jarvice/screenshot | Returns a screenshot for a running job (if it is graphical).
[**status_get**](StatusAndInformationApi.md#status_get) | **GET** /jarvice/status | Queries status for a previously submitted job.
[**tail_get**](StatusAndInformationApi.md#tail_get) | **GET** /jarvice/tail | Returns a tail (or optionally all) of the output of a completed job.
[**teamjobs_get**](StatusAndInformationApi.md#teamjobs_get) | **GET** /jarvice/teamjobs | Returns job information and status for all queued and running jobs for an entire team.
[**teamusers_get**](StatusAndInformationApi.md#teamusers_get) | **GET** /jarvice/teamusers | (Team Admins only) Returns a list of JARVICE users who are members of the callers team
[**vault_get**](StatusAndInformationApi.md#vault_get) | **GET** /jarvice/vault | List files in a vault.


# **appdef_get**
> AppDef appdef_get(apikey, username, name)

Returns the Application Definition (AppDef) for a given application.

Returns the Application Definition (AppDef) for a given application.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.app_def import AppDef
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate
    username = 'username_example' # str | Name of user to authenticate
    name = 'name_example' # str | Name of application to return information for; please note this is the application ID, not necessarily the same as the name value in the AppDef

    try:
        # Returns the Application Definition (AppDef) for a given application.
        api_response = api_instance.appdef_get(apikey, username, name)
        print("The response of StatusAndInformationApi->appdef_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->appdef_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate | 
 **username** | **str**| Name of user to authenticate | 
 **name** | **str**| Name of application to return information for; please note this is the application ID, not necessarily the same as the name value in the AppDef | 

### Return type

[**AppDef**](AppDef.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | On success, a JSON payload with the AppDef requested. |  -  |
**400** | Required parameter(s) missing | Invalid parameter(s) |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_get**
> List[AppDef] apps_get(apikey=apikey, username=username, name=name, version=version)

Returns the Application Definition (AppDef) for a given application.

On success, a JSON payload with application information for each available application, or for the specific application name if available. The application name is used as the dictionary key, and the data subkey contains the raw definition in JSON format. The price value is the application price itself, not including underlying machine price (which is available by querying the machine type using /jarvice/machines). Note that application name is the application ID, not necessarily the same as the human readable name in the AppDef for the given application.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.app_def import AppDef
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate  (optional)
    username = 'username_example' # str | Name of user to authenticate - if unspecified, public apps only (optional)
    name = 'all' # str | Name of application to return information for (optional) (default to 'all')
    version = 1 # int | Filter applications by appdef version (optional) (default to 1)

    try:
        # Returns the Application Definition (AppDef) for a given application.
        api_response = api_instance.apps_get(apikey=apikey, username=username, name=name, version=version)
        print("The response of StatusAndInformationApi->apps_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->apps_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate  | [optional] 
 **username** | **str**| Name of user to authenticate - if unspecified, public apps only | [optional] 
 **name** | **str**| Name of application to return information for | [optional] [default to &#39;all&#39;]
 **version** | **int**| Filter applications by appdef version | [optional] [default to 1]

### Return type

[**List[AppDef]**](AppDef.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of AppDef |  -  |
**400** | Required parameter(s) missing | Invalid parameter(s) |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_get**
> bytearray billing_get(apikey, username, reportuser=reportuser, zone=zone, billingcode=billingcode, statuses=statuses, machtypes=machtypes, jobapp=jobapp, itemized=itemized, timeperiod=timeperiod, startdate=startdate, enddate=enddate)

(JXE/System Admins only) Returns billing report for JARVICE users

On success, a CSV file containing generated billing report 1. Endpoint is for JARVICE XE System Administrators only 2. If reportuser is a payer of a team, all team members are included 3. Valid statuses fields are: COMPLETED, COMPLETED WITH ERROR, SUBMITTED, PROCESSING STARTING, CANCELED, EXEMPT, SEQUENTIALLY QUEUED, TERMINATED 4. Valid machtypes can be queried using /jarvice/machines API 5. startdate and enddate are required if timeperiod is set to range

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate
    username = 'username_example' # str | Name of user to authenticate
    reportuser = 'reportuser_example' # str | Comma separated list of users to filter (if not specified: list all users) (optional)
    zone = 'zone_example' # str | Zone for machines (optional)
    billingcode = 56 # int | Billing code to filter by (optional)
    statuses = 'statuses_example' # str | Comma seperated string of statuses to filter by (optional)
    machtypes = 'machtypes_example' # str | Comma seperated string of machine types to filter (optional)
    jobapp = 'jobapp_example' # str | Application name to filter by (e.g. jarvice-ubuntu) (optional)
    itemized = 'false' # str | Set to true to generate itemized report (optional) (default to 'false')
    timeperiod = 'timeperiod_example' # str | Includes jobs in the previous/current month or custom range (either last, current, or range) (optional)
    startdate = 'startdate_example' # str | Range start of time period to generate report (YYYY-MM-DD) (optional)
    enddate = 'enddate_example' # str | Range end of time period to generate report (YYYY-MM-DD) (optional)

    try:
        # (JXE/System Admins only) Returns billing report for JARVICE users
        api_response = api_instance.billing_get(apikey, username, reportuser=reportuser, zone=zone, billingcode=billingcode, statuses=statuses, machtypes=machtypes, jobapp=jobapp, itemized=itemized, timeperiod=timeperiod, startdate=startdate, enddate=enddate)
        print("The response of StatusAndInformationApi->billing_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->billing_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate | 
 **username** | **str**| Name of user to authenticate | 
 **reportuser** | **str**| Comma separated list of users to filter (if not specified: list all users) | [optional] 
 **zone** | **str**| Zone for machines | [optional] 
 **billingcode** | **int**| Billing code to filter by | [optional] 
 **statuses** | **str**| Comma seperated string of statuses to filter by | [optional] 
 **machtypes** | **str**| Comma seperated string of machine types to filter | [optional] 
 **jobapp** | **str**| Application name to filter by (e.g. jarvice-ubuntu) | [optional] 
 **itemized** | **str**| Set to true to generate itemized report | [optional] [default to &#39;false&#39;]
 **timeperiod** | **str**| Includes jobs in the previous/current month or custom range (either last, current, or range) | [optional] 
 **startdate** | **str**| Range start of time period to generate report (YYYY-MM-DD) | [optional] 
 **enddate** | **str**| Range end of time period to generate report (YYYY-MM-DD) | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CSV file containing generated billing report |  -  |
**400** | Required parameter(s) missing | Invalid parameter(s) |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_get**
> RuntimeConnect connect_get(apikey, username, name=name, number=number)

Requests the network address and user nimbix password (if set), for an interactive job.

Requests the network address and user nimbix password (if set), for an interactive job. Additional Notes : 1. One of name or number must be specified 2. Job must be running an application endpoint that has interactive set to true in its AppDef in order for it to respond successfully 3. This method may take a few seconds to respond successfully after starting a job, as its connection parameters are not known until its application components start

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.runtime_connect import RuntimeConnect
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate
    username = 'username_example' # str | Name of user to authenticate
    name = 'name_example' # str | Job name (name key returned from /jarvice/submit *Must be specifed or number is specified (optional)
    number = 56 # int | Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified (optional)

    try:
        # Requests the network address and user nimbix password (if set), for an interactive job.
        api_response = api_instance.connect_get(apikey, username, name=name, number=number)
        print("The response of StatusAndInformationApi->connect_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->connect_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate | 
 **username** | **str**| Name of user to authenticate | 
 **name** | **str**| Job name (name key returned from /jarvice/submit *Must be specifed or number is specified | [optional] 
 **number** | **int**| Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified | [optional] 

### Return type

[**RuntimeConnect**](RuntimeConnect.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connection information |  -  |
**400** | Required parameter(s) missing | No job specified | Bad Request | User required |  -  |
**401** | Unauthorized |  -  |
**404** | Job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_get**
> str events_get(apikey, username, name=name, number=number)

(JXE/System Admins only) Retrieves event logs for a running job that are related to the cluster infrastructure

Retrieves event logs for a running job that are related to the cluster infrastructure

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate 
    username = 'username_example' # str | Name of user to authenticate
    name = 'name_example' # str | Job name (name key returned from /jarvice/submit) (optional)
    number = 56 # int | Job number (number key returned from /jarvice/submit) (optional)

    try:
        # (JXE/System Admins only) Retrieves event logs for a running job that are related to the cluster infrastructure
        api_response = api_instance.events_get(apikey, username, name=name, number=number)
        print("The response of StatusAndInformationApi->events_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->events_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate  | 
 **username** | **str**| Name of user to authenticate | 
 **name** | **str**| Job name (name key returned from /jarvice/submit) | [optional] 
 **number** | **int**| Job number (number key returned from /jarvice/submit) | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Logs |  -  |
**400** | Required parameter(s) missing | No job specified | Bad Request | User required |  -  |
**401** | Unauthorized |  -  |
**404** | Job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **info_get**
> SchedJobStatusEntry info_get(apikey, username, name=name, number=number)

Get info from job

Get info from job

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.sched_job_status_entry import SchedJobStatusEntry
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate
    username = 'username_example' # str | Name of user to authenticate
    name = 'name_example' # str | Job name (name key returned from /jarvice/submit *Must be specifed or number is specified (optional)
    number = 56 # int | Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified (optional)

    try:
        # Get info from job
        api_response = api_instance.info_get(apikey, username, name=name, number=number)
        print("The response of StatusAndInformationApi->info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->info_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate | 
 **username** | **str**| Name of user to authenticate | 
 **name** | **str**| Job name (name key returned from /jarvice/submit *Must be specifed or number is specified | [optional] 
 **number** | **int**| Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified | [optional] 

### Return type

[**SchedJobStatusEntry**](SchedJobStatusEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Required parameter(s) missing | No job specified | Bad Request | User required |  -  |
**401** | Unauthorized |  -  |
**404** | Job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_get**
> Dict[str, JobEntry] jobs_get(apikey, username, completed=completed)

Returns job information and status for all queued and running jobs.

On success, a JSON payload with job status for each queued or running job (keyed by job number), formatted like the response of /jarvice/status

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.job_entry import JobEntry
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate 
    username = 'username_example' # str | Name of user to authenticate
    completed = False # bool | Set to true (case sensitive) to show only completed jobs (optional) (default to False)

    try:
        # Returns job information and status for all queued and running jobs.
        api_response = api_instance.jobs_get(apikey, username, completed=completed)
        print("The response of StatusAndInformationApi->jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->jobs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate  | 
 **username** | **str**| Name of user to authenticate | 
 **completed** | **bool**| Set to true (case sensitive) to show only completed jobs | [optional] [default to False]

### Return type

[**Dict[str, JobEntry]**](JobEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of jobs |  -  |
**400** | Required parameter(s) missing | Invalid parameter(s) |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **license_get**
> str license_get(apikey, username)

(JXE/System Admins only) Retrieves Jarvice license

(JXE/System Admins only) Retrieves Jarvice license

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate
    username = 'username_example' # str | Name of user to authenticate

    try:
        # (JXE/System Admins only) Retrieves Jarvice license
        api_response = api_instance.license_get(apikey, username)
        print("The response of StatusAndInformationApi->license_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->license_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate | 
 **username** | **str**| Name of user to authenticate | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | License |  -  |
**400** | Required parameter(s) missing | Invalid parameter(s) |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **live_get**
> object live_get()

Get info is API is alive

Get info is API is alive

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)

    try:
        # Get info is API is alive
        api_response = api_instance.live_get()
        print("The response of StatusAndInformationApi->live_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->live_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | {&#39;status&#39;: &#39;OK&#39;} |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **machines_get**
> Dict[str, object] machines_get(apikey, username, name=name, vault=vault)

Returns information about available machine type(s).

Returns information about available machine type(s). On success, a JSON payload with machine information for each available machine type, or for the specific machine name if available. The machine name is used as the dictionary key.

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate 
    username = 'username_example' # str | Name of user to authenticate
    name = 'all' # str | Name of machine type to return information for (optional) (default to 'all')
    vault = 'vault_example' # str | Vault name to use for machine compatibility; if specified, response will be a list of machines that can be used against that vault; if not specified, the user's default vault is used to determine machine compatibility (optional)

    try:
        # Returns information about available machine type(s).
        api_response = api_instance.machines_get(apikey, username, name=name, vault=vault)
        print("The response of StatusAndInformationApi->machines_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->machines_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate  | 
 **username** | **str**| Name of user to authenticate | 
 **name** | **str**| Name of machine type to return information for | [optional] [default to &#39;all&#39;]
 **vault** | **str**| Vault name to use for machine compatibility; if specified, response will be a list of machines that can be used against that vault; if not specified, the user&#39;s default vault is used to determine machine compatibility | [optional] 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of machines |  -  |
**400** | Required parameter(s) missing | Invalid parameter(s) |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_get**
> RuntimeMetrics metrics_get(apikey, username, name=name, number=number)

Returns the last known CPU and memory utilization metrics for a given job.

Returns the last known CPU and memory utilization metrics for a given job. On success, a JSON payload indicating summary values in the summary key, and itemized values (one for each parallel node in the job) in the itemized key. Additional Notes : 1. One of name or number must be specified 2. cpu_used is always a percentage value (percentage of total CPU resource allocated), while memory_used and memory_total are always in kilobytes. 3. In the summary section, cpu_used is the average of all CPU utilization across all nodes in the job, while the memory values are the sum total, in kilobytes. 4. The percentage of memory utilized from the summary can be calculated by dividing memory_used by memory_total and multiplying by 100. 5. All values are \"point in time\" rather than rolling average or any type of cumulative calculation, and are collected periodically (typically every 30 seconds) 6. This endpoint may return a 404 for approximately the first minute that a job is running, until metrics become available

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.runtime_metrics import RuntimeMetrics
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate 
    username = 'username_example' # str | Name of user to authenticate
    name = 'name_example' # str | Job name (name key returned from /jarvice/submit) *Must be specifed or number is specified (optional)
    number = 56 # int | Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified (optional)

    try:
        # Returns the last known CPU and memory utilization metrics for a given job.
        api_response = api_instance.metrics_get(apikey, username, name=name, number=number)
        print("The response of StatusAndInformationApi->metrics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->metrics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate  | 
 **username** | **str**| Name of user to authenticate | 
 **name** | **str**| Job name (name key returned from /jarvice/submit) *Must be specifed or number is specified | [optional] 
 **number** | **int**| Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified | [optional] 

### Return type

[**RuntimeMetrics**](RuntimeMetrics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Required parameter(s) missing | No job specified | Bad Request | User required |  -  |
**401** | Unauthorized |  -  |
**404** | Job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **output_get**
> str output_get(apikey, username, name=name, number=number, lines=lines)

Returns a tail (or optionally all) of the output of a completed job.

Returns a tail (or optionally all) of the output of a completed job. On success, the requested output tail in text/plain format (with single \\n for line breaks), up to and including the number of lines requested; if the total length of the output is less than lines requested, the entire output is returned. If lines requested is 0, all lines in the output are returned rather than just a tail of it. Additional Notes : 1. One of name or number must be specified 2. Job must have completed; to get the output of a running job instead, use /jarvice/tail

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate 
    username = 'username_example' # str | Name of user to authenticate
    name = 'name_example' # str | Job name (name key returned from /jarvice/submit) *Must be specifed or number is specified (optional)
    number = 56 # int | Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified (optional)
    lines = 100 # int | Number of lines to tail from the end - use 0 to return all lines rather than just a tail (optional) (default to 100)

    try:
        # Returns a tail (or optionally all) of the output of a completed job.
        api_response = api_instance.output_get(apikey, username, name=name, number=number, lines=lines)
        print("The response of StatusAndInformationApi->output_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->output_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate  | 
 **username** | **str**| Name of user to authenticate | 
 **name** | **str**| Job name (name key returned from /jarvice/submit) *Must be specifed or number is specified | [optional] 
 **number** | **int**| Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified | [optional] 
 **lines** | **int**| Number of lines to tail from the end - use 0 to return all lines rather than just a tail | [optional] [default to 100]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Required parameter(s) missing | No job specified | Bad Request | User required |  -  |
**401** | Unauthorized |  -  |
**404** | Job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get**
> Dict[str, List[str]] projects_get(apikey, username)

(JXE/System Admins only) Returns all JARVICE projects and members

(JXE/System Admins only) Returns all JARVICE projects and members Additional Notes: 1. Endpoint is for JARVICE XE System Administrators only 2. Project name contains the project owner, <owner>-<project-name>

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate 
    username = 'username_example' # str | Name of user to authenticate

    try:
        # (JXE/System Admins only) Returns all JARVICE projects and members
        api_response = api_instance.projects_get(apikey, username)
        print("The response of StatusAndInformationApi->projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->projects_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate  | 
 **username** | **str**| Name of user to authenticate | 

### Return type

**Dict[str, List[str]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON payload with projects |  -  |
**400** | Required parameter(s) missing | No job specified | Bad Request | User required |  -  |
**401** | Unauthorized |  -  |
**404** | Job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **queues_get**
> List[Queue] queues_get(apikey, username, name=name, info=info)

(JXE only) Returns information about available queue(s).

Retrieves event logs for a running job that are related to the cluster infrastructure

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.queue import Queue
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate 
    username = 'username_example' # str | Name of user to authenticate
    name = 'all' # str | Name of queue to return information for (optional) (default to 'all')
    info = 56 # int | Display additional info for each queue (optional)

    try:
        # (JXE only) Returns information about available queue(s).
        api_response = api_instance.queues_get(apikey, username, name=name, info=info)
        print("The response of StatusAndInformationApi->queues_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->queues_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate  | 
 **username** | **str**| Name of user to authenticate | 
 **name** | **str**| Name of queue to return information for | [optional] [default to &#39;all&#39;]
 **info** | **int**| Display additional info for each queue | [optional] 

### Return type

[**List[Queue]**](Queue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON payload with an array of (string) available queues or when info&#x3D;true, a JSON payload with queue information. |  -  |
**400** | Required parameter(s) missing | No job specified | Bad Request | User required |  -  |
**401** | Unauthorized |  -  |
**404** | Queue not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ready_get**
> Dict[str, object] ready_get()

Get info if DAL is ready

Get info if DAL is ready

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)

    try:
        # Get info if DAL is ready
        api_response = api_instance.ready_get()
        print("The response of StatusAndInformationApi->ready_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->ready_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | {&#39;status&#39;: &#39;OK&#39;} |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Queue not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **screenshot_get**
> bytearray screenshot_get(apikey, username, name=name, number=number, width=width, height=height, emphatic=emphatic)

Returns a screenshot for a running job (if it is graphical).

Returns a screenshot for a running job (if it is graphical). On success, an image/png payload with the requested screenshot if available Additional Notes: 1. One of name or number must be specified 2. If emphatic is not specified, but width and/or height is, the aspect ratio of the screenshot image is preserved when resizing.

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate
    username = 'username_example' # str | Name of user to authenticate
    name = 'name_example' # str | Job name (name key returned from /jarvice/submit *Must be specifed or number is specified (optional)
    number = 56 # int | Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified (optional)
    width = 56 # int | Pixel width to restrict screenshot to (optional)
    height = 56 # int | Pixel height to restrict screenshot to (optional)
    emphatic = True # bool | If specified, emphatically resize (disregarding aspect ratio) to specified width and/or height (optional)

    try:
        # Returns a screenshot for a running job (if it is graphical).
        api_response = api_instance.screenshot_get(apikey, username, name=name, number=number, width=width, height=height, emphatic=emphatic)
        print("The response of StatusAndInformationApi->screenshot_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->screenshot_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate | 
 **username** | **str**| Name of user to authenticate | 
 **name** | **str**| Job name (name key returned from /jarvice/submit *Must be specifed or number is specified | [optional] 
 **number** | **int**| Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified | [optional] 
 **width** | **int**| Pixel width to restrict screenshot to | [optional] 
 **height** | **int**| Pixel height to restrict screenshot to | [optional] 
 **emphatic** | **bool**| If specified, emphatically resize (disregarding aspect ratio) to specified width and/or height | [optional] 

### Return type

**bytearray**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | image/png payload with the requested screenshot if available. |  -  |
**400** | Required parameter(s) missing | No job specified | Bad Request | User required |  -  |
**401** | Unauthorized |  -  |
**404** | Job not found |  -  |
**501** | Invalid image |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_get**
> Dict[str, SchedJobStatusEntry] status_get(apikey, username, name=name, number=number)

Queries status for a previously submitted job.

Queries status for a previously submitted job. Additional Notes: 1. One of name or number must be specified 2. All \"time\" values are represented in UNIX time (seconds since the Epoch); values may be 0 if the data is not yet available (e.g. a job that hasn't completed yet will have a 0 for job_end_time); additional values may be returned in the future.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.sched_job_status_entry import SchedJobStatusEntry
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate
    username = 'username_example' # str | Name of user to authenticate
    name = 'name_example' # str | Job name (name key returned from /jarvice/submit *Must be specifed or number is specified (optional)
    number = 56 # int | Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified (optional)

    try:
        # Queries status for a previously submitted job.
        api_response = api_instance.status_get(apikey, username, name=name, number=number)
        print("The response of StatusAndInformationApi->status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->status_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate | 
 **username** | **str**| Name of user to authenticate | 
 **name** | **str**| Job name (name key returned from /jarvice/submit *Must be specifed or number is specified | [optional] 
 **number** | **int**| Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified | [optional] 

### Return type

[**Dict[str, SchedJobStatusEntry]**](SchedJobStatusEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON payload with job status |  -  |
**400** | Required parameter(s) missing | No job specified | Bad Request | User required |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tail_get**
> str tail_get(apikey, username, name=name, number=number, lines=lines)

Returns a tail (or optionally all) of the output of a completed job.

Returns a tail (or optionally all) of the output of a completed job. On success, the requested output tail in text/plain format (with single \\n for line breaks), up to and including the number of lines requested; if the total length of the output is less than lines requested, the entire output is returned. If lines requested is 0, all lines in the output are returned rather than just a tail of it. Additional Notes : 1. One of name or number must be specified 2. Job must still be running; to get the output of a completed job instead, use /jarvice/output

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate 
    username = 'username_example' # str | Name of user to authenticate
    name = 'name_example' # str | Job name (name key returned from /jarvice/submit) *Must be specifed or number is specified (optional)
    number = 56 # int | Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified (optional)
    lines = 100 # int | Number of lines to tail from the end - use 0 to return all lines rather than just a tail (optional) (default to 100)

    try:
        # Returns a tail (or optionally all) of the output of a completed job.
        api_response = api_instance.tail_get(apikey, username, name=name, number=number, lines=lines)
        print("The response of StatusAndInformationApi->tail_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->tail_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate  | 
 **username** | **str**| Name of user to authenticate | 
 **name** | **str**| Job name (name key returned from /jarvice/submit) *Must be specifed or number is specified | [optional] 
 **number** | **int**| Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified | [optional] 
 **lines** | **int**| Number of lines to tail from the end - use 0 to return all lines rather than just a tail | [optional] [default to 100]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Required parameter(s) missing | No job specified | Bad Request | User required |  -  |
**401** | Unauthorized |  -  |
**404** | Job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teamjobs_get**
> Dict[str, JobEntry] teamjobs_get(apikey, username, completed=completed)

Returns job information and status for all queued and running jobs for an entire team.

Returns job information and status for all queued and running jobs for an entire team. On success, a JSON payload with job status for each queued or running job (keyed by job number), formatted like the response of /jarvice/status Note: If username does not refer to a team payer, only jobs for that user will be listed

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.job_entry import JobEntry
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate 
    username = 'username_example' # str | Name of user to authenticate
    completed = False # bool | Set to true (case sensitive) to show only completed jobs (optional) (default to False)

    try:
        # Returns job information and status for all queued and running jobs for an entire team.
        api_response = api_instance.teamjobs_get(apikey, username, completed=completed)
        print("The response of StatusAndInformationApi->teamjobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->teamjobs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate  | 
 **username** | **str**| Name of user to authenticate | 
 **completed** | **bool**| Set to true (case sensitive) to show only completed jobs | [optional] [default to False]

### Return type

[**Dict[str, JobEntry]**](JobEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of jobs |  -  |
**400** | Required parameter(s) missing | Invalid parameter(s) |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teamusers_get**
> Dict[str, TeamUser] teamusers_get(apikey, username)

(Team Admins only) Returns a list of JARVICE users who are members of the callers team

(Team Admins only) Returns a list of JARVICE users who are members of the callers team On success, a JSON payload with a list of team members

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.team_user import TeamUser
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate
    username = 'username_example' # str | Name of user to authenticate

    try:
        # (Team Admins only) Returns a list of JARVICE users who are members of the callers team
        api_response = api_instance.teamusers_get(apikey, username)
        print("The response of StatusAndInformationApi->teamusers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->teamusers_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate | 
 **username** | **str**| Name of user to authenticate | 

### Return type

[**Dict[str, TeamUser]**](TeamUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON payload with a list of team members |  -  |
**400** | Required parameter(s) missing | Invalid parameter(s) |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vault_get**
> List[List[str]] vault_get(apikey, username, vault, path, details=details, sort=sort)

List files in a vault.

List files in a vault. On success, a list of lists in application/json format; each element pertains to a file or directory, and includes its name, size, and modification time \"modification time\" (3rd value in each element) is represented in UNIX time (seconds since the Epoch) Additional Notes: 1. Listing is not recursive - only the files in the directory specified by the path parameter are listed 2. Directories are marked with a trailing / character 3. Both size and modification time may be 0 if details is not true 4. Sorting by anything other than name requires details to be set to true 5. Requesting a detailed listing may be significantly slower for certain storage topologies or if listing very large numbers of files; use only if necessary

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatusAndInformationApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate 
    username = 'username_example' # str | Name of user to authenticate
    vault = 'vault_example' # str | Name of vault to list files in
    path = 'path_example' # str | Directory in vault to list files in
    details = False # bool | Include file details such as size and modification time if set to true (optional) (default to False)
    sort = '"n"' # str | either n, s, or m to sort by name, size, or modification time (respectively) in ascending order; use uppercase for reverse sort (optional) (default to '"n"')

    try:
        # List files in a vault.
        api_response = api_instance.vault_get(apikey, username, vault, path, details=details, sort=sort)
        print("The response of StatusAndInformationApi->vault_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusAndInformationApi->vault_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate  | 
 **username** | **str**| Name of user to authenticate | 
 **vault** | **str**| Name of vault to list files in | 
 **path** | **str**| Directory in vault to list files in | 
 **details** | **bool**| Include file details such as size and modification time if set to true | [optional] [default to False]
 **sort** | **str**| either n, s, or m to sort by name, size, or modification time (respectively) in ascending order; use uppercase for reverse sort | [optional] [default to &#39;&quot;n&quot;&#39;]

### Return type

**List[List[str]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File list |  -  |
**400** | Required parameter(s) missing | Invalid parameter(s) |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

