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

def bit_field_to_XGMII(head:np.ndarray, body: np.ndarray) -> np.ndarray:
    head_val = utils.read_byte(head, 0, 1)
    if head_val == 1:
        return body
    elif head_val == 0 or head_val == 3:
        return np.array(body)
    
    _term = np.array([1, 1, 1, 1, 1, 1, 0, 1])
    _idle = [0, 0, 0, 0, 0, 1, 1, 1]
    val = utils.read_byte(body, 0, 7)
    match val:
        case 0x87:
            return np.append(_term, np.array(_idle * 7))
        case 0x99:
            output = np.append(body[8:16], _term)
            return np.append(output, np.array(_idle * 6))
        case 0xaa:
            output = np.append(body[8:24], _term)
            return np.append(output, np.array(_idle * 5))
        case 0xb4:
            output = np.append(body[8:32], _term)
            return np.append(output, np.array(_idle * 4))
        case 0xcc:
            output = np.append(body[8:40], _term)
            return np.append(output, np.array(_idle * 3))
        case 0xd2:
            output = np.append(body[8:48], _term)
            return np.append(output, np.array(_idle * 2))
        case 0xe1:
            output = np.append(body[8:56], _term)
            return np.append(output, np.array(_idle * 1))
        case 0xff:
            return np.append(body[8:64], _term)
    return np.array(body)

def decoder(encoded_data: np.ndarray) -> np.ndarray:
    decoded_data = np.array([], dtype=np.int8)

    for i in range(0, encoded_data.size, 66):
        block = encoded_data[i:i + 66]
        header = block[0:2]
        body = block[2:66]
        body = unscrambler(body)
        code = bit_field_to_XGMII(header, body)
        decoded_data = np.append(decoded_data, code)

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
