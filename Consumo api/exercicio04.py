import requests

url = 'https://viacep.com.br/'
cep = 'abc/'

r = requests.get(url + cep)

if (r.status_code == 200):
    print()
    print('JSON : ', r.content)
    print()
else:
    print('Nao houve sucesso na requisicao.')
    print('Código de retorno: ', r.status_code)
    print('Mensagem ', r.text)
