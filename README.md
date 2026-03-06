
# 🚀 Real-Time Data Streaming Pipeline
### Kafka • Spark Structured Streaming • Airflow • Cassandra • Prometheus • Grafana

---

# 📌 Project Overview

This project implements a **real-time distributed data engineering pipeline** using modern Big Data technologies.

The system performs the following workflow:

1. Fetches **user data from an external API**
2. Streams data into **Apache Kafka**
3. Processes streaming data using **Spark Structured Streaming**
4. Stores processed records in **Apache Cassandra**
5. Orchestrates ingestion using **Apache Airflow**
6. Monitors infrastructure using **Prometheus and Grafana**

✅ The pipeline has been **tested end‑to‑end** and successfully streams records into Cassandra.

---

# 🏗️ System Architecture

## 🔄 Data Flow

External API  
↓  
Apache Airflow (DAG Trigger)  
↓  
Apache Kafka (user_data topic)  
↓  
Spark Structured Streaming  
↓  
Apache Cassandra (user_keyspace.users)

### Monitoring Layer

Kafka Exporter → Prometheus → Grafana

---

# 🛠️ Technology Stack

| Layer | Technology |
|------|------------|
| Messaging | Apache Kafka |
| Coordination | Zookeeper |
| Stream Processing | Apache Spark 3.5 |
| Orchestration | Apache Airflow 2.6 |
| Storage | Apache Cassandra 4.1 |
| Monitoring | Prometheus |
| Visualization | Grafana |
| Containerization | Docker & Docker Compose |

---

# 📂 Project Structure

realtime_data_streaming/

├── cassandra/  
│ ├── cassandra-env.sh  
│ ├── init.cql  
│ ├── jmxremote.access  
│ └── jmxremote.password  

├── dags/  
│ └── kafka_stream.py  

├── spark/  
│ └── spark_stream.py  

├── monitoring/  
│ ├── prometheus.yml  
│ └── jmx-cassandra.yml  

├── script/  
│ └── entrypoint.sh  

├── docker-compose.yml  
├── requirements.txt  
└── README.md  

---

# 🐳 Infrastructure Overview

All services run inside a dedicated **Docker network**:

confluent

Messaging Layer:
- Zookeeper
- Kafka Broker
- Schema Registry
- Kafka Control Center

Processing Layer:
- Spark Master
- Spark Worker

Orchestration Layer:
- Airflow Webserver
- Airflow Scheduler
- PostgreSQL

Storage Layer:
- Cassandra

Monitoring Layer:
- Prometheus
- Grafana
- Kafka Exporter

---

# 🚀 Running the Project

Start infrastructure:

docker compose up -d

Verify:

docker compose ps

---

# 🌐 Service Access

Airflow → http://localhost:8080  
Kafka Control Center → http://localhost:9021  
Spark UI → http://localhost:8083  
Prometheus → http://localhost:9090  
Grafana → http://localhost:3000  

---

# 📊 Monitoring

Prometheus scrapes metrics from Kafka Exporter.

Grafana visualizes:

- Kafka Brokers
- Topic partitions
- Message throughput
- Consumer lag

---

# 🧠 Engineering Concepts Demonstrated

- Real‑time data streaming
- Event‑driven architecture
- Distributed processing with Spark
- Stream‑to‑NoSQL ingestion
- Workflow orchestration with Airflow
- Monitoring with Prometheus & Grafana
- Containerized distributed systems

---

# 👨‍💻 Author

Hamza Zekri  
Master’s Student — Big Data & Cloud Computing
