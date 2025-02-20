grocery_prices={"milk":10,"bread":50,"egg":30,"soap":20}
grocery_quantity={"milk":3,"bread":2,"egg":2,"soap":5}
total_cost=0

for k1,k2 in zip(grocery_prices.keys(),grocery_quantity.keys()):
    total_cost+=(grocery_prices[k1]*grocery_quantity[k2])

print(f"Total cost of groceries is: {total_cost}")