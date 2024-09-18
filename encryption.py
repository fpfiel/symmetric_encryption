#for block length 12
pbox_12 = [3, 1, 4, 0, 6, 8, 7, 5, 11, 2, 9, 10]
inverse_pbox_12 = [pbox_12.index(i) for i in range(len(pbox_12))] #iterable.index(x) returns the first index of a value

sbox_12 = [3, 8, 15, 1, 10, 6, 5, 11, 14, 13, 12, 7, 4, 9, 0, 2] #if splitted into blocks of 4 bits 16 substitutes required
inverse_sbox_12 = [sbox_12.index(x) for x in range(16)]


def p_box(block, p_box: list[int]):
    return ''.join(block[i] for i in p_box)


def s_box(block, s_box: list[int]):
    return ''.join(format(s_box[int(block[i:i+4], 2)], '04b') for i in range(0, len(block), 4))


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
    if(len(blocks) == 0): return ''

    binary_string = ''.join(blocks)

    byte_values = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]

    ascii_characters = [chr(int(byte, 2)) for byte in byte_values[:-1]] # all bytes except the last one shall be appended no matter if only 0 or not

    last_byte = byte_values[-1]
    if last_byte != '00000000' and last_byte != '0000': #last byte could be padding byte without information
        ascii_characters.append(chr(int(last_byte, 2)))
    
    return ''.join(ascii_characters)


def enc_string_to_blocks(input_string, block_size=12):
    ascii_values = [ord(char) for char in input_string]
    
    binary_values = [format(ascii_val, '08b') for ascii_val in ascii_values[:-1]]
    
    binary_values.append(format(ascii_values[-1], 'b'))

    # sum_length_bin_values = sum(len(x) for x in binary_values)
    sum_length_bin_values = (8 * (len(binary_values) -1)) + len(binary_values[-1])
    length_mod_blocksize = sum_length_bin_values%12

    fill_zeroes = 12 - (length_mod_blocksize) if length_mod_blocksize != 0 else 0

    binary_values[-1] = binary_values[-1].rjust(fill_zeroes + len(binary_values[-1]), '0') #fill so mod 12 is null
    
    binary_string = ''.join(binary_values)
    
    blocks = [binary_string[i:i + block_size] for i in range(0, len(binary_string), block_size)]
    
    if len(blocks) > 0 and len(blocks[-1]) < block_size:
        # this should not be reachable, padding should always be filled to 12 blocksize
        blocks[-1] = blocks[-1].ljust(block_size, '0') # string.ljust(length, char) appends the char length-len(string) times so afterwards len(string) is equal to length 
    
    return blocks


def enc_blocks_to_string(blocks: list[str]):
    binary_string = ''.join(blocks)

    byte_values = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]

    ascii_characters = [chr(int(byte, 2)) for byte in byte_values] # all bytes except the last one shall be appended no matter if only 0 or not

    return ''.join(ascii_characters)


def encryption(clear_text: str, key: str, rounds: int):

    blocks = string_to_blocks(clear_text)

    for i in range(rounds):
        round_key = generate_roundkey(key, i)
        blocks = [xor(p_box(s_box(block, s_box=sbox_12), p_box=pbox_12), key=round_key) for block in blocks]

    return enc_blocks_to_string(blocks)

def decryption(cipher_text: str, key: str, rounds: int):
    #do everything in the single rounds in reverse?
    blocks = enc_string_to_blocks(cipher_text)

    for i in reversed(range(rounds)):
        round_key = generate_roundkey(key, i)
        blocks = [s_box(p_box(xor(block, round_key), p_box=inverse_pbox_12), s_box=inverse_sbox_12) for block in blocks]

    return blocks_to_string(blocks)