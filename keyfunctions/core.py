from functools import reduce
import keyfunctions.globals as consts


def create_key(values, depth):
    """
    This function returns a Z-order key for any number of dimensions.

     :param values: a list of floats - one of dimension - each of them with value between 0 and 1 [0,1)
     :param depth: an strictly positive int
     :return: a string of depth size
     """
    mul = 1 << depth
    val_casted = [int(value * mul) for value in values]
    key = ""
    for i in range(0, depth):
        mask = 1 << i
        last = reduce(
            lambda x, y: x | y,
            [((value & mask) >> i) << dimension for dimension, value in enumerate(val_casted)])
        # We want to use printable chars: from char '!' to '~' (we skipped space).
        key = chr(last + consts.PRINTABLE_OFFSET) + key
    return key


def create_element_rand(element_id):
    """
    This function simply returns a 32 bit hash of the element id.
    The result value should be used a random priority.
    :param element_id: The element unique identifier
    :return: an random integer
    """
    import mmh3
    import struct

    if isinstance(element_id, int):
        obj = struct.pack('i', element_id)
    elif isinstance(element_id, long):
        obj = struct.pack('q', element_id)
    elif isinstance(element_id, str):
        obj = element_id
    else:
        raise TypeError('Unknown type: pack it yourself with struct')

    return int(mmh3.hash(obj))
