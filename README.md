# Spark Transactions Example

## Overview
This project demonstrates how to use Apache Spark to process transaction data and identify the top K users with the highest total transaction amounts.

## Requirements
- Apache Spark
- Python 3.x
- PySpark

## Installation
Ensure you have PySpark installed. You can install it using:
```sh
pip install pyspark
```

## Usage
1. Initialize a Spark session.
2. Create sample user and transaction data.
3. Compute the total transaction amount per user.
4. Join the transaction totals with user data to get user names.
5. Sort the users by total transaction amount in descending order.
6. Display the top K users.

## Code Explanation
- **SparkSession Initialization**: Required to run Spark operations.
- **Data Creation**: Two DataFrames - `user_df` (user details) and `transactions_df` (transaction records).
- **Aggregation**: Computes total transaction amount per user.
- **Join Operation**: Merges the transaction totals with user details.
- **Sorting**: Orders the results by total transaction amount in descending order.
- **Displaying Results**: Outputs the top K users.

## Example Output
```
+-------+-------------+-------+
|user_id|total_amount|  name |
+-------+-------------+-------+
|      3|        500 |Charlie|
|      2|        500 |  Bob  |
|      1|        300 | Alice |
|      4|        300 |Raghav |
+-------+-------------+-------+
```

## Customization
Modify the `K` variable in the script to change the number of top users displayed.
