#!/usr/bin/env python3
"""Estimate a Higgsfield API job cost from the prices shown on the Explore page.

Numbers are as displayed at the time of the snapshot; currency was not
labelled on the card, so only bare numbers are printed. Re-check the
pricing page before relying on them.

Usage: python3 cost_estimate.py MODEL QUANTITY
  MODEL     one of the keys in PRICES
  QUANTITY  seconds for video models, image count for image models
"""
import sys

# key: (unit, discounted price, list price)
PRICES = {
    'seedance-2.5': ('s', 0.144, 0.2057),
    'kling-3.0': ('s', 0.042, 0.084),
    'genjutsu-motion-transfer': ('s', 0.159, 0.318),
    'cinema-studio-4.0': ('s', 0.2057, 0.2057),
    'marketing-studio-image': ('image', 0.0121, 0.0162),
}


def estimate(model: str, quantity: float) -> tuple[float, float]:
    unit, discounted, full = PRICES[model]
    return quantity * discounted, quantity * full


def main() -> None:
    if len(sys.argv) != 3 or sys.argv[1] not in PRICES:
        print('usage: cost_estimate.py MODEL QUANTITY')
        print('models: ' + ', '.join(PRICES))
        sys.exit(2)
    model = sys.argv[1]
    quantity = float(sys.argv[2])
    unit = PRICES[model][0]
    low, high = estimate(model, quantity)
    print(f'{model}: {quantity:g} {unit}')
    print(f'  discounted: {low:.4f}')
    print(f'  list:       {high:.4f}')
    if unit == 's' and quantity > 30:
        print('  note: Seedance 2.5 is listed as up to 30 s per clip')


if __name__ == '__main__':
    main()
