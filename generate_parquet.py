import pandas as pd
import random
import pyarrow as pa
import pyarrow.parquet as pq

# Function to generate random latitude and longitude
def generate_random_coordinates():
    lat = random.uniform(-90, 90)
    lon = random.uniform(-180, 180)
    return lat, lon

# Define the Parquet file path
parquet_file_path = 'test_input.parquet'

# Function to generate rows with random coordinates
def generate_random_rows(row_count):
    data = {'lat1': [], 'lon1': [], 'lat2': [], 'lon2': []}
    for _ in range(row_count):
        lat1, lon1 = generate_random_coordinates()
        lat2, lon2 = generate_random_coordinates()
        data['lat1'].append(lat1)
        data['lon1'].append(lon1)
        data['lat2'].append(lat2)
        data['lon2'].append(lon2)
    return data

# Number of rows to generate (you can change this value)
row_count = 20000000

# Generate the data rows
data = generate_random_rows(row_count)

# Convert to a DataFrame
df = pd.DataFrame(data)

# Write the data to a Parquet file
table = pa.Table.from_pandas(df)
pq.write_table(table, parquet_file_path)

print(f"Test Parquet file created at {parquet_file_path} with {row_count} rows")
