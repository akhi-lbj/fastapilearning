from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional

class Patient(BaseModel):

    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int =Field(gt=0, lt=120)
    weight: float = Field(gt=0)
    married: bool = False
    allergies: Optional[List[str]] = Field(default=None, max_length=5)
    contact_details: Dict[str, str]

def insert_patient(patient: Patient):

     print(patient.name)
     print(patient.email)
     print(patient.linkedin_url)
     print(patient.age)
     print(patient.weight)
     print(patient.married)
     print(patient.allergies)
     print(patient.contact_details)
     print('inserted')

def update_patient_data(patient: Patient):

     print(patient.name)
     print(patient.email)
     print(patient.linkedin_url)
     print(patient.age)
     print(patient.weight)
     print(patient.married)
     print(patient.allergies)
     print(patient.contact_details)
     print('updated')
    
patient_info = { 'name': 'nitish', 'email': 'nitish@example.com', 'linkedin_url': 'https://linkedin.com/nitish', 'age': 30, 'weight': 70.5, 'contact_details': { 'phone': '1234567890'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)