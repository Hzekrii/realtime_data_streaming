from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, udf
from pyspark.sql.types import StructType, StringType
import uuid

# ✅ UDF to generate UUID for each record
def generate_uuid():
    return str(uuid.uuid4())

spark = SparkSession.builder \
    .appName("KafkaToCassandra") \
    .config("spark.cassandra.connection.host", "cassandra") \
    .config("spark.cassandra.connection.port", "9042") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# ✅ Register UUID UDF
uuid_udf = udf(generate_uuid, StringType())

# ✅ Updated schema matching kafka_stream.py format_data()
schema = StructType() \
    .add("first_name", StringType()) \
    .add("last_name", StringType()) \
    .add("gender", StringType()) \
    .add("address", StringType()) \
    .add("postcode", StringType()) \
    .add("email", StringType()) \
    .add("username", StringType()) \
    .add("dob", StringType()) \
    .add("registered_date", StringType()) \
    .add("phone", StringType()) \
    .add("picture", StringType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "broker:29092") \
    .option("subscribe", "user_data") \
    .option("startingOffsets", "earliest") \
    .load()

json_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# ✅ Add UUID as id column - required by Cassandra primary key
final_df = json_df.withColumn("id", uuid_udf())

query = final_df.writeStream \
    .format("org.apache.spark.sql.cassandra") \
    .option("keyspace", "user_keyspace") \
    .option("table", "users") \
    .option("checkpointLocation", "/tmp/checkpoint") \
    .start()

query.awaitTermination()