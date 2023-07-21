
import requests
from keys.mytoken import tokenFut

API_TOKEN = tokenFut()
BASE_URL = 'https://api.api-futebol.com.br/v1'

def Ranking():
    app_tabela = requests.get(
        url=f'{BASE_URL}/campeonatos/10/fases/317',
        headers={
            'Authorization': API_TOKEN
        }
    )
    app_info = requests.get(
        url=f'{BASE_URL}/campeonatos/10',
        headers={
            'Authorization': API_TOKEN
        }
    )
    classification_br = app_tabela.json()
    info_championship = app_info.json()

    list_tabela = []
    print(classification_br['tabela'])
    for team in classification_br['tabela']:
        posicao = team['posicao']
        time = team['time']['nome_popular']
        pontos = team['pontos']
        classificacao = f'''{posicao}º {time} ------- {pontos} Pontos\n'''
        list_tabela.append(classificacao)

    nome_camp = info_championship['nome_popular']
    temp_camp = info_championship['edicao_atual']['temporada']
    rodada_camp = info_championship['rodada_atual']['nome']

    info_ = f'-'*10, f'*{nome_camp} {temp_camp}*', '-'*10, f'\n› _{rodada_camp}_'
    msf_classification = *info_,'\n\n',*list_tabela
    return msf_classification
