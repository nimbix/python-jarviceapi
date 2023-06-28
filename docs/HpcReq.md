# HpcReq


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hpc_envs** | **Dict[str, str]** |  | [optional] 
**hpc_job_env_config** | **str** |  | [optional] 
**hpc_job_script** | **str** |  | [optional] 
**hpc_job_shell** | **str** |  | [optional] 
**hpc_queue** | **str** |  | [optional] 
**hpc_resources** | **Dict[str, str]** |  | [optional] 
**hpc_umask** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.hpc_req import HpcReq

# TODO update the JSON string below
json = "{}"
# create an instance of HpcReq from a JSON string
hpc_req_instance = HpcReq.from_json(json)
# print the JSON string representation of the object
print HpcReq.to_json()

# convert the object into a dict
hpc_req_dict = hpc_req_instance.to_dict()
# create an instance of HpcReq from a dict
hpc_req_form_dict = hpc_req.from_dict(hpc_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


