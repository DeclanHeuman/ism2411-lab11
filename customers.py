
# Reflection 1:
# I would use .get() when a key might not exist and I want to avoid an error.
# I would use bracket notation when I know the key exists and need its value.
# My rule of thumb is to use .get() for optional information and brackets for required information.

# Reflection 2:
# The summary dictionary pattern reminds me of using SUMIF in Excel because it
# adds values that match a specific category. Python is more useful for large
# datasets because it can process many records automatically and be customized.

# EXERCISE 1

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250
}

print("EXERCISE 1")
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# EXERCISE 2

print("\nEXERCISE 2")

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# EXERCISE 3

print("\nEXERCISE 3")

email = customer.get("email", "no email on file")
print(email)

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist in the dictionary")


# EXERCISE 4

print("\nEXERCISE 4")

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives you the keys.
# With .items(), the loop gives you both the keys and their values.

for key in customer:
    print(key)


# EXERCISE 5

print("\nEXERCISE 5")

tier_discounts = {
    "bronze": 0,
    "silver": .05,
    "gold": .10,
    "platinum": .15
}

tier = customer["tier"]
discount_rate = tier_discounts.get(tier, 0)
purchase_price = 200
final_price = purchase_price - (purchase_price * discount_rate)

print(f"Tier: {tier}")
print(f"Discount rate: {discount_rate * 100}%")
print(f"Final price: ${final_price:.2f}")


# EXERCISE 6

print("\nEXERCISE 6")

customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]

for person in customers:
    tier = person["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(
        f"{person['name']} | {tier} | "
        f"Discount: ${discount_amount:.2f}"
    )


# EXERCISE 7

print("\nEXERCISE 7")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(
            f"LOW STOCK: {product} "
            f"({details['stock']} remaining)"
        )


# EXERCISE 8

print("\nEXERCISE 8")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(f"{region}: ${sales_summary[region]:.2f}")
