import random
import os
import linecache

pronomes_pessoais = ["yo", "tú", "él/ella/usted", "nosotros", "vosotros", "ellos/ellas/ustedes"]

lista_verbos_ar = ["trabajar", "comprar", "hablar", "andar"]
lista_verbos_er = ["comer", "saber", "correr", "hacer", "traer"]
lista_verbos_ir = ["salir", "vivir", "dormir", "decir"]

lista_completa = lista_verbos_ar + lista_verbos_er + lista_verbos_ir

resp_ar = {'id': "1", 'trabajar': {'presente de indicativo': ('trabajo', 'trabajas', 'trabaja',
                        'trabajamos', 'trabajáis', 'trabajan'),
                        'pretérito indefinido': ('trabajé', 'trabajaste', 'trabajó',
                         'trabajamos', 'trabajasteis', 'trabajaron'),},
           'comprar': {'presente de indicativo': ('compro', 'compras', 'compra',
                       'compramos', 'compráis', 'compran'),
                       'pretérito indefinido': ('compré', 'compraste', 'compró',
                        'compramos', 'comprasteis', 'compraron')},
           'hablar': {'presente de indicativo': ('hablo', 'hablas', 'habla',
                      'hablamos', 'habláis', 'hablan'),
                      'pretérito indefinido': ('hablé', 'hablaste', 'habló',
                        'hablamos', 'hablasteis', 'hablaron')},
            'andar': {'presente de indicativo': ('ando', 'andas', 'anda',
                      'andamos', 'andáis', 'andan'),
                      'pretérito indefinido': ('anduve', 'anduviste', 'anduvo',
                        'anduvimos', 'anduvisteis', 'anduvieron')}
           }
tempos_verbais = ["presente de indicativo", "pretérito indefinido", "pretérito imperfecto"]


resp_er = {'id': "2", 'comer': {'presente de indicativo': ('como', 'comes', 'come',
                        'comemos', 'coméis', 'comen'),
                        'pretérito indefinido': ('comí', 'comiste', 'comió',
                         'comimos', 'comisteis', 'comieron')},
           'saber': {'presente de indicativo': ('sé', 'sabes', 'sabe',
                       'sabemos', 'sabéis', 'saben'),
                       'pretérito indefinido': ('supe', 'supiste', 'supo',
                        'supimos', 'supisteis', 'supieron')},
           'correr': {'presente de indicativo': ('corro', 'corres', 'corre',
                      'corremos', 'corréis', 'corren'),
                      'pretérito indefinido': ('corrí', 'corriste', 'corrió',
                        'corrimos', 'corristeis', 'corrieron')},
            'hacer': {'presente de indicativo': ('hago', 'haces', 'hace',
                      'hacemos', 'hacéis', 'hacen'),
                      'pretérito indefinido': ('hice', 'hiciste', 'hizo',
                        'hicimos', 'hicisteis', 'hicieron')},
            'traer': {'presente de indicativo': ('traigo', 'traes', 'trae',
                      'traemos', 'traéis', 'traen'),
                      'pretérito indefinido': ('traje', 'trajiste', 'trajo',
                        'trajimos', 'trajisteis', 'trajeron')}
           }


resp_ir = {'id': "3", 'salir': {'presente de indicativo': ('salgo', 'sales', 'sale',
                        'salimos', 'salís', 'salen'),
                        'pretérito indefinido': ('salí', 'saliste', 'salió',
                         'salimos', 'salisteis', 'salieron')},
           'vivir': {'presente de indicativo': ('vivo', 'vives', 'vive',
                       'vivemos', 'vivís', 'viven'),
                       'pretérito indefinido': ('viví', 'viviste', 'vivió',
                        'vivimos', 'vivisteis', 'vivieron')},
           'dormir': {'presente de indicativo': ('duermo', 'duermes', 'duerme',
                      'dormimos', 'dormís', 'duermen'),
                      'pretérito indefinido': ('dormí', 'dormiste', 'durmió',
                        'dormimos', 'dormisteis', 'durmieron')},
            'decir': {'presente de indicativo': ('digo', 'dices', 'dice',
                      'decimos', 'decís', 'dicen'),
                      'pretérito indefinido': ('dije', 'dijiste', 'dijo',
                        'dijimos', 'dijisteis', 'dijeron')}
           }




# função de criar novo save
def novo_save(nome_usuario):
    f = open(f'{nome_usuario}.txt', 'x')
    f.write(f'{nome_usuario}')
    f.write("\n0")
    f.write("\n0")
    f.close()


# função de ler save existente e pegar valores
def save_existe(nome_usuario):
    f = open(f'{nome_usuario}.txt', 'r')
    dados = f.readlines()
    nome_usuario = dados[0]
    verbos_perfeitos = dados[1]
    recorde_save = dados[2]
    f.close()
    return int(verbos_perfeitos), int(recorde_save)

# save antes de fechar o programa
def salvar_dados(nome_usuario, verbos_perfeitos, recorde_save):
    f = open(f'{nome_usuario}.txt', 'w')
    f.write(f'{nome_usuario}')
    f.write(f'\n{verbos_perfeitos}')
    f.write(f'\n{recorde_save}')
    f.close()

# Boas vindas
def bem_vindo(nome_usuario, verbos_perfeitos, recorde):
    print(f"Bem-vindo, {nome_usuario}!\n"
          f"Você está com uma sequência de {verbos_perfeitos}.\n"
          f"Seu recorde é de {recorde} verbos perfeitos seguidos.")
# menu
lista_opcoes = ['1', '2', '3', '4']
def menu():
    print("1 - Terminado em -ar\n"
          "2 - Terminado em -er\n"
          "3 - Terminado em -ir\n"
          "4 - Qualquer um\n")

