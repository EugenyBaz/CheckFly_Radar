from app.db.database import init_db
from app.services.user_service import UserService

if __name__ == "__main__":
    init_db()
    user = UserService.get_or_create_user(telegram_id=123456789, username="eugeny")
    print(user)
