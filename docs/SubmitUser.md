# SubmitUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apikey** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from jarviceapi_client.models.submit_user import SubmitUser

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitUser from a JSON string
submit_user_instance = SubmitUser.from_json(json)
# print the JSON string representation of the object
print SubmitUser.to_json()

# convert the object into a dict
submit_user_dict = submit_user_instance.to_dict()
# create an instance of SubmitUser from a dict
submit_user_form_dict = submit_user.from_dict(submit_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


