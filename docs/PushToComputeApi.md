# jarviceapi_client.PushToComputeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_get**](PushToComputeApi.md#build_get) | **GET** /jarvice/build | Builds a JARVICE application image for a Docker repository. The JARVICE application ID must already exist.
[**history_get**](PushToComputeApi.md#history_get) | **GET** /jarvice/history | Retrieve build/pull history for a JARVICE application image.
[**pull_get**](PushToComputeApi.md#pull_get) | **GET** /jarvice/pull | Pulls a Docker repository into a JARVICE application image. The JARVICE application image must already exist.
[**validate_post**](PushToComputeApi.md#validate_post) | **POST** /jarvice/validate | Validates an AppDef (application definition).


# **build_get**
> object build_get(apikey, username, target, pull=pull, abort=abort)

Builds a JARVICE application image for a Docker repository. The JARVICE application ID must already exist.

Builds a JARVICE application image for a Docker repository. The JARVICE application ID must already exist. Additional Notes : 1. You will receive a notification once the build starts and completes, either with or without error, per your account's notification preferences 2. If abort is specified, any running build is aborted immediately; if not, a build is scheduled; note that scheduling a build with one already running results in failure 3. abort does not automatically schedule a new build - it merely changes the meaning of this endpoint from schedule to abort build

### Example

```python
import time
import os
import jarviceapi_client
from jarviceapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jarviceapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with jarviceapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jarviceapi_client.PushToComputeApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate 
    username = 'username_example' # str | Name of user to authenticate
    target = 'target_example' # str | Target application ID to build an image for (must exist)
    pull = False # bool | On successful build, pull Docker repository into a JARVICE application image (optional) (default to False)
    abort = False # bool | Abort a running image build  (optional) (default to False)

    try:
        # Builds a JARVICE application image for a Docker repository. The JARVICE application ID must already exist.
        api_response = api_instance.build_get(apikey, username, target, pull=pull, abort=abort)
        print("The response of PushToComputeApi->build_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushToComputeApi->build_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate  | 
 **username** | **str**| Name of user to authenticate | 
 **target** | **str**| Target application ID to build an image for (must exist) | 
 **pull** | **bool**| On successful build, pull Docker repository into a JARVICE application image | [optional] [default to False]
 **abort** | **bool**| Abort a running image build  | [optional] [default to False]

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
**200** | A JSON payload with the status message in the status key. |  -  |
**400** | Required parameter(s) missing | Invalid parameter(s) |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **history_get**
> str history_get(apikey, username, target, limit=limit, reltime=reltime)

Retrieve build/pull history for a JARVICE application image.

Retrieve build/pull history for a JARVICE application image. On success, the requested reverse chronological history (most recent first) in text/plain format (with single \\n for line breaks), up to and including the limit requested. Blank output indicates either the target does not exist, or has no associated build/pull history (yet).

### Example

```python
import time
import os
import jarviceapi_client
from jarviceapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jarviceapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with jarviceapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jarviceapi_client.PushToComputeApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate 
    username = 'username_example' # str | Name of user to authenticate
    target = 'target_example' # str | Target image name to get history for (usually same as the application ID)
    limit = 100 # int | The number of entries to limit the output to (optional) (default to 100)
    reltime = True # bool | True : Use relative timestamps - False : Use absolute timestamps (optional) (default to True)

    try:
        # Retrieve build/pull history for a JARVICE application image.
        api_response = api_instance.history_get(apikey, username, target, limit=limit, reltime=reltime)
        print("The response of PushToComputeApi->history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushToComputeApi->history_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate  | 
 **username** | **str**| Name of user to authenticate | 
 **target** | **str**| Target image name to get history for (usually same as the application ID) | 
 **limit** | **int**| The number of entries to limit the output to | [optional] [default to 100]
 **reltime** | **bool**| True : Use relative timestamps - False : Use absolute timestamps | [optional] [default to True]

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
**200** | Chronological history |  -  |
**400** | Required parameter(s) missing | Invalid parameter(s) |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pull_get**
> object pull_get(apikey, username, repo, target)

Pulls a Docker repository into a JARVICE application image. The JARVICE application image must already exist.

Pulls a Docker repository into a JARVICE application image. The JARVICE application image must already exist. Additional Notes : 1. You will receive a notification once the pull starts and completes, either with or without error, per your account's notification preferences 2. repo uses the same syntax as the docker pull does 3. If pulling a private repository, you must log into the Docker registry in the JARVICE portal from the PushToCompute™ page first

### Example

```python
import time
import os
import jarviceapi_client
from jarviceapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jarviceapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with jarviceapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jarviceapi_client.PushToComputeApi(api_client)
    apikey = 'apikey_example' # str | API key for user to authenticate 
    username = 'username_example' # str | Name of user to authenticate
    repo = 'repo_example' # str | Docker repository to pull from
    target = 'target_example' # str | Target application ID to build an image for (must exist)

    try:
        # Pulls a Docker repository into a JARVICE application image. The JARVICE application image must already exist.
        api_response = api_instance.pull_get(apikey, username, repo, target)
        print("The response of PushToComputeApi->pull_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushToComputeApi->pull_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apikey** | **str**| API key for user to authenticate  | 
 **username** | **str**| Name of user to authenticate | 
 **repo** | **str**| Docker repository to pull from | 
 **target** | **str**| Target application ID to build an image for (must exist) | 

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
**200** | A JSON payload with the status message in the status key. {&#39;status&#39;: &#39;Pull successfully scheduled&#39;} |  -  |
**400** | Required parameter(s) missing | Invalid parameter(s) |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_post**
> object validate_post(var_json)

Validates an AppDef (application definition).

Validates an AppDef (application definition). A valid AppDef can be used to customize the user interface endpoints for an application, as well as descriptive metadata. Response: A JSON payload with the boolean status in the valid key if successful, or a 400 error with a descriptive message on failure. Notes: Validation is done in a single pass and may not pinpoint the exact location of the error in every case

### Example

```python
import time
import os
import jarviceapi_client
from jarviceapi_client.models.app_def import AppDef
from jarviceapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jarviceapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with jarviceapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jarviceapi_client.PushToComputeApi(api_client)
    var_json = jarviceapi_client.AppDef() # AppDef | JSON payload containing an AppDef (application definition) to validate. Please see the Application Definition Guide for details on the format. A valid AppDef can be used to customize the user interface endpoints for an application, as well as descriptive metadata.

    try:
        # Validates an AppDef (application definition).
        api_response = api_instance.validate_post(var_json)
        print("The response of PushToComputeApi->validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PushToComputeApi->validate_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_json** | [**AppDef**](AppDef.md)| JSON payload containing an AppDef (application definition) to validate. Please see the Application Definition Guide for details on the format. A valid AppDef can be used to customize the user interface endpoints for an application, as well as descriptive metadata. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | {&#39;valid&#39;: true} |  -  |
**400** | Error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

