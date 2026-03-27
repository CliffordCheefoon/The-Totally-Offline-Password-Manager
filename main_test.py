from main import generate_hash


def test_generate_hash_consistency():
    # Run generate_hash 100 times and store results
    hash_results = []
    for _ in range(100):
        hash_results.append(generate_hash("test", "Hello, World!"))

    # Check that the first hash is the same as all others
    first_hash = hash_results[0]
    for i, hash_value in enumerate(hash_results):
        assert hash_value == first_hash, f"Hash at index {i} does not match first hash"
    assert True


def test_white_space_changes_in_input_string():
    hash1 = generate_hash("test", "Hello,World!")
    hash2 = generate_hash("test", "Hello,  World!")
    assert hash1 == hash2


def test_case_changes_in_input_string():
    hash1 = generate_hash("test", "Hello,World!")
    hash2 = generate_hash("test", "HELlo,worlD!")
    assert hash1 == hash2


def test_both_white_space_and_case_changes_in_input_string():
    hash1 = generate_hash("test", "Hello,World!")
    hash2 = generate_hash("test", "HELlo,  worlD!")
    assert hash1 == hash2


def test_master_password_case_change():
    hash1 = generate_hash("tesT", "Hello,World!")
    hash2 = generate_hash("test", "HELlo,  worlD!")
    assert hash1 != hash2


def test_long_term_consistency_1():
    hash = generate_hash("test", "Hello,World!")
    expected_hash = "hello,world!_&6C4cf9a&F7143de98760C86321%8*?3c6aBf38(a9de8*3e9^6$82@!9)9eC77@"
    assert hash == expected_hash


def test_long_term_consistency_2():
    hash = generate_hash("tesT", "Hello,World!")
    expected_hash = "hello,world!_)#2%%D%(5CDe(?C%a4b27%0Cd2#3B4193?B#B&()$42#6(575@5^b4499787Eb25"
    assert hash == expected_hash
