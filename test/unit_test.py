#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## 107transfer_2019
## File description:
## unit_test
##

import unittest

import error


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.var = "USAGE\n" \
                   "\t./107transfer [num den]*\n" \
                   "\nDESCRIPTION\n" \
                   "\tnum\tpolynomial numerator defined by its coefficients\n" \
                   "\tden\tpolynomial denominator defined by its coefficients"
        pass

    def test_usage(self):
        self.assertEqual(self.var, "USAGE\n"
                                   "\t./107transfer [num den]*\n"
                                   "\nDESCRIPTION\n"
                                   "\tnum\tpolynomial numerator defined by its coefficients\n"
                                   "\tden\tpolynomial denominator defined by its coefficients")

    def test_is_float(self):
        self.assertEqual(error.is_float("1.5"), 1)

    def test_is_not_float(self):
        self.assertNotEqual(error.is_float("1.5"), 0)

    def test_nbr_arg(self):
        with self.assertRaises(SystemExit) as cm:
            error.error_nbr_arg(1)
        self.assertEqual(cm.exception.code, 84)

    def test_nbr_arg1(self):
        with self.assertRaises(SystemExit) as cm:
            error.error_nbr_arg(2)
        self.assertEqual(cm.exception.code, 84)

    def test_nbr_arg2(self):
        with self.assertRaises(SystemExit) as cm:
            error.error_nbr_arg(4)
        self.assertEqual(cm.exception.code, 84)

    def test_nbr_arg3(self):
        self.assertEqual(error.error_nbr_arg(3), 0)

    def test_is_number(self):
        with self.assertRaises(SystemExit) as cm:
            error.error_arg(5)
        self.assertEqual(cm.exception.code, 84)


if __name__ == '__main__':
    unittest.main()
