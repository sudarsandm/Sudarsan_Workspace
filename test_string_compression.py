from string_compression import compress
import pytest

def test_compress():
    assert compress("AAABBBCCCDDD") == "A3B3C3D3"
    assert compress("AAB") == "A2B1"
    assert compress("") == 0
    assert compress('a') == 'a1'
