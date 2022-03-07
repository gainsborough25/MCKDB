from pickle import TRUE
import pyodbc
import pandas as pd
from IKeycapsRepository import IKeycapsRepository
from KeycapSet import KeycapSet
from Color import Color
from KeycapSetColor import KeycapSetColor
from Vendor import Vendor
from KeycapSetVendor import keycapSetVendor
from VwMain import VwMain
from colorsearch import ColorSearch
from vwVendorSearch import VwVendorSearch


class KeycapsRepository(IKeycapsRepository):
    

    def add_set(self, set: KeycapSet) -> None:
        connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}', \
                                    server = '.', \
                                    database = 'MKCDB', \
                                    trusted_connection = 'yes')

        sql = 'INSERT INTO KeycapSet([KeycapSetID], [KeycapName], [Manufacturer], [Material], [PrintingMethod], [Profile]) VALUES \n'\
             f'(\'{set.id}\', \'{set.keycapName}\', \'{set.manu}\', \'{set.material}\', \'{set.printingMethod}\', \'{set.profile}\');'

        cursor = connection.cursor()
        cursor.execute(sql)
        cursor.commit()

        return_value = self.get_set(set.keycapName)

        return return_value
        

    def get_set(self, name: str) -> KeycapSet:
        connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}', \
                                    server = '.', \
                                    database = 'MKCDB', \
                                    trusted_connection = 'yes')

        sql = f'SELECT * FROM KeycapSet WHERE KeycapName = ?'

        parameters = [name]

        cursor = connection.cursor()
        cursor.execute(sql, parameters)

        row = cursor.fetchone()

        set = KeycapSet(keycapName= row.KeycapName, \
                         manufacturer= row.Manufacturer, \
                         material= row.Material, \
                         printingMethod= row.PrintingMethod, \
                         profile= row.Profile, \
                         id= row.KeycapSetID)
        
        return set
    
    def get_list_of_sets(self) -> list:
        connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}', \
                                    server = '.', \
                                    database = 'MKCDB', \
                                    trusted_connection = 'yes')

        sql = 'SELECT * FROM KeycapSet'

        cursor = connection.cursor()

        sets = []

        for row in cursor.execute(sql):
            sets.append(KeycapSet(id = row.KeycapSetID, keycapName = row.KeycapName, manufacturer = row.Manufacturer, \
                                                    material = row.Material, printingMethod = row.PrintingMethod, profile = row.Profile))

        return sets

    def get_agg_of_sets(self) -> list:
        connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}', \
                                    server = '.', \
                                    database = 'MKCDB', \
                                    trusted_connection = 'yes')

        sql = 'SELECT * FROM VwMain AS M'

        cursor = connection.cursor()

        sets = []

        for row in cursor.execute(sql):
            keycapSet_instance_from_row = KeycapSet(id = row.KeycapSetID, keycapName = row.KeycapName, manufacturer = row.Manufacturer, \
                                                    material = row.Material, printingMethod = row.PrintingMethod, profile = row.Profile)
            sets.append(VwMain(set_instance = keycapSet_instance_from_row, colors = row.SetColors, numberOfKits = row.NumberOfKits, regionList = row.VendorAvailabilityByRegion))

        return sets


    def view_all_color(self) -> list:
        connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}', \
                                    server = '.', \
                                    database = 'MKCDB', \
                                    trusted_connection = 'yes')

        sql = 'SELECT * FROM vwColorSearch'

        cursor = connection.cursor()

        sets = []
        
        for row in cursor.execute(sql):
            sets.append(ColorSearch(keycapSetID = row.KeycapSetID, manufacturer = row.Manufacturer, keycapName = row.KeycapName, \
                                    material = row.Material, printingMethod = row.PrintingMethod, profile = row.Profile,\
                                    numberOfKits = row.NumberOfKits, colorFam = row.ColorFamily, classesMatchingColor = row.ClassesMatchingColor))
        if len(sets) == 0:
            raise Exception()
        else:    
            return sets


    def search_color(self, color) -> list: #uses vwColorSearch w/ VALUE(keycapSetID, Manufacturer, keycapName, Material, PrintingMethod, Profile, NumberOfKits, ColorFamily, ClassesMatchingColor)
        connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}', \
                                    server = '.', \
                                    database = 'MKCDB', \
                                    trusted_connection = 'yes')

        remove_commas_from_input_if_they_exist = color.replace(',', ' ')
        split_input = remove_commas_from_input_if_they_exist.split()

        results = []

        for value in split_input:
            sql = 'SELECT * FROM vwColorSearch WHERE ColorFamily = ?'

            parameters = [value]

            cursor = connection.cursor()

            for row in cursor.execute(sql, parameters):
                results.append(ColorSearch(keycapSetID = row.KeycapSetID, manufacturer = row.Manufacturer, keycapName = row.KeycapName, \
                                        material = row.Material, printingMethod = row.PrintingMethod, profile = row.Profile,\
                                        numberOfKits = row.NumberOfKits, colorFam = row.ColorFamily, classesMatchingColor = row.ClassesMatchingColor))


        if len(results) == 0:
            raise Exception()
        else:    
            return results   

    def search_manu(self, manu_value) -> list:
        connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}', \
                                    server = '.', \
                                    database = 'MKCDB', \
                                    trusted_connection = 'yes')

        sql = 'SELECT * FROM VwMain WHERE Manufacturer = ?'

        parameters = [manu_value]

        cursor = connection.cursor()
    
        sets = []

        for row in cursor.execute(sql, parameters):
            keycapSet_instance_from_row = KeycapSet(id = row.KeycapSetID, keycapName = row.KeycapName, manufacturer = row.Manufacturer, \
                                                    material = row.Material, printingMethod = row.PrintingMethod, profile = row.Profile)
            sets.append(VwMain(set_instance = keycapSet_instance_from_row, colors = row.SetColors, numberOfKits = row.NumberOfKits, regionList = row.VendorAvailabilityByRegion))

        if len(sets) == 0:
            raise Exception()
        else:    
            return sets

    def search_vendor(self, vendor_value) -> list:
        connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}', \
                                    server = '.', \
                                    database = 'MKCDB', \
                                    trusted_connection = 'yes')

        sql = 'SELECT * FROM vwVendorSearch WHERE KeycapName = ?'

        parameters = [vendor_value]

        cursor = connection.cursor()
    
        sets = []

        for row in cursor.execute(sql, parameters):
             sets.append(VwVendorSearch(vendorID = row.VendorID, \
                                        vendorName = row.VendorName, \
                                        region = row.VendorRegion, \
                                        vendorWebsite = row.VendorWebsite, \
                                        manu = row.Manufacturer, \
                                        keycapName= row.KeycapName))

        if len(sets) == 0:
            raise Exception()
        else:    
            return sets

    def update_material(self, id: str, ) -> None:
        print()
        connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}', \
                                    server = '.', \
                                    database = 'MKCDB', \
                                    trusted_connection = 'yes')
        new_mat = input('What is the new material for the set?\n'\
                        '---> ')
        sql = 'UPDATE KeycapSet\n'\
                'SET Material = ?\n'\
                'WHERE KeycapSetID = ?'

        parameters = [new_mat, id]
        cursor = connection.cursor()
        cursor.execute(sql, parameters)

        cursor.commit()
        print()
        new_sql = 'SELECT * FROM KeycapSet WHERE KeycapSetID = ?'

        new_parameters = [id]
        cursor.execute(new_sql, new_parameters)
        new_row = cursor.fetchone()

        updated_row = KeycapSet(keycapName= new_row.KeycapName, \
                                manufacturer= new_row.Manufacturer, \
                                material= new_row.Material, \
                                printingMethod= new_row.PrintingMethod, \
                                profile= new_row.Profile, \
                                id= new_row.KeycapSetID)

        return updated_row

    def update_color(self, keycap_id: str) -> None:
        connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}', \
                                    server = '.', \
                                    database = 'MKCDB', \
                                    trusted_connection = 'yes')
        assign_color = input('What is the ColorID of the color you would like to assign for this keycap set?\n'\
                                 '---> ')
        sql = 'UPDATE KeycapSetColor\n'\
                'SET ColorID = ?\n'\
                'WHERE KeycapSetID = ?'

        parameters = [assign_color, keycap_id]
        cursor = connection.cursor()
        cursor.execute(sql, parameters)

        cursor.commit()
        

    def update_manu(self, id: str) -> None:
        connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}', \
                                    server = '.', \
                                    database = 'MKCDB', \
                                    trusted_connection = 'yes')
        new_manu = input('What is the new Manufacturer?\n'\
                                 '---> ')
        sql = 'UPDATE KeycapSet\n'\
              'SET Manufacturer = ?\n'\
              'WHERE KeycapSetID = ?'

        parameters = [new_manu, id]
        cursor = connection.cursor()
        cursor.execute(sql, parameters)

        cursor.commit()
        new_sql = 'SELECT * FROM KeycapSet WHERE KeycapSetID = ?'

        new_parameters = [id]
        cursor.execute(new_sql, new_parameters)
        new_row = cursor.fetchone()

        updated_row = KeycapSet(keycapName= new_row.KeycapName, \
                                manufacturer= new_row.Manufacturer, \
                                material= new_row.Material, \
                                printingMethod= new_row.PrintingMethod, \
                                profile= new_row.Profile, \
                                id= new_row.KeycapSetID)

        return updated_row

    def update_set_vendor_table(self, id: str) -> None:
        pass

    def update_kit_table(self, id: str) -> None:
        pass

    def delete_set(self, id: str) -> None:
        try:
            connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}', \
                                        server = '.', \
                                        database = 'MKCDB', \
                                        trusted_connection = 'yes')

            sql = 'DELETE FROM KeycapSet WHERE KeycapSetID = ?'

            parameters = [id]

            cursor = connection.cursor()

            cursor.execute(sql, parameters)
            cursor.commit()

            print()
            print('Keycap set has been deleted from database')
            print()

        except:
            raise Exception()
