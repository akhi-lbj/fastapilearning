# 🩺 Pydantic Tutorial: Data Validation & Settings Management

Welcome to the Pydantic Tutorial folder! This guide covers the essential concepts of using **Pydantic** for robust data validation in Python, specifically tailored for application in frameworks like FastAPI.

---

## 🚀 Overview

Pydantic is a library for data validation and settings management using Python type annotations. It enforces type hints at runtime and provides user-friendly errors when data is invalid.

## 📚 Key Concepts Covered

### 1. The `BaseModel` Class
The core of Pydantic is the `BaseModel`. By inheriting from this class, you can define the "schema" of your data.

```python
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
```

### 2. Basic & Advanced Type Hinting
We explored various Python types that Pydantic uses to validate incoming data:
- **Primitive Types**: `str`, `int`, `float`, `bool`.
- **Default Values**: Fields can have default values (e.g., `married: bool = False`).
- **Complex Types**: Using the `typing` module:
    - `List[str]`: A list containing only strings.
    - `Dict[str, str]`: A dictionary with string keys and string values.
- **Optional Fields**: Using `Optional[T]` for values that can be `None`.

### 3. Special Pydantic Types (p3)
Pydantic provides specialized types for common data formats:
- **`EmailStr`**: Validates that a string is a valid email address.
    - *Note: Requires `pip install "pydantic[email]"`*
- **`AnyUrl`**: Validates strings as valid URLs.

### 4. Advanced Field Validation (p3)
Using the `Field` class, you can add powerful constraints to your data:
- **Numeric Constraints**: `gt` (greater than), `ge` (greater or equal), `lt` (less than), `le` (less or equal).
- **String/List Constraints**: `max_length`, `min_length`.
- **Custom Metadata**: Adding descriptions or default values via `Field(default=...)`.

```python
from pydantic import Field

class Patient(BaseModel):
    age: int = Field(gt=0, lt=120)
    weight: float = Field(gt=0)
    allergies: Optional[List[str]] = Field(default=None, max_length=5)
```

### 5. Model Instances & Dictionary Unpacking
Create instances by unpacking dictionaries—perfect for processing JSON API payloads.

```python
patient_info = { 'name': 'Nitish', 'age': 30 }
patient = Patient(**patient_info)
```

---

## 📂 File Structure

- **`pydantic_p1_intro.py`**: Introduction to `BaseModel` and basic string/integer validation.
- **`pydantic_p2.py`**: Deep dive into advanced types like `List`, `Dict`, `Optional`, and default values.
- **`pydantic_p3.py`**: Advanced validation using `EmailStr`, `AnyUrl`, and the `Field` class for constraints.

## 🛠️ Installation & Usage

### ⚙️ Dependencies
To use email validation, make sure to install:
```bash
pip install "pydantic[email]"
```

### 🏃 Running the Scripts
Run any tutorial script using the Python interpreter:
```bash
python pydantic_p3.py
```
