game = {"item": 0, "profit": 0}

items = [
    {"name": "teeth", "profit": 1, "cost": 0},
    {"name": "rusty scissors", "profit": 5,"cost": 5},
    {"name": "push lawnmower", "profit": 50, "cost": 25},
    {"name": "battery-powered mower", "profit": 100, "cost": 250},
    {"name": "team of starving students", "profit": 250, "cost": 500}
]

### game options
def mow_lawn():
    item = items[game["item"]]
    print(f"You mow a lawn with your {item['name']} and make ${item['profit']}")
    print(f"You have ${game['profit']}")
    game["profit"] += item["profit"]

def check_stats():
    item = items[game["item"]]
    print(f"You currently have ${game['profit']} and are using your {item['name']}")

def upgrade():
    if(game["item"] >= len(items) - 1):
        print("No more items")
        return 0
    next_item = items[game["item"] + 1]
    if(next_item == None):
        print("you earned all the tools")
        return 0
    if(game["profit"] < next_item["cost"]):
        print("get ya paper up fam")
        return 0
    game["profit"] -= next_item["cost"]
    game["item"] += 1

is_playing = True 
    
def win_check():
    if(game["item"] == 4 and game["profit"] >= 1000):
        print("Congratulations, You played yourself")
        is_playing = False
    return False
while (is_playing):
    i = input("[1] Mow A Lawn [2] Check Stats [3] Upgrade [4] Quit")
    i = int(i)
    if(i == 1):
        mow_lawn()
        
    if( i == 2):
        check_stats()
        
    if(i == 3):
        upgrade()
        print(f"You upgraded to the next item!")
        
    if(i == 4): 
         break
     
    if(win_check()):
        break
        