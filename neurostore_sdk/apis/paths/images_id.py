from neurostore_sdk.paths.images_id.get import ApiForget
from neurostore_sdk.paths.images_id.put import ApiForput
from neurostore_sdk.paths.images_id.delete import ApiFordelete


class ImagesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
