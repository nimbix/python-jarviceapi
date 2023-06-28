# openapi_client.JobControlApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**action_get**](JobControlApi.md#action_get) | **GET** /jarvice/action | Perform a configured action on your job
[**batch_post**](JobControlApi.md#batch_post) | **POST** /jarvice/batch | Submits a job for processing.
[**shutdown_get**](JobControlApi.md#shutdown_get) | **GET** /jarvice/shutdown | Requests a graceful termination of a job, executing the operating system poweroff mechanism if applicable.
[**signal_get**](JobControlApi.md#signal_get) | **GET** /jarvice/signal | Send a signal to a running job (e.g. SIGTSTP/20).
[**submit_post**](JobControlApi.md#submit_post) | **POST** /jarvice/submit | Submits a job for processing.
[**terminate_get**](JobControlApi.md#terminate_get) | **GET** /jarvice/terminate | Immediately terminates a running job. NB: This will terminate the job regardless of current status.


# **action_get**
> object action_get(apikey, username, action, name=name, number=number)

Perform a configured action on your job

Executes an application-defined command inside a running job. The command runs asynchronously and its standard output/standard error is accessible with /jarvice/tail while the job is running.

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
    api_instance = openapi_client.JobControlApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate
    username = 'username_example' # str | Name of user to authenticate
    action = 'action_example' # str | The name of the action to run (must be a valid action from /jarvice/info)
    name = 'name_example' # str | Job name (name key returned from /jarvice/submit *Must be specifed or number is specified (optional)
    number = 56 # int | Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified (optional)

    try:
        # Perform a configured action on your job
        api_response = api_instance.action_get(apikey, username, action, name=name, number=number)
        print("The response of JobControlApi->action_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobControlApi->action_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate | 
 **username** | **str**| Name of user to authenticate | 
 **action** | **str**| The name of the action to run (must be a valid action from /jarvice/info) | 
 **name** | **str**| Job name (name key returned from /jarvice/submit *Must be specifed or number is specified | [optional] 
 **number** | **int**| Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified | [optional] 

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
**200** | {&#39;status&#39;: &#39;action requested&#39;} |  -  |
**400** | Required parameter(s) missing | No job specified | Bad Request | User required | Invalid parameter(s) |  -  |
**401** | Unauthorized |  -  |
**404** | Job not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_post**
> Dict[str, object] batch_post(var_json)

Submits a job for processing.

Submits a job for processing. The body is in JSON format similar to /jarvice/submit with the addition of the container blob. NOTE: Public containers from DockerHub must include the library/ prefix. e.g. library/ubuntu:latest On success, a JSON payload indicating the job name and job number (with name and number keys). Additional Notes: 1. All boolean values default to false if not specified 2. The nodes parameter in the machine section defaults to 1 if not specified 3. Even if a vault section is specified, password is optional and should only be supplied for encrypted block vaults 4. Even if vault section is specified, vault objects is optional and applies only to object storage vaults; it indicates which objects should be moved into the environments's backing store for processing. If readonly is set to false, JARVICE automatically copies any new or changed objects from the backing store back to the object storage on normal job completion (but not immediate termination with /jarvice/terminate).

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.submission import Submission
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
    api_instance = openapi_client.JobControlApi(api_client)
    var_json = openapi_client.Submission() # Submission | JSON payload to run the compute job, generated as specified above. If copying from the web portal, paste the text into a file or script to use as the JSON payload to submit. Please note that authentication is performed from the username and apikey values in the JSON itself.

    try:
        # Submits a job for processing.
        api_response = api_instance.batch_post(var_json)
        print("The response of JobControlApi->batch_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobControlApi->batch_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_json** | [**Submission**](Submission.md)| JSON payload to run the compute job, generated as specified above. If copying from the web portal, paste the text into a file or script to use as the JSON payload to submit. Please note that authentication is performed from the username and apikey values in the JSON itself. | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON payload indicating the job name and job number |  -  |
**400** | Missing or Malformed API Syntax | Invalid container in request | Container cannot create Application |  -  |
**401** | Not Authorized | Account billing not active |  -  |
**404** | Application Not Found |  -  |
**429** | Only one active job allowed per VM |  -  |
**500** | Error reading bytes | Unable to get user | Unable to create Job Object | Unable to create Job Submission |  -  |
**501** | Failed to access user meta table |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown_get**
> object shutdown_get(apikey, username, name=name, number=number)

Requests a graceful termination of a job, executing the operating system poweroff mechanism if applicable.

Requests a graceful termination of a job, executing the operating system poweroff mechanism if applicable. On success: {\"status\": \"shutdown requested\"} A job not in PROCESSING STARTING status will return an error, e.g. {\"error\": \"Running job is not found\"} Additional Notes: 1. One of name or number must be specified 2. Shutdown is requested asynchronously - job status can be monitored with /jarvice/status 3. Current job status must be PROCESSING STARTING as indicated by output of /jarvice/status, e.g. {\"job_status\": \"PROCESSING STARTING\"}. For other states, see /jarvice/terminate

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
    api_instance = openapi_client.JobControlApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate
    username = 'username_example' # str | Name of user to authenticate
    name = 'name_example' # str | Job name (name key returned from /jarvice/submit *Must be specifed or number is specified (optional)
    number = 56 # int | Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified (optional)

    try:
        # Requests a graceful termination of a job, executing the operating system poweroff mechanism if applicable.
        api_response = api_instance.shutdown_get(apikey, username, name=name, number=number)
        print("The response of JobControlApi->shutdown_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobControlApi->shutdown_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate | 
 **username** | **str**| Name of user to authenticate | 
 **name** | **str**| Job name (name key returned from /jarvice/submit *Must be specifed or number is specified | [optional] 
 **number** | **int**| Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified | [optional] 

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
**200** | {&#39;status&#39;: &#39;shutdown requested&#39;} |  -  |
**400** | Required parameter(s) missing | No job specified | Bad Request | User required |  -  |
**401** | Unauthorized |  -  |
**404** | {&#39;error&#39;: &#39;Not found&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signal_get**
> object signal_get(apikey, username, name=name, number=number, signal=signal)

Send a signal to a running job (e.g. SIGTSTP/20).

Send a signal to a running job (e.g. SIGTSTP/20). On success: {\"signal\": <signal>, \"pid\": <pid>} Where pid is the process that receives the signal. Additional Notes: 1. One of name or number must be specified 2. signal must use the integer representation for the signal 3. /jarvice/signal will set the substatus 'Suspended by user' which is updated on the JARVICE Dashboard. This substatus is cleared by signaling SIGCONT/18. Processes that ignore SIGTSTP are not suspended even if the job substatus is set to 'Suspended by user' 4. JarviceXE applications can override signal behavior by setting JARVICE_SIGNAL_OVERRIDE environment variable to a custom script to handle signals sent to the application from the JARVICE API. (see example Dockerfile using ENV to set JARVICE_SIGNAL_OVERRIDE and override script)

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
    api_instance = openapi_client.JobControlApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate
    username = 'username_example' # str | Name of user to authenticate
    name = 'name_example' # str | Job name (name key returned from /jarvice/submit *Must be specifed or number is specified (optional)
    number = 56 # int | Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified (optional)
    signal = 20 # int | Signal to send to job (optional) (default to 20)

    try:
        # Send a signal to a running job (e.g. SIGTSTP/20).
        api_response = api_instance.signal_get(apikey, username, name=name, number=number, signal=signal)
        print("The response of JobControlApi->signal_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobControlApi->signal_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate | 
 **username** | **str**| Name of user to authenticate | 
 **name** | **str**| Job name (name key returned from /jarvice/submit *Must be specifed or number is specified | [optional] 
 **number** | **int**| Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified | [optional] 
 **signal** | **int**| Signal to send to job | [optional] [default to 20]

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
**200** | {&#39;signal&#39;: &lt;signal&gt;, &#39;pid&#39;: &lt;pid&gt;} |  -  |
**400** | Required parameter(s) missing | No job specified | Bad Request | User required |  -  |
**401** | Unauthorized |  -  |
**404** | {&#39;error&#39;: &#39;Not found&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_post**
> Dict[str, object] submit_post(var_json)

Submits a job for processing.

Submits a job for processing. The body is in JSON format and can be generated from the JARVICE web portal by clicking the PREVIEW SUBMISSION tab in the task builder and copying its contents to the clipboard. Click the copy icon above the SUBMIT button to copy the contents of the API call to the clipboard. NOTE: Adding the identity object in the submission json will replace the NIMBIX Application Environment nimbix user. The JARVICE API cannot override an identity set by an AppDef file. On success, a JSON payload indicating the job name and job number (with name and number keys). Additional Notes: 1. All boolean values default to false if not specified 2. The nodes parameter in the machine section defaults to 1 if not specified 3. Even if a vault section is specified, password is optional and should only be supplied for encrypted block vaults 4. Even if vault section is specified, vault objects is optional and applies only to object storage vaults; it indicates which objects should be moved into the environments's backing store for processing. If readonly is set to false, JARVICE automatically copies any new or changed objects from the backing store back to the object storage on normal job completion (but not immediate termination with /jarvice/terminate). 5. ipaddr will be validated by the underlying platform for authorization for the user; it may also fail if the address is already assigned (but this won't be known until the job starts running).

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.job_obj import JobObj
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
    api_instance = openapi_client.JobControlApi(api_client)
    var_json = openapi_client.JobObj() # JobObj | JSON payload to run the compute job, generated as specified above. If copying from the web portal, paste the text into a file or script to use as the JSON payload to submit. Please note that authentication is performed from the username and apikey values in the JSON itself.

    try:
        # Submits a job for processing.
        api_response = api_instance.submit_post(var_json)
        print("The response of JobControlApi->submit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobControlApi->submit_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_json** | [**JobObj**](JobObj.md)| JSON payload to run the compute job, generated as specified above. If copying from the web portal, paste the text into a file or script to use as the JSON payload to submit. Please note that authentication is performed from the username and apikey values in the JSON itself. | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JSON payload indicating the job name and job number |  -  |
**400** | Missing or Malformed API Syntax | Container cannot create Application |  -  |
**401** | Not Authorized | Account billing not active |  -  |
**404** | Application Not Found |  -  |
**429** | Only one active job allowed per VM |  -  |
**500** | Error reading bytes | Unable to get user | Unable to create Job Object | Unable to create Job Submission |  -  |
**501** | Failed to access user meta table |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_get**
> Dict[str, object] terminate_get(apikey, username, name=name, number=number)

Immediately terminates a running job. NB: This will terminate the job regardless of current status.

Immediately terminates a running job. NB: This will terminate the job regardless of current status. Best Practice: Use the /jarvice/shutdown for a job in PROCESSING STARTING state and only use /jarvice/terminate for a job not in a PROCESSING STARTING state or not responding to a /jarvice/shutdown. On success: {\"status\": \"terminated\"} A job not in PROCESSING STARTING status will return an error, e.g. {\"error\": \"Running job is not found\"} Notes: One of name or number must be specified

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
    api_instance = openapi_client.JobControlApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate
    username = 'username_example' # str | Name of user to authenticate
    name = 'name_example' # str | Job name (name key returned from /jarvice/submit *Must be specifed or number is specified (optional)
    number = 56 # int | Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified (optional)

    try:
        # Immediately terminates a running job. NB: This will terminate the job regardless of current status.
        api_response = api_instance.terminate_get(apikey, username, name=name, number=number)
        print("The response of JobControlApi->terminate_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobControlApi->terminate_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate | 
 **username** | **str**| Name of user to authenticate | 
 **name** | **str**| Job name (name key returned from /jarvice/submit *Must be specifed or number is specified | [optional] 
 **number** | **int**| Job number (number key returned from /jarvice/submit) *Must be specifed or name is specified | [optional] 

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
**200** | {&#39;status&#39;: &#39;shutdown requested&#39;} |  -  |
**400** | Required parameter(s) missing | No job specified | Bad Request | User required |  -  |
**401** | Unauthorized |  -  |
**404** | {&#39;error&#39;: &#39;Not found&#39;} |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

