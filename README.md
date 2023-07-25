# jarviceapi-client
The JARVICE API allows full control on running jobs as well as managing applications via PushToCompute™.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0.13
- Build package: org.openapitools.codegen.languages.PythonNextgenClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/nimbix/python-jarviceapi.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/nimbix/python-jarviceapi.git`)

Then import the package:
```python
import jarviceapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import jarviceapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
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
    api_instance = jarviceapi_client.JobControlApi(api_client)
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
    except ApiException as e:
        print("Exception when calling JobControlApi->action_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*JobControlApi* | [**action_get**](docs\JobControlApi.md#action_get) | **GET** /jarvice/action | Perform a configured action on your job
*JobControlApi* | [**batch_post**](docs\JobControlApi.md#batch_post) | **POST** /jarvice/batch | Submits a job for processing.
*JobControlApi* | [**shutdown_get**](docs\JobControlApi.md#shutdown_get) | **GET** /jarvice/shutdown | Requests a graceful termination of a job, executing the operating system poweroff mechanism if applicable.
*JobControlApi* | [**signal_get**](docs\JobControlApi.md#signal_get) | **GET** /jarvice/signal | Send a signal to a running job (e.g. SIGTSTP/20).
*JobControlApi* | [**submit_post**](docs\JobControlApi.md#submit_post) | **POST** /jarvice/submit | Submits a job for processing.
*JobControlApi* | [**terminate_get**](docs\JobControlApi.md#terminate_get) | **GET** /jarvice/terminate | Immediately terminates a running job. NB: This will terminate the job regardless of current status.
*PushToComputeApi* | [**build_get**](docs\PushToComputeApi.md#build_get) | **GET** /jarvice/build | Builds a JARVICE application image for a Docker repository. The JARVICE application ID must already exist.
*PushToComputeApi* | [**history_get**](docs\PushToComputeApi.md#history_get) | **GET** /jarvice/history | Retrieve build/pull history for a JARVICE application image.
*PushToComputeApi* | [**pull_get**](docs\PushToComputeApi.md#pull_get) | **GET** /jarvice/pull | Pulls a Docker repository into a JARVICE application image. The JARVICE application image must already exist.
*PushToComputeApi* | [**validate_post**](docs\PushToComputeApi.md#validate_post) | **POST** /jarvice/validate | Validates an AppDef (application definition).
*StatusAndInformationApi* | [**appdef_get**](docs\StatusAndInformationApi.md#appdef_get) | **GET** /jarvice/appdef | Returns the Application Definition (AppDef) for a given application.
*StatusAndInformationApi* | [**apps_get**](docs\StatusAndInformationApi.md#apps_get) | **GET** /jarvice/apps | Returns the Application Definition (AppDef) for a given application.
*StatusAndInformationApi* | [**billing_get**](docs\StatusAndInformationApi.md#billing_get) | **GET** /jarvice/billing | (JXE/System Admins only) Returns billing report for JARVICE users
*StatusAndInformationApi* | [**connect_get**](docs\StatusAndInformationApi.md#connect_get) | **GET** /jarvice/connect | Requests the network address and user nimbix password (if set), for an interactive job.
*StatusAndInformationApi* | [**events_get**](docs\StatusAndInformationApi.md#events_get) | **GET** /jarvice/events | (JXE/System Admins only) Retrieves event logs for a running job that are related to the cluster infrastructure
*StatusAndInformationApi* | [**info_get**](docs\StatusAndInformationApi.md#info_get) | **GET** /jarvice/info | Get info from job
*StatusAndInformationApi* | [**jobs_get**](docs\StatusAndInformationApi.md#jobs_get) | **GET** /jarvice/jobs | Returns job information and status for all queued and running jobs.
*StatusAndInformationApi* | [**license_get**](docs\StatusAndInformationApi.md#license_get) | **GET** /jarvice/license | (JXE/System Admins only) Retrieves Jarvice license
*StatusAndInformationApi* | [**live_get**](docs\StatusAndInformationApi.md#live_get) | **GET** /jarvice/live | Get info is API is alive
*StatusAndInformationApi* | [**machines_get**](docs\StatusAndInformationApi.md#machines_get) | **GET** /jarvice/machines | Returns information about available machine type(s).
*StatusAndInformationApi* | [**metrics_get**](docs\StatusAndInformationApi.md#metrics_get) | **GET** /jarvice/metrics | Returns the last known CPU and memory utilization metrics for a given job.
*StatusAndInformationApi* | [**output_get**](docs\StatusAndInformationApi.md#output_get) | **GET** /jarvice/output | Returns a tail (or optionally all) of the output of a completed job.
*StatusAndInformationApi* | [**projects_get**](docs\StatusAndInformationApi.md#projects_get) | **GET** /jarvice/projects | (JXE/System Admins only) Returns all JARVICE projects and members
*StatusAndInformationApi* | [**queues_get**](docs\StatusAndInformationApi.md#queues_get) | **GET** /jarvice/queues | (JXE only) Returns information about available queue(s).
*StatusAndInformationApi* | [**ready_get**](docs\StatusAndInformationApi.md#ready_get) | **GET** /jarvice/ready | Get info if DAL is ready
*StatusAndInformationApi* | [**screenshot_get**](docs\StatusAndInformationApi.md#screenshot_get) | **GET** /jarvice/screenshot | Returns a screenshot for a running job (if it is graphical).
*StatusAndInformationApi* | [**status_get**](docs\StatusAndInformationApi.md#status_get) | **GET** /jarvice/status | Queries status for a previously submitted job.
*StatusAndInformationApi* | [**tail_get**](docs\StatusAndInformationApi.md#tail_get) | **GET** /jarvice/tail | Returns a tail (or optionally all) of the output of a completed job.
*StatusAndInformationApi* | [**teamjobs_get**](docs\StatusAndInformationApi.md#teamjobs_get) | **GET** /jarvice/teamjobs | Returns job information and status for all queued and running jobs for an entire team.
*StatusAndInformationApi* | [**teamusers_get**](docs\StatusAndInformationApi.md#teamusers_get) | **GET** /jarvice/teamusers | (Team Admins only) Returns a list of JARVICE users who are members of the callers team
*StatusAndInformationApi* | [**vault_get**](docs\StatusAndInformationApi.md#vault_get) | **GET** /jarvice/vault | List files in a vault.


## Documentation For Models

 - [App](docs\App.md)
 - [AppDef](docs\AppDef.md)
 - [AppDefCmd](docs\AppDefCmd.md)
 - [AppDefIdent](docs\AppDefIdent.md)
 - [AppDefImage](docs\AppDefImage.md)
 - [Application](docs\Application.md)
 - [Container](docs\Container.md)
 - [HpcReq](docs\HpcReq.md)
 - [JobEntry](docs\JobEntry.md)
 - [JobStats](docs\JobStats.md)
 - [Machine](docs\Machine.md)
 - [MachineDef](docs\MachineDef.md)
 - [ParDef](docs\ParDef.md)
 - [Queue](docs\Queue.md)
 - [RTMetricsItemized](docs\RTMetricsItemized.md)
 - [RTMetricsSummary](docs\RTMetricsSummary.md)
 - [RuntimeConnect](docs\RuntimeConnect.md)
 - [RuntimeInfo](docs\RuntimeInfo.md)
 - [RuntimeMetrics](docs\RuntimeMetrics.md)
 - [SchedJobStatusEntry](docs\SchedJobStatusEntry.md)
 - [Submission](docs\Submission.md)
 - [SubmitUser](docs\SubmitUser.md)
 - [TeamUser](docs\TeamUser.md)
 - [Variable](docs\Variable.md)
 - [Vault](docs\Vault.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

support@nimbix.net


