import random
import string
import sqlite3
from faker import Faker

# Function to create a Faker object
def create_faker():
    return Faker()

# Function to generate a random name using Faker
def generate_random_name(faker):
    return faker.first_name().lower()

# Function to generate a random ID number
def generate_random_id():
    return ''.join(random.choice(string.digits) for i in range(8))

# Function to generate a random sub-county
def generate_random_sub_county():
    sub_counties = ['kiambu', 'nairobi', 'mombasa', 'kisumu', 'eldoret']
    return random.choice(sub_counties)

# Function to create the 'people' table if it doesn't exist
def create_people_table():
    conn = sqlite3.connect('weekend_event.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY,
            name TEXT,
            id_number TEXT,
            sub_county TEXT,
            is_selected INTEGER,
            weekend_num INTEGER
        )
    ''')

    conn.commit()
    conn.close()

# Function to fill the database with dummy data
def fill_database_with_dummy_data(num_entries):
    conn = sqlite3.connect('weekend_event.db')
    c = conn.cursor()

    for i in range(num_entries):
        # Create a Faker object
        faker = create_faker()

        # Generate a random name
        name = generate_random_name(faker)
        id_number = generate_random_id()
        sub_county = generate_random_sub_county()

        # Insert the data into the database and set is_selected and weekend_num to 0
        c.execute('INSERT INTO people (name, id_number, sub_county, is_selected, weekend_num) VALUES (?, ?, ?, ?, ?)',
                  (name, id_number, sub_county, 0, 0))

    conn.commit()
    conn.close()


# Check if the 'people' table exists, and create it if not
create_people_table()

# Fill the database with 200 dummy entries
fill_database_with_dummy_data(20)


# Function to print the first 5 rows from the database
def print_first_5_rows():
    conn = sqlite3.connect('weekend_event.db')
    c = conn.cursor()

    # Retrieve the first 5 rows from the 'people' table
    c.execute('SELECT * FROM people LIMIT 5')
    rows = c.fetchall()

    print("First 5 rows from the database:")
    for row in rows:
        print(row)

    


# Print the first 5 rows as proof
print_first_5_rows()
# Function to get user input for individuals' information
def get_user_input():
    name = input("Enter name: ")
    id_number = input("Enter ID number: ")
    sub_county = input("Enter sub-county: ")

    # Connect to the SQLite database
    conn = sqlite3.connect('weekend_event.db')
    c = conn.cursor()

    # Insert the user input into the database
    c.execute('INSERT INTO people (name, id_number, sub_county, is_selected, weekend_num) VALUES (?, ?, ?, ?, ?)',
              (name, id_number, sub_county, 0, 0))

    # Commit the changes
    conn.commit()
    

# Function to check if all names have been picked
def check_all_names_picked(sub_county):
    conn = sqlite3.connect('weekend_event.db')
    c = conn.cursor()
    c.execute('SELECT is_selected FROM people WHERE sub_county = ? AND is_selected = 0', (sub_county,))
    all_names_picked = len(c.fetchall()) == 0
    conn.close()
    return all_names_picked

# Function to pick one name for the current weekend
def pick_name_for_weekend(sub_county, weekend_num):
    # Connect to the SQLite database
    conn = sqlite3.connect('weekend_event.db')
    c = conn.cursor()

    # Filter individuals from the specified sub-county who have not been selected yet
    c.execute('SELECT name FROM people WHERE sub_county = ? AND is_selected = ? AND weekend_num = ?',
              (sub_county, 0, 0))
    selected_names = [row[0] for row in c.fetchall()]

    if not selected_names:
        # If there are no names from user-input data, select from dummy data
        c.execute('SELECT name FROM people WHERE sub_county = ? AND is_selected = ? AND weekend_num = ?',
                  ('', 0, 0))
        selected_names = [row[0] for row in c.fetchall()]
        if not selected_names:
            print("All names have been picked. Weekend selection is complete.")
            conn.close()
            return None

    # Randomly select one name from the list of eligible individuals
    name_to_pick = random.choice(selected_names)

    # Mark the selected name as already chosen for the current weekend in the database
    c.execute('UPDATE people SET is_selected = ?, weekend_num = ? WHERE name = ? AND sub_county = ?',
              (1, weekend_num, name_to_pick, sub_county))

    # Commit the changes
    conn.commit()
    conn.close()

    print(f"Weekend {weekend_num} selection for {sub_county}: {name_to_pick}")
    return name_to_pick# Function to get the last weekend number from the database
def get_last_weekend_number():
    conn = sqlite3.connect('weekend_event.db')
    c = conn.cursor()
    c.execute('SELECT MAX(weekend_num) FROM people')
    last_weekend_number = c.fetchone()[0]
    conn.close()
    return last_weekend_number if last_weekend_number else 0

# Create a connection to the SQLite database
conn = sqlite3.connect('weekend_event.db')
c = conn.cursor()

# Create a table to store individuals' information if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY,
        name TEXT,
        id_number TEXT,
        sub_county TEXT,
        is_selected INTEGER,
        weekend_num INTEGER
    )
          
    
''')


# Commit the changes
conn.commit()
conn.close()

# Example usage: Get user input for individuals' information and insert into the database
num_people = int(input("Enter the number of people you want to add: "))
for _ in range(num_people):
    get_user_input()

# Function to perform the weekend selection process
def perform_weekend_selection():
    # Get the last weekend number from the database
    weekend_num = get_last_weekend_number() + 1

    # Loop until all names are picked for each sub-county
    while True:
        sub_county = input("Enter the sub-county to select names for (or enter 'exit' to end): ")
        if sub_county.lower() == 'exit':
            print("Weekend selection is complete.")
            break

        if check_all_names_picked(sub_county):
            print(f"All names have been picked for {sub_county}.")
        else:
            selected_name = pick_name_for_weekend(sub_county, weekend_num)
            if selected_name is None:
                print("No more names to pick for this sub-county.")
            else:
                weekend_num += 1

# Call the function to perform the weekend selection process
perform_weekend_selection()