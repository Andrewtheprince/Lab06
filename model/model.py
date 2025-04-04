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