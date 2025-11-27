weight = 41.5
#Ground Shipping
if weight <= 2:
   ground_shipping_cost = weight * 1.50 + 20.00
   print('Ground Shipping =' + '',ground_shipping_cost)
elif weight <= 6:
   ground_shipping_cost = weight * 3.00 + 20.00
   print('Ground Shipping =' + '',ground_shipping_cost)
elif weight <= 10:
   ground_shipping_cost = weight * 4.00 + 20.00
   print('Ground Shipping =' + '',ground_shipping_cost)
elif weight >= 10:
   ground_shipping_cost = weight * 4.75 + 20.00
   print('Ground Shipping =' + '',ground_shipping_cost)
else:
   print(N/A) 
# Price of Premium Shipping
ground_shipping_premium = 125.00
print('Ground Shipping Premium =' + '',ground_shipping_premium) 
# Drone Shipping
if weight <= 2:
   drone_shipping_cost = weight * 4.50
   print('Drone Shipping =' + '',drone_shipping_cost)
elif weight <= 6:
   drone_shipping_cost = weight * 9.00
   print('Drone Shipping =' + '',drone_shipping_cost)
elif weight <= 10:
  drone_shipping_cost = weight * 12.00
  print('Drone Shipping =' + '',drone_shipping_cost)
elif weight >= 10:
  drone_shipping_cost = weight * 14.25
  print('Drone Shipping =' + '',drone_shipping_cost)
else:
  print(N/A)              