import flet as ft


class Controller:
    def __init__(self, view, model):
        self._retailer = None
        self._view = view
        self._model = model


    def fillAnno(self):
        anni = self._model.getAnni()
        for anno in anni:
            self._view._tendinaAnno.options.append(ft.dropdown.Option(anno))

    def fillBrand(self):
        brands = self._model.getBrand()
        for brand in brands:
            self._view._tendinaBrand.options.append(ft.dropdown.Option(brand))

    def fillRetailer(self):
        for retailer in self._model.getRetailers():
            self._view._tendinaRetailer.options.append(ft.dropdown.Option(key=retailer.Retailer_code, text=retailer.Retailer_name, data=retailer, on_click=self.read_retailer))
            
    def read_retailer(self, e):
        self._retailer = e.control.data

    def handleTopVendite(self, e):
        pass

    def handleAnalizzaVendite(self, e):
        pass

