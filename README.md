# The Totally Offline Password Manager

A password manager that uses hashing to deterministically generate passwords. 

## How It Works

This password manager takes your master password, the name of a service, and an optional username/email as inputs, then uses cryptographic hashing to generate a unique password for each service. This means you never have to store or remember individual passwords - just remember one master password. The benefit of this approach is that naturally, the same password is never reused across different services, since each service's password is generated independently based on its unique name. The optional username parameter allows you to have multiple accounts on the same service, each with a distinct password.

## Technical Features

- No Internet or Network Dependency: The application runs completely offline. No data is ever transmitted or stored externally.
- Stateless Operating Security Model: Because output is generated on the fly, there are no vaults, caches, or persistent secrets. There is no database or file to attack. The attack surface is minimized to the code and the runtime environment.
- Password Variation: Passwords for different services or under different usernames are never the same
- Password Strength: Passwords are long and highly complex. 
- Deterministic Output: Cryptographic hash functions ensure that identical inputs always yield identical outputs, enabling password regeneration without storage.

## Usage

1. Enter your master password
2. Enter the name of the service (e.g., "gmail", "github")
3. Optionally enter a username or email for that service
4. The application will generate a unique password for that service and username combination

## Security

This approach eliminates the need to store passwords in databases or files (online or local), reducing attack surface significantly. 

## Requirements

- Python 3.14
- Standard library only (no external dependencies)

## Installation

No installation required - just run the script.

## License

 CC0-1.0 license

## Disclaimer

This tool is provided for educational purposes only. The creators and contributors make no guarantees regarding the security, reliability, or suitability of this tool for any particular purpose. By using this tool, you acknowledge that you use it at your own risk. This tool does not provide any legal remediation or service guarantees, and the authors shall not be held liable for any damages or losses arising from its use.