#função para selecionar um verbo aleatoriamente
chave = ''
id = ''
def selecao_verbos(opcao):
    if opcao == "1":
        verbo_aleat = random.randint(0, len(lista_verbos_ar)-1)
        aparece = lista_verbos_ar[verbo_aleat]
        id = "1"
    if opcao == "2":
        verbo_aleat = random.randint(0, len(lista_verbos_er)-1)
        aparece = lista_verbos_er[verbo_aleat]
        id = "2"
    if opcao == "3":
        verbo_aleat = random.randint(0, len(lista_verbos_ir)-1)
        aparece = lista_verbos_ir[verbo_aleat]
        id = "3"
    if opcao == "4":
        verbo_aleat = random.randint(0, len(lista_completa) - 1)
        aparece = lista_completa[verbo_aleat]
        if aparece in lista_verbos_ar:
            id = "1"
        if aparece in lista_verbos_er:
            id = "2"
        if aparece in lista_verbos_ir:
            id = "3"

    print(f"O verbo a ser conjugado é:\n"
          f"-=-=-=-=-=-=-=-=-=-=\n"
          f"{aparece:^20}\n"
          f"-=-=-=-=-=-=-=-=-=-=\n")
    return aparece, id

# função para selecionar o tempo verbal
lista_tempo = ["1", "2"]
def tempo_verbal():
    print("1 - presente de indicativo\n"
          "2 - pretérito indefinido\n")
    opcao_tempo = input("Qual o tempo verbal?")
    while opcao_tempo not in lista_tempo:
        print("Opção inválida!\n")
        opcao_tempo = input("Qual o tempo verbal?")
    if opcao_tempo == "1":
        return 'presente de indicativo'
    if opcao_tempo == '2':
        return 'pretérito indefinido'

# seleciona um verbo aleatório e retorna chave e id para identificação do tempo
def opcao_verbo():
    while True:
        verbo = input("Qual tipo de verbo você quer conjugar? ")
        if verbo not in lista_opcoes:
            print("Essa opção não existe!")
        else:
            chave_int = selecao_verbos(verbo)
            return chave_int
            break


lista_continua = ['S', 'N']
# começando de um save existente
load = input("Você quer continuar da sessão anterior? [S/N]").upper()
while load not in lista_continua:
    load = input("Você quer continuar da sessão anterior? [S/N]").upper()
if load in "Ss":
    while True:
        try:
            nome = input("Qual o seu nome (que também é o nome do save)?")
            save_existe(nome)
            break
        except:
            print("Não existe um save com esse nome.")
            opcao_save = input("Você quer criar um novo save com esse nome? [S/N]").upper()
            while opcao_save not in lista_continua:
                opcao_save = input("Você quer criar um novo save com esse nome? [S/N]").upper()
            if opcao_save in 'Ss':
                novo_save(nome)
                break
if load in 'Nn':
    nome = input("Qual o seu nome (que também vai ser o nome do save)?")
    novo_save(nome)

# conjugando
verbos_perfeitos, recorde = save_existe(nome)
bem_vindo(nome, verbos_perfeitos, recorde)
menu() # imprime menu
chave, id = opcao_verbo() # dados para selecionar o verbo
tempo = tempo_verbal() # seleciona o tempo verbal
acertos = 0

while True:
    print(tempo)
    if id == "1":
        for i in range(0, 6):
            conjug = input(f'{pronomes_pessoais[i]} ')
            if conjug == resp_ar[chave][tempo][i]:
                print('Correto!')
                acertos += 1
                print(f'Acertos: {acertos}/6')
            else:
                print(f'Que pena! A resposta correta é: {resp_ar[chave][tempo][i]}')
                print(f'Acertos: {acertos}/6')
    if id == "2":
        for i in range(0, 6):
            conjug = input(f'{pronomes_pessoais[i]} ')
            if conjug == resp_er[chave][tempo][i]:
                print('Correto!')
                acertos += 1
                print(f'Acertos: {acertos}/6')
            else:
                print(f'Que pena! A resposta correta é: {resp_er[chave][tempo][i]}')
                print(f'Acertos: {acertos}/6')
    if id == "3":
        for i in range(0, 6):
            conjug = input(f'{pronomes_pessoais[i]} ')
            if conjug == resp_ir[chave][tempo][i]:
                print('Correto!')
                acertos += 1
                print(f'Acertos: {acertos}/6')
            else:
                print(f'Que pena! A resposta correta é: {resp_ir[chave][tempo][i]}')
                print(f'Acertos: {acertos}/6')

    if acertos == 6:
        verbos_perfeitos +=1
        if verbos_perfeitos > recorde:
            recorde = verbos_perfeitos
    else:
        verbos_perfeitos = 0
        print('Ah! Você perdeu uma sequência de conjugações perfeitas.')
    if acertos == 6 and verbos_perfeitos == 1:
        print(f'Show! Você acertou o verbo perfeitamente. Continue para conseguir uma sequência!')
    if acertos == 6 and verbos_perfeitos > 1:
        print(f'Agora sim! Você está com uma sequência de {verbos_perfeitos} verbos conjugados '
              f'perfeitamente.')

    continuar = input("Quer continuar? [S/N]").upper()
    while continuar not in lista_continua:
        continuar = input("Quer continuar? [S/N]").upper()
    if continuar in 'Ss':
        acertos = 0
        menu()
        chave, id = opcao_verbo()
        tempo = tempo_verbal()
    if continuar in 'Nn':
        salvar_dados(nome, verbos_perfeitos, recorde)
        break