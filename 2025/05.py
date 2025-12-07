import time

start = time.time()

ranges = []
products = []
filepath = "input/05.txt"
with open(filepath) as file:
    is_ranges = True
    for line in file:
        if line == "\n":
            is_ranges   = False
            continue

        if is_ranges:
            ranges.append(line.strip())
        else:
            products.append(line.strip())

fresh_products = 0
for product in products:
    is_fresh = False
    for id_range in ranges:
        lower_limit, upper_limit = [int(number) for number in id_range.split('-')]

        if int(product) <= upper_limit and int(product) >= lower_limit:
            # print(f"prodct {product} is fresh!")
            is_fresh = True
            break

    if is_fresh:
        fresh_products += 1

print(f"{fresh_products} fresh products")


end = time.time()
print(f"{end - start:.2f} seconden")

print(list(range(3, 5 + 1)))