# Completed Clinic class   
import requests
from db_connector import create_connection

class Clinic:
    def __init__(self):
        self.connection = create_connection()
        self.additional_info = {
            "1": {"ophthalmology": "service1", "address": "address1", "password": "password1", "contact": "contact1"},
            "2": {"gynecology": "service2", "address": "address2", "password": "password2", "contact": "contact2"},
            "3": {"otolaryngology": "service3", "address": "address3", "password": "password3", "contact": "contact3"},
            "4": {"general": "service4", "address": "address4", "password": "password4", "contact": "contact4"},
            "5": {"orthopedics": "service5", "address": "address5", "password": "password5", "contact": "contact5"},
            "6": {"cardiology": "service6", "address": "address6", "password": "password6", "contact": "contact6"},
            "7": {"dental": "service7", "address": "address7", "password": "password7", "contact": "contact7"},
           
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
