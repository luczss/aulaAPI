import requests
"""
cep = '01311000'
link = f'https://viacep.com.br/ws/{cep}/json'

try:
    requisicao = requests.get(link)

    if requisicao.status_code == 200:
        dic_requisicao = requisicao.json()

        print(f"CEP: {dic_requisicao['cep']}")
        print(f"Logradouro: {dic_requisicao['logradouro']}")
        print(f"Complemento: {dic_requisicao['complemento']}")
        print(f"Bairro: {dic_requisicao['bairro']}")
        print(f"Localidade: {dic_requisicao['localidade']}")
        print(f"UF: {dic_requisicao['uf']}")

    elif requisicao.status_code == 404:
        print('Não foi possível encontrar o endereço passado como parâmetro')

    elif requisicao.status_code == 500:
        print('Ocorreu algum erro no servidor')

    else:
        print(requisicao.status_code)
except ConnectionError:
    print('Erro de Conexão')

except Exception:
    print('Erro')
"""
"""
cep = input('Digite o CEP: ')
link = f'https://viacep.com.br/ws/{cep}/json'

try:
    resposta = requests.get(link)

    if resposta.status_code == 200:
        print(f'Erro: {resposta.status_code}')
    else:
        dicionario = resposta.json()
        print(dicionario)
except ConnectionError:
    print('Erro de Conexão')
except Exception:
    print('Erro')
"""
"""
UF = input('Digite o UF:')
link = f'http://servicodados.ibge.gov.br/api/v1/localidades/estados/{UF}/municipios'

try:
    requisicao = requests.get(link)

    if requisicao.status_code == 200:
        dic_requisicao = requisicao.json()

        if dic_requisicao.get('erro'):
            print('CEP não encontrado')
        else:
            print(f"CEP: {dic_requisicao['cep']}")
            print(f"Logradouro: {dic_requisicao['logradouro']}")
            print(f"Complemento: {dic_requisicao['complemento']}")
            print(f"Bairro: {dic_requisicao['bairro']}")
            print(f"Localidade: {dic_requisicao['localidade']}")
            print(f"UF: {dic_requisicao['uf']}")

    elif requisicao.status_code == 404:
        print('Não foi possível encontrar o endereço.')

    elif requisicao.status_code == 500:
        print('Ocorreu um erro no servidor.')

    else:
        print(f'Erro HTTP: {requisicao.status_code}')

except requests.exceptions.ConnectionError:
    print('Erro de conexão.')

except Exception as erro:
    print(f'Erro: {erro}')
"""
"""
try:
    n = int(input('Quantidade: '))
    resposta = requests.get(f'https://randomuser.me/api/?results={n}')

    if resposta.status_code == 200:
        dicionario = resposta.json()
        lista = dicionario['results']                   # lista de resultados

        lista_nomes = []
        for item in lista:                              # insere nomes em outra lista
            nome = item['name']
            lista_nomes.append(f"{nome['first']} {nome['last']}")
        lista_nomes.sort()                              # ordena lista de nomes
        for nome in lista_nomes:                        # exibe nomes
            print(nome)
    else:
        print('Erro de requisição')
except Exception as erro:
    print(f'Erro: {erro}')
"""
"""
try:
    resposta = requests.get(f'http://dummyjson.com/recipes?limit=50')
    if resposta.status_code == 200:
        ing_busca = input('Ingrediente: ')
        dicionario = resposta.json()
        lista_receitas = dicionario['recipes']
        for receita in lista_receitas:
            lista_ing = receita['ingredients']
            for ingrediente in lista_ing:
                if ing_busca.lower() in ingrediente.lower():
                    print('-'*50)
                    print(receita['name'])
                    print(receita['ingredients'])
    else:
        print('Erro de requisição')
except Exception as erro:
    print(f'Erro: {erro}')
"""

import json

try:
    resposta = requests.get(f'http://dummyjson.com/products?limit=100')

    if resposta.status_code == 200:
        dicionario = resposta.json()

        with open('ex04.json', 'w', encoding='utf-8') as arquivo:
            json.dump(dicionario, arquivo, indent=4, ensure_ascii=False)

        print()

        lista_produtos = dicionario['products']     # lista de produtos

        quantidade = 0
        valor_total = 0
        for produto in lista_produtos:              # percorre lista de produtos
            preco = float(produto['price'])
            desconto = float(produto['discountPercentage'])
            quantidade += int(produto['stock'])
            preco -= preco * desconto / 100         # calcula preço com desconto
            valor_total += preco * quantidade       # somatório de valores

        print(f'Quantidade de produtos: {quantidade}')
        print(f'Valor Total: {valor_total:.2f}')
    else:
        print(f'Erro de requisição: {resposta.status_code}')
except Exception as erro:
    print(f'Erro de requisição: {erro}')