import csv

# Define the CSV file path
csv_file_path = 'test_input.csv'

# Define the column names
fieldnames = ['lat1', 'lon1', 'lat2', 'lon2']

# Define the data rows
rows = [
    {'lat1': 40.7128, 'lon1': -74.0060, 'lat2': 34.0522, 'lon2': -118.2437},
    {'lat1': 51.5074, 'lon1': -0.1278, 'lat2': 48.8566, 'lon2': 2.3522},
    {'lat1': 35.6895, 'lon1': 139.6917, 'lat2': 37.7749, 'lon2': -122.4194}
]

# Write the data to a CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Test CSV file created at {csv_file_path}")
