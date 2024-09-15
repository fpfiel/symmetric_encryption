from encryption import blocks_to_string, inverse_p_box, inverse_s_box, p_box, s_box, string_to_blocks, xor
import random

####### TESTS #######


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
    input_string = "HELLO WORLD"
    for block_size in range(4, 16):
        assert input_string == blocks_to_string(string_to_blocks(input_string, block_size)), f"Test 4 failed at block_size={block_size}."

    # random string, random length <= 20
    input_string = "".join([chr(random.randint(32, 126)) for i in range(0, random.randint(1, 20))])
    assert input_string == blocks_to_string(string_to_blocks(input_string, block_size)), f"Test 5 random string."

    print("All tests string_to_blocks_and_back passed")


def test_p_box():
    print("\nTest pbox")

    # block with length 12
    block = "110010110101"
    assert block == inverse_p_box(p_box(block)), "Test 1 failed"

    # edege case all 0
    block = "000000000000"
    assert block == inverse_p_box(p_box(block)), "Test all 0 failed"

    # edege case all 1
    block = "111111111111"
    assert block == inverse_p_box(p_box(block)), "Test all 1 failed"

    # random block
    block = "".join([str(random.randint(0, 1)) for i in range(12)])
    assert block == inverse_p_box(p_box(block)), f"Test random block failed for block: {block}"

    print("All p_box tests passed!")


def test_s_box():
    print("\nTest sbox")

    # block with length 12
    block = "110010110101"
    assert block == inverse_s_box(s_box(block)), "Test 1 failed"

    # edege case all 0
    block = "000000000000"
    assert block == inverse_s_box(s_box(block)), "Test all 0 failed"

    # edege case all 1
    block = "111111111111"
    assert block == inverse_s_box(s_box(block)), "Test all 1 failed"

    # random block
    block = "".join([str(random.randint(0, 1)) for i in range(12)])
    assert block == inverse_s_box(s_box(block)), f"Test random block failed for block: {block}"

    print("All s_box tests passed!")


def test_xor():
    # basic xor test
    block = "110010110101"
    key = "101011001110"
    expected_output = "011001111011"
    assert xor(block, key) == expected_output, "Test 1 failed"

    # Test 2: test invertibility
    block = "110010110101"
    key = "101011001110"
    assert xor(xor(block, key), key) == block, f"Test invertibility failed: Expected {block}"

# Testaufrufe
test_string_to_blocks_and_back()
test_p_box()
test_s_box()
test_xor()