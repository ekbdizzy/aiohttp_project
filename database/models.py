from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    birth_date = Column(Date)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    permissions = relationship("Permission", back_populates="user", uselist=False, cascade="all, delete-orphan")

    @property
    def full_name(self):
        """Return the user's full name."""
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"<User {self.username}>"


class Permission(Base):
    __tablename__ = "permissions"

    id = Column(Integer, primary_key=True)
    is_blocked = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    is_read_only = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    user = relationship("User", back_populates="permissions")

    def __repr__(self):
        return f"<Permission {self.id} for User {self.user_id}>"
