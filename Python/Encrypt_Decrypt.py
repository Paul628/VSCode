import cryptography
from Crypto.Cipher import AES
import hashlib
import base64


enc_message = "LkVrc/W+MtCgMh+tnCmk9K977jlmcpfLW+4oPpXGaV6NwBeLPhoyeYQqa8XJpp27yvOFIiu0taT4Nj6g8khNhCRTtxQmzr2tzvR8CcwqdVCYgQ4TFgFdf7n//wdOa0OM1ZkTE1aEfFkmVWFZpgZ5kGQJsYlzGGLsTZAQkYhYRkx9zmW8rQ8E0OQ2O+5QFRqOWJ+2wepU0W2z5jF2TAu5KwBmz8g3p2PZLN6KCkkYvzdDL6bRU4VnyYKweVyZirb0dpSHIYTzgFDZCatgI/mCiv4eSpjcyrxL2y7K/3Byi9Q="


List = open("Liste.txt", encoding='utf-8').read().splitlines()



dec_message = ""


for i in range(len(List)):
    custom_key = List[i]
    #input_data = b'This is secret message'
    key = custom_key.encode('UTF-8')


    ## ENCRYPTION

    encryption_cipher = AES.new(key, AES.MODE_OPENPGP)

    # use a nonce, e.g when the mode is AES.MODE_EAX
    #nonce = encryption_cipher.nonce
    ciphertext = encryption_cipher.encrypt(input_data)

    #b64_ciphertext = base64.b64encode(ciphertext).decode()
    b64_ciphertext = enc_message
    #print("Base64 of AES-encrypted message: ", b64_ciphertext)

    ## DECRYPTION

    unb64_ciphertext = base64.b64decode(b64_ciphertext.encode())
    iv = unb64_ciphertext[0:18]
    unb64_ciphertext = unb64_ciphertext[18:]

    decryption_cipher = AES.new(key, AES.MODE_OPENPGP, iv=iv)#, nonce=nonce)
    output_data = decryption_cipher.decrypt(unb64_ciphertext)

    f = open("output.txt", "a")
    f.write(output_data)
    f.close()


    print("Decrypted message: ", output_data)



