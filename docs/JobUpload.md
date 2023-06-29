# JobUpload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**target** | **str** |  | [optional] 

## Example

```python
from jarviceapi_client.models.job_upload import JobUpload

# TODO update the JSON string below
json = "{}"
# create an instance of JobUpload from a JSON string
job_upload_instance = JobUpload.from_json(json)
# print the JSON string representation of the object
print JobUpload.to_json()

# convert the object into a dict
job_upload_dict = job_upload_instance.to_dict()
# create an instance of JobUpload from a dict
job_upload_form_dict = job_upload.from_dict(job_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


