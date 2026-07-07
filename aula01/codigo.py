# Aula 01 - Jornada Python

# Importação das bibliotecas necessárias
import pyautogui
import time
import pandas as pd

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Passo 1: Entrar no sistema da empresa
# Abrir o navegador 
pyautogui.PAUSE = 0.5 # pausa de tempo entre um comando e outro

pyautogui.press("win") # clicar na tecla windows
pyautogui.write("chrome") # pesquisar o navegador
pyautogui.press("enter") # clicar na tecla enter

# variável para armazenar a url do site
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(site) # pesquisar site 
pyautogui.press("enter") # entrar no site

time.sleep(10) # tempo para esperar carregar o site

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Passo 2: Fazer login
# clicar no campo de email
pyautogui.click(x=635, y=479) # local da tela que contém o input
pyautogui.write("samaramend@gmail.com") # email de login
pyautogui.press("tab") # passar para o próximo campo

# encrever no campo de senha
pyautogui.write("senha") # senha

# clicar no botão de logar
pyautogui.press("tab")
pyautogui.press("enter")

# fazer pausa para o site carregar
time.sleep(3)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Passo 3: Abrir a base de dados
arquivo_dados = pd.read_csv("produtos.csv")
print("Arquivo aberto com sucesso!", arquivo_dados)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Passo 4: Cadastrar primeiro produto

# clicar no campo do código
pyautogui.click(x=613, y=325) 

# Código
pyautogui.write("000999hhhhh")
pyautogui.press("tab") # passar próximo campo

# Marca
pyautogui.write("Marca")
pyautogui.press("tab") # passar próximo campo

# Tipo
pyautogui.write("Tipo")
pyautogui.press("tab") # passar próximo campo

# Categoria
pyautogui.write("Categoria")
pyautogui.press("tab") # passar próximo campo

# Preço Unitário
pyautogui.write("Preco")
pyautogui.press("tab") # passar próximo campo

# Custo
pyautogui.write("Custo")
pyautogui.press("tab") # passar próximo campo

# obs
pyautogui.write("Observacoes")
pyautogui.press("tab") # passar para o botão enviar

pyautogui.press("enter")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Passo 5: Repetir passo 4 até o último produto
# Para cada linha do arquivo .csv
for linha in arquivo_dados.index:
    pyautogui.click(x=613, y=325) 

    # Código
    codigo = str(arquivo_dados.loc[linha, "codigo"])

    pyautogui.write(codigo)
    pyautogui.press("tab") # passar próximo campo

    # Marca
    marca = str(arquivo_dados.loc[linha, "marca"])

    pyautogui.write(marca)
    pyautogui.press("tab") # passar próximo campo

    # Tipo
    tipo = str(arquivo_dados.loc[linha, "tipo"])

    pyautogui.write(tipo)
    pyautogui.press("tab") # passar próximo campo

    # Categoria
    categoria = str(arquivo_dados.loc[linha, "categoria"])

    pyautogui.write(categoria)
    pyautogui.press("tab") # passar próximo campo

    # Preço Unitário
    preco_uni = str(arquivo_dados.loc[linha, "preco_unitario"])

    pyautogui.write(preco_uni)
    pyautogui.press("tab") # passar próximo campo

    # Custo
    custo = str(arquivo_dados.loc[linha, "custo"])

    pyautogui.write(custo)
    pyautogui.press("tab") # passar próximo campo

    # obs
    obs = str(arquivo_dados.loc[linha, "obs"])

    pyautogui.write(obs)
    pyautogui.press("tab") # passar para o botão enviar

    pyautogui.press("enter")

    pyautogui.scroll(1000)

print("Base de dados cadastrada!")