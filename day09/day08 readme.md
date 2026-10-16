# Day 9: Order validation and exception handling

Run the example from this folder with:

```console
python exception_handling.py
```

The program checks each order independently, validates it before calculating a
total, and continues through the input after a rejection.

## Exceptions and validation

The sample runs entirely in memory, so it does not read files, connect to a
database, or perform network operations. It has no expected input/output
exceptions to catch. Expected data problems are handled with explicit checks
and rejection reasons instead of exception handling. A narrow `TypeError`
handler around multiplication is a defensive guard in case supported numeric
types are changed later; with the current validation, ordinary sample data
cannot reach that handler.

Validation catches these data-quality problems before calculation:

- An order that is not a dictionary.
- Any missing required field (`order_id`, `customer`, `price`, or `quantity`).
- A customer value that is not text or is empty/whitespace-only.
- A price that is not a built-in integer or float, is not finite, or is
  negative. The strict type check also rejects `True` and `False` as prices.
- A quantity that is not a positive integer. `type(value) is int` rejects
  booleans as well as fractional values.

The code checks for every required key before reading its value. It returns a
reason as soon as an order fails a check, so it never tries to multiply an
invalid price or quantity.

## Valid and rejected orders

`process_orders` builds two separate lists. Valid orders are copied into
`valid_orders` with a calculated `total`. Invalid orders are represented in
`rejected_orders` by their order ID (or `unknown` if unavailable) and a reason.
The loop continues after appending each rejected record.

## Example output

```text
Valid orders:
- order 101 (Asha): total = 39.98
Rejected orders:
- order 102: missing required field 'price'
- order 103: price must be a number
```

## Limitations

- The example uses a small hard-coded list; it does not load orders from a CSV
  file, API, or database.
- It stops at the first validation problem per order, so it reports one reason
  for each rejected record rather than collecting every problem on that order.
- Monetary values use Python `int` and `float`; production financial code
  should normally use decimal arithmetic and define currency/rounding rules.
- It does not persist rejected records or valid totals.
