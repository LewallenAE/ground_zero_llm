#!/usr/bin/env python3
"""
 Import The Verdict by Edith Wharton to pre-train the LLM.
"""

# ----------------- Futures -----------------
from __future__ import annotations

# ----------------- Standard Library -----------------
import re

# ----------------- Third Party Library -----------------


# ----------------- Application Imports -----------------


# ----------------- Module-level Configuration -----------------

with open("the_verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()
print("Total number of characters:", len(raw_text))
print(raw_text[:99])

preprocessed = re.split(r'([,.:;?_!"()\'@#$%^&*{}_<>]|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(len(preprocessed))
print(preprocessed[:30])

