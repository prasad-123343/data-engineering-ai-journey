orders = [
    {"order_id": 101, "customer": "Ravi", "amount": 500},
    {"order_id": 102, "customer": "Priya", "amount": -200},
    {"order_id": 103, "customer": "", "amount": 300}
]

valid_orders = []
rejected_orders = []

for order in orders:
    reasons = []

    if not order.get("order_id"):
        reasons.append("Missing order ID")

    if not order.get("customer") or not order["customer"].strip():
        reasons.append("Missing or blank customer")

    if order.get("amount") is None or order["amount"] < 0:
        reasons.append("Amount must be zero or greater")

    if reasons:
        rejected_orders.append({
            "order": order,
            "reasons": reasons
        })
    else:
        valid_orders.append(order)

print("Total orders:", len(orders))
print("Valid order count:", len(valid_orders))
print("Rejected order count:", len(rejected_orders))

print("Valid orders:", valid_orders)
print("Rejected orders:", rejected_orders)


if len(orders) == len(valid_orders) + len(rejected_orders):
    print("Pipeline count check: PASS")
else:
    print("Pipeline count check: FAIL")


if len(orders) > 0:
    rejection_rate = len(rejected_orders) / len(orders) * 100
    print("Rejection rate:", round(rejection_rate, 2), "%")
else:
    print("No orders to process")


# using try and except 

values =    ["100", "250", "abc", "400", "xyz"]


total = 0
invalid_count = 0

for value in values :
    try:
        number = int(value)
        total += number
    except ValueError:
        invalid_count +=1
print("total:",total)
print("no of invalid values:",invalid_count)



orders = [
    {"order_id": 101, "amount": 500},
    {"order_id": 102},
    {"order_id": 103, "amount": 300},
    {"order_id": 104}
]


total = 0
missing_amount_count = 0

for order in orders:
    try:
        amount =order["amount"]
        total += amount
    except KeyError:
        missing_amount_count +=1

print("Total :",total)
print("missing amount count :" ,missing_amount_count)





orders = [
    {"order_id": 201, "amount": "500"},
    {"order_id": 202},
    {"order_id": 203, "amount": "abc"},
    {"order_id": 204, "amount": "300"},
    {"order_id": 205, "amount": "xyz"}
]


# using  key and value errors

Total = 0
Missing_amount_count = 0
Invalid_amount_count = 0

for order in orders:
    try:
        
        amount = order["amount"]
        number = int(amount)
        Total += number

    except ValueError:
         Invalid_amount_count += 1

    except KeyError:
        Missing_amount_count += 1

print("total:",Total)
print("missing amount error:",Missing_amount_count)
print("invalid amount count :",Invalid_amount_count)






# else and finally

values = ["100", "abc", "250"]

for value in values:
       try:
              number = int(value)
       except ValueError:
              print("invalid error")
       else: 
              print("valid error",number)

       finally:
              print("Processing attempt finished")



values = [100, 200, -50, 300, -10]

for value in values:
    try:
        number =int(value)

        if number < 0:
            raise ValueError("negative values are not allowed")
        
        print("accepted :",value)

    except ValueError as error:
        print("rejected:",value,"-",error)