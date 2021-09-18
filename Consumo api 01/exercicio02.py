import requests

url = 'https://viacep.com.br/ws/'
ceps = ['30140071', '30140072', '30140073', '30140074', '30140075']
formato = '/xml/'

for i in ceps:
    r = requests.get(url + i + formato)

    if (r.status_code == 200):
        print()
        print('JSON : ', r.content)
        print()
    else:
        print('Nao houve sucesso na requisicao.')
