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

    def getTopVendite(self):
        cnx = DBConnect.get_connection()
        topVendite = []
        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT s.Date, s.Unit_sale_price, s.Quantity, s.Retailer_code, s.Product_number, p.Product_brand
                    FROM go_daily_sales s, go_products p
                    WHERE s.Product_number = p.Product_number"""
        cursor.execute(query)
        for row in cursor:
            vendita = {"Date" : row["Date"], "Retailer_code" : row["Retailer_code"], "Product_number" : row["Product_number"], "Ricavo" : float(row["Unit_sale_price"])*float(row["Quantity"]), "Product_brand" : row["Product_brand"]}
            topVendite.append(vendita)
        cursor.close()
        cnx.close()
        return topVendite

