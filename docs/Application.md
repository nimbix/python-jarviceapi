# Application


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** |  | [optional] 
**geometry** | **str** |  | [optional] 
**ipaddr** | **str** |  | [optional] 
**nosubmit** | **bool** | If this is set, then the API server just returns the jobobj rather than send it to the scheduler. Development mode python API does the same This only applies if JARVICE_API_LOG_ENABLE environment var is set | [optional] 
**parameters** | **object** |  | [optional] 
**walltime** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.application import Application

# TODO update the JSON string below
json = "{}"
# create an instance of Application from a JSON string
application_instance = Application.from_json(json)
# print the JSON string representation of the object
print Application.to_json()

# convert the object into a dict
application_dict = application_instance.to_dict()
# create an instance of Application from a dict
application_form_dict = application.from_dict(application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


