cat << 'EOF' > README.md
# 🛠️ Data Engineering Lab & Practice Repository

[![CI Pipeline](https://github.com/TarasTTN/data-engineering-practice/actions/workflows/ci.yml/badge.svg)](https://github.com/TarasTTN/data-engineering-practice/actions/workflows/ci.yml)
![Python 3.12](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)

A structured repository containing practical data engineering modules, database schemas, storage format benchmarks, and ETL pipelines.

---

## 📂 Repository Architecture

- **`01_python_core/`** — Advanced Python logic: stateful parsing with `Decimal`, memory-efficient `yield` generators, and OOP wrappers.
- **`02_sql_databases/`** — Relational database development (PostgreSQL): DDL schema definitions (`users`, `orders`, `order_items`), constraints, indexes, and analytical queries.
- **`03_storage_formats/`** — Big Data columnar and binary serialization benchmarks (Apache Parquet, Avro, PyArrow).
- **`04_etl_pipelines/`** — End-to-end database replication and ETL pipelines utilizing `psycopg2`, transactional integrity (`commit`/`rollback`), and batch ingestion.
- **`05_data_quality/`** — Defensive data ingestion: schema enforcement, error handling, and quarantine routing for corrupted records.

---

## 🧪 CI/CD & Automated Testing
The repository is automatically verified via **GitHub Actions**:
- **Linting:** Code formatting and PEP 8 enforcement via `ruff`.
- **Unit Testing:** Automated assertions and pipeline sanity checks via `pytest`.
EOF