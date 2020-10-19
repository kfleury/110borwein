#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## 107transfer
## File description:
## error handling
##
import sys


def usage():
    var = "USAGE\n\t" \
          "./110borwein n\n\n" \
          "DESCRIPTION\n\t" \
          "n constant defining the integral to be computed"
    print(var)
    sys.exit(0)


def error_arg(av):
    try:
        for argv in av:
            if not argv.isdigit():
                print("Error : '" + argv + "' is not a valid argument")
                sys.exit(84)
    except ValueError as error:
        print("error:" + str(error))
        return 0


def error_nbr_arg(ac):
    if ac != 2:
        sys.stderr.write("This program needs one arguments\n")
        sys.exit(84)
    return 0


def all_error(av, ac):
    error_nbr_arg(ac)
    av.pop(0)
    error_arg(av)
    return 0
