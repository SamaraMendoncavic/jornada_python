# Passo a Passo que este projeto irá fazer

# Título
# input de mensagem 
# A cada mensagem que o usuário enviar:
    # Mostrar a mensagem que o usuário enviou no chat
    # Pegar a pergunta e enviar para a IA responder 
    # Exibir a resposta da iA na tela

# Ferramentas

# Streamlit -> Apenas com o python criar o Frontend e o Backend
# IA -> OpenIA

# -----------------------------------------------------------

# Bibliotecas
import streamlit as st
from openai import OpenAI

# -----------------------------------------------------------

# Modelo de IA da OpenIA
modelo = OpenAI(api_key="adicionar chave de api")

# Criação título (Formato de texto -> markdown)
st.write("### Chatbot com IA - Feito por Samara Mendonça")

# Lista para armazenar todo o histórico de mensagem
# Caso a lista ainda não exista ele cria uma
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# Criação da input
input_usuario = st.chat_input("O que deseja saber hoje?")    

# Loop que mostrará todo o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

# Verifica se o texto existe
if input_usuario:

    # Fazer aparecer na tela
    # .chat_message(icone de quem esta enviando) 
    # Sua função dentro do chat
    st.chat_message("user").write(input_usuario)
    mensagem_usuario = {"role": "user", "content": input_usuario} # Dicionário para dicionar as mensaagem do usuários
    st.session_state["lista_mensagens"].append(mensagem_usuario) # Adicionar mensagem dentro da lista de mensagens

    # Começo resposta da IA
    resposta_ia = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model = "gpt-4o"
    )

    print(resposta_ia)
    texto_resp_ia = "Você enviou: " + input_usuario

    # Resposta da IA
    st.chat_message("assistant").write(texto_resp_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resp_ia} # Dicionário para adicionar as mensagem da ia
    st.session_state["lista_mensagens"].append(mensagem_ia)  # Adicionar mensagem dentro da lista de mensagens

print(st.session_state["lista_mensagens"])

    