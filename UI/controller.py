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
        self._view.lvTxtOut.controls.clear()
        anno = self._view._tendinaAnno.value
        if anno =="Nessun filtro":
            anno = None
        brand = self._view._tendinaBrand.value
        if brand == "Nessun filtro":
            brand = None
        retailer = self._view._tendinaRetailer.value
        if retailer == "Nessun filtro":
            retailer = None
        topVendite = self._model.getTopVendite(anno, brand, retailer)
        for vendita in topVendite:
            self._view.lvTxtOut.controls.append(ft.Text(vendita))
        self._view._page.update()

    def handleAnalizzaVendite(self, e):
        self._view.lvTxtOut.controls.clear()
        anno = self._view._tendinaAnno.value
        if anno == "Nessun filtro":
            anno = None
        brand = self._view._tendinaBrand.value
        if brand == "Nessun filtro":
            brand = None
        retailer = self._view._tendinaRetailer.value
        if retailer == "Nessun filtro":
            retailer = None
        infoVenditeAnalizzate = self._model.analizzaVendite(anno, brand, retailer)
        self._view.lvTxtOut.controls.append(ft.Text("Statistiche vendite:"))
        for info in infoVenditeAnalizzate:
            self._view.lvTxtOut.controls.append(ft.Text(info))
        self._view._page.update()

