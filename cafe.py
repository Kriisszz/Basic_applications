#Creating the list of the 4 type of items sold in the cafe.
cafe=["coffee","water","cola","sandwich"]
#Creating the dictionary for the stock.
stock= {'coffee': 15 ,'water':23,'cola':17,'sandwich':9}
#Creating the dictionary for the pricelist.
price={'coffee': 4 ,'water':3,'cola':5,'sandwich':7}
item_value=[]
for item in cafe:
    item_value.append(int(stock[item])*int(price[item]))
print(f"Total value of coffee:£",{item_value[0]},"\n ","Total value of water:£",{item_value[1]},)
print(f"Total value of cola:£",{item_value[2]},"\n","Total value of sandwich:£",{item_value[3]})