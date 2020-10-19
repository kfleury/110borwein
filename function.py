#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## 107transfer
## File description:
## calculated integrals
##
import sys
import math as m


class myEquation:
    def __init__(self, a, b, k):
        self.a = a
        self.b = b
        self.k = k

    @staticmethod
    def equation(x, i):
        try:
            result = 1.0
            a = 0
            while a <= x:
                if i != 0:
                    var = i / (2 * a + 1)
                    result *= (m.sin(var) / var)
                a += 1
            return result
        except ZeroDivisionError as error:
            print("error: " + str(error))
            sys.exit(84)

    @staticmethod
    def equa(x, i):
        try:
            result = 1.0
            var = i / (2 * x + 1)
            result *= (m.sin(var) / var)
            return result
        except ZeroDivisionError as error:
            print("error: " + str(error))
            sys.exit(84)

    def midpoint(self):
        try:
            my = myEquation(self.a, self.b, self.k)
            result = 0.0
            h = (self.a + self.b) / 2
            x = self.k
            a = float(self.a)
            while a < self.b:
                result += (self.b - self.a) * my.equa(x, h)
                a += 0.5
            return result * h
        except ZeroDivisionError as error:
            print("error: " + str(error))
            sys.exit(84)

    def trapezoid(self):
        try:
            my = myEquation(self.a, self.b, self.k)
            result = 0.0
            n = self.b * 2
            h = self.b / n
            a = 1
            x = self.k
            while a < n:
                result += my.equation(x, a * h)
                a += 1
            result *= 2
            result += my.equation(x, 5000) + my.equation(x, 0)
            result *= (h / 2)
            return result
        except ZeroDivisionError as error:
            print("error: " + str(error))
            sys.exit(84)

    def simpson(self):
        try:
            my = myEquation(self.a, self.b, self.k)
            res = 0.0
            ult = 0.0
            h = self.b / (self.b * 2)
            a = 1
            while a < self.b * 2:
                res = res + my.equation(self.k, a * h)
                a += 1
            a = 0
            while a < 10000:
                ult = ult + my.equation(self.k, (a * h) + (h / 2))
                a += 1
            result = my.equation(self.k, 5000) + my.equation(self.k, 0) + (2 * res) + (4 * ult)
            result = result * (self.b / (6 * self.b * 2))
            return result
        except ZeroDivisionError as error:
            print("error: " + str(error))
            sys.exit(84)


def calc(n):
    try:
        my = myEquation(0, 5000, n)
        res = my.midpoint()
        print("Midpoint:\nI%d = %.10f" % (n, res))
        print("diff = %.10f" % m.fabs(float(res - (m.pi / 2))))
        res = my.trapezoid()
        print("\nTrapezoidal:\nI%d = %.10f" % (n, res))
        print("diff = %.10f" % m.fabs(float(res - (m.pi / 2))))
        res = my.simpson()
        print("\nSimpson:\nI%d = %.10f" % (n, res))
        print("diff = %.10f" % m.fabs(float(res - (m.pi / 2))))
    except ZeroDivisionError as error:
        print("error: " + str(error))
        sys.exit(84)
