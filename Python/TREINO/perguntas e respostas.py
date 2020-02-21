print('--- SISTEMA DE PROVAS 1.0 ---')

questoes = {
        'QUESTÃO 1':{
                'pergunta': 'Quanto é 2+15?',
                'resposta':{'a':'1', 'b':'17', 'c':'23',
                            'd':'40', 'e':'52'},
                'resposta_correta':'b',
                },
        'QUESTÃO 2':{
                'pergunta': 'Quem é o melhor professor?',
                'resposta':{'a':'Aratã', 'b':'Laeycio', 'c':'Ana',
                            'd':'Gleiser', 'e':'João Batista'},
                'resposta_correta':'a',
                },
        'QUESTÃO 3':{
                'pergunta': 'Quanto é 60+63?',
                'resposta':{'a':'174', 'b':'197', 'c':'243',
                            'd':'123', 'e':'529'},
                'resposta_correta':'d',
                },
        'QUESTÃO 4':{
                'pergunta': 'QUAL A LIGUAGEM MAIS POLULAR DO MUNDO ?',
                'resposta':{'a':'JAVA', 'b':'JAVASCRIPT', 'c':'PYTHON',
                            'd':'C#', 'e':'C++'},
                'resposta_correta':'b',
                },
        'QUESTÃO 5':{
                'pergunta': 'QUANTO É 123*542?',
                'resposta':{'a':'187942', 'b':'117', 'c':'23',
                            'd':'40', 'e':'66666'},
                'resposta_correta':'e',
                },
        }
print()

respostas_certas = 0


for pk,pv in questoes.items():
    print(f'{pk}: {pv["pergunta"]}')
    
    print('Escolha as opções')
    for rk,rv in pv['resposta'].items():
        print(f'[{rk}]:{rv}')
  
    user = input('Sua Reposta: ')
    
    if user == pv['resposta_correta']:
        print('Parabens está correto')
        respostas_certas += 1
    else:
        print('Você errou, estude mais na proxima !')
    print()
    
qtd_perguntas = len(questoes)
porcentagem_acerto = respostas_certas /qtd_perguntas * 100

print(f'Voce acertou {respostas_certas} resposta.')
print(f'Sua porcetagem de acerto foi {porcentagem_acerto}%.')
        