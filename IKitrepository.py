from abc import ABC, abstractmethod
from typing import AbstractSet

from Kit import Kit

class IKitRepository(ABC):

    @abstractmethod
    def add_kit(self, product: Kit) -> None:
        pass

    @abstractmethod
    def get_list_of_kits(self) -> list:
        pass

    @abstractmethod
    def update_kit(self, id: int, product: Kit) -> None:
        pass

    @abstractmethod
    def delete_kit(self, id: int) -> None:
        pass
