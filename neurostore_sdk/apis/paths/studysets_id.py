from neurostore_sdk.paths.studysets_id.get import ApiForget
from neurostore_sdk.paths.studysets_id.put import ApiForput
from neurostore_sdk.paths.studysets_id.delete import ApiFordelete


class StudysetsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
