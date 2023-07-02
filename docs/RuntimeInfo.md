# RuntimeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**about** | **str** |  | [optional] 
**actions** | **Dict[str, Dict]** |  | [optional] 
**address** | **str** |  | [optional] 
**help** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from jarviceapi_client.models.runtime_info import RuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeInfo from a JSON string
runtime_info_instance = RuntimeInfo.from_json(json)
# print the JSON string representation of the object
print RuntimeInfo.to_json()

# convert the object into a dict
runtime_info_dict = runtime_info_instance.to_dict()
# create an instance of RuntimeInfo from a dict
runtime_info_form_dict = runtime_info.from_dict(runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


