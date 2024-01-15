# Completed Clinic class   
import requests
from db_connector import create_connection

class Clinic:
    def __init__(self):
        self.connection = create_connection()
        self.additional_info = {
            "1": {"service": "ophthalmology", "address": "address1", "password": "ab12518maj", "contact": "09123758274"},
            "2": {"service": "gynecology", "address": "address2", "password": "kj13827kti", "contact": "09194726482"},
            "3": {"service": "otolaryngology", "address": "address3", "password": "qp02983njh", "contact": "09185746253"},
            "4": {"service": "general", "address": "address4", "password": "pc01382ooq", "contact": "09109584726"},
            "5": {"service": "orthopedics", "address": "address5", "password": "br12256pqp", "contact": "09108876543"},
            "6": {"service": "cardiology", "address": "address6", "password": "pp09892bbu", "contact": "09124837264"},
            "7": {"service": "dental", "address": "address7", "password": "hq89204nnb", "contact": "09127564728"},
           
        }

    def get_info(self):
        response = requests.get('http://127.0.0.1:5000/slots')
        return response.json()

    def insert_data(self):
        data = self.get_info()
        if data is not None:
            with self.connection.cursor() as cursor:
                sql = """
                INSERT INTO clinics (clinic_id , capacity , service , reserved_appointments , address , clinic_password , clinic_contact_info ) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
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
