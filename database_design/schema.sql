CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE warehouses (
    id SERIAL PRIMARY KEY,
    company_id INT REFERENCES companies(id),
    name TEXT,
    location TEXT
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    company_id INT REFERENCES companies(id),
    name TEXT,
    sku TEXT UNIQUE,
    price DECIMAL
);

CREATE TABLE inventory (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id),
    warehouse_id INT REFERENCES warehouses(id),
    quantity INT,
    UNIQUE(product_id, warehouse_id)
);

CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    company_id INT,
    name TEXT,
    contact_email TEXT
);
