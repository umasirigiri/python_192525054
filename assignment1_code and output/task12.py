from decimal import Decimal
import milkrate, milkrate2 as m2

print("A. Impact of two-decimal readings (fat 4.23, snf 8.57, 10 L)")
print("   float step test (4.23-3.5)/0.1 =", (4.23 - 3.5) / 0.1, "-> round() gives", round((4.23 - 3.5) / 0.1))
print("   ORIGINAL design  rate:", milkrate.rate_per_litre(4.23, 8.57), " payout:", milkrate.payout(10, 4.23, 8.57))
print("   REVISED design   rate:", m2.rate_per_litre("4.23", "8.57"), " payout:", m2.payout(10, "4.23", "8.57"))
print()
print("B. Original design under the new season rates (fat 4.2, snf 8.7)")
print("   ORIGINAL (summer ignored):", milkrate.rate_per_litre(4.2, 8.7), "  REVISED summer:", m2.rate_per_litre("4.2", "8.7", "summer"))
print()
print("C/D. Tests")
tests = [
 ("normal, standard milk",        m2.rate_per_litre("3.5", "8.5", "normal"),   "30.00"),
 ("normal, 4.2 / 8.7",            m2.rate_per_litre("4.2", "8.7", "normal"),   "33.40"),
 ("summer, standard milk",        m2.rate_per_litre("3.5", "8.5", "summer"),   "32.00"),
 ("summer, 4.2 / 8.7",            m2.rate_per_litre("4.2", "8.7", "summer"),   "35.75"),
 ("summer, 3.1 / 8.3",            m2.rate_per_litre("3.1", "8.3", "summer"),   "29.60"),
 ("2-decimal normal 4.23 / 8.57", m2.rate_per_litre("4.23", "8.57", "normal"), "33.13"),
 ("2-decimal summer 4.23 / 8.57", m2.rate_per_litre("4.23", "8.57", "summer"), "35.50"),
 ("season_of(3)",                 m2.season_of(3), "normal"),
 ("season_of(4)",                 m2.season_of(4), "summer"),
 ("season_of(6)",                 m2.season_of(6), "summer"),
 ("season_of(7)",                 m2.season_of(7), "normal"),
 ("bonus at exactly 500 L",       m2.bonus(500),    "0.00"),
 ("bonus at 500.01 L",            m2.bonus("500.01"), "250.01"),
 ("bonus at 650 L",               m2.bonus(650),    "325.00"),
]
print(f"{'Case':<32}{'Expected':>10}{'Actual':>10}  Result")
for name, act, exp in tests:
    ok = str(act) == exp
    print(f"{name:<32}{exp:>10}{str(act):>10}  {'PASS' if ok else 'FAIL'}")
    assert ok, name
entries = [(300, "3.5", "8.5"), (200, "3.5", "8.5"), (100, "3.5", "8.5")]
for season in ("normal", "summer"):
    milk, b, tot = m2.ten_day_payment(entries, season)
    print(f"600 L standard milk, {season:<6}: milk {milk:>9}  bonus {b:>7}  total {tot:>9}")
assert m2.ten_day_payment(entries, "summer")[2] == Decimal("19500.00")
assert m2.ten_day_payment(entries, "normal")[2] == Decimal("18300.00")
print("All tests passed")
