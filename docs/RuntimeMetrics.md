# RuntimeMetrics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**itemized** | [**RTMetricsItemized**](RTMetricsItemized.md) |  | [optional] 
**summary** | [**RTMetricsSummary**](RTMetricsSummary.md) |  | [optional] 

## Example

```python
from jarviceapi_client.models.runtime_metrics import RuntimeMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeMetrics from a JSON string
runtime_metrics_instance = RuntimeMetrics.from_json(json)
# print the JSON string representation of the object
print RuntimeMetrics.to_json()

# convert the object into a dict
runtime_metrics_dict = runtime_metrics_instance.to_dict()
# create an instance of RuntimeMetrics from a dict
runtime_metrics_form_dict = runtime_metrics.from_dict(runtime_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


