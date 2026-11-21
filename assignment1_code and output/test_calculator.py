from decimal import Decimal
import calculator as c

cases = [  # (description, (litres, fat, snf), expected amount or 'ERR')
 ("Standard milk 3.5 / 8.5",          (10, 3.5, 8.5),  "300.00"),
 ("Fat above, SNF above",             (8.5, 4.2, 8.7), "283.90"),
 ("Fat below, SNF below",             (12, 3.1, 8.3),  "333.60"),
 ("Fat above, SNF below",             (10, 4.0, 8.2),  "311.00"),
 ("Fat below, SNF above",             (10, 3.0, 8.8),  "289.00"),
 ("Lowest allowed fat 2.0",           (10, 2.0, 8.5),  "240.00"),
 ("Highest allowed fat 7.0",          (10, 7.0, 8.5),  "440.00"),
 ("Fat just below minimum 1.9",       (10, 1.9, 8.5),  "ERR"),
 ("Fat just above maximum 7.1",       (10, 7.1, 8.5),  "ERR"),
 ("Negative quantity",                (-5, 3.5, 8.5),  "ERR"),
 ("Zero quantity",                    (0, 3.5, 8.5),   "ERR"),
 ("Text instead of number",           ("eight", 3.5, 8.5), "ERR"),
 ("NaN quantity",                     (float("nan"), 3.5, 8.5), "ERR"),
]
print(f"{'#':>2} {'Case':<30}{'Expected':>10}{'Actual':>10}  Result")
passed = 0
for i, (desc, e, exp) in enumerate(cases, 1):
    try:
        act = str(c.payout(*e))
    except ValueError:
        act = "ERR"
    ok = act == exp
    passed += ok
    print(f"{i:>2} {desc:<30}{exp:>10}{act:>10}  {'PASS' if ok else 'FAIL'}")
    assert ok, desc
# 5 entries calculated by hand
five = [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3), (15.5, 4.0, 8.6), (9, 3.8, 8.4)]
# hand rates: 30.00, 33.40, 27.80, 32.30 (4.0/8.6), 30.90 (3.8/8.4)
exp_total = Decimal("300.00") + Decimal("283.90") + Decimal("333.60") + Decimal("500.65") + Decimal("278.10")
act_total = c.ten_day_total(five)
print(f"{'':>2} {'5-entry total (by hand)':<30}{exp_total:>10}{act_total:>10}  {'PASS' if exp_total == act_total else 'FAIL'}")
assert exp_total == act_total
print(f"\nAll {passed + 1} tests passed")
