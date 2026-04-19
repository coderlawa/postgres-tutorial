from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Programmer" table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subcalss defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our Programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

babatomiwa_ogundimu = Programmer(
    first_name="Babatomiwa",
    last_name="Ogundimu",
    gender="M",
    nationality="Nigerian",
    famous_for="LAND3.NET [https://land3.net]"
)

# add each session of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(babatomiwa_ogundimu)

# updating a single record in the database
# programmer = session.query(Programmer).filter_by(id=18).first()
# programmer.gender = "M"

# commit our session to the database
# session.commit()

# updating multiple records in the database
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person. gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined for " + person.first_name + " " + person.last_name)
#     session.commit()

# deleting a single record in the database
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# # defensive programming - check if the programmer exists before trying to delete
# if programmer is not None:
#     print("Programmer found: " + programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n): ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted.")
#     else:
#         print("Programmer has not been deleted.")
# else:
#     print("No programmer found with the name " + fname + " " + lname)

# deleting entire database records - be careful with this! [needs defensive programming to avoid deleting everything by accident]
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()


# query the database to find all Programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )