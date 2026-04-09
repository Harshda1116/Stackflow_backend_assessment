def get_low_stock_alerts():
    alerts = []

    # Sample dummy data (represents database)
    products = [
        {
            "id": 1,
            "name": "Widget A",
            "sku": "WID-001",
            "stock": 5,
            "threshold": 20,
            "warehouse": {"id": 1, "name": "Main Warehouse"},
            "supplier": {
                "id": 1,
                "name": "Supplier Corp",
                "contact_email": "orders@supplier.com"
            }
        }
    ]

    for p in products:
        if p["stock"] < p["threshold"]:
            alerts.append({
                "product_id": p["id"],
                "product_name": p["name"],
                "sku": p["sku"],
                "warehouse_id": p["warehouse"]["id"],
                "warehouse_name": p["warehouse"]["name"],
                "current_stock": p["stock"],
                "threshold": p["threshold"],
                "days_until_stockout": p["stock"] // 2,
                "supplier": p["supplier"]
            })

    return {
        "alerts": alerts,
        "total_alerts": len(alerts)
    }
