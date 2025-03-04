تمرین اول  
سیستم‌های توزیع‌شده  
**سید امیرمسعود میرکاظمی**  
**۴۰۳۶۱۶۰۲۰۰۳**

**Data Engineering Roadmap for Distributed Systems**

---

## **1\. Foundations of Distributed Data Engineering**

* **Distributed Computing Principles**  
  * CAP Theorem  
  * Consistency vs. Availability vs. Partition Tolerance  
  * Fault Tolerance & Scalability  
* **Data Storage & Movement**  
  * Data Lake vs. Data Warehouse vs. Lakehouse  
  * Distributed File Systems (HDFS, S3, MinIO)  
  * Columnar vs. Row-Based Storage

---

## **2\. Storage Layer: Distributed Storage & Databases**

### **A. Data Warehousing & Analytical Storage**

* **OLAP vs. OLTP vs. HTAP**

* **Data Modeling for OLAP**  
  * Star Schema, Snowflake Schema  
  * Partitioning, Clustering, Indexing  
* **Columnar Storage & Query Engines**  
  * Parquet & ORC  
  * Apache Iceberg for Data Lake Optimization  
  * DuckDB & StarRocks for Analytical Workloads  
* **Merge Tree Storage Engines (ClickHouse)**  
  * ClickHouse Architecture  
  * Sharding & Replication  
  * Distributed Query Processing

### **B. NoSQL & Distributed Databases**

* **Column-Family Databases (ScyllaDB, Cassandra)**  
  * Column-Family Data Model  
  * Distributed Architecture & Virtual Nodes  
  * Replication & Consistency  
* **Object Storage for Distributed Systems**  
  * MinIO: Private S3-compatible Storage  
  * Iceberg vs. Delta Lake

---

## **3\. Kafka & Event-Driven Architecture**

### **A. Kafka Fundamentals**

* Kafka Architecture & Components  
  * Brokers, Partitions, Topics  
  * Producers & Consumers  
* Kafka Storage Internals  
  * Log Segments & Retention Policies  
* Kafka Performance Tuning  
  * Message Batching  
  * Compression & Acks

### **B. Kafka Stream Processing**

* Kafka Streams API vs. ksqlDB  
* Stateful Stream Processing  
* Windowing Operations (Sliding, Tumbling, Session Windows)  
* Handling Out-of-Order Data with Watermarks

### **C. Kafka Integration with Other Systems**

* Kafka Connect  
  * Connecting to Databases (JDBC, MongoDB, Elasticsearch)  
  * S3 & HDFS Integration  
* Kafka \+ Spark Structured Streaming

---

## **4\. Distributed Data Processing: Apache Spark**

### **A. Batch Processing**

* DataFrame Transformations  
* Aggregations & Joins  
* Processing Complex Data Types (Arrays, Structs)  
* Handling Missing Values  
* Managing Type Safety with DataFrames  
* Spark Internals & Optimizations (Catalyst Optimizer, Tungsten Execution)

### **B. Stream Processing**

* **Structured Streaming**

  * Real-time Joins, Aggregations, and Windowing  
  * Watermarking & Event-Time Processing  
* **DStreams for Low-Level Control**

  * Operations: Map, FlatMap, Filter, Reduce  
  * Windowing: Sliding, Tumbling, Reduce by Key  
* **Integration with External Sources**

  * Kafka, JDBC, Data Lakes, Delta Lake

---

## **5\. Orchestration & Containerization**

### **A. Containerized Data Pipelines**

* **Docker & Kubernetes Basics**  
  * Running Spark in Kubernetes  
  * Managing Data Workloads in Containers

### **B. Workflow Orchestration**

* **Apache Airflow** (Task Scheduling & DAGs)  
* **Kubernetes Operators** for Spark, Kafka, ClickHouse

