import hashlib
import sys
import os

BUF_SIZE = 65536
sha1 = hashlib.sha1()

with open(sys.argv[1], 'rb') as f:
    while True:
        data = f.read(BUF_SIZE)
        if not data:
            break
        sha1.update(data)

print("SHA1: {0}".format(sha1.hexdigest()))




hash = hashlib.sha1(b"ffxiv_act_plugin.dll")
pbHash = hash.hexdigest()
print("Parser filename: " + pbHash)



hash = hashlib.sha1(b"dalamud.injector.dll")
pbHash = hash.hexdigest()
print("Dalamud filename: " + pbHash)
