
---

# Password Hashing Script

A simple Python script that hashes passwords using a custom shuffled character map.
It’s built for practice and educational use only.

## Features

* No external libraries required
* Custom one-way character mapping
* 3-attempt password verification system
* Input validation for empty passwords
* Clears screen between steps for better user experience
* Easy to run in any terminal

## How It Works

* User enters a password
* Script hashes it using a shuffled map of characters
* User is asked to re-enter the password
* The hashed versions are compared to verify identity
* Access is granted or denied based on match and attempts

## Requirements

* Python 3.x
* No additional packages needed

## Usage

Run the script in your terminal:

```bash
python password\ hashing.py
```

## Disclaimer

This hashing method is not secure.
Do not use it in production or with sensitive data.
It's for learning and demonstration purposes only.
