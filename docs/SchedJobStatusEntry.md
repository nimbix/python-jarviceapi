# SchedJobStatusEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_application** | **str** |  | [optional] 
**job_command** | **str** |  | [optional] 
**job_end_time** | **int** |  | [optional] 
**job_name** | **str** |  | [optional] 
**job_project** | **str** |  | [optional] 
**job_start_time** | **int** |  | [optional] 
**job_status** | **str** |  | [optional] 
**job_submit_time** | **int** |  | [optional] 
**job_substatus** | **int** |  | [optional] 
**job_walltime** | **str** |  | [optional] 

## Example

```python
from jarviceapi_client.models.sched_job_status_entry import SchedJobStatusEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SchedJobStatusEntry from a JSON string
sched_job_status_entry_instance = SchedJobStatusEntry.from_json(json)
# print the JSON string representation of the object
print SchedJobStatusEntry.to_json()

# convert the object into a dict
sched_job_status_entry_dict = sched_job_status_entry_instance.to_dict()
# create an instance of SchedJobStatusEntry from a dict
sched_job_status_entry_form_dict = sched_job_status_entry.from_dict(sched_job_status_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


