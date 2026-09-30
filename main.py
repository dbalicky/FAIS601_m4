# Imports the calculator function from the calculator module in the app folder
from app.calculator import calculator

# Runs only when this file is directly executed 
# __name__ is a special variable in Python. When run directly, Python sets it to "__main__"
if __name__ == "__main__":
    # Starts the calculator program
    calculator()