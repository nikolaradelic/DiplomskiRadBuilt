import csv
import random

# Function to generate random latitude and longitude
def generate_random_coordinates():
    lat = random.uniform(-90, 90)
    lon = random.uniform(-180, 180)
    return lat, lon

# Define the CSV file path
csv_file_path = 'test_input.csv'

# Define the column names
fieldnames = ['lat1', 'lon1', 'lat2', 'lon2']

# Function to generate rows with random coordinates
def generate_random_rows(row_count):
    rows = []
    for _ in range(row_count):
        lat1, lon1 = generate_random_coordinates()
        lat2, lon2 = generate_random_coordinates()
        rows.append({'lat1': lat1, 'lon1': lon1, 'lat2': lat2, 'lon2': lon2})
    return rows

# Number of rows to generate (you can change this value)
row_count = 20000000

# Generate the data rows
rows = generate_random_rows(row_count)

# Write the data to a CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Test CSV file created at {csv_file_path} with {row_count} rows")

