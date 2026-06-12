# 📊 TimeSeries Database Benchmark

A comparative performance analysis of **InfluxDB**, **TimescaleDB**, and **MariaDB ColumnStore** under different workloads and dataset sizes.

This project evaluates the behavior of three popular database management systems when handling time-series data, focusing on query performance, throughput, CPU utilization, memory consumption, and storage requirements.


## Project Objective

Time-series databases have become increasingly important in areas such as IoT, monitoring systems, observability platforms, industrial automation, and analytics.

The objective of this study was to compare the performance characteristics of:

* **InfluxDB**
* **TimescaleDB**
* **MariaDB ColumnStore**

under controlled experimental conditions and determine which database performs best across different scenarios.


## 🛠 Technologies Used

### Databases

<p>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="48"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/influxdb/influxdb-original.svg" width="48"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mariadb/mariadb-original.svg" width="48"/>
</p>

### Data Analysis

<p>
  <img src="https://skillicons.dev/icons?i=python" />
</p>


## 📈 Evaluated Metrics

The following metrics were collected and analyzed:

* Simple query execution time
* Aggregated query execution time
* Throughput
* CPU utilization
* Memory utilization
* Storage consumption

Each database was evaluated using:

* Small datasets
* Medium datasets
* Large datasets


## Experimental Methodology

The benchmark was conducted using the same workloads and query patterns across all database systems.

For every experiment:

1. Data was loaded into each database.
2. Identical query sets were executed.
3. Resource utilization was monitored.
4. Results were statistically analyzed.

The study includes:

* Descriptive statistics
* ANOVA analysis
* Tukey HSD post-hoc testing
* Graphical comparisons


## 📊 Results

### Simple Query Execution Time

TimescaleDB consistently achieved the best response times across all dataset sizes due to its efficient indexing mechanisms and PostgreSQL-based query optimization.

<p align="center">
  <img src="figures/fig_tiempo_simple_pequeno.png" width="300">
  <img src="figures/fig_tiempo_simple_mediano.png" width="300">
  <img src="figures/fig_tiempo_simple_grande.png" width="300">
</p>


### Aggregated Query Execution Time

InfluxDB demonstrated superior performance for aggregation-heavy workloads, benefiting from its architecture specifically designed for time-series processing.

<p align="center">
  <img src="figures/fig_tiempo_agregado_pequeno.png" width="300">
  <img src="figures/fig_tiempo_agregado_mediano.png" width="300">
  <img src="figures/fig_tiempo_agregado_grande.png" width="300">
</p>


### Throughput

InfluxDB generally achieved the highest throughput values, while TimescaleDB remained competitive under moderate workloads.

<p align="center">
  <img src="figures/fig_throughput_pequeno.png" width="300">
  <img src="figures/fig_throughput_mediano.png" width="300">
  <img src="figures/fig_throughput_grande.png" width="300">
</p>


### CPU Utilization

CPU consumption remained relatively stable across experiments, although InfluxDB typically consumed more processing resources in exchange for better performance.

<p align="center">
  <img src="figures/fig_cpu_pequeno.png" width="300">
  <img src="figures/fig_cpu_mediano.png" width="300">
  <img src="figures/fig_cpu_grande.png" width="300">
</p>


### Memory Utilization

Memory requirements varied significantly between systems, with some databases prioritizing performance at the cost of increased memory usage.

<p align="center">
  <img src="figures/fig_memoria_pequeno.png" width="300">
  <img src="figures/fig_memoria_mediano.png" width="300">
  <img src="figures/fig_memoria_grande.png" width="300">
</p>


### Storage Consumption

Storage efficiency was analyzed to determine the cost of maintaining large-scale time-series datasets.

<p align="center">
  <img src="figures/fig_almacenamiento_pequeno.png" width="300">
  <img src="figures/fig_almacenamiento_mediano.png" width="300">
  <img src="figures/fig_almacenamiento_grande.png" width="300">
</p>


## Statistical Analysis

The project includes formal statistical validation of the collected data using:

* One-Way ANOVA
* Tukey HSD Tests
* Confidence Intervals
* Pairwise Comparisons

These methods were used to determine whether observed performance differences were statistically significant.
