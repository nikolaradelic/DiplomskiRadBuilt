import sys
from pyspark.sql import SparkSession

def main(input_path):
    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("Read Parquet Files") \
        .getOrCreate()

    # Read Parquet file
    df = spark.read.parquet(input_path)

    # Show the data
    df.show()

    # Stop SparkSession
    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: read_parquet.py <input_path>")
        sys.exit(-1)

    input_path = sys.argv[1]
    main(input_path)
