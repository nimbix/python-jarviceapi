# RTMetricsSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_used** | **int** |  | [optional] 
**memory_total** | **int** |  | [optional] 
**memory_used** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.rt_metrics_summary import RTMetricsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of RTMetricsSummary from a JSON string
rt_metrics_summary_instance = RTMetricsSummary.from_json(json)
# print the JSON string representation of the object
print RTMetricsSummary.to_json()

# convert the object into a dict
rt_metrics_summary_dict = rt_metrics_summary_instance.to_dict()
# create an instance of RTMetricsSummary from a dict
rt_metrics_summary_form_dict = rt_metrics_summary.from_dict(rt_metrics_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


