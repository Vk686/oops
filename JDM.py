import json 

with open('food.json') as f:
    data = json.load(f)

for food in data['foods']:
    print(food) 