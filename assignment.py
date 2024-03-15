# customer class
class Customer:
    def __init__(self, name):
      # Checking if name is a string and its length is between 1 and 15 characters
        if not isinstance(name, str):
            raise ValueError("the name must be a string")
        if not (1 <= len(name) <= 15):
            raise ValueError("the name must have characters between 1 and 15")
        self._name = name
        self._orders = []
        
    @property
    def name(self):
        return self._name
        
    def orders(self):
        return self._orders
        # Get unique list of coffees from orders associated with this customer
    def coffees(self):
        return list(set(order.coffee for order in self._orders))
        
    def create_order(self, coffee, price):
       # Create a new order associated with this customer and the provided coffee
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.add_order(order)
        return order
        
    @classmethod
    def most_aficionado(cls, coffee):
      # Find the customer who has spent the most money on the provided coffee
        customers = coffee.customers()
        if not customers:
            return None
        return max(customers, key=lambda customer: sum(order.price for order in customer.orders()))
    
    
# coffee class
class Coffee:
    def __init__(self, name):
       # Checking if name is a string and its length is at least 3 characters
        if not isinstance(name, str):
            raise ValueError("the name must be of type string")
        if len(name) < 3:
            raise ValueError("the name must be equal or greater than 3")
        self._name = name
        self._orders = []
        
    @property
    def name(self):
        return self._name
        
    def orders(self):
        return self._orders
        
    def customers(self):
      # Getting unique list of customers who ordered this coffee
        return list(set(order.customer for order in self._orders))
        
    def add_order(self, order):
      # Adding an order to the list of orders associated with this coffee
        if not isinstance(order, Order):
            raise ValueError("The argument must be an Order instance")
        self._orders.append(order)
        
    def num_orders(self):
      # Getting the total number of orders for this coffee
        return len(self._orders)
        
    def average_price(self):
      # Calculate the average price of orders for  coffee
        if not self._orders:
            return 0
        total = sum(order.price for order in self._orders)
        return total / len(self._orders)
    
    
# order class
class Order:
    def __init__(self, customer, coffee, price):
      # Check if price is a float and within the range of 1.0 to 10.0
        if not isinstance(price, float):
            raise ValueError("Price must be of type float")
        if not (1.0 <= price <= 10.0):
            raise ValueError("the price must be a value between 1.0 and 10.0 included")
        self._customer = customer
        self._coffee = coffee
        self._price = price
        
    @property
    def price(self):
        return self._price
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee


# creting instances for coffee order and customers for testing purposes
# customer
customer1 = Customer("Winnie")
customer2 = Customer("Tess")

# coffee
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

# orders

order1 = customer2.create_order(coffee1, 4.0)
order2 = customer2.create_order(coffee2, 6.0)
# outputs
print("Customer 1 name:", customer1.name)
print("Customer 2 name:", customer2.name)

print("Customer 1 orders:", customer1.orders())
print("Customer 2 orders:", customer2.orders())

print("Customer 1 coffees:", customer1.coffees())
print("Customer 2 coffees:", customer2.coffees())

print("Coffee 1 orders:", coffee1.orders())
print("Coffee 2 orders:", coffee2.orders())

print("Number of orders for Coffee 1:", coffee1.num_orders())
print("Average price for Coffee 1:", coffee1.average_price())

print("Customers who spent a lot on coffee:", Customer.most_aficionado(coffee1))
print("Number of orders for Coffee 2:", coffee2.num_orders())

print("Average price for Coffee 2:", coffee2.average_price())
print("Customers who spent a lot on coffee:", Customer.most_aficionado(coffee2))