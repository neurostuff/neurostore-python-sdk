from neurostore_sdk.paths.conditions_id.get import ApiForget
from neurostore_sdk.paths.conditions_id.put import ApiForput
from neurostore_sdk.paths.conditions_id.delete import ApiFordelete


class ConditionsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
