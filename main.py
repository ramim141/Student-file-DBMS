import pymysql

# Open database connection
db = pymysql.connect(
    host='localhost',
    user='root',
    password='password',
    database='university' 
)

# Function to create a table
def create_table(table_name, cursor):
    query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                NAME VARCHAR(50) NOT NULL,
                AGE INT,
                GRADE FLOAT
            )
            """
    cursor.execute(query)
    print(f"Table '{table_name}' created successfully.")

# Function to add students
def add_students(NAME, Age, grade, table_name, cursor):
    query = f"""
            INSERT INTO {table_name} (NAME, AGE, GRADE) VALUES (%s, %s, %s)
            """
    cursor.execute(query, (NAME, Age, grade))
    db.commit()
    print("Student inserted successfully!")

# Function to update grade
def update_grade(ID, tableName, newGrade, cursor):
    query = f"""
            UPDATE {tableName} SET GRADE = %s WHERE ID = %s
            """
    cursor.execute(query, (newGrade, ID))
    db.commit()
    print("Grade updated successfully!")

# Function to update age
def update_age(ID, newAge, table_name, cursor):
    query = f"""
            UPDATE {table_name} SET AGE = %s WHERE ID = %s
            """
    cursor.execute(query, (newAge, ID))
    db.commit()
    print("Age updated successfully!")

# Function to view students
def view_students(table_name, cursor):
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    
    allData = cursor.fetchall()
    print("+----------------------------------+")
    print("ID       NAME       AGE      GRADE")
    print("+----------------------------------+")
    for student in allData:
        id, name, age, grade = student
        print(f"{id}    {name}     {age}     {grade}")



# Main program loop
while True:
    print(
        """
    1. Create Table
    2. Add Students
    3. Update Grade
    4. Update Age
    5. View All Students
    6. Exit
        """
    )

    option = int(input("Enter your choice: "))

    if option == 1:
        table_name = input("Enter table name: ")
        create_table(table_name, db.cursor())
        
    elif option == 2:
        table_name = input("Enter table name: ")
        NAME = input("Enter student name: ")
        Age = int(input("Enter age: "))
        grade = float(input("Enter grade: "))
        add_students(NAME, Age, grade, table_name, db.cursor())
        
    elif option == 3:
        table_name = input("Enter table name: ")
        ID = int(input("Enter student ID: "))
        newGrade = float(input("Enter new grade: "))
        update_grade(ID, table_name, newGrade, db.cursor())
        
    elif option == 4:
        table_name = input("Enter table name: ")
        ID = int(input("Enter student ID: "))
        newAge = int(input("Enter new age: "))
        update_age(ID, newAge, table_name, db.cursor())
        
    elif option == 5:
        table_name = input("Enter table name: ")
        view_students(table_name, db.cursor())
        
    elif option == 6:
        break
        
    else:
        print("Invalid Choice")

# Close the database connection when done
db.close()
