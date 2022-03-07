from abc import ABC, abstractmethod
from typing import AbstractSet

from KeycapSet import KeycapSet
from Color import Color
from KeycapSetColor import KeycapSetColor
from VwMain import VwMain


'''
some notes to self:
- might need to make IColorRepository and ColorRepository since adding a keycapSet requires adding multiple colors, not sure how I could put all of that in DB at one time
- vendor as well?  
- Hmmmm.  It's a lot of work, but maybe it makes more sense to have KeycapSetColor and Color have it's own repository / IRepository, same with keycapSetVendor and Vendor
- define and use VIEWS to set up what database should return to the user - this should simplify the code significantly
- make vendor with junction its own repository
- can use triggers to put data into child tables when putting data into KeycapSet (possibly - not sure how that would work, though)
'''
class IKeycapsRepository(ABC):

    @abstractmethod
    def add_set(self, KeycapSet: KeycapSet) -> None:
        pass

    @abstractmethod
    def get_set(self, name: int) -> KeycapSet:
        pass
    
    @abstractmethod
    def get_list_of_sets(self, id: int) -> list:
        pass    

    @abstractmethod
    def get_agg_of_sets(self, id: int) -> list:
        pass

    @abstractmethod
    def search_color(self) -> list:
        pass

    @abstractmethod
    def view_all_color(self) -> list:
        pass
        
    @abstractmethod
    def delete_set(self, id: int) -> None:
        pass

    @abstractmethod
    def search_manu(self, manu_value) -> list:
        pass
    
    @abstractmethod
    def search_vendor(self, vendor_value) -> list:
        pass
    
    @abstractmethod
    def update_material(self, id: str) -> None:
        pass

    @abstractmethod
    def update_color(self, id: str) -> None:
        pass

    @abstractmethod
    def update_manu(self, id: str) -> None:
        pass

    @abstractmethod
    def update_set_vendor_table(self, id: str) -> None:
        pass