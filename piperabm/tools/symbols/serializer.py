from piperabm.tools.symbols import SYMBOLS


def serialize_symbol(symbol):
    result = None
    for key in SYMBOLS:
        if SYMBOLS[key] == symbol:
            result = key
            break
    if result is None: # when unable to serialzie
        result = symbol
    return result

def deserialize_symbol(symbol: str):
    result = None
    for key in SYMBOLS:
        if symbol == key:
            result = SYMBOLS[symbol]
            break
    if result is None: # when unable to deserialzie
        result = symbol
    return result


if __name__ == "__main__":
    a = deserialize_symbol('inf')
    print(a)
