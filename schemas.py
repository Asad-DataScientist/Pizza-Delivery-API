# Pydantic
# Purpose:
# Pydantic is a data validation and settings management library for Python.
# It is used to validate data and manage settings using Python type 
# annotations.

from pydantic import BaseModel, Field, root_validator
from typing import Optional
from jsonschema import validate
import secrets

# class config:
#         str_strip_whitespace = True 

# Define a Pydantic model for signing up users
class SignUpModel(BaseModel):
    id:Optional[int]            # Optional integer field for the user ID
    username:str                # Required string field for the username
    email:str                   # Required string field for the email
    password:str                # Required string field for the password
    is_staff:Optional[bool]     # Optional boolean field for staff status
    is_active:Optional[bool]    # Optional boolean field for active status
  
    class Config:
        orm_mode=True           # Automatically convert query results to models
        schema_extra={
            'example':{
                "username":"johndoe",
                "email":"johndoe@gmail.com",
                "password":"1234",
                "is_staff":False,
                "is_active":True
            }
        }

# class for JWT authentication
class Settings(BaseModel):
    authjwt_secret_key:str='1f7185bf07058743e193524640a09067b4f9498b8dd5954eaaa2f1cab66550fa'

# Define a Pydantic model for user login
class LoginModel(BaseModel):
    username:str            # Required string field for the username
    password:str            # Required string field for the password
    

class OrderModel(BaseModel):
    id:Optional[int]
    quantity:int
    order_status:Optional[str]="PENDING"
    pizza_size:Optional[str]="SMALL"
    user_id:Optional[int]


    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "quantity":2,
                "pizza_size":"LARGE"
            }
        }


class OrderStatusModel(BaseModel):
    order_status:Optional[str]="PENDING"

    class Config:
        orm_mode=True
        schema_extra={
            "example":{
                "order_status":"PENDING"
            }
        }