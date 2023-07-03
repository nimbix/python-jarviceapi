# MachineDef


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mc_arch** | **str** |  | [optional] 
**mc_cores** | **int** |  | [optional] 
**mc_description** | **str** |  | [optional] 
**mc_devices** | **str** |  | [optional] 
**mc_gpus** | **int** |  | [optional] 
**mc_lesser** | **int** |  | [optional] 
**mc_max_concurrent** | **int** |  | [optional] 
**mc_name** | **str** |  | [optional] 
**mc_price** | **float** |  | [optional] 
**mc_priority** | **int** |  | [optional] 
**mc_privs** | **List[str]** |  | [optional] 
**mc_properties** | **str** |  | [optional] 
**mc_ram** | **int** |  | [optional] 
**mc_scale_max** | **int** |  | [optional] 
**mc_scale_min** | **int** |  | [optional] 
**mc_scale_select** | **str** |  | [optional] 
**mc_sched_id** | **int** |  | [optional] 
**mc_scratch** | **int** |  | [optional] 
**mc_slave_cores** | **int** |  | [optional] 
**mc_slave_gpus** | **int** |  | [optional] 
**mc_slave_properties** | **str** |  | [optional] 
**mc_slave_ram** | **int** |  | [optional] 
**mc_slots** | **int** |  | [optional] 
**mc_swap** | **int** |  | [optional] 

## Example

```python
from jarviceapi_client.models.machine_def import MachineDef

# TODO update the JSON string below
json = "{}"
# create an instance of MachineDef from a JSON string
machine_def_instance = MachineDef.from_json(json)
# print the JSON string representation of the object
print MachineDef.to_json()

# convert the object into a dict
machine_def_dict = machine_def_instance.to_dict()
# create an instance of MachineDef from a dict
machine_def_form_dict = machine_def.from_dict(machine_def_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


