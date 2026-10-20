from pydantic import BaseModel,ConfigDict


class UserResponse(BaseModel):
    id: int
    username: str
    realname: str
    role: str
    email: str | None = None
    mobile: str | None = None
    avatar: str | None = None
    status: int

    model_config = ConfigDict(from_attributes=True)