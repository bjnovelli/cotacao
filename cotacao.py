import requests
import tkinter as tk

def pegar_cotacoes():
    try:
        moedas = "USD-BRL,EUR-BRL,BTC-BRL"
        requisicao = requests.get(f"https://economia.awesomeapi.com.br/json/last/{moedas}")
        requisicao_dic = requisicao.json()

        cotacao_dolar = requisicao_dic['USDBRL']['bid']
        cotacao_euro = requisicao_dic['EURBRL']['bid']
        cotacao_btc = requisicao_dic['BTCBRL']['bid']

        texto = f'''
Dólar: R$ {cotacao_dolar}
Euro: R$ {cotacao_euro}
BTC : R$ {cotacao_btc}
'''
        texto_cotacoes["text"] = texto
    except Exception as e:
        texto_cotacoes["text"] = f"Erro ao buscar cotações:\n{e}"

# Criando a janela principal
janela = tk.Tk()
janela.title("Cotação Atual das Moedas")
janela.geometry("350x220")

# Define a cor de fundo da janela
cor_fundo = "#D0E7FF"  # Azul bem claro
janela.configure(bg=cor_fundo)

# Texto de orientação
texto_orientacao = tk.Label(
    janela,
    text="Clique no botão para ver as cotações das moedas",
    bg=cor_fundo,
    font=("Arial", 10)
)
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)

# Botão para buscar cotações
botao = tk.Button(
    janela,
    text="Buscar cotações Dólar/Euro/BTC",
    command=pegar_cotacoes
)
botao.grid(column=0, row=1, padx=10, pady=10)

# Campo onde o resultado será exibido
texto_cotacoes = tk.Label(janela, text="", bg=cor_fundo, font=("Arial", 10))
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10)

# Inicia a interface
janela.mainloop()
