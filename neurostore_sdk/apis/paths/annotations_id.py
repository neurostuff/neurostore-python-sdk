from neurostore_sdk.paths.annotations_id.get import ApiForget
from neurostore_sdk.paths.annotations_id.put import ApiForput
from neurostore_sdk.paths.annotations_id.delete import ApiFordelete


class AnnotationsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
