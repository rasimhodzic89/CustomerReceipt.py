# Describing the lovely loveseat.
lovely_loveseat_description ="""Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
# Price of the lovely loveseat.
lovely_loveseat_price = 254.00

# Describing the syltish settee
stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
# Price of the stylish settee 
stylish_settee_price = 180.50
# Describing the luxurious lamp.
luxurious_lamp_dexcription = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
# Price of the luxurious lamp.
luxurious_lamp_price = 52.15
# Sales tax on items
sales_tax = .088
# First Customer
customer_one_total = (lovely_loveseat_price + luxurious_lamp_price)
customer_one_itemization = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.""" + " " + """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
customer_one_tax = (customer_one_total * sales_tax)
print('Customer One Items')
print(customer_one_itemization)
print('Customer One Total')
print(customer_one_total)