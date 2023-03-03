import random
import openpyxl

# Define the list of fruits and vegetables
fruits = ["Apple", "Orange", "Pineapple", "Mango", "Banana"]
vegetables = ["Tomato", "Potato", "Onion", "Garlic", "Cabbage", "Spinach", "Carrot", "Broccoli"]

# Create a workbook and select the active worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active

# Set the number of rows to generate
num_rows = 1000

# Set the maximum number of entries per row
max_entries_per_row = 15

# Loop through each row and randomly generate entries
for i in range(num_rows):
    # Randomly choose the number of entries for this row
    num_entries = random.randint(1, max_entries_per_row)
    
    # Create a list to store the entries for this row
    row_entries = []
    
    # Generate the entries for this row
    while len(row_entries) < num_entries:
        # Randomly choose a fruit or vegetable
        entry = random.choice(fruits + vegetables)
        
        # If this entry is not already in the row, add it
        if entry not in row_entries:
            row_entries.append(entry)
    
    # Write the entries to the worksheet
    for j, entry in enumerate(row_entries):
        worksheet.cell(row=i+1, column=j+1, value=entry)

# Save the workbook
workbook.save("fruits_and_veggies.xlsx")