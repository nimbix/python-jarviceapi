# Container


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** |  | [optional] 
**interactive** | **bool** |  | [optional] 
**jobscript** | **str** |  | [optional] 
**pullsecret** | **str** |  | [optional] 

## Example

```python
from jarviceapi_client.models.container import Container

# TODO update the JSON string below
json = "{}"
# create an instance of Container from a JSON string
container_instance = Container.from_json(json)
# print the JSON string representation of the object
print Container.to_json()

# convert the object into a dict
container_dict = container_instance.to_dict()
# create an instance of Container from a dict
container_form_dict = container.from_dict(container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


