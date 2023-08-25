#Usuario Model:

########################################################

from pydantic import BaseModel

########################################################

class Usuario(BaseModel):
    Nombres: str
    Apellidos: str
    Documentos: str
    TarjetaDeCredito: float
    CodigoCVV: int
    Direccion: str
    EMail: str
    Usuario: str
    Clave: str