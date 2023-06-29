# TeamUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from jarviceapi_client.models.team_user import TeamUser

# TODO update the JSON string below
json = "{}"
# create an instance of TeamUser from a JSON string
team_user_instance = TeamUser.from_json(json)
# print the JSON string representation of the object
print TeamUser.to_json()

# convert the object into a dict
team_user_dict = team_user_instance.to_dict()
# create an instance of TeamUser from a dict
team_user_form_dict = team_user.from_dict(team_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


