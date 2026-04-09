# Stackflow_backend_assessment - Technical Assessment

## Overview
This repository is for the technical solution for the StockFlow B2B inventory platform. It contains a code review of existing endpoints, a scalable database schema design, and a low-stock alert API implementation.

## Part 1: Code Review
- Identified issues in API code
- Fixed validation, transaction, and error handling problems

---
## Part 2: Database Design
- Designed schema for:
  - Products
  - Warehouses
  - Inventory
  - Suppliers
- Supports multi-warehouse inventory system
---
## Part 3: Low Stock API
- Detects low stock products
- Works across warehouses
- Includes supplier information
---
## Assumptions
- Products can exist in multiple warehouses
- SKU is unique
- Threshold is fixed
- Simplified sales logic
