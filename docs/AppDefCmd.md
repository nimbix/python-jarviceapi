# AppDefCmd


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmdscript** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**desktop** | **bool** |  | [optional] 
**interactive** | **bool** |  | [optional] 
**machines** | **List[str]** |  | [optional] 
**mpirun** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**noconnect** | **bool** |  | [optional] 
**noqueue** | **bool** |  | [optional] 
**parameters** | [**Dict[str, ParDef]**](ParDef.md) |  | [optional] 
**path** | **str** |  | [optional] 
**ports** | **List[str]** |  | [optional] 
**publicip** | **bool** |  | [optional] 
**scale_max** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**variables** | [**Dict[str, Variable]**](Variable.md) |  | [optional] 
**verboseinit** | **bool** |  | [optional] 
**walltime** | **str** |  | [optional] 
**webshell** | **bool** |  | [optional] 

## Example

```python
from jarviceapi_client.models.app_def_cmd import AppDefCmd

# TODO update the JSON string below
json = "{}"
# create an instance of AppDefCmd from a JSON string
app_def_cmd_instance = AppDefCmd.from_json(json)
# print the JSON string representation of the object
print AppDefCmd.to_json()

# convert the object into a dict
app_def_cmd_dict = app_def_cmd_instance.to_dict()
# create an instance of AppDefCmd from a dict
app_def_cmd_form_dict = app_def_cmd.from_dict(app_def_cmd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


