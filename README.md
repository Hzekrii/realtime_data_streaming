# 🚀 Real-Time Data Streaming Pipeline

![Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?style=flat&logo=apachekafka&logoColor=white)
![Spark](https://img.shields.io/badge/Apache%20Spark-E25A1C?style=flat&logo=apachespark&logoColor=white)
![Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=flat&logo=apacheairflow&logoColor=white)
![Cassandra](https://img.shields.io/badge/Cassandra-1287B1?style=flat&logo=apachecassandra&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=flat&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=flat&logo=grafana&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

---

## 📌 Project Overview

Modern data platforms increasingly require **real-time data processing** rather than traditional batch pipelines. This project demonstrates how to build a distributed streaming data architecture using popular technologies from the Big Data ecosystem.

The system **ingests** user data from an external API, **streams** it through a messaging system, **processes** it in real time, and **stores** the results in a distributed database — while exposing metrics for monitoring.

### Key Objectives

- ⚡ Build a real-time streaming pipeline
- 🔄 Demonstrate event-driven architecture
- 🔥 Process streaming data with Spark Structured Streaming
- 🗄️ Store results in a distributed NoSQL database
- 🕹️ Orchestrate ingestion workflows with Airflow
- 📊 Monitor the system with Prometheus and Grafana
- 🐳 Deploy the entire infrastructure using Docker containers

> ✅ The pipeline has been successfully tested end-to-end, from ingestion to storage and monitoring.

---

## 🏗️ System Architecture

### High-Level Architecture

```
External API
     │
     ▼
Apache Airflow (DAG)
     │
     ▼
Apache Kafka (Streaming Broker)
     │
     ▼
Spark Structured Streaming
     │
     ▼
Apache Cassandra (NoSQL Storage)
```

### Monitoring Layer

```
Kafka Exporter
      │
      ▼
Prometheus
      │
      ▼
Grafana
```

---

## 🔄 Data Pipeline Workflow

### 1️⃣ Data Ingestion

Apache Airflow periodically triggers a DAG that retrieves user data from an external API.

**Example API used:**
```
https://randomuser.me/api/
```

Airflow sends this data to a Kafka topic.

### 2️⃣ Message Streaming (Kafka)

Apache Kafka acts as a distributed messaging system. It:

- Receives messages from Airflow
- Stores them in the topic `user_data`
- Allows consumers (Spark) to read the stream

Kafka ensures **scalability**, **fault tolerance**, and **high throughput messaging**.

### 3️⃣ Stream Processing (Spark)

Spark Structured Streaming continuously reads messages from Kafka via:

```
spark/spark_stream.py
```

**Responsibilities:**
- Consume Kafka messages
- Parse JSON user data
- Transform records
- Insert processed data into Cassandra

> Spark processes data in **micro-batches**, enabling near real-time processing.

### 4️⃣ Data Storage (Cassandra)

Processed records are stored in:

| Property | Value |
|----------|-------|
| Keyspace | `user_keyspace` |
| Table | `users` |

Cassandra is used for its **distributed storage**, **high availability**, **horizontal scalability**, and **fast write throughput**.

### 5️⃣ Monitoring

System metrics are collected using **Kafka Exporter → Prometheus → Grafana**.

Grafana visualizes metrics such as:
- Broker health
- Message throughput
- Consumer lag
- Topic partitions

---

## 🛠️ Technology Stack

| Layer | Technology |
|-------|------------|
| Messaging | Apache Kafka |
| Coordination | Zookeeper |
| Stream Processing | Apache Spark 3.5 |
| Workflow Orchestration | Apache Airflow 2.6 |
| Database | Apache Cassandra 4.1 |
| Monitoring | Prometheus |
| Visualization | Grafana |
| Containerization | Docker |
| Infrastructure | Docker Compose |

---

## 📂 Project Structure

```
realtime_data_streaming/
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
```

### Important Components

| File | Description |
|------|-------------|
| `dags/kafka_stream.py` | Airflow DAG — fetches API data and produces Kafka messages |
| `spark/spark_stream.py` | Spark app — consumes Kafka streams and writes to Cassandra |
| `monitoring/prometheus.yml` | Prometheus config — defines metric scrape targets |
| `cassandra/init.cql` | Initial Cassandra schema (keyspace + table definitions) |

---

## 🐳 Infrastructure Overview

All services run inside a **shared Docker network**, organized into layers:

### Messaging Layer
- Zookeeper
- Kafka Broker
- Schema Registry
- Kafka Control Center — [`http://localhost:9021`](http://localhost:9021)

### Processing Layer
- Spark Master
- Spark Worker
- Spark UI — [`http://localhost:8083`](http://localhost:8083)

### Orchestration Layer
- Airflow Webserver
- Airflow Scheduler
- PostgreSQL (Airflow metadata database)
- Airflow UI — [`http://localhost:8080`](http://localhost:8080)

### Storage Layer
- Apache Cassandra — stores processed user records

### Monitoring Layer
- Prometheus — collects metrics
- Grafana — visualizes dashboards
- Kafka Exporter

---

## ⚙️ Prerequisites

Ensure the following tools are installed before running the project:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Git](https://git-scm.com/)

Verify installations:

```bash
docker --version
docker compose version
git --version
```

---

## 🚀 Running the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/realtime_data_streaming.git
cd realtime_data_streaming
```

### 2️⃣ Start the Infrastructure

```bash
docker compose up -d
```

This launches: Kafka, Spark, Airflow, Cassandra, Prometheus, and Grafana.

### 3️⃣ Verify Running Containers

```bash
docker compose ps
```

All services should appear as **running**.

---

## 🌐 Service Access

| Service | URL |
|---------|-----|
| Airflow | [http://localhost:8080](http://localhost:8080) |
| Kafka Control Center | [http://localhost:9021](http://localhost:9021) |
| Spark UI | [http://localhost:8083](http://localhost:8083) |
| Prometheus | [http://localhost:9090](http://localhost:9090) |
| Grafana | [http://localhost:3000](http://localhost:3000) |

> **Default Grafana credentials:** `admin` / `admin`

---

## ▶️ Running the Data Pipeline

1. Open Airflow at [`http://localhost:8080`](http://localhost:8080)
2. Enable the DAG: **`kafka_stream`**
3. Trigger the DAG manually

Airflow will **fetch API data** and **send messages to Kafka**.

---

## 🔎 Verifying the Pipeline

### Kafka
Check topic messages inside **Kafka Control Center**.

### Spark
Open **Spark UI** and verify streaming jobs are active.

### Cassandra

Enter the Cassandra container:

```bash
docker exec -it cassandra cqlsh
```

Query the stored data:

```sql
SELECT * FROM user_keyspace.users;
```

You should see the streamed records.

---

## 📊 Monitoring

Open Grafana at [`http://localhost:3000`](http://localhost:3000).

**Available dashboards:**
- Kafka Broker metrics
- Message throughput
- Topic partitions
- Consumer lag

---

## 🧠 Engineering Concepts Demonstrated

This project showcases key Data Engineering concepts:

- ⚡ Real-time data pipelines
- 🔄 Event-driven architecture
- 📨 Distributed messaging systems
- 🔥 Stream processing
- 🗄️ NoSQL distributed storage
- 🕹️ Workflow orchestration
- 📊 Infrastructure monitoring
- 🐳 Containerized microservices architecture

---

## 🔮 Possible Improvements

- [ ] Add Kafka Connect for additional source/sink connectors
- [ ] Implement schema validation
- [ ] Add data quality checks
- [ ] Scale Spark workers horizontally
- [ ] Deploy on Kubernetes
- [ ] Add alerting rules with Prometheus

---

## 👨‍💻 Author

**Hamza Zekri**  
*Master's Student — Big Data & Cloud Computing*
