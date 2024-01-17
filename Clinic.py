import requests
from db_connector import create_connection

class Clinic:
    def __init__(self):
        self.connection = create_connection()
        self.additional_info = {
            "1": {"service": "ophthalmology", "address": "Los Angeles; Beverly Hills", "password": "ab12518maj", "contact": "09123758274"},
            "2": {"service": "gynecology", "address": "900 Pacific Ave, Everett", "password": "kj13827kti", "contact": "09194726482"},
            "3": {"service": "otolaryngology", "address": "Harborview, 325 9th Ave, Seattle", "password": "qp02983njh", "contact": "09185746253"},
            "4": {"service": "general", "address": "Hoyt Ave, Everett", "password": "pc01382ooq", "contact": "09109584726"},
            "5": {"service": "orthopedics", "address": "45th St, Seattle", "password": "br12256pqp", "contact": "09108876543"},
            "6": {"service": "cardiology", "address": "Cleveland, Ohio", "password": "pp09892bbu", "contact": "09124837264"},
            "7": {"service": "dental", "address": "Alderwood Mall Blvd, Lynnwood", "password": "hq89204nnb", "contact": "09127564728"},
        }

    def get_info(self):
        response = requests.get('http://127.0.0.1:5000/slots')
        return response.json()

    def insert_data(self):
        data = self.get_info()
        if data is not None:
            cursor = self.connection.cursor()
            sql = """
            INSERT INTO clinics (clinic_id , capacity , service , reserved_appointments , address , clinic_password , clinic_contact_info ) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
                  """
            values = []
            for clinic_id, capacity in data.items():
                info = self.additional_info.get(clinic_id, {})
                service = info.get("service", "")
                address = info.get("address", "")
                password = info.get("password", "")
                contact = info.get("contact", "")
                values.append((clinic_id, capacity, service, 0, address, password, contact))
            cursor.executemany(sql, values)
            self.connection.commit()

    def close_connection(self):
        self.connection.close()