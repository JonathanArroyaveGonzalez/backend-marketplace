from pydantic import BaseModel, EmailStr, Field, validator

class UserModel(BaseModel):
    name: str = Field(pattern="^[a-zA-Z ]{3,50}$", description="El campo nombres debe contener mínimo 3 y máximo 50 caracteres válidos")
    lastName: str = Field(pattern="^[a-zA-Z ]{3,50}$", description="El campo apellidos debe contener mínimo 3 y máximo 50 caracteres válidos")
    email: EmailStr = Field(default="no@gmail.com")
    phone: str = Field(pattern="^\d{10}$", description="El campo teléfono debe contener exactamente 10 caracteres numéricos")
    password: str = Field(min_length=8, description="La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un número.")

    @validator('password')
    def validate_password(cls, value):
        if not any(char.isdigit() for char in value):
            raise ValueError('La contraseña debe contener al menos un número')
        if not any(char.islower() for char in value):
            raise ValueError('La contraseña debe contener al menos una letra minúscula')
        if not any(char.isupper() for char in value):
            raise ValueError('La contraseña debe contener al menos una letra mayúscula')
        return value