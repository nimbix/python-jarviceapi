# Submission


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | **str** |  | [optional] 
**application** | [**Application**](Application.md) |  | [optional] 
**container** | [**Container**](Container.md) |  | [optional] 
**gen_sshkey** | **bool** |  | [optional] 
**hpc** | [**HpcReq**](HpcReq.md) |  | [optional] 
**identity** | [**AppDefIdent**](AppDefIdent.md) |  | [optional] 
**job_label** | **str** |  | [optional] 
**job_project** | **str** |  | [optional] 
**jobsub** | **str** |  | [optional] 
**licenses** | **str** |  | [optional] 
**machine** | [**Machine**](Machine.md) |  | [optional] 
**nopasssubt** | **bool** | subt is not a typo | [optional] 
**public_ip** | **bool** |  | [optional] 
**queue** | **str** |  | [optional] 
**test_comment** | **str** | Remove later | [optional] 
**user** | [**SubmitUser**](SubmitUser.md) |  | [optional] 
**vault** | [**Vault**](Vault.md) |  | [optional] 

## Example

```python
from openapi_client.models.submission import Submission

# TODO update the JSON string below
json = "{}"
# create an instance of Submission from a JSON string
submission_instance = Submission.from_json(json)
# print the JSON string representation of the object
print Submission.to_json()

# convert the object into a dict
submission_dict = submission_instance.to_dict()
# create an instance of Submission from a dict
submission_form_dict = submission.from_dict(submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


