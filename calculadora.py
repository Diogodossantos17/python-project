

Sistema_de_vote = 'Comissão Nacional Eleitoral'



nome = str  (input('Insira por favor o seu nome caro cidadão. '))

print('Nome do Cidadão ', nome  )

dia_de_nascimento = int(input('Insira o seu dia de Nascimento '))

mes_de_nascimento = str (input('Mês de nascimento '))

ano_de_nascimento = float (input('Ano de nascimento '))

print('Dados de Nascimento:  ', dia_de_nascimento, 'de', mes_de_nascimento, 'de',  ano_de_nascimento)


idade = int (2025 - ano_de_nascimento)

print('Idade do cidadão ', idade),

if idade < 18:  print('Cidadão menor de idade, tem de ter 18 anos ou mais para exercer o seu direito de voto. ')

else: print('Cidadão maior de idade, pode exercer o seu direito de voto. ')


partido = str(input(' Escolha o seu Partido / Coligação: '))

print('Partido / Coligação: ', partido)






