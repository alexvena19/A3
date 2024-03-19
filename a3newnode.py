import psycopg2
from psycopg2 import sql


# connects to the PostgreSQL database. It uses the psycopg2 driver to 
# connect to created a3 database
def connection_to_db():
        host = "localhost"
        db_name = "a3"
        user = "postgres"
        password = "postgres"

        connection_string = f"dbname='{db_name}' user='{user}' host='{host}' password='{password}'"

        try:
            connection = psycopg2.connect(connection_string)

            if connection is not None:
                    print("connection successful")
                    return connection
            else:
                print("connection failed")
                return None
        
        except (Exception, psycopg2.DatabaseError) as error:
              print("error connecting to database", error)
              return None

# function to retrieve all students from the students table and print
# them out in an organized table format. Cursor object is created and executes the
# SQL query to selects all students from the table.
def getAllStudents():
      connection = connection_to_db();
      if connection is not None:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM students;")
            students = cursor.fetchall()

            headers = ["ID", "First name", "Last name", "Email", "Enrolment Date"]
            headerFormat = "{:<3} {:<10} {:<10} {:<30} {}".format(*headers)
            print(headerFormat)
            print("-" * len(headerFormat))

            for student in students:
                output_table = "{:<3} {:<10} {:<10} {:<30} {}".format(
                    student[0],  # student_id
                    student[1],  # first_name
                    student[2],  # last_name
                    student[3],  # email
                    student[4].strftime('%Y-%m-%d') 
            )
                print(output_table)
            cursor.close()
            connection.close()

# adds student to the student table, accepting appropriate paramaters for input
# connects to database and creates a cursor, and executes the INSERT INTO query
# to add the student into the table
def addStudent(first_name, last_name, email, enrollment_date):
      connection = connection_to_db();
      if connection is not None:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);", 
                           (first_name, last_name, email, enrollment_date))
            connection.commit()
            cursor.close()
            connection.close()


# updates an exisiting students email based on student ID. If no student
# exists w/ that ID, error message is printed out
def updateStudentEmail(student_id, new_email):
        connection = connection_to_db()
        if connection is not None:
                cursor = connection.cursor()
                try: 
                    cursor.execute("UPDATE students SET email=%s WHERE student_id=%s;",
                               (new_email, student_id))
                    
                    if cursor.rowcount == 0:
                            print("No student found")
                    connection.commit()
                except psycopg2.Error as e:
                        print("Error!")
                        connection.rollback()                

                finally:   
                    cursor.close()
                    connection.close()

# deletes a student from the database table, based on student ID.
def deleteStudent(student_id):
    connection = connection_to_db()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM students WHERE student_id=%s;", (student_id,))
            if cursor.rowcount == 0:
                print("No student found")
            connection.commit()
            connection.commit()

        except psycopg2.Error as e:
            print("Error!")
            connection.rollback()                

        finally:   
            cursor.close()
            connection.close()


#getAllStudents()

## adding student
#addStudent('Alex', 'Vena', 'alexvena@cmail.carleton.ca', '2023-10-01')
#getAllStudents()

## updating a student email
#updateStudentEmail(9, 'updatedemail@email.com')
#getAllStudents()

## deleting a student
#deleteStudent(9)
#getAllStudents()