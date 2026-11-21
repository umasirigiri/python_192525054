BASE_RATE = 30.00
def rate_per_litre(fat, snf):
    """Return price per litre (float, Rs) for the given fat % and SNF %."""
    return round(BASE_RATE + round((fat - 3.5) / 0.1) * 0.40 + round((snf - 8.5) / 0.1) * 0.30, 2)

def payout(litres, fat, snf):
    """Return the amount payable (Rs) for one entry."""
    return round(litres * rate_per_litre(fat, snf), 2)

def ten_day_total(entries):
    """Return the total of payout() over a list of (litres, fat, snf) tuples."""
    return round(sum(payout(l, f, s) for l, f, s in entries), 2)

def show_payout(litres, fat, snf):      # prints but returns nothing
    print(round(litres * rate_per_litre(fat, snf), 2))

def bad_change():
    BASE_RATE += 1                      # tries to modify a global inside a function
    return BASE_RATE

a = payout(8.5, 4.2, 8.7)
b = show_payout(8.5, 4.2, 8.7)
print("returned value usable   :", a + 1)
print("printing function gives :", b)
try:
    print(bad_change())
except UnboundLocalError as e:
    print("UnboundLocalError:", e)
print(ten_day_total([(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]))
print(rate_per_litre.__doc__)
pay = lambda l, f, s: round(l * (30.0 + round((f-3.5)/0.1)*0.4 + round((s-8.5)/0.1)*0.3), 2)
print("lambda version         :", pay(8.5, 4.2, 8.7))
import timeit, random
random.seed(1)
data = [(round(random.uniform(1, 30), 1), round(random.uniform(3, 5), 1), round(random.uniform(8, 9), 1)) for _ in range(150000)]
t_fn = timeit.timeit(lambda: [payout(*d) for d in data], number=3) / 3
t_in = timeit.timeit(lambda: [round(l * round(30.0 + round((f-3.5)/0.1)*0.4 + round((s-8.5)/0.1)*0.3, 2), 2) for l, f, s in data], number=3) / 3
print(f"n=150000  with functions: {t_fn*1000:7.1f} ms | inline expression: {t_in*1000:7.1f} ms")
