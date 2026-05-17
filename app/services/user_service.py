from app.db.repositories.user_repository import (
    UserRepository,
)
from app.models.user import User


class UserService:

    @staticmethod
    def get_or_create_user(
        telegram_id: int,
        username: str | None = None
    ) -> User:

        user = UserRepository.get_by_telegram_id(
            telegram_id
        )

        if user is not None:
            return user

        return UserRepository.create_user(
            telegram_id=telegram_id,
            username=username
        )