# =====================================
# PERSONAL AI AGENT SBC
# models/user.py
# =====================================

from dataclasses import dataclass

@dataclass
class User:
    id: int
    username: str
    email: str
    password: str

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
