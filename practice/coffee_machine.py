# espresso 
# 50ml water
# 18g coffee
# $1.50

# latte
# 200ml water
# 24g coffee
# 150ml milk
# $2.50

# cappuccino
# 250ml water
# 24g coffee
# 100ml milk
# $3.00

# start with
# 300ml water
# 200ml milk
# 100g coffee

menu ={"espresso":{"ingredients":{"water":50,"coffee":18},"money":1.50},
       "latte":{"ingredients":{"water":200,"coffee":24,"milk":150},"money":2.50},
       "cappuccino":{"ingredients":{"water":250,"coffee":24,"milk":100},"money":3.00}}
   
#initial   
water = 300
milk = 200
coffee = 100
money = 0
     
#asking money
def ask_money(n,order):
    global money
    quarters = int(input("quarters:"))
    dimes = int(input("dimes:"))
    nickles = int(input("nickles:"))
    pennies = int(input("pennies:"))

    total = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    change = total - n
    
    if(total<n):
        print("need more")
    else:
        print(f"your change is ${change}")
        money  += menu[order]["money"]
    

flag = True

while (flag):
    order = input("What would you like? (espresso/latte/cappuccino):").lower()
    if (order == "report"):
        print(f"Water:{water}")
        print(f"milk:{milk}")
        print(f"coffee:{coffee}")
        print(f"money earned:${money}")
    
    elif (order == "off"):
        flag =False

    elif (order == "espresso"):
        if(menu[order]["ingredients"]["water"] < water):
            water -= menu[order]["ingredients"]["water"]
            if(menu[order]["ingredients"]["coffee"] < coffee):
                coffee -= menu[order]["ingredients"]["coffee"]
                print(f"you will need to pay ${menu[order]["money"]}")
                ask_money(menu[order]["money"],order)
                #money  +=menu[order]["money"]
        else:
            print("we dont have the resources")
    
    elif (order == "latte"):
        if(menu[order]["ingredients"]["water"] < water):
            water -= menu[order]["ingredients"]["water"]
            if(menu[order]["ingredients"]["milk"] < milk):
                milk -= menu[order]["ingredients"]["milk"]
                if(menu[order]["ingredients"]["coffee"] < coffee):
                    coffee -= menu[order]["ingredients"]["coffee"]
                    print(f"you will need to pay ${menu[order]["money"]}")
                    ask_money(menu[order]["money"],order)
                    #money  +=menu[order]["money"]
        else:
            print("we dont have the resources")
    
    elif (order == "cappuccino"):
        if(menu[order]["ingredients"]["water"] < water):
            water -= menu[order]["ingredients"]["water"]
            if(menu[order]["ingredients"]["milk"] < milk):
                milk -= menu[order]["ingredients"]["milk"]
                if(menu[order]["ingredients"]["coffee"] < coffee):
                    coffee -= menu[order]["ingredients"]["coffee"]
                    print(f"you will need to pay ${menu[order]["money"]}")
                    ask_money(menu[order]["money"],order)
                    #money  +=menu[order]["money"]
        else:
            print("we dont have the resources")       
             
    elif (order == "refill"):
        water += 300
        milk += 200
        coffee += 100
        
    else:
        print("invalid input")
        
    