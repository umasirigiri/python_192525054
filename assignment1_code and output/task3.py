BASE_RATE = 30.00
x = 10
print(type(x), x)
x = "ten"
print(type(x), x)
a, b = 3, 4
a, b = b, a
print("after swap:", a, b)
BASE_RATE = 99          # Python allows this - no true constants
print("BASE_RATE now:", BASE_RATE, "(convention only)")
RATE_CARD = {"base": 30.0, "fat": 0.40, "snf": 0.30}
print(RATE_CARD["base"] + 7 * RATE_CARD["fat"] + 2 * RATE_CARD["snf"])
