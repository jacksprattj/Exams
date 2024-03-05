#Student Name=Jack Spratt


print("Household budget calculator")
print("Information:")
num_adults = int(input("Please enter the amount of Adults in your houshold: "))
num_child = int(input("Please enter the amount of Children in your houshold: "))
inflation = int(input("Please enter a inflation rate: "))
food_budget = 300
cost_food_adult = 50
cost_food_child = 35

child_allowance = 140
extra_child = 20
print("Children's allowance total: €", child_allowance*num_child)
print("Total household food cost: €", cost_food_adult*num_adults+cost_food_child*num_child)
if num_child> <3:
    print("Children's allowance total: €", child_allowance*num_child+extra_child)
print("Total household food cost with onflation: €", cost_food_adult*num_adults+cost_food_child*num_child+inflation)
total_houshold_food_cost_with_inflation = print("Percentage spend on food: %" , cost_food_adult%cost_food_child%num_child%num_adults)
print("Budget remaining after food spend: €" , Childrens allowance total+food_budget-Total household food cost with inflation)