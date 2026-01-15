from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Optional, Annotated, Literal
import json

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description='Name of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient', examples=['Ananya Sharma'])]
    city: Annotated[str, Field(..., description='City where the patient is living', examples=['Guwahati'])]
    age: Annotated[int, Field(..., description='Age of the patient', examples=[28])]
    gender: Annotated[Literal['male', 'female'], Field(..., description='Gender of the patient', examples=['female'])]
    height: Annotated[float, Field(...,gt=0, description='Height of the patient', examples=[1.65])]
    weight: Annotated[float, Field(...,gt=0, description='Weight of the patient', examples=[90.0])]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi <18.5:
            return 'Underweight'
        elif self.bmi <25:
            return 'Normal'
        elif self.bmi <30:
            return 'Overweight'
        else:
            return 'Obese'

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(description='Name of the patient', examples=['Ananya Sharma'], default=None)]
    city: Annotated[Optional[str], Field(description='City where the patient is living', examples=['Guwahati'], default=None)]
    age: Annotated[Optional[int], Field(description='Age of the patient', examples=[28], default=None)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(description='Gender of the patient', examples=['female'], default=None)]
    height: Annotated[Optional[float], Field(gt=0, description='Height of the patient', examples=[1.65], default=None)]
    weight: Annotated[Optional[float], Field(gt=0, description='Weight of the patient', examples=[90.0], default=None)]

def load_data(): 
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)

@app.get("/")
def hello():
    return { 'message' : 'Patient Management System API'}

@app.get('/about')
def about():
    return { 'message': 'A fully functional API to manage your patient records'}

@app.get('/view')
def view():
    data = load_data()
    return data 

@app.get('/patient/{patient_id}')
def get_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):
    # load all the patients data
    data = load_data()
    # check if the patient exists
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight and BMI'), order: str = Query('asc', description='Sort in ascending or descending order')):
    valid_fields=['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail='Invalid field to select from {valid_fields}')

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order to select from {order}')

    data = load_data()

    sort_order = True if order=='desc' else False
    
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse = sort_order)

    return sorted_data 

@app.post('/create')
def create_patient(patient: Patient):

    # Load data
    data = load_data()

    # Check if patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')

    # Add new patient to the data
    data[patient.id] = patient.model_dump(exclude={'id'})

    # save data to the file
    save_data(data)

    return JSONResponse(status_code=201, content={"message": "Patient added successfully"})

@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):
    # Load data
    data = load_data()
    # Check if the patient exists
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    existing_patient_info = data[patient_id]

    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    existing_patient_info['id'] = patient_id
    patient_pydantic_obj = Patient(**existing_patient_info)

    existing_patient_info = patient_pydantic_obj.model_dump(exclude={'id'})


    data[patient_id] = existing_patient_info

    save_data(data)

    return JSONResponse(status_code=200, content={"message": "Patient updated successfully"})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    # Load data
    data = load_data()
    # Check if the patient exists
    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]
    save_data(data)
    return JSONResponse(status_code=200, content={"message": "Patient deleted successfully"})

    
    


    






