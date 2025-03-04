cost_of_things = float(input("Enter price of an item:"))
total_cost = []
while cost_of_things != 0:
    total_cost.append(cost_of_things)
    cost_of_things = float(input("Enter price of another item (if done, enter 0):"))
if cost_of_things == 0:
    actual_total_cost = sum(total_cost)
    if actual_total_cost >= 100:
        actual_total_cost = actual_total_cost*0.9
    else: actual_total_cost = actual_total_cost
print("Your total is:", actual_total_cost)