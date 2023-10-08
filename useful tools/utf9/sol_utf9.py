#!/usr/bin/python3
from bitarray import bitarray as _bitarray
def utf9decode(data):
    """Takes utf9-encoded data and returns the corresponding string."""
    bits = _bitarray()
    bits.frombytes(data)
    chunks = (bits[x:x+9] for x in range(0, len(bits), 9))
    string = ''
    codepoint = ''
    for chunk in chunks:
        if len(chunk) < 9:
            break
        if chunk[0] == 0:
            codepoint, string = '', string + codepoint
        codepoint += chr(int(chunk[1:].to01(), 2))
    return string + codepoint
dt = ''
with open('key_is_here_but_do_you_know_rfc_released_on_1_April_2005', 'rb') as f:
    t = f.read()
    dt=utf9decode(t)
print(dt)
