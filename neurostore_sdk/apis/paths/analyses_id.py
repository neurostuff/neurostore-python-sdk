from neurostore_sdk.paths.analyses_id.get import ApiForget
from neurostore_sdk.paths.analyses_id.put import ApiForput
from neurostore_sdk.paths.analyses_id.delete import ApiFordelete


class AnalysesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
