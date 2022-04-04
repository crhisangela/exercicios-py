# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = str(input('Insira seu usuário. '))
senha = str(input('Insira sua senha. '))


while (nome == senha):
    print('Sua senha não pode ser igual seu usuário, vamos tentar de novo.')
    nome = str(input('Insira seu usuário. '))
    senha = str(input('Insira sua senha. '))

print('Usuário e senha cadastrado com sucesso, obrigada!')