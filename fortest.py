import sqlite3

connection = sqlite3.connect('students.db')
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    name TEXT,
    score INTEGER
)
''')

while True:

    name = input("ples enter name : ")
    score = int(input("enter score :"))
    
    if name.lower() == 'exit':
        break

    
    cursor.execute("""INSERT INTO students (name, score) VALUES (?, ?)""", (name, score))


connection.commit()



print("\n show deta :")
cursor.execute("""SELECT * FROM students""")
for row in cursor.fetchall():
    print(f" name: {row[0]} | score: {row[1]}")
while True:
    enter=input("do you want search,updet,delet , sort of score just writ wich one :")
    if enter=="updet":
        name=input("wich one just wrut name for update :")
        ask=input("do you want edit name y/n:")
        if ask=="y":
            newneame=input("writ new name :")
            cursor.execute("""UPDATE students SET name=? WHERE name=?""",(newneame,name))
            connection.commit()
            print("\n show deta :")
            cursor.execute("""SELECT * FROM students""")
            for row in cursor.fetchall():
                print(f" name: {row[0]} | score: {row[1]}")
        else:
            score=int(input("new score : "))
            cursor.execute("""UPDATE students SET score=? WHERE name=?""",(score,name))
            connection.commit()
            print("\n show deta :")
            cursor.execute("""SELECT * FROM students""")
            for row in cursor.fetchall():
                print(f" name: {row[0]} | score: {row[1]}")
    if enter=="delet":
        name = input("Enter name for deletion: ")
        sql = "DELETE FROM students WHERE name = ?"
        name_tuple = (name,)  
        cursor.execute(sql, name_tuple)
        connection.commit()
        print("\n show deta :")
        cursor.execute("""SELECT * FROM students""")
        for row in cursor.fetchall():
            print(f" name: {row[0]} | score: {row[1]}")
        print(name_tuple,"is deleted ")
    if enter=="search":
        name=input("name of student : ")
        sql = "SELECT * FROM students WHERE name LIKE ?"
        cursor.execute(sql, (name,))

        # Fetch the search results
        search_results = cursor.fetchall()

        # Check if any results were found
        if search_results:
            print("\nSearch Results:")
            for row in search_results:
                print(f"Name: {row[0]} | Score: {row[1]}")
        else:
            print("No student found with the given name.")
    if enter == "sort":
        print("\nShow sorted data:")
        cursor.execute("""SELECT * FROM students ORDER BY score DESC""")  
        for row in cursor.fetchall():
            print(f"Name: {row[0]} | Score: {row[1]}")

    if enter=="no":
        print(" so bay bye")
        break
connection.close()