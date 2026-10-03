# def greet(name):
#     print(name + ", welcome to data engineering!")
# greet("mahesh")

# # using return
# def greet (name):
#     return name + ", welcome to data engineering!"
# message = greet("mahesh")
# print(message)


# # using another example
# def greet(name):
#     return name + ", welcome to data engineering!"
# message = greet("Ravi")
# print(message)



# # another example
# def calculate_total(price, quantity):
#     return price * quantity
# total = calculate_total(250, 4)
# total1 = calculate_total(150, 3)
# total2 = calculate_total(500, 2)
# print("Total amount:", total)
# print("Total amount:", total1)
# print("Total amount:", total2)


# Create a function named calculate_sum that:
# Accepts a list called amounts.
# Returns the sum of all values in that list using Python's built-in sum() function.
# Call it with [100, 200, 300, 400].
# Store the result in total and print it.

# def calculate_sum(amounts):
#     return sum(amounts)

# total = calculate_sum([100, 200, 300, 400])
# print("Total amount:", total)



# Next exercise: Calculate the average
# Modify your function or create a new function named calculate_average(amounts) that:
# Accepts a list of numbers.
# Returns the average using sum() and len().
# Calls the function with [100, 200, 300, 400].
# Stores the result in average and prints it.
# Hint: Average = sum of values ÷ number of values.

# def calculate_average(amounts):
#     if len(amounts) == 0:
#         return None  # Handle empty list case to avoid division by zero
#     return sum(amounts) / len(amounts)

# average = calculate_average([100, 200, 300, 400])
# print("Average amount:", average)

# empty_average = calculate_average([])
# print("Average amount for empty list:", empty_average)


# order = {
#     "order_id": 101,
#     "quantity": 3,
#     "price": 250
# }

# def get_order_total(order):
#     return order["price"] * order["quantity"]
# total1 = get_order_total(order)
# print("Total amount for order 101:", total1)




# product = {
#     "product_id": 301,
#     "name": "Laptop",
#     "price": 45000,
#     "quantity": 2
# }

# def calculate_product_total(product):
#     return product["price"] * product["quantity"]
# total2 = calculate_product_total(product)
# print("Total amount for product 301:", total2)




# Create a function calculate_product_total(product).
# Use a for loop to go through each product.
# Calculate each product's total using the function.
# Print each product's name and total price.

# products = [
#     {"product_id": 301, "name": "Laptop", "price": 45000, "quantity": 2},
#     {"product_id": 302, "name": "Mouse", "price": 500, "quantity": 3},
#     {"product_id": 303, "name": "Keyboard", "price": 1200, "quantity": 2}
# ]


# def calculate_products_total(products):
#     return sum(product["price"] * product["quantity"] for product in products)
# grand_total = 0
# for product in products:
#     total = calculate_products_total([product])
#     print("Total amount for " + product["name"] + ": " + str(total))  
#     grand_total += total

# print("Grand total amount:", grand_total)





orders = [
    {"order_id": 101, "customer": "Ravi", "price": 250, "quantity": 3},
    {"order_id": 102, "customer": "Mahesh", "price": 500, "quantity": 2},
    {"order_id": 103, "customer": "Ravi", "price": 150, "quantity": 4},
    {"order_id": 104, "customer": "Priya", "price": 300, "quantity": 2},
    {"order_id": 105, "customer": "Mahesh", "price": 200, "quantity": 5}
]

# customer_revenue = {}
# for order in orders:
#     customer = order["customer"]
#     total = order["price"] * order["quantity"]
#     if customer in customer_revenue:
#         customer_revenue[customer] += total
#     else:
#         customer_revenue[customer] = total
# print(customer_revenue)


        # Next step: Make it reusable

        # Let's put your working logic into a function called calculate_customer_revenue(orders) that accepts the list of orders and returns the customer revenue dictionary.

        # You already have most of the solution. Move your existing code inside the function, return customer_revenue, and then call the function with orders.

# def calculate_customer_revenue(orders):
#     customer_revenue = {}
#     for order in orders:
#         customer = order["customer"]
#         total = order["price"] * order["quantity"]
#         if customer in customer_revenue:
#             customer_revenue[customer] += total
#         else:
#             customer_revenue[customer] = total
#     return customer_revenue

# customer_summary = calculate_customer_revenue(orders)
# print(customer_summary)



# # Let's extend your function's output. Using the customer_summary dictionary, write code to find the customer with the highest revenue and print their name and revenue.
# customer_summary = calculate_customer_revenue(orders)
# highest_revenue_customer = max(customer_summary, key=customer_summary.get)
# print("Customer with highest revenue and revenue:", highest_revenue_customer, customer_summary[highest_revenue_customer])


# for customer, revenue in customer_summary.items():
#     if revenue > 1000:
#         print("Customer with revenue greater than 1000:", customer, revenue)




# highest_revenue_customers = {}

# for customer, revenue in customer_summary.items():
#     if revenue > 1000:
#         highest_revenue_customers[customer] = revenue

# # Using your high_revenue_customers dictionary, write code to count how many customers have revenue greater than ₹1,000, and print the count.

# count_high_revenue_customers = len(highest_revenue_customers)
# print("Number of customers with revenue greater than 1000:", count_high_revenue_customers)





# Next step: Put it all together
# Let's now combine these operations into one reusable function that returns:
# Total revenue per customer
# The highest-revenue customer
# Customers with revenue greater than ₹1,000
# The count of those customers


import json

def analyze_customer_revenue(orders):
    customer_revenue = {}

    for order in orders:
        customer = order["customer"]
        total = order["price"] * order["quantity"]

        if customer in customer_revenue:
            customer_revenue[customer] += total
        else:
            customer_revenue[customer] = total
    if not customer_revenue:
        return {
            "customer_revenue": {},
            "highest_revenue_customer": None,
            "high_revenue_customers": {},
            "count_high_revenue_customers": 0
        }

    highest_revenue_customer = max(customer_revenue, key=customer_revenue.get)
    highest_revenue_amount = customer_revenue[highest_revenue_customer]

    high_revenue_customers = {customer: revenue for customer, revenue in customer_revenue.items() if revenue > 1500}
    count_high_revenue_customers = len(high_revenue_customers)

    return {
        "customer_revenue": customer_revenue,
        "highest_revenue_customer": (highest_revenue_customer, highest_revenue_amount),
        "high_revenue_customers": high_revenue_customers,
        "count_high_revenue_customers": count_high_revenue_customers
    }


with open("orders.json", "r") as file:
    orders = json.load(file)

print(orders)