from models.user import User
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def create_user(self, name: str, email, password: str):
        try:
            user = User(name=name, email=email, password=password)
            self.repository.save_user(user)
            print("Usuário salvo com sucesso!")
        except TypeError as error:
            print(f"Erro ao salvar o arquivo: {error}")
        except Exception as error:
            print(f"Ocorreu um erro inesperado: {error}")

    def list_all_users(self):
        return self.repository.list_all_users()