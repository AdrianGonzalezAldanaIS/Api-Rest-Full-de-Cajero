from datetime import datetime

class Dateformat:
    @classmethod
    def conver_to_date(self, fecha):
        return datetime.strftime(fecha, '%d/%m/%Y')