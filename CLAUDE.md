# Unit Converter

A small personal tool for converting a number from one unit to another, so there's no need to search the web for a converter each time. See [BRIEF.md](BRIEF.md) for the full brief.

## Who it's for

The owner, when cooking from a recipe in unfamiliar measurements.

## Scope

- Category: **cooking measurements** (US units). Volume: tsp, tbsp, floz, cup, ml, l. Mass: g, kg, oz, lb. Volume-to-mass (cups to grams) is unsupported because it needs ingredient density.
- Input: a number, a "from" unit, and a "to" unit. Output: the converted value.

## Acceptance criteria

- Converts correctly between any two supported units in the category.
- An unsupported unit produces a clear message that names the supported units. It never returns a wrong number.
- Results are rounded to a sensible number of decimal places for the unit, not a long unreadable decimal. If a nonzero input would round to 0, show 2 significant digits instead and print a note to stderr (the number alone stays on stdout).

## Non-goals

- Supporting categories beyond cooking measurements.
- Currency conversion in v1, including a static local rate table.
- Live, constantly updated exchange rates.
- A graphical interface. Keep it command-line or library-level.

## Working notes

- Keep it small and simple; resist adding categories or features not in the brief.
- Python, standard library only. Code is in `converter.py`; tests are in `test_converter.py`.
- Run: `python3 converter.py 2 cup ml`
- Test: `python3 -m unittest`
- Add tests for each acceptance criterion, including the unsupported-unit and rounding cases.

## When asked about a bug or unexpected behavior

Follow these steps in order:

1. Give a hypothesis explaining what you think is causing the problem. Do not change anything yet.
2. Wait for the user to confirm the hypothesis makes sense to them.
3. Only after that confirmation, propose a plan for the smallest fix that addresses the stated cause. Do not edit any files until the user approves the plan.

## Adding packages

Before adding a package, explain what it does, whether it's actively maintained, and whether there's a simpler way to get the same result without adding a dependency.
