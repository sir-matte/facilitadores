# Dica 2: Variável 'Throw-away'

nome, _, idade = ['John', 2000, 22]
print(nome)
print(idade)
print('-' * 10)
primeiro, *_, ultimo = (1, 2, 3, 4, 5, 6, 7)
print(primeiro)
print(ultimo)
print(*_)
print('-' * 10)
for _ in range(3):
    print('Olá, Mundo!')