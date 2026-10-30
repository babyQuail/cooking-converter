"""Convert cooking measurements between US volume units or between mass units."""

import sys

# name -> (category, size in the base unit, decimal places to round to)
# Base units: milliliters for volume, grams for mass.
UNITS = {
    "tsp": ("volume", 4.92892159375, 2),
    "tbsp": ("volume", 14.78676478125, 2),
    "floz": ("volume", 29.5735295625, 2),
    "cup": ("volume", 236.5882365, 2),
    "ml": ("volume", 1, 0),
    "l": ("volume", 1000, 3),
    "g": ("mass", 1, 0),
    "kg": ("mass", 1000, 3),
    "oz": ("mass", 28.349523125, 2),
    "lb": ("mass", 453.59237, 2),
}


class UnsupportedUnitError(ValueError):
    pass


def supported_units():
    return ", ".join(UNITS)


def convert_detailed(value, from_unit, to_unit):
    """Return (result, note). note is None unless the result needed extra precision."""
    for unit in (from_unit, to_unit):
        if unit not in UNITS:
            raise UnsupportedUnitError(
                f"Unsupported unit '{unit}'. Supported units: {supported_units()}"
            )
    from_category, from_size, _ = UNITS[from_unit]
    to_category, to_size, to_decimals = UNITS[to_unit]
    if from_category != to_category:
        raise UnsupportedUnitError(
            f"Can't convert {from_unit} ({from_category}) to {to_unit} ({to_category}); "
            f"that needs the ingredient's density. Supported units: {supported_units()}"
        )
    exact = value * from_size / to_size
    result = round(exact, to_decimals)
    note = None
    if result == 0 and exact != 0:
        # Rounding would hide a nonzero amount, so keep 2 significant digits instead.
        result = float(f"{exact:.2g}")
        note = (
            f"Note: result is smaller than {0.5 * 10 ** -to_decimals:g} {to_unit}, "
            "shown with extra precision."
        )
    return result, note


def convert(value, from_unit, to_unit):
    return convert_detailed(value, from_unit, to_unit)[0]


def main(argv):
    if len(argv) != 4:
        print("Usage: python converter.py <number> <from_unit> <to_unit>", file=sys.stderr)
        print(f"Supported units: {supported_units()}", file=sys.stderr)
        return 2
    try:
        value = float(argv[1])
    except ValueError:
        print(f"'{argv[1]}' is not a number", file=sys.stderr)
        return 2
    try:
        result, note = convert_detailed(value, argv[2], argv[3])
    except UnsupportedUnitError as error:
        print(error, file=sys.stderr)
        return 1
    print(int(result) if result == int(result) else result)
    if note:
        print(note, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
