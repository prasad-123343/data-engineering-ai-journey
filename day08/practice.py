# # # def calculate_total (price,quantity) :
# # #     print( price * quantity)
# # # calculate_total(100,3)





# # # def calculate_total(price, quantity):
# # #     # Return the calculated total here
# # #     return price *quantity
    

# # # order_total = calculate_total(150, 4)
# # # print("Order total:", order_total)
# # # print("With delivery charge:", order_total + 50)




# # # def create_order_summary (customer, amount):
# # #    return f"{customer} ordered for {amount}"

# # # summary = create_order_summary("ravi",800)
# # # print(summary)


# # def calculate_order_amount (price,quantity = 1):
# #     return price *  quantity
# # print(calculate_order_amount(300))




# # def calculate_total(price, quantity):
# #     total = price * quantity
# #     return total

# # result = calculate_total(100, 5)
# # print(result)



# # def create_order_summary(customer, price, quantity=1):
# #     total = price * quantity
# #     return f"{customer} ordered for {total}"

# # summary = create_order_summary("Ravi", 250, quantity=3)
# # print(summary)


# # def calculate_bill(customer ,price,quantity=1):
# #     total = price * quantity
# #     return f"{customer}'s bill is {total}"

# # summary = calculate_bill("Priya",200,quantity =3)
# # print(summary)

# # def validate_amount(amount):
# #     if amount < 0:
# #         return "Invalid amount"
# #     return "Valid amount"

# # print(validate_amount(0))



# # def is_valid_quantity(quantity):

# #     if quantity <=  0:
# #         return False
# #     return True

# # print(is_valid_quantity(5))
# # print(is_valid_quantity(0))
# # print(is_valid_quantity(-2))


# def is_valid_quantity(quantity):
#     return quantity > 0
# print(is_valid_quantity(5))
# print(is_valid_quantity(0))
# print(is_valid_quantity(-2))
# print(is_valid_quantity(10.5))
# print(is_valid_quantity("5"))




# Sample order data
orders = [
    {"order_id": 101, "customer": "Ravi", "price": 200, "quantity": 3},
    {"order_id": 102, "customer": "", "price": 150, "quantity": 2},
    {"order_id": 103, "customer": "Priya", "price": -50, "quantity": 1},
    {"order_id": 104, "customer": "Arjun", "price": 100, "quantity": 0},
    {"order_id": 0, "customer": "Kiran", "price": 100, "quantity": 2}
]


# Step 1: Validate each order
def validate_order(order):
    if not order["customer"].strip():
        return False, "Customer is empty"

    if order["price"] < 0:
        return False, "Price is negative"

    if order["quantity"] <= 0:
        return False, "Quantity is invalid"

    if order["order_id"] <= 0:
        return False, "Order ID is invalid"

    return True, "Valid order"


# Step 2: Process all orders
def process_orders(orders):
    valid_orders = []
    rejected_orders = []

    for order in orders:
        is_valid, reason = validate_order(order)

        if is_valid:
            valid_orders.append(order)
        else:
            rejected_orders.append({
                "order": order,
                "rejection_reason": reason
            })

    return valid_orders, rejected_orders


# Step 3: Run the pipeline
valid_orders, rejected_orders = process_orders(orders)


# Step 4: Display the results
print("--- VALID ORDERS ---")
for order in valid_orders:
    print(order)

print("\n--- REJECTED ORDERS ---")
for rejected in rejected_orders:
    print("Order:", rejected["order"])
    print("Reason:", rejected["rejection_reason"])
    print()

print("Total orders:", len(orders))
print("Valid orders:", len(valid_orders))
print("Rejected orders:", len(rejected_orders))

