# Vault


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** |  | [optional] 
**confirm** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**force** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**objects** | **List[str]** |  | [optional] 
**password** | **str** |  | [optional] 
**readonly** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.vault import Vault

# TODO update the JSON string below
json = "{}"
# create an instance of Vault from a JSON string
vault_instance = Vault.from_json(json)
# print the JSON string representation of the object
print Vault.to_json()

# convert the object into a dict
vault_dict = vault_instance.to_dict()
# create an instance of Vault from a dict
vault_form_dict = vault.from_dict(vault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


