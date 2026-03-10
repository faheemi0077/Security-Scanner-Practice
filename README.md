# Config Exposure Scanner

This project is a command-line tool that scans configuration files for potentially dangerous network exposure settings and replaces them with safer alternatives.

The tool analyzes files such as `.env`, `.json`, `.yaml`, and `.yml` and automatically redacts risky values like public IP addresses or open network bindings.

## Features

- Scans configuration files for insecure patterns
- Detects public IP addresses and open network bindings
- Automatically replaces risky values with safer alternatives
- Saves sanitized versions of affected files
- Generates a remediation log

## Supported File Types

- `.env`
- `.json`
- `.yaml`
- `.yml`

## How It Works

1. The program scans a directory for configuration files.
2. Each file is checked against known risky patterns such as:
   - `0.0.0.0`
   - `0.0.0.0/0`
   - public IP addresses
3. If a risky pattern is detected, the program replaces it with a safer value.
4. A sanitized copy of the file is created and a remediation log is generated.

## Requirements

- Python 3
