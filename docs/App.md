# App


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
from jarviceapi_client.models.app import App

# TODO update the JSON string below
json = "{}"
# create an instance of App from a JSON string
app_instance = App.from_json(json)
# print the JSON string representation of the object
print App.to_json()

# convert the object into a dict
app_dict = app_instance.to_dict()
# create an instance of App from a dict
app_form_dict = app.from_dict(app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


