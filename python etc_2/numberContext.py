#!usr/bin/env/python3

import decimal

PENNY = decimal.Decimal("0.00")
price = decimal.Decimal('15.99')
rate = decimal.Decimal('0.0075')
print(f"Tax={(price * rate).quantize(PENNY)}, Fully={price * rate}")
with decimal.localcontext() as ctx:
	ctx.rounding = decimal.ROUND_DOWN
	tax = (price*rate).quantize(PENNY)
print(f"Tax={tax}")