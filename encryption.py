

#for block length 12
pbox_12 = [3, 1, 4, 0, 6, 8, 7, 5, 11, 2, 9, 10]
inverse_pbox_12 = [pbox_12.index(i) for i in range(len(pbox_12))] #iterable.index(x) returns the first index of a value

sbox_12 = [3, 8, 15, 1, 10, 6, 5, 11, 14, 13, 12, 7, 4, 9, 0, 2] #if splitted into blocks of 4 bits 16 substitutes required
inverse_sbox_12 = [sbox_12.index(x) for x in range(16)]


def p_box(block):
    return ''.join(block[i] for i in pbox_12)

def inverse_p_box(block):
    return ''.join(block[i] for i in inverse_pbox_12)


def s_box(block):
    return ''.join(format(sbox_12[int(block[i:i+4], 2)], '04b') for i in range(0, len(block), 4))

def inverse_s_box(block):
    return ''.join(format(inverse_sbox_12[int(block[i:i+4], 2)], '04b') for i in range(0, len(block), 4))



def xor(block, key):
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(block, key))


def generate_roundkey(key, round_number):
    rotated_key = key[round_number:] + key[:round_number]
    return rotated_key


def string_to_blocks(input_string, block_size=12):
    ascii_values = [ord(char) for char in input_string]
    
    binary_values = [format(ascii_val, '08b') for ascii_val in ascii_values]
    
    binary_string = ''.join(binary_values)
    
    # when slicing in python with string[a:b] with b>len(string) python automatically cuts until the end of the string
    blocks = [binary_string[i:i + block_size] for i in range(0, len(binary_string), block_size)]
    
    if len(blocks) > 0 and len(blocks[-1]) < block_size:
        #required_padding = block_size - len(blocks[-1])
        blocks[-1] = blocks[-1].ljust(block_size, '0') # string.ljust(length, char) appends the char length-len(string) times so afterwards len(string) is equal to length 
    
    return blocks

def blocks_to_string(blocks: list[str]):
    binary_string = ''.join(blocks)

    byte_values = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]

    ascii_characters = [chr(int(byte, 2)) for byte in byte_values if byte != '00000000'] # in case the last 8 bits got padded, dont add padded bits

    return ''.join(ascii_characters)


def encryption(clear_text: str, key: str, rounds: int):

    blocks = string_to_blocks(clear_text)

    for i in range(rounds):
        round_key = generate_roundkey(key, i)
        blocks = [xor(p_box(s_box(block)), key=round_key) for block in blocks]

    return blocks_to_string(blocks)

def decryption(cipher_text: str, key: str, rounds: int):
    #do everything in the single rounds in reverse?
    blocks = string_to_blocks(cipher_text)

    for i in reversed(range(rounds)):
        round_key = generate_roundkey(key, i)
        blocks = [inverse_s_box(inverse_p_box(xor(block, round_key))) for block in blocks]

    return blocks_to_string(blocks)