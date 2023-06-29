# RuntimeConnect


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from jarviceapi_client.models.runtime_connect import RuntimeConnect

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeConnect from a JSON string
runtime_connect_instance = RuntimeConnect.from_json(json)
# print the JSON string representation of the object
print RuntimeConnect.to_json()

# convert the object into a dict
runtime_connect_dict = runtime_connect_instance.to_dict()
# create an instance of RuntimeConnect from a dict
runtime_connect_form_dict = runtime_connect.from_dict(runtime_connect_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


