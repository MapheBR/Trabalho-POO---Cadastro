from abc import ABC, abstractmethod 
import time
import sys 
    
def exibir_resultados_gradualmente(linhas, pausa_segundos=0.5):
    print("\n\n--- 🏁 Resultados Finais (Exibição Pausada) ---") 
    time.sleep(pausa_segundos * 1.5) 
    
    for linha in linhas: 
        print(linha)
        sys.stdout.flush() 
        time.sleep(pausa_segundos) 
    print("--------------------------------------------------")
    print("✅ Fim da Execução.") 

class Usuario(ABC): 
    def __init__(self, nome, email): 
        self.nome = nome 
        self.email = email  

    @abstractmethod 
    def get_tipo(self):
        pass 
    def __str__(self): 
        return f"Nome: {self.nome}, Email: {self.email}" 

class UsuarioAdmin(Usuario): 
    def __init__(self, nome, email, nivel_acesso):
        super().__init__(nome, email) 
        self.nivel_acesso = nivel_acesso 

    def get_tipo(self):
        return "Administrador"
    
    def __str__(self):
        return f"{super().__str__()} | Tipo: {self.get_tipo()}, Nível: {self.nivel_acesso}" 

class UsuarioComum(Usuario): 
    def __init__(self, nome, email, departamento): 
        super().__init__(nome, email) 
        self.departamento = departamento 

    def get_tipo(self): 
        return "Comum" 

    def __str__(self):
        return f"{super().__str__()} | Tipo: {self.get_tipo()}, Departamento: {self.departamento}" 

class UsuarioFactory: 
    @staticmethod 
    def criar_usuario(tipo, nome, email, **kwargs): 
        if tipo.lower() == "admin": 
            return UsuarioAdmin(nome, email, kwargs.get('nivel_acesso', 'Médio'))
        elif tipo.lower() == "comum": 
            return UsuarioComum(nome, email, kwargs.get('departamento', 'Geral'))
        else:
            raise ValueError(f"Tipo de usuário desconhecido: {tipo}") 

class GerenciadorDeUsuarios: 
    _instancia = None 

    def __new__(cls): 
        if cls._instancia is None: 
            cls._instancia = super(GerenciadorDeUsuarios, cls).__new__(cls) 
            cls._instancia.usuarios = [] 
        return cls._instancia 

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_usuarios(self):
        linhas = [] 
        if not self.usuarios: 
            linhas.append("❌ Não há usuários cadastrados.")
        else:
            linhas.append("--- 👥 LISTA DE USUÁRIOS CADASTRADOS (Gerenciador Singleton) ---")
            for u in self.usuarios:
                linhas.append(f"- {u}")
            linhas.append("-----------------------------------------------------------------")
        return linhas 

print("Iniciando o sistema de cadastro e configurando Singletons/Factories...")
usuario1 = UsuarioFactory.criar_usuario("admin", "Alice Silva", "alice@empresa.com", nivel_acesso="Alto")
usuario2 = UsuarioFactory.criar_usuario("comum", "Bruno Lima", "bruno@empresa.com", departamento="TI")
usuario3 = UsuarioFactory.criar_usuario("comum", "Carla Reis", "carla@empresa.com")


gerenciador1 = GerenciadorDeUsuarios() 
gerenciador1.adicionar_usuario(usuario1) 
gerenciador1.adicionar_usuario(usuario2) 

gerenciador2 = GerenciadorDeUsuarios() 
gerenciador2.adicionar_usuario(usuario3) 


resultados_finais = [
    "--- Status do Sistema ---",
    f"Usuário 1 (Admin) criado: {usuario1.nome} - Tipo: {usuario1.get_tipo()}", 
    f"Usuário 2 (Comum) criado: {usuario2.nome} - Tipo: {usuario2.get_tipo()}",
    f"Usuário 3 (Comum) criado: {usuario3.nome} - Tipo: {usuario3.get_tipo()}",
    "",
    f"Verificação Singleton: Gerenciador1 ID: {id(gerenciador1)}", 
    f"Verificação Singleton: Gerenciador2 ID: {id(gerenciador2)}", 
]

if id(gerenciador1) == id(gerenciador2): 
    resultados_finais.append("✅ Confirmação: As duas variáveis apontam para a mesma instância Singleton.")
else:
    resultados_finais.append("❌ Erro: O padrão Singleton falhou.")

resultados_finais.extend(gerenciador1.listar_usuarios())

exibir_resultados_gradualmente(resultados_finais, pausa_segundos=0.3) 