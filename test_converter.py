import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

from converter import UNITS, UnsupportedUnitError, convert, convert_detailed, main


class ConvertTests(unittest.TestCase):
    def test_cup_to_ml(self):
        self.assertEqual(convert(1, "cup", "ml"), 237)

    def test_ml_to_cup(self):
        self.assertEqual(convert(250, "ml", "cup"), 1.06)

    def test_tbsp_to_tsp(self):
        self.assertEqual(convert(2, "tbsp", "tsp"), 6)

    def test_oz_to_g(self):
        self.assertEqual(convert(4, "oz", "g"), 113)

    def test_same_unit_is_unchanged(self):
        self.assertEqual(convert(3, "cup", "cup"), 3)

    def test_unknown_unit_names_supported_units(self):
        with self.assertRaises(UnsupportedUnitError) as caught:
            convert(1, "cup", "parsec")
        message = str(caught.exception)
        self.assertIn("parsec", message)
        for unit in UNITS:
            self.assertIn(unit, message)

    def test_unknown_from_unit_is_rejected(self):
        with self.assertRaises(UnsupportedUnitError):
            convert(1, "furlong", "ml")

    def test_volume_to_mass_is_rejected(self):
        with self.assertRaises(UnsupportedUnitError) as caught:
            convert(1, "cup", "g")
        self.assertIn("density", str(caught.exception))

    def test_result_is_rounded_to_readable_decimals(self):
        self.assertEqual(convert(1, "tsp", "cup"), 0.02)
        self.assertEqual(convert(1, "lb", "kg"), 0.454)

    def test_tiny_result_keeps_significant_digits_and_adds_note(self):
        result, note = convert_detailed(1, "ml", "cup")
        self.assertEqual(result, 0.0042)
        self.assertIn("smaller than 0.005 cup", note)

    def test_tiny_negative_result_also_uses_fallback(self):
        result, note = convert_detailed(-1, "ml", "cup")
        self.assertEqual(result, -0.0042)
        self.assertIsNotNone(note)

    def test_normal_result_has_no_note(self):
        self.assertIsNone(convert_detailed(1, "tsp", "cup")[1])

    def test_zero_input_has_no_note(self):
        self.assertEqual(convert_detailed(0, "ml", "cup"), (0, None))


class CommandLineTests(unittest.TestCase):
    def run_main(self, *args):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = main(["converter.py", *args])
        return code, out.getvalue(), err.getvalue()

    def test_note_goes_to_stderr_and_number_to_stdout(self):
        code, out, err = self.run_main("1", "ml", "cup")
        self.assertEqual(code, 0)
        self.assertEqual(out.strip(), "0.0042")
        self.assertIn("Note:", err)

    def test_normal_result_prints_no_note(self):
        code, out, err = self.run_main("2", "cup", "ml")
        self.assertEqual((code, out.strip(), err), (0, "473", ""))


if __name__ == "__main__":
    unittest.main()
