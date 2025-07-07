import requests

def get_cotacao(destino):

    url = 'https://api.exchangerate-api.com/v4/latest/' + destino

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:

        return data["rates"]

    else:
        print('Erro ao obter cotações: ', response.status_code)
        return None
    
def converterCotaca(origem, destino, valor = 1):
    rates = get_cotacao(destino)
    return round(valor / rates[origem], 4)

print(converterCotaca('JPY', 'BRL', 2000000))