from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

def insert_patient(patient: Patient):

     print(patient.name)
     print(patient.age)
     print(patient.weight)
     print(patient.married)
     print(patient.allergies)
     print(patient.contact_details)
     print('inserted')

def update_patient_data(patient: Patient):

     print(patient.name)
     print(patient.age)
     print(patient.weight)
     print(patient.married)
     print(patient.allergies)
     print(patient.contact_details)
     print('updated')
    
patient_info = {  'name': 'nitish', 'age': 30, 'weight': 70.5, 'contact_details': { 'phone': '1234567890', 'email': 'nitish@example.com' }}

patient1 = Patient(**patient_info)

update_patient_data(patient1)