import time

start = time.time()

filepath = "input/04.txt"
with open(filepath) as file:
    pass

end = time.time()
print(f"{end - start:.2f} seconden")