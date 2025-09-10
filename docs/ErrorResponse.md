# ErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | 
**title** | **str** | Short, human-readable summary | 
**detail** | **str** | Human-readable explanation | 
**type** | **str** | URI reference for error type | [optional] [default to 'about:blank']
**instance** | **str** | URI reference for specific occurrence | [optional] 
**errors** | [**List[ErrorDetail]**](ErrorDetail.md) | Field-specific validation errors | [optional] 
**timestamp** | **datetime** | ISO 8601 timestamp | 
**request_id** | **str** | Unique request identifier | 

## Example

```python
from neurostore_sdk.models.error_response import ErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponse from a JSON string
error_response_instance = ErrorResponse.from_json(json)
# print the JSON string representation of the object
print(ErrorResponse.to_json())

# convert the object into a dict
error_response_dict = error_response_instance.to_dict()
# create an instance of ErrorResponse from a dict
error_response_from_dict = ErrorResponse.from_dict(error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


