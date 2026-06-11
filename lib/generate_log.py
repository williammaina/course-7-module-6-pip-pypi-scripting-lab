import os
from datetime import datetime

def generate_log(log_data):
    # 1. Validation: The test expects a ValueError if input is not a list
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list")

    # 2. Filename: Must follow pattern log_YYYYMMDD.txt
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # 3. Write data
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    # 4. Confirmation message: The test checks for this print output
    print(f"Log written to {filename}")
    
    return filename

if __name__ == "__main__":
    # Example usage for when you run the script manually
    data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(data)