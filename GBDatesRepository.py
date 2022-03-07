import pyodbc
import pandas as pd
from IGBDatesRepository import IGBDatesRepository
from GBDates import GBDates


class GBDatesRepository(IGBDatesRepository):
    

    def add_dates(self, GBDates: GBDates) -> None:
        # connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}',
        # server = '.', database = 'Products', trusted_connection = 'yes')

        # sql = 'INSERT INTO Product([Name], [Price]) VALUES '
        # sql += f'(\'{product.name}\', {product.price});'

        # cursor = connection.cursor()
        # cursor.execute(sql)
        # cursor.commit()
        pass

    def get_dates(self, id: int) -> GBDates:
        # connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}',
        # server = '.', database = 'ProductsDB', trusted_connection = 'yes')

        # sql = f'SELECT * FROM Product WHERE Id = ?'

        # parameters = [id]

        # cursor = connection.cursor()
        # cursor.execute(sql, parameters)

        # row = cursor.fetchone()

        # return Product(row.Id, name=row.Name, price=row.Price)        
        pass

    
    def get_list_of_dates(self) -> list:
        # connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}',
        # server = '.', database = 'Products', trusted_connection = 'yes')

        # sql = 'SELECT * FROM Product;'

        # cursor = connection.cursor()

        # products = [] # list()

        # for row in cursor.execute(sql):
        #     products.append(Product(row.Id, name=row.Name, price=row.Price))

        # return products
        pass

    def update_dates(self, id: int, product: GBDates) -> None:
        pass

    def delete_dates(self, id: int) -> None:
        pass
