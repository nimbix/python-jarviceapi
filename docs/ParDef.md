# ParDef


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cmdscript** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**filter** | **str** |  | [optional] 
**var_if** | **List[str]** |  | [optional] 
**ifnot** | **List[str]** |  | [optional] 
**max** | **object** |  | [optional] 
**min** | **object** |  | [optional] 
**mvalues** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**positional** | **bool** |  | [optional] 
**required** | **bool** |  | [optional] 
**size** | **str** |  | [optional] 
**step** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **object** |  | [optional] 
**values** | **List[str]** |  | [optional] 
**variable** | **bool** |  | [optional] 

## Example

```python
from jarviceapi_client.models.par_def import ParDef

# TODO update the JSON string below
json = "{}"
# create an instance of ParDef from a JSON string
par_def_instance = ParDef.from_json(json)
# print the JSON string representation of the object
print ParDef.to_json()

# convert the object into a dict
par_def_dict = par_def_instance.to_dict()
# create an instance of ParDef from a dict
par_def_form_dict = par_def.from_dict(par_def_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


