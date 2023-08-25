#Base64 Decrypt:

###########################################################

import base64

###########################################################

class Base64Decrypt:
    def decrypt(self, encrypted_text):
        encrypted_bytes = encrypted_text.encode('utf-8')
        decrypted_bytes = base64.b64decode(encrypted_bytes)
        return decrypted_bytes.decode('utf-8')
