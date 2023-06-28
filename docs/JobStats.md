# JobStats


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_cost** | **float** |  | [optional] 
**compute_cost** | **float** |  | [optional] 
**compute_time** | **int** |  | [optional] 
**job_count** | **int** |  | [optional] 
**queue_time** | **int** |  | [optional] 
**wall_time** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.job_stats import JobStats

# TODO update the JSON string below
json = "{}"
# create an instance of JobStats from a JSON string
job_stats_instance = JobStats.from_json(json)
# print the JSON string representation of the object
print JobStats.to_json()

# convert the object into a dict
job_stats_dict = job_stats_instance.to_dict()
# create an instance of JobStats from a dict
job_stats_form_dict = job_stats.from_dict(job_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


