# 🚀 Incremental Load with PySpark

This project demonstrates how to build an **incremental ETL pipeline** with PySpark.  
Instead of reloading the full dataset daily, the pipeline processes **only new or updated records**, making it efficient and cost-effective.

## 📌 Use Case
- Data engineers often face huge daily datasets.
- Reloading all data is costly and slow.
- Solution: Incremental load → process only new records.

## ⚙️ Tech Stack
- Python 3.x
- Apache Spark / PySpark
- Sample CSV data

## 📂 Project Structure
```
spark-incremental-load/
│── README.md
│── data/
│   ├── customers_2025-09-05.csv
│   ├── customers_2025-09-06.csv
│── scripts/
│   ├── incremental_load.py
```

## 🏗️ Incremental Logic
1. Read yesterday’s curated data (Parquet).
2. Read today’s raw data (CSV).
3. Compare using **customer_id**.
4. Append only new/updated records.

## ▶️ Run Script
```bash
spark-submit scripts/incremental_load.py
```

## 📊 Example Output
- Input:  
  - `customers_2025-09-05.csv` (yesterday’s customers)  
  - `customers_2025-09-06.csv` (today’s customers)  
- Output:  
  - Only new customers are appended to the curated dataset.

✅ This project is for learning/demo purposes. You can extend it with S3, Delta Lake, or Airflow orchestration.
