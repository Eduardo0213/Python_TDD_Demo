
"""
Core math utilities for TDD practice.

All functions use basic `float` types only.
"""

from typing import List

def add(a: float, b: float) -> float:
    return a + b

def safe_divide(a: float, b: float) -> float:
    if b == 0.0:
        raise ValueError("denominator must not be zero")
    return a / b

def average(xs: List[float]) -> float:
    if not xs:
        raise ValueError("xs must not be empty")
    return sum(xs) / len(xs)

def sqrt_approx(x: float) -> float:
    """
    Return an approximation of the square root of x.
    """
    raise NotImplementedError