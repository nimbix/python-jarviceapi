# Apps


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** |  | [optional] 
**data** | [**AppDef**](AppDef.md) |  | [optional] 
**owner** | **float** |  | [optional] 
**arch** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**privs** | **List[str]** |  | [optional] 
**src** | **str** |  | [optional] 
**updated** | **int** |  | [optional] 
**checkedout** | **bool** |  | [optional] 
**certified** | **bool** |  | [optional] 
**walltime** | **str** |  | [optional] 
**repo** | **str** |  | [optional] 

## Example

```python
from jarviceapi_client.models.apps import Apps

# TODO update the JSON string below
json = "{}"
# create an instance of Apps from a JSON string
apps_instance = Apps.from_json(json)
# print the JSON string representation of the object
print Apps.to_json()

# convert the object into a dict
apps_dict = apps_instance.to_dict()
# create an instance of Apps from a dict
apps_form_dict = apps.from_dict(apps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


