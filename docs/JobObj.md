# JobObj


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | **str** |  | [optional] 
**app_owner** | **str** |  | [optional] 
**appdefversion** | **int** |  | [optional] 
**arch** | **str** |  | [optional] 
**cmdargs** | **List[str]** |  | [optional] 
**cmdargtypes** | **List[str]** |  | [optional] 
**cmdscript** | **str** |  | [optional] 
**command_line** | **str** |  | [optional] 
**command_name** | **str** |  | [optional] 
**cores** | **int** |  | [optional] 
**ctrsecret** | **str** |  | [optional] 
**desktop** | **bool** |  | [optional] 
**devices** | **List[str]** |  | [optional] 
**geometry** | **str** |  | [optional] 
**gpus** | **int** |  | [optional] 
**hpc_envs** | **Dict[str, str]** |  | [optional] 
**identity** | [**AppDefIdent**](AppDefIdent.md) |  | [optional] 
**interactive** | **bool** |  | [optional] 
**ipaddr** | **str** |  | [optional] 
**job_label** | **str** |  | [optional] 
**job_project** | **str** |  | [optional] 
**jobtoken** | **str** |  | [optional] 
**licenses** | **str** |  | [optional] 
**machine** | **str** |  | [optional] 
**memlimit** | **int** |  | [optional] 
**mpirun** | **bool** |  | [optional] 
**nae** | **str** |  | [optional] 
**noconnect** | **bool** |  | [optional] 
**nodes** | **int** |  | [optional] 
**nopasssubt** | **bool** | subt is not a typo | [optional] 
**ports** | **List[str]** |  | [optional] 
**privileged** | **bool** |  | [optional] 
**properties** | **List[str]** |  | [optional] 
**publicip** | **bool** |  | [optional] 
**ram** | **int** |  | [optional] 
**repo** | **str** |  | [optional] 
**scratch** | **int** |  | [optional] 
**slave_cores** | **int** |  | [optional] 
**slave_gpus** | **int** |  | [optional] 
**slave_properties** | **List[str]** |  | [optional] 
**slave_ram** | **int** |  | [optional] 
**slave_scratch** | **int** |  | [optional] 
**slots** | **int** |  | [optional] 
**sshpriv** | **str** |  | [optional] 
**sshpub** | **str** |  | [optional] 
**upload** | [**JobUpload**](JobUpload.md) |  | [optional] 
**url** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**variables** | **Dict[str, str]** |  | [optional] 
**variabletypes** | **Dict[str, str]** |  | [optional] 
**vault** | [**JobObjVault**](JobObjVault.md) |  | [optional] 
**verboseinit** | **bool** |  | [optional] 
**vmemlimit** | **int** |  | [optional] 
**walltime** | **str** |  | [optional] 
**webshell** | **bool** |  | [optional] 

## Example

```python
from jarviceapi_client.models.job_obj import JobObj

# TODO update the JSON string below
json = "{}"
# create an instance of JobObj from a JSON string
job_obj_instance = JobObj.from_json(json)
# print the JSON string representation of the object
print JobObj.to_json()

# convert the object into a dict
job_obj_dict = job_obj_instance.to_dict()
# create an instance of JobObj from a dict
job_obj_form_dict = job_obj.from_dict(job_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


