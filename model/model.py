import database.DAO as db

class Model:
    def __init__(self):
        self.dao = db.DAO()

    def getAnni(self):
        return self.dao.getAnni()

    def getBrand(self):
        return self.dao.getBrand()

    def getRetailers(self):
        return self.dao.getRetailer()

    def getTopVendite(self, anno, brand, retailer):
        topVendite = self.dao.getTopVendite()
        venditeAggiornate = []
        for vendita in topVendite:
            if brand is not None:
                if vendita["Product_brand"] == brand:
                    pass
                else:
                    continue
            if retailer is not None:
                if vendita["Retailer_code"] == retailer:
                    pass
                else:
                    continue
            if anno is not None:
                if vendita["YEAR(s.Date)"] == anno:
                    pass
                else:
                    continue
            venditeAggiornate.append(f"Data:{vendita["YEAR(s.Date)"]}; Ricavo:{float(vendita["Unit_sale_price"])*float(vendita["Quantity"])}; Retailer: {vendita["Retailer_code"]}; Product: {vendita["Product_number"]}")
        print(venditeAggiornate)
        return venditeAggiornate