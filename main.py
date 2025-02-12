from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, col

spark = SparkSession.builder.appName("Transactions").getOrCreate()

user_data = [(1, "Alice"), (2, "Bob"), (3, "Charlie"), (4, "Raghav")]
user_columns = ["user_id", "name"]
user_df = spark.createDataFrame(user_data, user_columns)

transactions_data = transactions = [(1, 100, "2023-01-01"), (1, 200, "2023-01-02"), (2, 300, "2023-01-03"),
 (2, 200, "2023-01-01"), (3, 500, "2023-01-01" ), (4, 300, "2023-01-01")] 
transactions_columns = ["user_id", "amount", "date"]
transactions_df = spark.createDataFrame(transactions_data, transactions_columns)

#user_df.show()
#transactions_df.show()

transactions_total_amount = transactions_df.groupBy("user_id").agg(sum("amount").alias("total_amount"))
#transactions_total_amount.show()
result_df = transactions_total_amount.join(user_df, "user_id")

sorted_df = result_df.orderBy(col("total_amount").desc())

#input
K = 4

#output
sorted_df.show(K)
