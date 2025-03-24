from collections import OrderedDict

# Read input
n = int(input().strip())
ordered_dict = OrderedDict()

# Process items
for _ in range(n):
    *item_name, price = input().rsplit(maxsplit=1)  # Split last value as price
    item_name = " ".join(item_name)  # Join the rest as item name
    ordered_dict[item_name] = ordered_dict.get(item_name, 0) + int(price)

# Print output
for item, net_price in ordered_dict.items():
    print(item, net_price)
