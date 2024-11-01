import pytest
from src.package_sorter import sort

def test_standard_package():
    assert sort(50, 50, 50, 10) == "STANDARD"

def test_bulky_package():
    assert sort(150, 50, 50, 10) == "SPECIAL"  # bulky because width is 150

def test_heavy_package():
    assert sort(50, 50, 50, 20) == "SPECIAL"  # heavy because mass is 20

def test_both_bulky_and_heavy():
    assert sort(200, 200, 200, 25) == "REJECTED"  # both bulky and heavy

def test_below_bulky_threshold():
    assert sort(100, 100, 100, 10) == "SPECIAL"  # not bulky or heavy

def test_exact_volume_threshold():
    assert sort(100, 100, 1000, 10) == "SPECIAL"  # bulky because volume = 1,000,000

def test_negative_dimensions():
    with pytest.raises(ValueError):
        sort(-1, 100, 100, 10)  # negative dimension should raise an error

def test_negative_mass():
    with pytest.raises(ValueError):
        sort(100, 100, 100, -10)  # negative mass should raise an error

def test_large_values():
    assert sort(500, 500, 500, 30) == "REJECTED"  # large dimensions and mass, both bulky and heavy
