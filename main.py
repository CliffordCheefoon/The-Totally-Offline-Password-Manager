import hashlib
import random
import string

def generate_hash(master_password: str, input_string: str, salt: str = "salt_string") -> str:
    """
    Create a cryptographic hash value by combining a master password, an input string, and a salt.
    This function uses SHA-256 hashing algorithm to produce a secure, fixed-length hash output
    that can be used for password verification, data integrity checks, or other security purposes.

    Args:
        master_password (str): The master password to use for hashing
        input_string (str): The string to be hashed
        salt (str): The salt to use for hashing

    Returns:
        str: The generated hash as a hexadecimal string
    """
    processed_string = input_string.lower().replace(' ', '')
    
    combined = master_password + processed_string + salt

    hash_object = hashlib.sha256(combined.encode())
    hash =  hash_object.hexdigest()
    

    # The int() function with base 16 converts the hexadecimal string to a decimal integer
    # The 16 indicates that the input string is in base-16 (hexadecimal) format
    # This is necessary because hexdigest() returns a hexadecimal string representation of the hash
    seed = int(hash, 16)

    #Ensure that the case_adjusted_hash contains at least one uppercase character
    case_adjusted_hash = randomize_case(hash_string=hash, seed=seed)
    while not any(c.isupper() for c in case_adjusted_hash):
        seed = seed + 1
        case_adjusted_hash = randomize_case(hash_string=hash, seed=seed)

    special_chars = "!@#$%^&*()?"
    case_adjusted_and_special_char_hash = randomize_special_characters(case_adjusted_hash, seed, special_chars)
    # Rerun the randomize_special_characters if case_adjusted_and_special_char_hash does not contain a special character
    while not any(c in special_chars for c in case_adjusted_and_special_char_hash):
        seed = seed + 1
        case_adjusted_and_special_char_hash = randomize_special_characters(case_adjusted_hash, seed, special_chars)
    return case_adjusted_and_special_char_hash


def randomize_case(hash_string: str, seed: int) -> str:
    """
    Randomly uppercase letters in the hash string.

    Args:
        hash_string (str): The hash string to process
        seed (int): The seed for randomization

    Returns:
        str: The hash string with randomly uppercased letters
    """
    random.seed(seed)
    result = ""
    for char in hash_string:
        if char.isalpha():
            # Randomly decide whether to uppercase the letter
            if random.choice([True, False]):
                    result += char.upper()
            else:
                    result += char
        else:
                result += char
    return result


# Randomize special characters in the final hash
def randomize_special_characters(text:str, seed:int, special_chars, probability=0.3):
    """
    Randomly replace characters in a string with special characters based on a given probability.

    Args:
        text (str): The input string to modify
        seed (int): The seed for randomization
        special_chars (str): A string containing the set of special characters to use for replacement
        probability (float): Probability (0-1) of changing each character

    Returns:
        str: Modified string with some characters replaced by special characters
    """
    random.seed(seed)

    result = []

    for char in text:
        if random.random() < probability:
            # Replace with a random special character
            new_char = random.choice(special_chars)
            result.append(new_char)
        else:
            result.append(char)

    return ''.join(result)

if __name__ == "__main__":
    hash = generate_hash("test", "Hello, World!")
    print(hash)

