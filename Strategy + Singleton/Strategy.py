class AuthStrategy:
    def authenticate(self, credentials):
        pass

class UsernamePasswordAuth(AuthStrategy):
    def authenticate(self, credentials):
        username, password = credentials
        if username == "usuario" and password == "contraseña":
            print("Autenticación exitosa.")
            return True


class OAuthAuth(AuthStrategy):
    def authenticate(self, credentials):
        token = credentials
        print("Autenticación OTP exitosa.")
        return True
  
class TokenAuth(AuthStrategy):
    def authenticate(self, credentials):
        token = credentials
        print("Autenticación mediante token exitosa.")
        return True
     

