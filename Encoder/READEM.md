# Encoder

This little python script is used for encode and encrypt then pack the binary into a powershell script.

## Usage

```shell
encoder.py -b ".\mybinary.exe" -n "CustomNamespace" -c "Program" -p "myPassword"
```

if the password parameter is not specified, the script generate a random 16 character long password and include it to the script.
