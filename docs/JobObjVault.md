# JobObjVault


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**force** | **bool** |  | [optional] 
**var_global** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**ro** | **bool** |  | [optional] 

## Example

```python
from jarviceapi_client.models.job_obj_vault import JobObjVault

# TODO update the JSON string below
json = "{}"
# create an instance of JobObjVault from a JSON string
job_obj_vault_instance = JobObjVault.from_json(json)
# print the JSON string representation of the object
print JobObjVault.to_json()

# convert the object into a dict
job_obj_vault_dict = job_obj_vault_instance.to_dict()
# create an instance of JobObjVault from a dict
job_obj_vault_form_dict = job_obj_vault.from_dict(job_obj_vault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


