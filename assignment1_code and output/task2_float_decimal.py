from decimal import Decimal
payments = ["33.40"] * 1000 + ["0.10"] * 3
print("Decimal(amount)       :", sum((Decimal(a) for a in payments), Decimal("0")))
print("Decimal(float(amount)):", sum((Decimal(float(a)) for a in payments), Decimal("0")))
print(Decimal(33.40))
