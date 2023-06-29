# JobEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_address** | **str** |  | [optional] 
**job_after** | **str** |  | [optional] 
**job_api_submission** | [**Submission**](Submission.md) |  | [optional] 
**job_app_discount** | **int** |  | [optional] 
**job_app_price** | **float** |  | [optional] 
**job_application** | **str** |  | [optional] 
**job_billed** | **bool** |  | [optional] 
**job_billing_code** | **int** |  | [optional] 
**job_command** | **str** |  | [optional] 
**job_dashboard_visible** | **int** |  | [optional] 
**job_end_time** | **int** |  | [optional] 
**job_exitcode** | **int** |  | [optional] 
**job_label** | **str** |  | [optional] 
**job_mc_discount** | **int** |  | [optional] 
**job_mc_name** | **str** |  | [optional] 
**job_mc_scale** | **int** |  | [optional] 
**job_name** | **str** |  | [optional] 
**job_nodes** | **str** |  | [optional] 
**job_number** | **int** |  | [optional] 
**job_owner_username** | **str** |  | [optional] 
**job_payer** | **str** |  | [optional] 
**job_price** | **float** |  | [optional] 
**job_sched_id** | **int** |  | [optional] 
**job_sched_job_id** | **str** |  | [optional] 
**job_start_time** | **int** |  | [optional] 
**job_stats** | [**JobStats**](JobStats.md) |  | [optional] 
**job_status** | **str** |  | [optional] 
**job_submit_time** | **int** |  | [optional] 
**job_substatus** | **int** |  | [optional] 
**job_substatus_text** | **str** |  | [optional] 
**job_walltime** | **str** |  | [optional] 

## Example

```python
from jarviceapi_client.models.job_entry import JobEntry

# TODO update the JSON string below
json = "{}"
# create an instance of JobEntry from a JSON string
job_entry_instance = JobEntry.from_json(json)
# print the JSON string representation of the object
print JobEntry.to_json()

# convert the object into a dict
job_entry_dict = job_entry_instance.to_dict()
# create an instance of JobEntry from a dict
job_entry_form_dict = job_entry.from_dict(job_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


