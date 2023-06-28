# AppDefIdent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **int** |  | [optional] 
**group** | **str** |  | [optional] 
**uid** | **int** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.app_def_ident import AppDefIdent

# TODO update the JSON string below
json = "{}"
# create an instance of AppDefIdent from a JSON string
app_def_ident_instance = AppDefIdent.from_json(json)
# print the JSON string representation of the object
print AppDefIdent.to_json()

# convert the object into a dict
app_def_ident_dict = app_def_ident_instance.to_dict()
# create an instance of AppDefIdent from a dict
app_def_ident_form_dict = app_def_ident.from_dict(app_def_ident_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


