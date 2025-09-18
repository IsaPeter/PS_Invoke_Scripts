from argparse import ArgumentParser
import base64
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import string
import random
import gzip
import io
import sys

def read_binary(path):
    if os.path.isfile(path):
        with open(path, "rb") as f:
            binary_data = f.read()
        return binary_data
    else:
        return []

def write_file(data, path):
    with open(path, 'w') as f:
        f.write(data)

def gzip_compress(data: bytes) -> bytes:
    buf = io.BytesIO()
    with gzip.GzipFile(fileobj=buf, mode="wb") as f:
        f.write(data)
    return buf.getvalue()


def id_generator(size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def _make_key(password: str) -> bytes:
    # kiegészítés/padding 32 bájtra és UTF-8
    key_str = (password + "0" * 32)[:32]
    return key_str.encode("utf-8")


def encrypt(plain_text: str, password: str) -> str:
    key = _make_key(password)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # PKCS7 padding
    pad_len = 16 - (len(plain_text.encode("utf-8")) % 16)
    padded = plain_text.encode("utf-8") + bytes([pad_len]) * pad_len

    encrypted_bytes = cipher.encrypt(padded)
    encrypted_with_iv = iv + encrypted_bytes
    encrypted_b64 = base64.b64encode(encrypted_with_iv).decode("utf-8")
    return encrypted_b64

def decrypt(encrypted_b64: str, password: str) -> str:
    key = _make_key(password)
    encrypted_with_iv = base64.b64decode(encrypted_b64)
    iv = encrypted_with_iv[:16]
    encrypted_bytes = encrypted_with_iv[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(encrypted_bytes)

    # PKCS7 unpadding
    pad_len = decrypted_padded[-1]
    decrypted = decrypted_padded[:-pad_len]
    return decrypted.decode("utf-8")


def create_script(base64_data, namespace, classname, password):
    script_data = """
    function Invoke-NAMESPACE
    {
    [CmdletBinding()]
    Param (
        [String]
        $Command = "--help"
        )
    $enc = "ENCDATA";
    $password = "PASSWORD";
    $dec = Decrypt $enc $password;
    $b=New-Object IO.MemoryStream(,[Convert]::FromBAsE64String($dec))
    $decompressed = New-Object IO.Compression.GzipStream($b,[IO.Compression.CoMPressionMode]::DEComPress)
    $out = New-Object System.IO.MemoryStream
    $decompressed.CopyTo( $out )
    [byte[]] $byteOutArray = $out.ToArray()

    $RAS = [System.Reflection.Assembly]::Load($byteOutArray)
    [NAMESPACE.CLASSNAME]::Main($Command.Split(" "))
    }
    function Decrypt($encryptedBase64, $password){
    $keyStr = $password.PadRight(32,'0').Substring(0,32);$secureKey = [System.Text.Encoding]::UTF8.GetBytes($keyStr);$encryptedWithIV2 = [Convert]::FromBase64String($encryptedBase64);$IV2 = $encryptedWithIV2[0..15];$realEncryptedBytes = $encryptedWithIV2[16..($encryptedWithIV2.Length-1)];$aes2 = [System.Security.Cryptography.Aes]::Create();$aes2.Key = $secureKey;$aes2.IV = $IV2;$decryptor = $aes2.CreateDecryptor();$decryptedBytes = $decryptor.TransformFinalBlock($realEncryptedBytes, 0, $realEncryptedBytes.Length);$decryptedText = [System.Text.Encoding]::UTF8.GetString($decryptedBytes);return $decryptedText;
    }
    """
    return script_data.replace("ENCDATA",base64_data).replace("PASSWORD",password).replace("NAMESPACE",namespace).replace("CLASSNAME", classname)

def parse_aerguments():
    parser = ArgumentParser()
    parser.add_argument("-b","--binary", dest="binpath", required=True, help="Set the binary path")
    parser.add_argument("-n","--namespace", dest = "namespace", required=True, help="Set the target namespace")
    parser.add_argument("-c", "--class", dest="classname", default="Program", help="Set the class name")
    parser.add_argument("-p","--password", dest="password", help="Set encryption password")


    return parser.parse_args()

def main():
    args = parse_aerguments()

    if args.binpath: 
        binpath = args.binpath
    
    if args.namespace: namespace = args.namespace
    if args.classname: classname = args.classname
    
    if args.password: 
        password = args.password
    else:
        # Generate a password if no password provided
        password = id_generator(size=16)
    

    # Execution
    binary_data = read_binary(binpath)
    compressed = gzip_compress(binary_data)
    compressed_b64 = base64.b64encode(compressed).decode("utf-8")
    binary_data_enc = encrypt(compressed_b64, password)

    script_data = create_script(binary_data_enc, namespace, classname, password)
    name = "Invoke-"+namespace+".ps1"
    write_file(script_data,name)


if __name__ == '__main__':
    main()
