#!/usr/bin/env python3
"""
A simple text parser for pretraining the model
""" 

# ----------------- Futures -----------------
from __future__ import annotations

# ----------------- Standard Library -----------------
import re


# ----------------- Third Party Library -----------------


# ----------------- Application Imports -----------------


# ----------------- Module-level Configuration -----------------
class TextParser:

    def __init__(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            self.text = f.read()

    def process(self):
        preprocessed = re.split(r'[[!,.:"?_()\'@#$%^&*{}<>/]|--|\s]', self.text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        
        return preprocessed


   