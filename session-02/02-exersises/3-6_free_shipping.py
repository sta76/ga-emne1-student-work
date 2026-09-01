order_amount = 800
is_member = True

free_shipping = order_amount >= 800 or is_member
if free_shipping is True:
    print("You get free shipping")
else:
    print("You need to pay a shipping fee")