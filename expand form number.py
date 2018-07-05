import string
from codecs import encode as _dont_use_this_


def rot13(s):
    result = ""

    # Loop over characters.
    for v in s:
        # Convert to number with ord.
        c = ord(v)

        # Shift number back or forward.
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        if c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c+=13
        result+=chr(c)
    return result   
        
print(rot13("test"))
print(rot13("Test"))
        
