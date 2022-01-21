#necessary code to connect to database and collection
from pymongo import MongoClient
url= "mongodb+srv://admin:admin@cluster0.qvqxw.mongodb.net/pytech?retryWrites=true&w=majority";
client=MongoClient(url)
db = client.pytech
students=db.students

#Displays using find method
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for key in students.find({},{"_id":0}):
    print("Student ID: ",key["student_id"], '\n'  "First Name: ",key["first_name"], '\n'  "Last Name: ",key["last_name"], '\n' )
print("")
#inserts student with the id of 1010
merry = {
    "student_id":"1010",
    "first_name":"Meriadoc",
    "last_name":"Brandybuck"
}
merry_student_id=students.insert_one(merry)

#Displays info about merry
print("-- INSERT STATEMENTS --")
print("Inserted student record Meriadoc Brandybuck into the students collection with document_id ",merry_student_id.inserted_id)
print("")
print("-- DISPLAYING STUDENT TEST DOC --")
one_student=students.find_one({"student_id": "1010"})
print("Student ID: ", one_student["student_id"], '\n' "First Name: ", one_student["first_name"], '\n' "Last Name: ", one_student["last_name"], '\n' '\n')

#deletes 1010 from database
result=students.delete_one({"student_id": "1010"})

#Displays using find method
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for key in students.find({},{"_id":0}):
    print("Student ID: ",key["student_id"], '\n'  "First Name: ",key["first_name"], '\n'  "Last Name: ",key["last_name"], '\n' )
print("")
print(input("End of program, press any key to continue..."))