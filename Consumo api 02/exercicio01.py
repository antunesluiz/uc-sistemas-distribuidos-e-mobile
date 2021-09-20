import requests
from datetime import datetime
import sqlite3

url = 'https://api.hgbrasil.com/finance?'

params = {
    'array_limit': 1,
    'fields':  'only_results,currencies',
    'key': 'ecfb2c0e'
}

response = requests.get(url, params=params)

if (response):
    currencies = response.json()['currencies']

    usd = currencies['USD']['buy']
    eur = currencies['EUR']['buy']
    date = datetime.now()

    params = [(
        date, usd, eur
    )]

    conn = sqlite3.connect('./bdcotacoes.db', timeout=10)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS moedas (
            Data DATE NOT NULL PRIMARY KEY,
            Dolar FLOAT NOT NULL,
            Euro FLOAT NOT NULL
        );
    """)

    cursor.executemany("""
        INSERT INTO moedas (Data, Dolar, Euro)
        VALUES (?,?,?)
    """, params)

    conn.commit()
    conn.close()
else:
    print('Erro na requisição da api')
