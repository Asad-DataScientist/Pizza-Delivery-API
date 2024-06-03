# SQLAlchemy
# Purpose:

# SQLAlchemy is a SQL toolkit and Object-Relational Mapping (ORM) 
# library for Python.

# It is used to interact with databases in a Pythonic way, allowing 
# developers to map Python classes to database tables.

from database import Base
from sqlalchemy import Column,Integer,Boolean,Text,String,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType

# User model mapped to the "user" table in the database
class User(Base):
    __tablename__="user"

      # Columns in the "user" table
    id=Column(Integer,primary_key=True)                 # Primary key column
    username=Column(String(25),unique=True)             # Unique username column
    email=Column(String(80),unique=True)                # Unique email column
    password=Column(Text,nullable=True)                 # Password column (nullable to handle cases like social logins)
    is_staff=Column(Boolean,default=False)              # Boolean column to check if the user is staff
    is_active=Column(Boolean,default=False)             # Boolean column to check if the user is active
    orders=relationship("Order",back_populates="user")  # Relationship to the Order model

 # String representation of the User model
def __repr__(self):
    return f"<User {self.username}"


# Order model mapped to the "orders" table in the database
class Order (Base):

 # Choices for order status and pizza size
    ORDER_STATUSES=(
        ('PENDING','Pending'),
        ('IN-TRANSIT','In-Transit'),
        ('DELIVERED','Delivered')

    )

    PIZZA_SIZES=(
        ('SMALL','Small'),
        ('MEDIUM','Medium'),
        ('LARGE','Large'),
        ('EXTRA-LARGE','Extra-Large')
    )

    __tablename__='orders'                                                      # Table name in the database
    id=Column(Integer,primary_key=True)                                         # Primary key column
    quantity=Column(Integer,nullable=False)                                     # Column Pizzas quantity can't be null
    order_status=Column(ChoiceType(choices=ORDER_STATUSES),default="PENDING")   # Order status with default value
    pizza_size=Column(ChoiceType(choices=PIZZA_SIZES),default="SMALL")          # Pizza size with default value
    user_id=Column(Integer,ForeignKey('user.id'))                               # Foreign key referencing the user table
    user=relationship('User',back_populates='orders')                           # Relationship to User model, with back reference to orders

    # String representation of the Order model
def __repr__(self):
    return f"<Order {self.id}>" # Return the order ID for better readability