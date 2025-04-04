from database.DB_connect import DBConnect
from model.retailer import Retailer

class DAO:
    def __init__(self):
        pass

    def getAnni(self):
        cnx = DBConnect.get_connection()
        anni = []
        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT YEAR(g.Date)
                    FROM go_daily_sales g"""
        cursor.execute(query)
        for row in cursor:
                anni.append(str(row["YEAR(g.Date)"]))
        cursor.close()
        cnx.close()
        anni2 = []
        for element in anni:
            if element not in anni2:
                anni2.append(element)
        return anni2

    def getBrand(self):
        cnx = DBConnect.get_connection()
        brand = []
        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT Product_brand
                    FROM go_products"""
        cursor.execute(query)
        for row in cursor:
            if row["Product_brand"] not in brand:
                brand.append(row["Product_brand"])
        cursor.close()
        cnx.close()
        return brand

    def getRetailer(self):
        cnx = DBConnect.get_connection()
        retailers = []
        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT *
                    FROM go_retailers"""
        cursor.execute(query)
        for row in cursor:
            retailers.append(Retailer(**row))
        cursor.close()
        cnx.close()
        return retailers