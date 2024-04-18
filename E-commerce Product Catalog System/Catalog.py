'''
Modular Design: Break down your application into logical modules. For instance, in the E-commerce Product Catalog System, 
you can have separate modules for the base class Product, and each subclass like Book, Electronic, and Clothing.

Reusability: By using modules, you can easily reuse code. For example, the Product module can be imported into each 
product subclass module, eliminating the need to rewrite common attributes and methods.

Maintainability: With modular code, making changes or updates becomes simpler and less risky. 
If you need to modify the Product class, you do it in one place, and the changes propagate through all subclasses.

Testing: Testing modules independently becomes more straightforward. You can write and run tests for each module 
to ensure its functionality before integrating it into the main system.

Importing Modules: Use the import statement to include modules in your main application script. For example, 
from product import Product would import the Product class from the product.py module.

Directory Structure: Organize your modules in a clear directory structure. For example, all product-related 
modules can reside in a products directory.

Naming Conventions: Follow Python naming conventions for your modules. Typically, module names should be lowercase 
with underscores to improve readability (e.g., smart_device.py).

Documenting Modules: Provide documentation for each module. A brief comment at the beginning of each module explaining 
its purpose and functionality can be very helpful. By adhering to a modular approach, your 
solutions for the assignments will not only be more effective and efficient but also align with industry standards. 
This practice will prepare you for larger-scale projects in your programming career.
'''
# Add a general product with minimal values needed ID,Name and price. Also being able to get those locked/private attributes to be able to see
# Them without an error happening.


class Product:
  def __init__(self,product_id, name, price):
    self.__product_id = product_id
    self.__name = name
    self.__price = price

  def get_product_id(self):
    return self.__product_id
  
  def get_name(self):
    return self.__name
  
  def get_price(self):
    return self.__price
  # Do not have a set new price but could go and do that at another time. I wanted  to practice working with setters
  def set_price(self,new_price):
    self.__price = new_price

  def display_info(self):
      print(f"ID Number-{self.get_product_id()}: {self.get_name()} cost ${self.get_price()}")

# This is building on the parent for a specific type (category books) of it.
class Book(Product):
  def __init__(self, product_id, name, price, author):
    super().__init__(product_id, name, price)
    self.__author = author
  
  def get_author(self):
    return self.__author
  
  def display_info(self):
    print(f"ID Number-{self.get_product_id()}: {self.get_name()} cost ${self.get_price()}\nAuthor:\n{self.__author}")

# This is building on the parent for a specific type (category electronics) of it.
class Electronic(Product):
  def __init__(self, product_id, name, price, specs):
    super().__init__(product_id, name, price)
    self.__specs = specs

  def get_specs(self):
    return self.__specs
  
  def display_info(self):
    print(f"ID Number-{self.get_product_id()}: {self.get_name()} cost ${self.get_price()}\nSpecs:\n{self.__specs}")

# This is building on the parent for a specific type (category clothing) of it.
class Clothing(Product):
  def __init__(self, product_id, name, price, size):
    super().__init__(product_id, name, price)
    self.__size = size

  def get_type(self):
    return self.__size

  def display_info(self):
    print(f"ID Number-{self.get_product_id()}: {self.get_name()} cost ${self.get_price()}\nSize: {self.__size}")
