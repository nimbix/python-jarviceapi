# RTMetricsItemized


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_used** | **List[int]** |  | [optional] 
**memory_total** | **List[int]** |  | [optional] 
**memory_used** | **List[int]** |  | [optional] 

## Example

```python
from openapi_client.models.rt_metrics_itemized import RTMetricsItemized

# TODO update the JSON string below
json = "{}"
# create an instance of RTMetricsItemized from a JSON string
rt_metrics_itemized_instance = RTMetricsItemized.from_json(json)
# print the JSON string representation of the object
print RTMetricsItemized.to_json()

# convert the object into a dict
rt_metrics_itemized_dict = rt_metrics_itemized_instance.to_dict()
# create an instance of RTMetricsItemized from a dict
rt_metrics_itemized_form_dict = rt_metrics_itemized.from_dict(rt_metrics_itemized_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


