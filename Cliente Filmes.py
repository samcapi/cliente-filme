from time import sleep

class Cliente():
    def __init__(self,nome,email,plano):
        self.nome=nome
        self.email=email
        self.lista_planos=['basic','premium']
        if plano in self.lista_planos:
            self.plano=plano
        else:
            print('Plano inválido!')

    def novo_plano(self,novo_plano):
        if novo_plano in self.lista_planos:
            self.plano=novo_plano
        else:
            print('Plano inválido!')

    def ver_filme(self,filme,plano_filme):
        if self.plano==plano_filme:
            print(f'Ver filme {filme}')
        elif self.plano=='premium':
            print(f'Ver filme {filme}')
        elif plano_filme=='premium' and self.plano=='basic':
            print('Você precisa de um upgrade no plano para ver esse filme!')
            mudar = input('Deseja mudar de plano [S/N]: ').upper()
            if mudar == 'S':
                cliente.novo_plano(input('Novo plano [basic, premium]: '))
                print('Novo plano cadastrado!')
        else:
            print('Plano inválido!')

nome=input('Nome: ').title()
while True:
    email=input('Email: ')
    if '@' and '.com' not in email:
        print('Digite seu email corretamente, exemplo: xxxxx@xxx.com')
    else:
        break
plano=input('Plano [basic, premium]: ')

try:
    cliente=Cliente(nome,email,plano)
except (ValueError,TypeError,):
    print('Há informações faltando!')

def titulo():
    print('~'*42)
    print(f'  FILMES'.center(42))
    print('~'*42)
print(titulo())

filmes = {1: 'Taxi Driver', 2: 'Star Wars', 3: 'Pulp Fiction',
          4: 'Forrest Gump', 5: 'Big Lebowski', 6: 'Scarface'}

while True:
    print(f'''\033[33m  Premium
    [1] Taxi Driver
    [2] Star Wars
    [3] Pulp Fiction\033[m
    \033[32m
      Basic
    [4] Forrest Gump
    [5] Big Lebowski
    [6] Scarface\033[m
''')
    esc=int(input('Qual filme deseja ver: '))
    sleep(2)
    if esc<=3:
        cliente.ver_filme(filmes[esc],'premium')
    elif esc>3:
        cliente.ver_filme(filmes[esc],'basic')
        break

print('Saindo do sistema...')



