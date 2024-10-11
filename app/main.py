from services.user_services import UserService
from repositories.user_repository import UserRepository
from config.connection import Session

def main():
    session = Session()
    repository = UserRepository(session)
    service = UserService(repository)

    service.create_user("Maiara", "Maiara@gmail.com", "12345")

    print("\nListando todos os usuários.")
    users = service.list_all_users()

    for user in users:
        print(f"{user.name} - {user.email}")

if __name__ == "__main__":
    main()