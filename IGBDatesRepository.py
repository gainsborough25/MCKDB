from abc import ABC, abstractmethod
from typing import AbstractSet

from GBDates import GBDates

class IGBDatesRepository(ABC):

    @abstractmethod
    def add_gbDates(self, gbDates: GBDates) -> None:
        pass

    @abstractmethod
    def get_gbDates(self, id: int) -> GBDates:
        pass

    @abstractmethod
    def get_allDates(self) -> list:
        pass

    @abstractmethod
    def update_gbDates(self, id: int, gbDates: GBDates) -> None:
        pass

    @abstractmethod
    def delete_gbDates(self, id: int) -> None:
        pass
