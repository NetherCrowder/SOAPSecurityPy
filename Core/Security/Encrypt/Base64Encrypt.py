#Base64 Encypt:

###########################################################

import base64

###########################################################

class Base64Encrypt:
    def encrypt(self, plaintext):
        plaintext_bytes = plaintext.encode('utf-8')
        encrypted_bytes = base64.b64encode(plaintext_bytes)
        return encrypted_bytes.decode('utf-8')

