# Packages in python
# a package is a container for multiple modules
# a package is a directory or folder
# a package consist of some related or imp modules not all modules but specific one
# we will create a empty directory or folder as ecommerce which will contain all imp module related to ecommerce

# import entire module
# package + module

# method 1
import ecommerce.shipping
# import any function or class we use this way then call function using package + module
ecommerce.shipping.calculate_shipping()          # output = calculate_shipping

# or
# to directly from package import module and call that function using module

# method 2
from ecommerce import shipping   # import entire module rest 1 and 3 methods are parts
shipping.calculate_shipping()

# or 
# we directly take package+module and import our fuction and then call that function only 

# method 3 
from ecommerce.shipping import calculate_shipping
calculate_shipping()