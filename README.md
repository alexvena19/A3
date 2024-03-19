# A3

SETUP INSTRUCTIONS:
1. Start by installing psycopg2 if not already installed. In your terminal, enter 'pip install psycopg2'
2. Create the students table in your database on PgAdmin 4.
3. Run query:
   SELECT * FROM public.students
   ORDER BY student_id ASC

Running instructions:
1. At this point, you can run the a3newnode.py file.
2. After a function is called, call getAllStudents() after it to output the results.

Function explanations:
connection_to_db():
connects to the PostgreSQL database. It uses the psycopg2 driver to connect to created a3 database

getAllStudents():
function to retrieve all students from the students table and print them out in an organized table format. Cursor object is created and executes the SQL query to selects all students from the table.

addStudent(first_name, last_name, email, enrollment_date):
adds student to the student table, accepting appropriate paramaters for input connects to database and creates a cursor, and executes the INSERT INTO query to add the student into the table

updateStudentEmail(student_id, new_email):
updates an exisiting students email based on student ID. If no student exists w/ that ID, error message is printed out

deleteStudent(student_id):
deletes a student from the database table, based on student ID.


# DATABASE QUERIES
CREATE TABLE students (
	student_id SERIAL,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	email	VARCHAR(255) UNIQUE NOT NULL,
	enrollment_date 	DATE,
	PRIMARY KEY(student_id)
);

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');




