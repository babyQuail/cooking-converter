# 🥄 Unit Converter

A small command-line tool for converting cooking measurements, so you can follow a recipe written in units you don't normally use without searching the web each time.

Version 1 handles **US cooking volumes and weights**. It does not convert currency or other categories (see [Limits](#limits)).

## 🔧 Setup

You need Python 3 and nothing else. There are no packages to install.

1. Check that Python is installed: `python3 --version`
2. Open a terminal in this folder.
3. That's it. You can run the tool straight away.

> **Tip: typing `python` instead of `python3`**
> On many Macs only `python3` exists. If you use zsh (the default on a Mac) and would rather type `python`, add this line to your `~/.zshrc` file:
>
> ```
> alias python=python3
> ```
>
> Then apply it to your current terminal window by running this (or just open a new terminal window):
>
> ```
> source ~/.zshrc
> ```
>
> This is optional, and it only applies when you type commands yourself in the terminal. Everything in this README works with `python3`.

## 🍳 How to use it

```
python3 converter.py <number> <from_unit> <to_unit>
```

Examples:

```
$ python3 converter.py 1 cup ml
237

$ python3 converter.py 3 tbsp tsp
9

$ python3 converter.py 8 oz g
227

$ python3 converter.py 1 l cup
4.23
```

### Supported units

| Kind   | Units                                               |
| ------ | --------------------------------------------------- |
| Volume | `tsp`, `tbsp`, `floz`, `cup`, `ml`, `l`             |
| Weight | `g`, `kg`, `oz`, `lb`                               |

- Unit names are lowercase and singular: `cup`, not `cups`.
- Fluid ounces are written `floz` (no space) so the shell doesn't split them. Plain `oz` is a weight.
- Volumes are US measures (1 cup is about 236.6 ml).

### Rounding

Results are rounded to a readable number of decimals for the unit you convert to: whole numbers for `ml` and `g`, three decimals for `l` and `kg`, and two for everything else.

If a result is so small that rounding would show `0`, the tool shows two significant digits instead and prints a note:

```
$ python3 converter.py 1 ml cup
Note: result is smaller than 0.005 cup, shown with extra precision.
0.0042
```

The note is printed separately from the number, so if you save or pipe the output you get only the number.

### Things it won't do

The tool tells you rather than guess. It exits with an error message that lists the supported units when:

- a unit isn't recognized: `python3 converter.py 1 cup parsec`
- you mix a volume and a weight: `python3 converter.py 1 cup g`. That depends on the ingredient (a cup of flour weighs less than a cup of honey), so it isn't supported.

If you give the wrong number of arguments or something that isn't a number, it prints a usage message.

## ✅ Running the tests

```
python3 -m unittest
```

## Limits

- One category only: cooking volume and weight.
- No currency conversion, and no live exchange rates.
- No graphical interface.

See [BRIEF.md](BRIEF.md) for the full scope.

## Files

- [converter.py](converter.py): the converter and command-line entry point
- [test_converter.py](test_converter.py): tests
- [BRIEF.md](BRIEF.md): what the tool is for and what's out of scope
- [CLAUDE.md](CLAUDE.md): working notes for Claude Code
