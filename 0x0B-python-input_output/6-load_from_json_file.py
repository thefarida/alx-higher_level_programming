#!/usr/bin/python3
"""Defines a JSON file reading function."""
import json


def load_from_json_file(filename):
    """Create a python object from a json file."""
    with open(filename) as f:
        return json.load(f)
