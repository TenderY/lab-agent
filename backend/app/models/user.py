from app.database import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"comment": "用户表"}

    username: Mapped[str] = mapped_column(String(50), nullable=False, comment="用户名")
    password: Mapped[str] = mapped_column(String(255), nullable=False, comment="密码")
    realname: Mapped[str] = mapped_column(String(50), nullable=False, comment="真实姓名")
    role: Mapped[str] = mapped_column(String(50), nullable=False, comment="角色")

    email: Mapped[str | None] = mapped_column(String(50), comment="邮箱")
    mobile: Mapped[str | None] = mapped_column(String(50), comment="手机号")
    avatar: Mapped[str | None] = mapped_column(String(255), comment="头像")
    status: Mapped[int] = mapped_column(Integer, default=1, comment="状态 0-禁用 1-启用")


