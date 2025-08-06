# Invoke-Certify

Build with Visual Studio by using the folowing repository: https://github.com/GhostPack/Certify

Used the following script to pack: https://gist.github.com/Mayfly277/2e5f34a7e7f70798d1f19c0c35f9fa0e

## Usage

Simple as you can imagine

```bash
# Import into memory
PS C:\Tools> . .\Invoke-Certify.ps1

# Execute it
PS C:\Tools> Invoke-Certify

   _____          _   _  __
  / ____|        | | (_)/ _|
 | |     ___ _ __| |_ _| |_ _   _
 | |    / _ \ '__| __| |  _| | | |
 | |___|  __/ |  | |_| | | | |_| |
  \_____\___|_|   \__|_|_|  \__, |
                             __/ |
                            |___./
  v1.1.0


  Find information about all registered CAs:

    Certify.exe cas [/ca:SERVER\ca-name | /domain:domain.local | /ldapserver:server.domain.local | /path:CN=Configuration,DC=domain,DC=local] [/hideAdmins] [/showAllPermissions] [/skipWebServiceChecks] [/quiet]
[...]
```

**Pass commands to the script**

```bash
PS C:\Tools> Invoke-Certify -Command cas

   _____          _   _  __
  / ____|        | | (_)/ _|
 | |     ___ _ __| |_ _| |_ _   _
 | |    / _ \ '__| __| |  _| | | |
 | |___|  __/ |  | |_| | | | |_| |
  \_____\___|_|   \__|_|_|  \__, |
                             __/ |
                            |___./
  v1.1.0

[*] Action: Find certificate authorities
[...]
```
