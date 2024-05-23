#!/usr/bin/python3
"""
Determines if data represents valid utf8
"""
def is_valid_utf8(data):
    """
    Determines if given data represents valid UTF-8.
    :param data: List of integers representing bytes of data
    :return: True if data is valid UTF-8, False otherwise
    """
    num_bytes = 0

    for number in data:
        binary_result = format(number, '#010b')[-8:]

        if num_bytes == 0:
            for bit in binary_result:
                if bit == '0':
                    break
                num_bytes += 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (binary_result[0] == '1' and binary_result[1] == '0'):
                return False

        num_bytes -= 1

    return num_bytes == 0
