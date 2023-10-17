import numpy as np
import math
import utils
import encoder

def unscrambler(block:np.ndarray) -> np.ndarray:
    seed = np.ones(58, dtype=np.int8)
    output = np.array([], dtype=np.int8)
    
    for i in range(0, block.size):
        s38 = int(seed[38])
        s57 = int(seed[57])
        res = s38 ^ s57
        output = np.append(output, res ^ int(block[i]))
        utils.shift_left_bits(seed, block[i])
    return output

def decoder(encoded_data: np.ndarray) -> np.ndarray:
    decoded_data = np.array([], dtype=np.int8)

    for i in range(0, encoded_data.size, 66):
        block = encoded_data[i:i + 66]
        body = block[2:66]
        body = unscrambler(body)
        decoded_data = np.append(decoded_data, body)

    return decoded_data

def main():
    _term = [1, 1, 1, 1, 1, 1, 0, 1]
    _idle = [0, 0, 0, 0, 0, 1, 1, 1]
    byte1 = np.array([0, 0, 0, 0, 0, 0, 0, 1] * 6 + 1 * _term + _idle * 1)
    # byte2 = np.array(byte1)
    # encoder.scrambler(byte2)
    # dec = unscrambler(byte2)
    en = encoder.encoder(byte1)
    dec = decoder(en)
    print(sum(dec != byte1))
    print(byte1)
    print(dec)
    # res1, logic = encoder.XGMII_to_bit_field(byte1)
    # res1 = np.append(np.array([1, 0]), res1)
    # res2 = bit_field_to_XGMII(res1)
    # print(sum(byte1 != res2))
    # print(byte1)
    # print(res2)

if __name__ == "__main__":
    main()
