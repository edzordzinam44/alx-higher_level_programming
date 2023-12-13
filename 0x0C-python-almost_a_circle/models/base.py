#!/bin/usr/python3
"""
This module will serve as a conttainer for all the base of other classes
"""

import csv
import json
import os
import turtle


class Base:
    """Base classes for all bases created """
    __nb_objects = 0

    def __ini__(self, id=None):
        if id is  not None:#If id is provided, assign it
            self.id = id
    else:# Generate a new id
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
