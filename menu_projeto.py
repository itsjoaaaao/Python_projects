dados = []
def cadastrarReceita(dados):
    rec = int(input("Digite o valor da receita:"))
    dados.append(rec)
    print("Receita cadastrada!")

def atualizarReceita():
    atu = int(input("Digite o valor da receita para ser atualizado:"))
    print("Receita atualizada!")

def excReceita():


def converterMoedas():
    API_KEY = "4afc7d2c60e8466ab39dbbf6ddb5f29c"
    r = requests.get(
        'https://openexchangerates.org/api/latest.json',
        params={
            'app_id': API_KEY,
            'symbols': 'BRL,USD',
            'show_alternative': 'true'
        }
    )
    rates_ = r.json()['rates']
    symbol_from = 'USD'
    symbol_to = 'BRL'
    value = int(input("Digite o quanto você quer converter:"))
    result = value * 1 / rates_.get(symbol_from) * rates_.get(symbol_to)
    print("O valor convertido de Dólar para Real é: ", result)

print("--------Organizador Financeiro-------- ")
op = 0
while op != 7:
    print('''
    1 - Cadastrar receita realizada
    2 - Atualizar receita realizada
    3 - Excluir receita realizada
    4 - Ver comparação de receitas e despesas
    5 - Ver o saldo
    6 - Análise de viabilidade de investimento
    7 - Converter moedas''')
    op = int(input("Selecione uma opção:"))
    if op == 1:
        cadastrarReceita(dados)
    elif op == 2:
        atualizarReceita()
    elif op == 3:
        excReceita()
    elif op == 4:
        print("teste")
    elif op == 5:
        print("teste")
    elif op == 6:
        print("teste")
    elif op == 7:
        print("----Converter moedas----")
        converterMoedas()
    else:
        print("Opção inválida")