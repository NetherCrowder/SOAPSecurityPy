#Soap Python:

#############################################

from fastapi import FastAPI
from Core.Security.Encrypt.Base64Encrypt import Base64Encrypt
from Core.Security.Decrypt.Base64Decrypt import Base64Decrypt

app: FastAPI = FastAPI(title='SOAP Security Python', description='USBSI 2023-02')

##############################################

@app.get("/Base64Encrypt", summary="Base64 Encrypt", tags="[Base64]")
async def Base64Encrypt(plaintText: str | None = None):
    base64Encrypt = Base64Encrypt()
    return Base64Encrypt.Encrypt(plaintText)
@app.get("/Base64Decrypt", summary="Base64 Decrypt", tags="[Base64]")
async def Base64Decrypt(encryptText: str | None = None):
    base64Decrypt = Base64Decrypt()
    return Base64Decrypt.Decrypt(encryptText)

##############################################