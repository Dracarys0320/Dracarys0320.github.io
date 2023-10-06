
# Implementación del patrón Singleton para autenticar en plataforma web
class AuthenticatorSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AuthenticatorSingleton, cls).__new__(cls)
            cls._instance.strategy = None
        return cls._instance

    def set_strategy(self, strategy):
        self.strategy = strategy

    def authenticate(self, credentials):
        if self.strategy:
            return self.strategy.authenticate(credentials)




