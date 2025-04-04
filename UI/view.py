import flet as ft
from flet_core import MainAxisAlignment


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self._btnAnalizzaVendite = None
        self._btnTopVendite = None
        self._tendinaRetailer = None
        self._tendinaBrand = None
        self._tendinaAnno = None
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self._controller = None
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        self._title = ft.Text("Analizza Vendite", color="blue", size=28)
        self._tendinaAnno = ft.Dropdown(label="Anno", width=200)
        self._tendinaBrand = ft.Dropdown(label="Brand", width=200)
        self._tendinaRetailer = ft.Dropdown(label="Retailer", width=500)
        self._tendinaAnno.options.append(ft.dropdown.Option("Nessun filtro"))
        self._tendinaBrand.options.append(ft.dropdown.Option("Nessun filtro"))
        self._tendinaRetailer.options.append(ft.dropdown.Option("Nessun filtro"))
        self._controller.fillAnno()
        self._controller.fillBrand()
        self._controller.fillRetailer()
        row1 = ft.Row([self._tendinaAnno, self._tendinaBrand, self._tendinaRetailer], alignment=MainAxisAlignment.CENTER, spacing=10)
        self._btnTopVendite = ft.ElevatedButton(text="Top Vendite", width=200, on_click=self._controller.handleTopVendite)
        self._btnAnalizzaVendite = ft.ElevatedButton(text="Analizza Vendite", width=200, on_click=self._controller.handleAnalizzaVendite)
        row2 = ft.Row([self._btnTopVendite, self._btnAnalizzaVendite], alignment=MainAxisAlignment.CENTER, spacing=10)
        self._page.add(self._title, row1, row2)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
