from sqlalchemy import create_engine, Column, String, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Create base table object
Base=declarative_base()

# Inherit base table into our table, so as to create a map of a table
class FormResponses(Base):
    __tablename__="FormResponses"
    
    name = Column(String, unique=False)
    email=Column(VARCHAR(50), unique=True,primary_key=True)
    password = Column(VARCHAR(50),unique=False)

# Store form data into database
def store_data(name, email, password):
    new_enty = FormResponses(name=name, email=email, password=password)

    entry = session.query(FormResponses).filter_by(email=email).first()

    if entry:
        session.rollback()
        return "Email already exists in database"
    else:
        session.add(new_enty)
        session.commit()
        return "Data saved successfully into the database"

# Fetch all the data from the database
def get_all_data():
    entries = session.query(FormResponses).all()
    try:
        if entries:
            session.commit()
            return entries
        else:
            return "Error in extracting data from database"
    except:
        session.rollback()
        return "Error in extracting data from database"

# Download db data into a csv file and return the contents of a file
# The file is created and removed so that data reading is easy and the content is returned to js ajax query which is downloaded as csv.
def download_db_data():
    form_responses = get_all_data()
    f = open('Form_Responses.csv',"w")
    for i in form_responses:
        f.write(f"{i.name},{i.email},{i.password},")
        f.write("\n")
    f.close()
    f = open('Form_Responses.csv','r')
    download_data = f.read()
    f.close()
    os.remove("Form_Responses.csv")
    return download_data

# Query engine to link code to cloud
engine = create_engine("mysql://uur4vogfmq09uxig:pWxcFrhhysWUl2DjBrvY@bglhb2br83duzqzh1fcv-mysql.services.clever-cloud.com:3306/bglhb2br83duzqzh1fcv")
Base.metadata.create_all(bind=engine)
Session=sessionmaker(bind=engine)
session = Session()
