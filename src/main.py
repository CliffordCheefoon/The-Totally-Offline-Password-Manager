
import hashlib


def generate_hash(master_password: str, input_string: str, salt: str) -> str:
    """
    Generate a hash using a master password, a string, and a salt.

    Args:
        master_password (str): The master password to use for hashing
        string (str): The string to be hashed
        salt (str): The salt to use for hashing

    Returns:
        str: The generated hash as a hexadecimal string
    """
    # Convert string to lowercase and remove whitespace
    processed_string = input_string.lower().replace(' ', '')
    
    # Combine master password, processed string, and salt
    combined = master_password + processed_string + salt

    # Generate SHA-256 hash
    hash_object = hashlib.sha256(combined.encode())
    return hash_object.hexdigest()


if __name__ == "__main__":
    hash = generate_hash("test", "Hello, World!", "salt")
    print(hash)
