people_list = []  # List to store names, ID numbers, sub-counties, and selection flags
import random
import string



current_weekend_names = []  # List to store names selected for the current weekend
last_weekend_date = None  # Variable to keep track of the last weekend's date


# Rest of the code remains the same as before...

# Function to pick names for the current weekend
def pick_names_for_weekend(sub_county):
    global current_weekend_names, people_list

    current_weekend_names = []  # Clear the list of names for the current weekend
    selected_names = []

    # Filter individuals from the specified sub-county who have not been selected yet
    for person in people_list:
        name, id_number, person_sub_county, is_selected = person
        if person_sub_county == sub_county and not is_selected:
            selected_names.append(name)

    if not selected_names:
        print("All names have been picked. Weekend selection is complete.")
        return

    # Randomly select names from the list of eligible individuals
    random.shuffle(selected_names)

    # Select the first batch of names for the current weekend
    current_weekend_names = selected_names[:6]

    # Mark the selected names as already chosen in the main list
    for person in people_list:
        name, _, person_sub_county, _ = person
        if name in current_weekend_names and person_sub_county == sub_county:
            person[3] = True  # Update the is_selected flag

# Rest of the code remains the same as before...
# Function to check if it's the next weekend
def is_next_weekend():
    global last_weekend_date
    # Compare the current date with the date of the last weekend
    # You may need to use a date library for this comparison
    # If the current date is one week or more ahead of the last weekend, return True
    # Otherwise, return False
    pass
all_names_picked = False

# Example usage
# Input the names, ID numbers, and sub-counties of individuals into the database or list
# Assuming people_info is a list of tuples (name, ID number, sub-county) containing the information
people_info = [
    ["John Doe", "ID001", "Kiambu", False],
    ["Jane Smith", "ID002", "Kiambu", False],
    ["Michael Johnson", "ID003", "Kiambu", False],
    ["Emily Williams", "ID004", "Kiambu", False],
    ["William Brown", "ID005", "Kiambu", False],
    ["Olivia Taylor", "ID006", "Kiambu", False],
    ["James Miller", "ID007", "Kiambu", False],
    ["Sophia Anderson", "ID008", "Kiambu", False],
    ["Benjamin Martinez", "ID009", "Kiambu", False],
    ["Isabella Hernandez", "ID010", "Kiambu", False],
    ["Elijah Thompson", "ID011", "Kiambu", False],
    ["Mia Garcia", "ID012", "Kiambu", False],
    ["Alexander Robinson", "ID013", "Kiambu", False],
    ["Ava Lopez", "ID014", "Kiambu", False],
    ["Daniel Hill", "ID015", "Kiambu", False],
    ["Charlotte Scott", "ID016", "Kiambu", False],
    ["Matthew Green", "ID017", "Kiambu", False],
    ["Amelia Adams", "ID018", "Kiambu", False],
    ["Samuel Lewis", "ID019", "Kiambu", False],
    ["Harper Carter", "ID020", "Kiambu", False]
]

for person_info in people_info:
    people_list.append([person_info[0], person_info[1], person_info[2], False])

# Loop until all names are picked
while not all_names_picked:
    # Assuming today's date is '2023-07-31'
    if is_next_weekend():
        # Reset the selection flags for all individuals to allow them to be picked again
        for person in people_list:
            person[3] = False

    # Pick names for this weekend (assuming sub-county is "Kiambu")
    pick_names_for_weekend("Kiambu")

    # Check if all names have been picked
    all_names_picked = all(person[3] for person in people_list)

    print("Weekend selection for Kiambu:", current_weekend_names)





