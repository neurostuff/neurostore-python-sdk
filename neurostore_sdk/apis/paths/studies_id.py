from neurostore_sdk.paths.studies_id.get import ApiForget
from neurostore_sdk.paths.studies_id.put import ApiForput
from neurostore_sdk.paths.studies_id.delete import ApiFordelete


class StudiesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
