from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark
spark = SparkSession.builder \
    .appName("IncrementalLoadDemo") \
    .getOrCreate()

# File paths
yesterday_path = "data/customers_2025-09-05.csv"
today_path = "data/customers_2025-09-06.csv"
output_path = "data/curated_customers.parquet"

# Read yesterday’s data
prev_df = spark.read.csv(yesterday_path, header=True, inferSchema=True)

# Read today’s data
new_df = spark.read.csv(today_path, header=True, inferSchema=True)

# Incremental logic (only new records)
incremental_df = new_df.join(prev_df, on="customer_id", how="left_anti")

# Write output
incremental_df.write.mode("append").parquet(output_path)

print("✅ Incremental load completed. New records added to curated dataset.")
