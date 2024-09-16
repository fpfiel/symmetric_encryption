from encryption import blocks_to_string, decryption, encryption, p_box, s_box, string_to_blocks, xor
import random

####### TESTS #######

pbox_12 = [3, 1, 4, 0, 6, 8, 7, 5, 11, 2, 9, 10]
inverse_pbox_12 = [pbox_12.index(i) for i in range(len(pbox_12))]

sbox_12 = [3, 8, 15, 1, 10, 6, 5, 11, 14, 13, 12, 7, 4, 9, 0, 2]
inverse_sbox_12 = [sbox_12.index(x) for x in range(16)]


def test_string_to_blocks_and_back():
    print("\nTest string to blocks and back")

    input_string = "HELLO, WORLD"
    block_size = 12
    assert input_string == blocks_to_string(string_to_blocks(input_string, block_size)), f"Test 1 failed."

    # input, which length isnt exactly a multiple of blocksize
    input_string = "HELLO, WORLD 123"
    block_size = 12
    assert input_string == blocks_to_string(string_to_blocks(input_string, block_size)), f"Test 2 failed."

    # empty string
    input_string = ""
    block_size = 12
    assert input_string == blocks_to_string(string_to_blocks(input_string, block_size)), f"Test 3 empty string failed."

    # different blocksizes
    # input_string = "HELLO WORLD"
    # for block_size in range(4, 16):
    #     assert input_string == blocks_to_string(string_to_blocks(input_string, block_size)), f"Test 4 failed at block_size={block_size}."

    # random string, random length <= 20
    input_string = "".join([chr(random.randint(32, 126)) for i in range(0, random.randint(1, 20))])
    assert input_string == blocks_to_string(string_to_blocks(input_string, block_size)), f"Test 5 random string."

    print("All tests string_to_blocks_and_back passed")


def test_p_box():
    print("\nTest pbox")

    # block with length 12
    block = "110010110101"
    assert block == p_box(p_box(block, p_box=pbox_12), p_box=inverse_pbox_12), "Test 1 failed"

    # edege case all 0
    block = "000000000000"
    assert block == p_box(p_box(block, p_box=pbox_12), p_box=inverse_pbox_12), "Test all 0 failed"

    # edege case all 1
    block = "111111111111"
    assert block == p_box(p_box(block, p_box=pbox_12), p_box=inverse_pbox_12), "Test all 1 failed"

    # random block
    block = "".join([str(random.randint(0, 1)) for i in range(12)])
    assert block == p_box(p_box(block, p_box=pbox_12), p_box=inverse_pbox_12), f"Test random block failed for block: {block}"

    print("All p_box tests passed!")


def test_s_box():
    print("\nTest sbox")

    # block with length 12
    block = "110010110101"
    assert block == s_box(s_box(block, s_box=sbox_12), s_box=inverse_sbox_12), "Test 1 failed"

    # edege case all 0
    block = "000000000000"
    assert block == s_box(s_box(block, s_box=sbox_12), s_box=inverse_sbox_12), "Test all 0 failed"

    # edege case all 1
    block = "111111111111"
    assert block == s_box(s_box(block, s_box=sbox_12), s_box=inverse_sbox_12), "Test all 1 failed"

    # random block
    block = "".join([str(random.randint(0, 1)) for i in range(12)])
    assert block == s_box(s_box(block, s_box=sbox_12), s_box=inverse_sbox_12), f"Test random block failed for block: {block}"

    print("All s_box tests passed!")


def test_xor():
    print("\nTest xor")

    # basic xor test
    block = "110010110101"
    key = "101011001110"
    expected_output = "011001111011"
    assert xor(block, key) == expected_output, "Test 1 failed"

    # Test 2: test invertibility
    block = "110010110101"
    key = "101011001110"
    assert xor(xor(block, key), key) == block, f"Test invertibility failed: Expected {block}"


    print("All xor tests passed!")



def test_encryption_decryption():

    print("\nTest encryption - decryption")

    key='0111001010001001' #keylength? 

    rounds=3

    for i in range(1, 14):
        input_string = 'a' * i
        encrypted_val = encryption(input_string, key, rounds)
        decrypted_val = decryption(encrypted_val, key, rounds)
        assert decrypted_val == input_string, f"Test with input length {len(input_string)} failed"

    input_string = 'a' * 33
    encrypted_val = encryption(input_string, key, rounds)
    decrypted_val = decryption(encrypted_val, key, rounds)
    assert decrypted_val == input_string, f"Test with input length {len(input_string)} failed"

    input_string = "".join([chr(random.randint(32, 125)) for x in range(1, random.randint(2, 20))])
    #print(input_string)
    encrypted_val = encryption(input_string, key, rounds)
    decrypted_val = decryption(encrypted_val, key, rounds)
    assert decrypted_val == input_string, f"Test with string={input_string} with length {len(input_string)} failed"

    print("All encryption - decryption tests passed!")


def test_weird_behaviour():
    #try_count = 100000 #134 in first run, 121 in second hits currently
    try_count = 100000  
    key='0111001010001001' #keylength? 
    rounds=3

    wrong_decrypts = []

    for i in range(try_count):
        input_string = "".join([chr(random.randint(32, 125)) for x in range(1, random.randint(2, 20))])
        # input_string = "".join([chr(random.randint(32, 125))for x in range(0, 2)])


        #print(input_string)
        encrypted_val = encryption(input_string, key, rounds)
        decrypted_val = decryption(encrypted_val, key, rounds)
        
        if(input_string != decrypted_val):
            wrong_decrypts.append([input_string, encrypted_val, decrypted_val])


    #print(wrong_decrypts[i][0] for i in range(len(wrong_decrypts)))

    #stats = [0 for i in range(20)]

    for wd in wrong_decrypts:
        print(wd[0])

    print(len(wrong_decrypts))



def test_temp():

    key='0111001010001001' #keylength? 
    rounds=3

    block_size = 12

    input_string = "dq-"
    print(len(input_string))
    print(input_string)

    encrypted_val = encryption(input_string, key, rounds)
    decrypted_val = decryption(encrypted_val, key, rounds)
    assert decrypted_val == input_string, f"Test with input length {len(input_string)} failed"

    #assert input_string == blocks_to_string(string_to_blocks(input_string, block_size)), f"Fail: strings and back len={len(input_string)}."



# Testaufrufe
# test_string_to_blocks_and_back()
# test_p_box()
# test_s_box()
# test_xor()
#test_encryption_decryption()

test_weird_behaviour()

#test_temp()