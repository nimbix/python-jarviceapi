# AppDef


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appdefversion** | **int** |  | [optional] 
**author** | **str** |  | [optional] 
**certified** | **bool** |  | [optional] 
**classifications** | **List[str]** |  | [optional] 
**commands** | [**Dict[str, AppDefCmd]**](AppDefCmd.md) |  | [optional] 
**description** | **str** |  | [optional] 
**enablehpc** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**identity** | [**AppDefIdent**](AppDefIdent.md) |  | [optional] 
**image** | [**AppDefImage**](AppDefImage.md) |  | [optional] 
**licensed** | **bool** |  | [optional] 
**machines** | **List[str]** |  | [optional] 
**nae** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**owner** | **str** |  | [optional] 
**price** | **str** | These are not in the JSON, but copied in XXX: Should this be removed? | [optional] 
**public** | **bool** |  | [optional] 
**scale_max** | **int** |  | [optional] 
**team** | **bool** |  | [optional] 
**variables** | [**Dict[str, Variable]**](Variable.md) |  | [optional] 
**vault_types** | **List[str]** |  | [optional] 
**walltime** | **str** |  | [optional] 

## Example

```python
from jarviceapi_client.models.app_def import AppDef

# TODO update the JSON string below
json = "{}"
# create an instance of AppDef from a JSON string
app_def_instance = AppDef.from_json(json)
# print the JSON string representation of the object
print AppDef.to_json()

# convert the object into a dict
app_def_dict = app_def_instance.to_dict()
# create an instance of AppDef from a dict
app_def_form_dict = app_def.from_dict(app_def_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


