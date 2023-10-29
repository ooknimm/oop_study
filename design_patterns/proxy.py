from abc import ABC, abstractmethod
from typing import Dict

class ImageServiceInterface(ABC):
    @abstractmethod
    def get_image(id: str) -> bytes: ...

class ImageService(ImageServiceInterface):
    def get_image(id: str) -> bytes:
        # download from remote server
        ...

class ImageServiceProxy(ImageServiceInterface):
    def __init__(self) -> None:
        self._image_service = ImageService()
        self.cache: Dict[str, bytes] = {}

    def get_image(self, id: str) -> bytes:
        if id in self.cache:
            return self.cache[id]
        image = self._image_service.get_image(id)
        self.cache[id] = image
        return image
    

image_service = ImageServiceProxy()
image_service.get_image("image_1")

    