def is_number(text):
    """Return True if text is a plain decimal number such as 8.5 or 12."""
    t = text.strip()
    return t.replace(".", "", 1).isdigit()

def read_number_check(text):
    t = text.strip()
    return float(t) if is_number(t) else None

def read_number_try(text):
    try:
        return float(text)
    except ValueError:
        return None

for s in ["8.5", " 8.5 ", "8,5", "eight", "-2", "1e1", ""]:
    print(f"{s!r:9} | isdigit-check -> {read_number_check(s)!s:5} | try/except -> {read_number_try(s)!s:5}")

print()
litres = input("Litres : ")
print(type(litres), repr(litres))
litres = float(litres)
print(type(litres), litres)
print()
print(f"{'ID':<6}{'Litres':>8}{'Fat':>6}{'SNF':>6}{'Rate':>8}{'Amount':>10}")
for fid, l, f, s, r, a in [("F001", 10, 3.5, 8.5, 30.0, 300.0), ("F002", 8.5, 4.2, 8.7, 33.4, 283.9), ("F003", 12, 3.1, 8.3, 27.8, 333.6)]:
    print(f"{fid:<6}{l:8.1f}{f:6.1f}{s:6.1f}{r:8.2f}{a:10.2f}")

import timeit
print()
for s in ["8.5", "eight"]:
    a = timeit.timeit(lambda: read_number_check(s), number=200000) / 200000 * 1e9
    b = timeit.timeit(lambda: read_number_try(s), number=200000) / 200000 * 1e9
    print(f"{s!r:8} isdigit-check {a:6.0f} ns | try/except {b:6.0f} ns")
print("float('nan') accepted by try/except:", read_number_try("nan"))
