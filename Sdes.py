from bitarray import bitarray

def permute(original, table):
    """Permute the bits in the original bitarray according to the given table."""
    result = bitarray()
    for index in table:
        result.append(original[index-1])
    return result

def split(bitarray):
    """Split the given bitarray into two equal parts."""
    mid = len(bitarray) // 2
    left = bitarray[:mid]
    right = bitarray[mid:]
    return left, right

def xor(bitarray1, bitarray2):
    """Perform an XOR operation on the two given bitarrays."""
    result = bitarray()
    for bit1, bit2 in zip(bitarray1, bitarray2):
        result.append(bit1 ^ bit2)
    return result

def sbox(input):
    """Apply the S-Box substitution to the given 6-bit input bitarray."""
    sboxes = [
        # S-Box 1
        [
            [14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
            [ 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
            [ 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
            [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]
        ],
        # S-Box 2
        [
            [15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10],
            [ 3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5],
            [ 0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15],
            [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9]
        ],
        # S-Box 3

            [10,  0,  9, 14,  6,  3, 15,  5]
