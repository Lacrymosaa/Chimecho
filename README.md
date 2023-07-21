# Chimecho
Chimecho é um programa que lembra seu usuário de colocar a música para tocar. Ele verifica sua atividade no spotify de 5 em 5 minutos (configuravel), e caso nada esteja tocando ele enviará uma notificação que irá durar 5 segundos.

# Modo de uso:
- É necessário logar no https://developer.spotify.com/ e criar um app. Vá em settings e pegue o Client ID e o Client Secret
- Modifique o arquivo credentials.json com seu Client ID e Secret.

# Issues:
- Compilar o programa com PyInstaller não deixa ele enviar as notificações. Testei trocar de biblioteca para win10toast mas o erro persiste.
