#!/usr/bin/python3
"""
This is the ``3-say_my_name.py`` module.
My name is <first name> <last name>
"""

import string


def say_my_name(first_name, last_name=""):
    """
         A function that print my first name and last name.

            Args:
                first_name must be a string
                last_name must be a string
    """

    if type(first_name) is not string:
        raise TypeError("first_name must be a string")

    if type(last_name) is not string:
        raise TypeError("last_name must be a string")

    return say_my_name(first_name, last_name)