from collections import OrderedDict


items = OrderedDict()


n = int(input())


for i in range(n):
  
    item_name, price = input().rsplit(' ', 1)
    price = int(price)
    
  
    items[item_name] = items.get(item_name, 0) + price


for item_name, price in items.items():
    print(item_name, price)
