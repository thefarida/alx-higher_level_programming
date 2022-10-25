#!/usr/bin/python3
"""Defines an object's attribute lookup function."""


def lookup(obj):
    """Return a list of attributes available from an object."""
    return (dir(obj))
