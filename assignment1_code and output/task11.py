import json, timeit, os
from decimal import Decimal
def load_rate_card(path):
    """Read the rate cards from a JSON file; amounts are kept as Decimal."""
    with open(path) as f:
        raw = json.load(f)
    return {season: {k: Decimal(v) for k, v in card.items()} for season, card in raw.items()}
card = load_rate_card("rates.json")
print(card["summer"])
n = 2000
t = timeit.timeit(lambda: load_rate_card("rates.json"), number=n) / n
print(f"start-up cost to read + convert 6 values: {t*1e6:.0f} microseconds (once per run)")
print("file size:", os.path.getsize("rates.json"), "bytes")
