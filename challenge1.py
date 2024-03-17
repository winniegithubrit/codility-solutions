class Customer:
  # defining the customer class with its respective arguments
    def __init__(self, first_name, last_name):
      # Initialize a private attribute _first_name and last_name to None
        self._first_name = None
        self._last_name = None
        # Call the setter method for first_name and last_name attribute to set its value
        self.first_name = first_name
        self.last_name = last_name
 # Define a property getter method for first_name and return the value of the private attribute
    @property
    def first_name(self):
        return self._first_name
# Define a setter method for first_name property
    @first_name.setter
    # Check if value is not a string
    def first_name(self, value):
        if not isinstance(value, str):
            raise ValueError("First name must be of type string")
          # Check if length of value is not between 1 and 25 characters
        if not 1 <= len(value) <= 25:
            raise ValueError("First name must be between 1 and 25 characters")
         # Set the value of _first_name attribute to the given value
        self._first_name = value
# same theory as the first_name
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Last name must be of type string")
        if not 1 <= len(value) <= 25:
            raise ValueError("Last name must be between 1 and 25 characters")
        self._last_name = value

# classes and instances
class Restaurant:
  # classes and instance methods
    def __init__(self, name):
        self._name = None
        # Call the setter method for name attribute to set its value
        self.name = name
        # Initialize a private attribute _reviews as an empty list
# Variable Scope: Defines an empty list to store reviews
        self._reviews = []
# Define a property getter method for name
    @property
    def name(self):
        return self._name
# Define a setter method for name property
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be of type string")
        if len(value) < 1:
            raise ValueError("Name must be at least 1 character")
        self._name = value
# Define a method to add a review to the restaurant
    def add_review(self, review):
      # Object Relationships: Adds a review to the list of reviews associated with the restaurant
       # Check if review is not an instance of Review class
        if not isinstance(review, Review):
            raise ValueError("Review must be an instance of Class Review")
         # Add the review to the list of reviews
        self._reviews.append(review)
# Define a method to get all reviews for the restaurant
    def reviews(self):
       # Object Relationships: Returns a list of all reviews for the restaurant
        return self._reviews

# Define the Review class
class Review:
    def __init__(self, customer, restaurant, rating):
        # Object Relationships: Initializes a Review instance with a customer, restaurant, and rating
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
# Define a property getter method for rating
    @property
    def rating(self):
      # Return the value of the private attribute _rating
        return self._rating
 # Define a setter method for rating property
    @rating.setter
    # Define the setter method for rating property with value as argument
    def rating(self, value):
       # Check if value is not an integer
        if not isinstance(value, int):
            raise ValueError("Rating must be of type integer")
          # Check if value is not between 1 and 5
        if not 1 <= value <= 5:
            raise ValueError("Rating must be between 1 and 5")
        self._rating = value



    #  Customer tests
customer = Customer("Winnie", "Jomo")
print(customer.first_name) 
print(customer.last_name)  

    # Restaurant  tests
restaurant = Restaurant("Sarova")
print(restaurant.name)  

    # Review  tests
review = Review(customer, restaurant, 3)
print(review.rating)  
