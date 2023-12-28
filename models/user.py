from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    username: str
    email: str
    password: str
    role: int


class User(UserBase, table=True):
    id: int = Field(default=None, nullable=False, primary_key=True)


class UserCreate(UserBase):
    pass
