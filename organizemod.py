'''parent_directory/
   	main.py
	ecommerce/
		__init__.py
		database.py
		products.py
		payments/
			__init__.py
			square.py
			stripe.py
'''
# Absolute imports
import ecommerce.products
product = ecommerce.products.Product()

from ecommerce.products import Product
product = Product()

from ecommerce import products
product = products.Product()

# Relative imports
# Asume cd parent_directory/ecomerce
from .database import Database

# asume cd parent_directory/ecomerce/paypal/
from ..database import Database
