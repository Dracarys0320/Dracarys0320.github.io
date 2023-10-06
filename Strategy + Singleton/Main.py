from Singleton import AuthenticatorSingleton
from Strategy import UsernamePasswordAuth, OAuthAuth, TokenAuth

if __name__ == "__main__":
    authenticator = AuthenticatorSingleton()

    print("Seleccione una plataforma:")
    print("1. Github")
    print("2. Google")
    print("3. Facebook")

    choice = input("Ingrese el número de la plataforma deseada: ")

    if choice == "1":
        authenticator.set_strategy(UsernamePasswordAuth())
    elif choice == "2":
        authenticator.set_strategy(OAuthAuth())
    elif choice == "3":
        authenticator.set_strategy(OAuthAuth())
    else:
        print("Plataforma no válida.")

    if authenticator.strategy:
        username = input("Ingrese el nombre de usuario: ")
        password = input("Ingrese la contraseña: ")
        TokenAuth = input("Ingrese el token: ")

        credentials = (username, password)
        authenticator.authenticate(credentials)
