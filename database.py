from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

# Create the database engine
engine=create_engine('postgresql://postgres:0345@localhost/Pizza_Delivery',
    echo=True
)
# ^ Creates an engine instance that connects to the PostgreSQL database
#   - 'postgresql://': Specifies the database dialect
#   - 'echo=True': Enables logging of all SQL commands executed by the engine

# Create a base class for models
Base=declarative_base()

# Creates a session factory
Session=sessionmaker()