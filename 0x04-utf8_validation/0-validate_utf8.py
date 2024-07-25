#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    Args:
        data: data set to be verified
    Return:
        True if data is a valid UTF-8 encoding, else return False
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the most significant bits (MSBs)
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        # Get the binary representation of the byte
        bin_rep = bin(byte).replace('0b', '').rjust(8, '0')

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            for bit in bin_rep:
                if bit == '0':
                    break
                num_bytes += 1

            # 1 byte character
            if num_bytes == 0:
                continue

            # Invalid scenarios according to the rules of UTF-8
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the byte starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # We decrease the number of bytes left to process
        num_bytes -= 1

    return num_bytes == 0
