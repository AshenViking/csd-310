from pymongo import MongoClient
url= "mongodb+srv://admin:admin@cluster0.qvqxw.mongodb.net/pytech?retryWrites=true&w=majority";
client=MongoClient(url)
db = client.pytech
students=db.students
bob = {
    "student_id":"1007",
    "first_name":"Bob",
    "last_name":"Billy Bob"
}
jerry={
    "student_id":"1008",
    "first_name":"Jerry",
    "last_name":"Jonas"
}
bethany={
    "student_id":"1009",
    "first_name":"Bethany",
    "last_name":"BellBottom"
}
bob_student_id=students.insert_one(bob)
jerry_student_id=students.insert_one(jerry)
bethany_student_id=students.insert_one(bethany)
print("-- INSERT STATEMENTS --")
print("Inserted student record Bob Billy Bobinto the student collection with document_ID ",bob_student_id.inserted_id)
print("Inserted student record Jerry Jonas into the student collection with document_ID ",jerry_student_id)
print("Inserted student record Bethany BellBottom into the student collection with document_ID ",bethany_student_id)
print("")
print("")
print(input("End of program, press any key to exit..."))