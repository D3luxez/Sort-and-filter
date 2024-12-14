from replit import db

# Create a table-like structure in the database
db["employees"] = [
  ["employee_id", "employee_name", "department", "salary"], 
  [1, "John Doe", "Sales", 50000],
  [2, "Jane Smith", "Marketing", 60000],
  [3, "Peter Jones", "Sales", 45000],
  [4, "Mary Brown", "Marketing", 55000]
]

# Access and print data from the database
print(db["employees"])