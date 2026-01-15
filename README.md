# FastAPI Patient Management System

A comprehensive project illustrating the core concepts of FastAPI, ranging from basic GET requests to advanced data validation using Pydantic, computed fields, and local data persistence.

## 📁 Project Structure

The core logic of the project is contained within the `Patients_Form_Project` directory:

- **`final_api_with_update_delete.py`**: The latest implementation of the Patient API. It features:
  - **Full CRUD Support**: Create, Read, Update, and Delete patients.
  - **Pydantic Models**: Robust data validation and serialization.
  - **Partial Updates**: Uses a separate `PatientUpdate` model for flexible `PUT` operations.
  - **Request Body Handling**: Efficiently processing incoming patient data.
  - **Computed Fields**: Automatic calculation of `BMI` and health `verdict` based on patient metrics.
  - **Validation**: Strict checks using `Annotated`, `Field`, and `Literal`.
  - **Data Persistence**: Local JSON storage for records.
  - **Dynamic Sorting**: Endpoint to sort patient data by specific fields like height, weight, or BMI.
- **`program_reqbody_incl.py`**: An advanced implementation focusing on creation and retrieval.
- **`patient_proj.py`**: A foundational version of the API focusing on path/query parameters and data retrieval.
- **`patients.json`**: Acts as a lightweight local database for storing patient records.

## 🚀 Key Features

- **Robust Data Validation**: Leveraging Pydantic to ensure all incoming data meets specific criteria (e.g., positive heights/weights, specific gender literals).
- **Computed Metrics**: No need to manually provide BMI; the API calculates it dynamically using properties and `@computed_field`.
- **Flexible Data Retrieval**: View all patients, search by ID, or sort the entire list based on physical metrics.
- **Update & Delete**: Easily modify existing records or remove them entirely from the system.
- **Persistent Storage**: Data is saved to and loaded from a local JSON file, allowing it to survive server restarts.

## 🛠️ Installation & Setup

If you are forking or cloning this project, follow these steps to get it running locally.

### 1. Prerequisites
Ensure you have **Python 3.12** or higher installed.

### 2. Install Dependencies
The project uses `fastapi`, `pydantic`, and `uvicorn`. You can install them using pip:

```bash
pip install "fastapi>=0.128.0" "pydantic[email]>=2.12.5" "uvicorn>=0.40.0"
```

*Note: These requirements are derived from the `pyproject.toml` configuration.*

### 3. Running the API
Navigate to the project directory and run the main application using Uvicorn:

```bash
uvicorn Patients_Form_Project.final_api_with_update_delete:app --reload
```

Once the server is running, you can access the interactive documentation at:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📡 API Endpoints Summary

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/` | System health check/welcome message. |
| **GET** | `/about` | Information about the Patient Management System. |
| **GET** | `/view` | Retrieve a list of all registered patients. |
| **GET** | `/patient/{id}` | Get detailed information for a specific patient. |
| **GET** | `/sort` | Sort patients by `height`, `weight`, or `bmi`. |
| **POST** | `/create` | Register a new patient in the database. |
| **PUT** | `/edit/{id}` | Update existing patient details (partial updates supported). |
| **DELETE** | `/delete/{id}` | Remove a patient from the database. |
