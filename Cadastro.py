from abc import ABC, abstractmethod
import time
import sys


def display_results_progressively(lines, pause_seconds=0.5):
    print("\n\nResultados finais\n\n")
    time.sleep(pause_seconds * 1.5)

    for line in lines:
        print(line)
        sys.stdout.flush()
        time.sleep(pause_seconds)
    print("\nFim da execução.")


class User(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    @abstractmethod
    def get_type(self):
        pass

    def __str__(self):
        return f"Nome: {self.name}, Email: {self.email}"


class AdminUser(User):
    def __init__(self, name, email, access_level):
        super().__init__(name, email)
        self.access_level = access_level

    def get_type(self):
        return "Administrador"

    def __str__(self):
        return f"{super().__str__()} | Tipo: {self.get_type()}, Nível: {self.access_level}"


class RegularUser(User):
    def __init__(self, name, email, department):
        super().__init__(name, email)
        self.department = department

    def get_type(self):
        return "Comum"

    def __str__(self):
        return f"{super().__str__()} | Tipo: {self.get_type()}, Departamento: {self.department}"


class UserFactory:
    @staticmethod
    def create_user(user_type, name, email, **kwargs):
        if user_type.lower() == "admin":
            return AdminUser(name, email, kwargs.get('access_level', 'Médio'))
        elif user_type.lower() == "regular" or user_type.lower() == 'comum':
            return RegularUser(name, email, kwargs.get('department', 'Geral'))
        else:
            raise ValueError(f"Tipo de usuário desconhecido: {user_type}")


class UserManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserManager, cls).__new__(cls)
            cls._instance.users = []
        return cls._instance

    def add_user(self, user):
        self.users.append(user)

    def list_users(self):
        lines = []
        if not self.users:
            lines.append("Não há usuários cadastrados.")
        else:
            lines.append("Usuários cadastrados:")
            for user in self.users:
                lines.append(f"- {user}")
        return lines


print("Iniciando o sistema de cadastro...")
admin_user = UserFactory.create_user("admin", "Alice Silva", "alice@company.com", access_level="Alto")
it_user = UserFactory.create_user("regular", "Bruno Lima", "bruno@company.com", department="TI")
regular_user = UserFactory.create_user("regular", "Carla Reis", "carla@company.com")


user_manager1 = UserManager()
user_manager1.add_user(admin_user)
user_manager1.add_user(it_user)

user_manager2 = UserManager()
user_manager2.add_user(regular_user)


final_results = [
    "Status do sistema",
    f"Usuário 1 (Admin) criado: {admin_user.name} - Tipo: {admin_user.get_type()}",
    f"Usuário 2 (Comum) criado: {it_user.name} - Tipo: {it_user.get_type()}",
    f"Usuário 3 (Comum) criado: {regular_user.name} - Tipo: {regular_user.get_type()}",
    "",
    f"Verificação Singleton: Gerenciador1 ID: {id(user_manager1)}",
    f"Verificação Singleton: Gerenciador2 ID: {id(user_manager2)}",
]

if id(user_manager1) == id(user_manager2):
    final_results.append("Sucesso")
else:
    final_results.append("Erro")

final_results.extend(user_manager1.list_users())

display_results_progressively(final_results, pause_seconds=0.3)
