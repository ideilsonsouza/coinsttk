import locale
from utils.constant import LIST_COINS

def converttk(ttk, base=0.01):
    value_in_rate = round(float(ttk) * base, 2)
    return value_in_rate

def convertPrince(ttk, rate):
    value_in_real = float(ttk) * float(rate)    
    return round(value_in_real,2)


def formatted_coin(coin, value):
    # Dicionário que mapeia moedas a seus símbolos
    symbols = {
        'BRL': 'R$',
        'USD': '$',
        'EUR': '€',
        'JPY': '¥'
    }

    # Verifica se a moeda está na lista suportada
    if coin not in symbols:
        raise ValueError(f"Moeda '{coin}' não suportada. Escolha uma das seguintes: {', '.join(LIST_COINS)}")

    try:
        # Tenta converter o valor para float
        numeric_value = float(value)
    except ValueError:
        raise ValueError(f"O valor '{value}' não pode ser convertido para um número.")

    # Formata o valor com duas casas decimais
    if coin in ['BRL', 'EUR']:
        formatted_value = f"{symbols[coin]} {numeric_value:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    else:  # Para USD e JPY
        formatted_value = f"{symbols[coin]} {numeric_value:,.2f}"

    return formatted_value