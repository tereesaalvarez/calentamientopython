shipping_cost_per_kg = 1.20
customer_basket_cost = 34
customer_basket_weight = 44
if (customer_basket_cost >= 100):
    print("No hay gastos de envio")
else:
    print("El precio de su envio es:")
    shipping_cost = customer_basket_weight*shipping_cost_per_kg
    print(shipping_cost)
    print("El precio total de la cesta es:")
    print(shipping_cost + customer_basket_cost)