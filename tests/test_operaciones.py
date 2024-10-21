import pytest
from src.operaciones import *

def test_mod_add():
    assert mod_add(3, 4, 7) == 0
    assert mod_add(2, 5, 11) == 7

def test_mod_subtract():
    assert mod_subtract(3, 4, 7) == 6
    assert mod_subtract(5, 2, 11) == 3

# Agregar más pruebas para otras operaciones