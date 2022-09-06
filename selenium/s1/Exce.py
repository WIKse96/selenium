itemsInCart = 0

if itemsInCart !=2:
    pass
assert(itemsInCart == 0)

try:
    with open('tekst.txt', 'r') as writer:
        writer.read()
except Exception as e:
    print(e)
finally:
    print("cleaning up resources")