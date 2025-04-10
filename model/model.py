from operator import itemgetter

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
                if str(vendita["Product_brand"]) != str(brand):
                    continue
            if retailer is not None:
                if str(vendita["Retailer_code"]) != str(retailer):
                    continue
            if anno is not None:
                pezzi = str(vendita["Date"]).split("-")
                anno2 = pezzi[0]
                if anno2 != str(anno):
                    continue
            venditeAggiornate.append(vendita)
        venditeAggiornate.sort(key=itemgetter('Ricavo'), reverse=True)
        venditeOrdinate = venditeAggiornate[:5]
        venditeDefinitive = []
        for venditaOrdinata in venditeOrdinate:
            venditeDefinitive.append(f"Data: {venditaOrdinata["Date"]}; Ricavo: {venditaOrdinata["Ricavo"]}; Retailer: {venditaOrdinata["Retailer_code"]}; Product: {venditaOrdinata["Product_number"]}")
        return venditeDefinitive

    def analizzaVendite(self, anno, brand, retailer):
        #ritorna una lista di stringhe con le info sulle vendite
        venditeTotali = self.dao.getTopVendite()
        venditeAggiornate = []
        for vendita in venditeTotali:
            if brand is not None:
                if str(vendita["Product_brand"]) != str(brand):
                    continue
            if retailer is not None:
                if str(vendita["Retailer_code"]) != str(retailer):
                    continue
            if anno is not None:
                pezzi = str(vendita["Date"]).split("-")
                anno2 = pezzi[0]
                if anno2 != str(anno):
                    continue
            venditeAggiornate.append(vendita)
        ricaviTotali = 0
        numeroVendite = len(venditeAggiornate)
        retailerCoinvolti = set()
        prodottiCoinvolti = set()
        for venditaAggiornata in venditeAggiornate:
            ricaviTotali += float(venditaAggiornata["Ricavo"])
            retailerCoinvolti.add(str(venditaAggiornata["Retailer_code"]))
            prodottiCoinvolti.add(str(venditaAggiornata["Product_number"]))
        info = [f"Giro d'affari: {format(ricaviTotali, ".2f")}", f"Numero vendite: {numeroVendite}", f"Numero retailer coinvolti: {len(retailerCoinvolti)}", f"Numero prodotti coinvolti: {len(prodottiCoinvolti)}"]
        return info