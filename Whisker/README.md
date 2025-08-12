# Invoke-Whisker

Build with Visual Studio by using the folowing repository: [https://github.com/GhostPack/SharpDPAPI](https://github.com/eladshamir/Whisker)

Used the following script to pack: https://gist.github.com/Mayfly277/2e5f34a7e7f70798d1f19c0c35f9fa0e

## Usage

```bash
PS C:\Users\isap\Desktop\Tools\workdir> Invoke-Whisker -Command ""

Whisker is a C# tool for taking over Active Directory user and computer accounts by manipulating their
msDS-KeyCredentialLink attribute, effectively adding Shadow Credentials to the target account.

  Usage: ./Whisker.exe [list|add|remove|clear] /target:<samAccountName> [/deviceID:<GUID>] [/domain:<FQDN>]
               [/dc:<IP/HOSTNAME>] [/password:<PASWORD>] [/path:<PATH>]

  Modes
    list            List all the values of the the msDS-KeyCredentialLink attribute of a target object
    add             Add a new value to the msDS-KeyCredentialLink attribute of a target object
    remove          Remove a value from the msDS-KeyCredentialLink attribute of a target object
    clear           Clear all the values of the the msDS-KeyCredentialLink attribute of a target object.
                    Warning: Clearing the msDS-KeyCredentialLink attribute of accounts configured for
                    passwordless authentication will cause disruptions.
[....]
```
