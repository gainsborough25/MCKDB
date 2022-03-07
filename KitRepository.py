import pyodbc
import pandas as pd
from pytest import param
from IKitrepository import IKitRepository
from Kit import Kit
from vwSearchNameAndKits import VWSearchNameAndKits


class KitRepository(IKitRepository):
    

    def add_kit(self, product: Kit) -> None:
        # connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}',
        # server = '.', database = 'Products', trusted_connection = 'yes')

        # sql = 'INSERT INTO Product([Name], [Price]) VALUES '
        # sql += f'(\'{product.name}\', {product.price});'

        # cursor = connection.cursor()
        # cursor.execute(sql)
        # cursor.commit()
        pass

    
    def get_list_of_kits(self, keycapName) -> list:
        connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}', \
                                    server = '.', \
                                    database = 'MKCDB', \
                                    trusted_connection = 'yes')

        sql = "SELECT * FROM vwSearchNameAndKits AS S WHERE S.KeycapName LIKE ?"

        parameters = [keycapName]

        cursor = connection.cursor()

        sets = [] #create empty list

        for row in cursor.execute(sql, parameters):
            sets.append(VWSearchNameAndKits(keycapSetID=row.KeycapSetID, manu=row.Manufacturer, keycapName=row.KeycapName, setColors=row.SetColors, \
                        kitID=row.KitID, kitName=row.KitName, legendChar=row.LegendChar, sublegendChar=row.SublegendChar, numberOfKeys=row.NumberOfKeys, \
                        tsangan=row.TsanganSupport, iso=row.ISOSupport))

        if len(sets) == 0:
            raise Exception()
        else:    
            return sets   

    def update_kit(self, id: int, product: Kit) -> None:
        pass

    def delete_kit(self, id: int) -> None:
        pass
