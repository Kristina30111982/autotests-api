from pydantic import BaseModel, EmailStr, Field, SecretStr, constr


# Общие ограничения для ФИО:
NameStr = constr(strip_whitespace=True, min_length=1, max_length=50)


class UserSchema(BaseModel):
    id: str = Field(..., description="Идентификатор пользователя")
    email: EmailStr
    last_name: NameStr = Field(..., alias="lastName")
    first_name: NameStr = Field(..., alias="firstName")
    middle_name: NameStr | None = Field(None, alias="middleName")


class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: SecretStr = Field(..., min_length=8, description="Пароль (не логировать!)")
    last_name: NameStr = Field(..., alias="lastName")
    first_name: NameStr = Field(..., alias="firstName")
    middle_name: NameStr | None = Field(None, alias="middleName")


class CreateUserResponseSchema(BaseModel):
    user: UserSchema

