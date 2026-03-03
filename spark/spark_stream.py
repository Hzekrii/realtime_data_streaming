from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType

spark = SparkSession.builder \
    .appName("KafkaToCassandra") \
    .config("spark.cassandra.connection.host", "cassandra") \
    .getOrCreate()

schema = StructType() \
    .add("first_name", StringType()) \
    .add("last_name", StringType()) \
    .add("gender", StringType()) \
    .add("email", StringType()) \
    .add("username", StringType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "broker:29092") \
    .option("subscribe", "user_data") \
    .option("startingOffsets", "earliest") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

query = json_df.writeStream \
    .format("org.apache.spark.sql.cassandra") \
    .option("keyspace", "user_keyspace") \
    .option("table", "users") \
    .option("checkpointLocation", "/tmp/checkpoint") \
    .start()

query.awaitTermination()