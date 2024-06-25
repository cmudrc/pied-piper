"""
List of symbols
"""

import sys


SYMBOLS = {
    'inf': float('inf'),  # Infinity
    'eps': sys.float_info.epsilon,  # Epsilon
}


if __name__ == "__main__":
    print(SYMBOLS)