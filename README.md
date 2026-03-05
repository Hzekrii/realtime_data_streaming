🚀 Real-Time Data Streaming Pipeline
Kafka • Spark • Airflow • Cassandra • Prometheus • Grafana
📌 Project Overview

This project implements a real-time distributed data engineering pipeline using modern Big Data technologies.

The system:

    Fetches user data from an external API
    Streams data into Apache Kafka
    Processes data using Spark Structured Streaming
    Stores processed records in Apache Cassandra
    Orchestrates ingestion using Apache Airflow
    Monitors the infrastructure using Prometheus & Grafana

✅ The pipeline has been tested end‑to‑end and successfully writes streamed records into Cassandra.
🏗️ Architecture
🔄 Data Flow

text

External API
     ↓
Apache Airflow (DAG Trigger)
     ↓
Apache Kafka (user_data topic)
     ↓
Spark Structured Streaming
     ↓
Apache Cassandra (user_keyspace.users table)

Monitoring Layer:
Kafka Exporter → Prometheus → Grafana

🛠️ Technology Stack
Layer	Technology
Messaging	Apache Kafka
Coordination	Zookeeper
Stream Processing	Apache Spark 3.5
Orchestration	Apache Airflow 2.6
Storage	Apache Cassandra 4.1
Monitoring	Prometheus
Visualization	Grafana
Containerization	Docker & Docker Compose
📂 Project Structure

text

Realtime_data_streaming/
│
├── cassandra/
│   ├── cassandra-env.sh
│   ├── init.cql
│   ├── jmxremote.access
│   └── jmxremote.password
│
├── dags/
│   └── kafka_stream.py
│
├── spark/
│   └── spark_stream.py
│
├── monitoring/
│   ├── prometheus.yml
│   └── jmx-cassandra.yml
│
├── script/
│   └── entrypoint.sh
│
├── docker-compose.yml
├── requirements.txt
└── README.md

🐳 Infrastructure Overview

All services run inside a dedicated Docker network:

text

confluent

✅ Messaging Layer

    Zookeeper
    Kafka Broker
    Schema Registry
    Kafka Control Center

✅ Processing Layer

    Spark Master
    Spark Worker

✅ Orchestration Layer

    Airflow Webserver
    Airflow Scheduler
    PostgreSQL (Airflow metadata database)

✅ Storage Layer

    Cassandra

✅ Monitoring Layer

    Prometheus
    Grafana
    Kafka Exporter

✅ Prerequisites

Make sure you have:

    Docker installed
    Docker Compose installed
    At least 8GB RAM available

Verify:

bash

docker --version
docker compose version

🚀 How To Run The Project
1️⃣ Start the Infrastructure

From the project root:

bash

docker compose up -d

This will:

    Pull required images
    Create containers
    Initialize network
    Start all services

2️⃣ Verify Running Containers

bash

docker compose ps

All services should appear as running or healthy.
🌐 Service Access
Service	URL	Credentials
Airflow	http://localhost:8080	admin / admin
Kafka Control Center	http://localhost:9021	-
Spark Master UI	http://localhost:8083	-
Prometheus	http://localhost:9090	-
Grafana	http://localhost:3000	admin / admin
Cassandra	localhost:9042	-
🗄️ Cassandra Setup (Already Tested ✅)

Keyspace created:

sql

CREATE KEYSPACE IF NOT EXISTS user_keyspace
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

Table created:

sql

CREATE TABLE IF NOT EXISTS users (
    username text PRIMARY KEY,
    first_name text,
    last_name text,
    gender text,
    email text
);

Verified:

sql

DESCRIBE TABLES;

Output:

text

users

🔄 Running the Pipeline
✅ Step 1 — Start Spark Streaming Job

Enter Spark container:

bash

docker exec -it spark-master bash

Submit the streaming job:

bash

/opt/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  --conf spark.jars.ivy=/tmp/.ivy2 \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,com.datastax.spark:spark-cassandra-connector_2.12:3.5.0 \
  /opt/spark-apps/spark_stream.py

✅ Leave this running (it runs continuously waiting for Kafka messages).
✅ Step 2 — Trigger Airflow DAG

    Open:

    text

    http://localhost:8080

    Login:

    text

    admin / admin

    Trigger DAG:

    text

    user_automation

Airflow will:

    Fetch users from API
    Publish messages to Kafka topic user_data

✅ Step 3 — Verify Data in Cassandra

bash

docker exec -it cassandra cqlsh

sql

USE user_keyspace;
SELECT * FROM users;

✅ Example Output (Verified):

text

username       | email                         | first_name | gender | last_name
---------------+------------------------------+------------+--------+-----------
greenbear113   | ftmh.aalyzdh@example.com     | فاطمه      | female | علیزاده
bluetiger135   | dean.cooper@example.com      | Dean       | male   | Cooper
heavyduck115   | jordan.garnier@example.com   | Jordan     | male   | Garnier

✅ This confirms end‑to‑end streaming works.
📊 Monitoring & Observability
✅ Spark UI

text

http://localhost:8083

    Shows active streaming job
    Shows worker status
    Shows running applications

✅ Prometheus

text

http://localhost:9090

Scrapes:

    Kafka Exporter
    Prometheus

✅ Grafana

text

http://localhost:3000

Add Prometheus data source:

text

http://prometheus:9090

Useful queries:
Brokers

promql

kafka_brokers

Topic Partitions

promql

kafka_topic_partitions

Messages Produced (Batch‑Friendly)

promql

sum(increase(kafka_topic_partition_current_offset[10m]))

Consumer Lag

promql

kafka_consumergroup_lag

🧠 Key Engineering Concepts Demonstrated

    Real-time data streaming
    Event-driven architecture
    Distributed processing with Spark
    Stream-to-NoSQL ingestion
    DAG orchestration with Airflow
    Kafka topic & partition monitoring
    PromQL usage (increase, rate)
    Containerized distributed systems
    Infrastructure debugging & dependency resolution

🛑 Stopping the Project

Stop containers safely:

bash

docker compose stop

Restart later:

bash

docker compose start

Remove everything:

bash

docker compose down

🎯 Project Statu

✅ End‑to‑end streaming tested
✅ Data successfully written to Cassandra
✅ Distributed Spark cluster operational
✅ Airflow orchestration working
✅ Monitoring layer functional

This project demonstrates a complete real-time data engineering pipeline.
👨‍💻 Author

Master’s Student in Big Data & Cloud Computing
Focused on Data Engineering & Distributed Systems