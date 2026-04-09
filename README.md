# Stackflow_backend_assessment - Technical Assessment
## Overview
This repository contains the technical solution for the StockFlow B2B inventory platform. It includes a code review of existing endpoints, a scalable database schema design, and a low-stock alert API implementation.

## Structure
* `debugging`: Analysis and corrected code for the Product Creation API.
* `db_design`: SQL schema and design justifications.
* `api`: Flask-based implementation of the Low-Stock Alert endpoint.

## Key Design Principles
* **Data Integrity:** Used database transactions and Decimal types for financial accuracy.
* **Auditability:** Implemented inventory logging to track stock movements.
* **Scalability:** Optimized schema with indexing for multi-warehouse queries.
