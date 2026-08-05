"""

Problem Statement:

A smart restaurant receives food orders from multiple
customers.

Whenever order processing starts, the system should
automatically establish an order processing session.

After processing all customer orders, the session should
automatically close irrespective of whether the processing
completes successfully or an exception occurs.

Each customer order contains:

Order ID
Customer Name
Food Item
Quantity
Price Per Item

Customer orders should be stored using a dictionary where:

Order ID → (Customer Name, Food Item, Quantity, Price)

The total bill for every customer should be calculated using
a function.

Create a decorator named:

@restaurant_log

The decorator should display:

Restaurant Session Started...

before executing the billing function and

Restaurant Session Completed...

after the function execution.

Create another decorator factory named:

@discount(percentage)

which applies the given discount percentage to the final bill.

The billing function should accept variable positional
arguments (*args) and keyword arguments (**kwargs).

After calculating all bills, generate the customer bills
one by one using a generator.

The generated bills should then be verified one by one
using an iterator.

If quantity is less than or equal to zero,
display:

Invalid Quantity

If price is less than or equal to zero,
display:

Invalid Price

Requirements:

1. Create a Context Manager using __enter__() and __exit__().
2. Create a decorator.
3. Create a decorator with arguments.
4. Use *args.
5. Use **kwargs.
6. Store records using a dictionary.
7. Generate bills using a generator.
8. Verify bills using an iterator.
9. Use raise and try-except.
10. Automatically close the restaurant session.

Input Format:

First line contains the number of customer orders.

Next N sets contain:

Order ID
Customer Name
Food Item
Quantity
Price Per Item

Output Format:

Opening Restaurant Session...

Restaurant Session Started...

Customer Bills:

O101 -> Ravi -> ₹720
O102 -> Priya -> ₹540
O103 -> Rahul -> ₹360

Restaurant Session Completed...

Verified Bills:

O101 -> Ravi -> ₹720
O102 -> Priya -> ₹540
O103 -> Rahul -> ₹360

Restaurant Session Closed

If the number of orders is less than or equal to zero,
display:

Invalid Number of Orders

If quantity is invalid,
display:

Invalid Quantity

If price is invalid,
display:

Invalid Price

Sample Input:

3
O101
Ravi
Pizza
2
400
O102
Priya
Burger
3
200
O103
Rahul
Pasta
2
200

Sample Output:

Opening Restaurant Session...

Restaurant Session Started...

Customer Bills:

O101 -> Ravi -> ₹720
O102 -> Priya -> ₹540
O103 -> Rahul -> ₹360

Restaurant Session Completed...

Verified Bills:

O101 -> Ravi -> ₹720
O102 -> Priya -> ₹540
O103 -> Rahul -> ₹360

Restaurant Session Closed

case=1
input=3
O101
Ravi
Pizza
2
400
O102
Priya
Burger
3
200
O103
Rahul
Pasta
2
200

output=
Opening Restaurant Session...

Restaurant Session Started...

Customer Bills:
O101 -> Ravi -> ₹720
O102 -> Priya -> ₹540
O103 -> Rahul -> ₹360

Restaurant Session Completed...

Verified Bills:
O101 -> Ravi -> ₹720
O102 -> Priya -> ₹540
O103 -> Rahul -> ₹360

Restaurant Session Closed

case=2
input=2
O201
Anu
Sandwich
1
150
O202
Kiran
Coffee
2
100

output=
Opening Restaurant Session...

Restaurant Session Started...

Customer Bills:
O201 -> Anu -> ₹135
O202 -> Kiran -> ₹180

Restaurant Session Completed...

Verified Bills:
O201 -> Anu -> ₹135
O202 -> Kiran -> ₹180

Restaurant Session Closed


case=3
input=1
O301
Mahesh
Biryani
4
250

output=
Opening Restaurant Session...

Restaurant Session Started...

Customer Bills:
O301 -> Mahesh -> ₹900

Restaurant Session Completed...

Verified Bills:
O301 -> Mahesh -> ₹900

Restaurant Session Closed

case=4
input=2
O401
Swetha
Pizza
0
300
O402
Ajay
Burger
2
150

output=
Opening Restaurant Session...
Restaurant Session Closed
Invalid Quantity


case=5
input=1
O601
Pooja
Pizza
2
0

output=
Opening Restaurant Session...
Restaurant Session Closed
Invalid Price


"""
class InvalidQuantityException(Exception):
    pass

class RestaurantSession:
    def __enter__(self):
        print("Opening Restaurant Session...")
        return self
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        print("Restaurant Session Closed")
        return False

def restaurant_log(func):
    def wrapper(*args,**kwargs):
        print()
        print("Restaurant Session Started...")
        print()
        bills = func(*args,**kwargs)
        print("Customer Bills:")
        for order_id,(name,amount) in bills.items():
            print(f"{order_id} -> {name} -> ₹{amount}")
        
        print()
        print("Restaurant Session Completed...")
        return bills
    return wrapper

def discount(percent):
    def decorator(func):
        def wrapper(*args,**kwargs):
            bills = func(*args,**kwargs)
            discounted = {}
            
            for order_id,(name,total) in bills.items():
                final = int(total - (total*percent/100))
                discounted[order_id] = (name,final)
                
            return discounted
        return wrapper
    return decorator

@restaurant_log
@discount(10)
def calculate_bill(*args,**kwargs):
    orders = kwargs["orders"]
    
    bills = {}
    
    
    for order_id,value in orders.items():
        name,food,qty,price = value
        total = qty*price
        bills[order_id] = (name,total)
    return bills

def bill_generator(bills):
    for order_id,(name, amount) in bills.items():
        yield order_id, name, amount

n = int(input())
if n<= 0:
    print("Invalid Number of Orders")
else:
    orders = {}
    try:
        with RestaurantSession():
            for _ in range(n):
                order_id = input()
                name = input()
                food = input()
                qty = int(input())
                price = int(input())
                if qty <= 0:
                    raise InvalidQuantityException("Invalid Quantity")
                if price <= 0:
                    raise ValueError("Invalid Price")
                orders[order_id] = (name,food,qty,price)
            bills = calculate_bill(orders, orders=orders)
                
            print()
            print("Verified Bills:")
             
            g = bill_generator(bills)
            it = iter(g)
            
            while True:
                try:
                    order_id, name , amount = next(it)
                    print(f"{order_id} -> {name} -> ₹{amount}")
                except StopIteration:
                    break
    except InvalidQuantityException as e:
        print(e)
    except ValueError as e:
        print(e)
                
                
                
                
                
                
                
                