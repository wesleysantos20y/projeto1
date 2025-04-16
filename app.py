import streamlit as st
import spacy
import random
import datetime

# Carrega o modelo de linguagem do spaCy
nlp = spacy.load("pt_core_news_sm")

# Funções de utilidade
def gerar_resposta(mensagem):
    mensagem = mensagem.lower()
    doc = nlp(mensagem)

    # Comandos secretos
    if "hora" in mensagem:
        agora = datetime.datetime.now().strftime("%H:%M")
        return f"🕒 Agora são {agora}."

    if "data" in mensagem:
        hoje = datetime.datetime.now().strftime("%d/%m/%Y")
        return f"📅 Hoje é {hoje}."

    if "piada" in mensagem or "piadas" in mensagem:
        return random.choice(respostas_piadas)

    if "me elogie" in mensagem:
        return random.choice(respostas_elogios)

    if "limpar" in mensagem:
        st.session_state["mensagens"] = []
        return "🧹 Conversa limpa!"

    if "obrigado" in mensagem or "valeu" in mensagem:
        return "De nada! 😄"

    # Cumprimentos
    if any(palavra in mensagem for palavra in ["oi", "olá", "bom dia", "boa tarde", "boa noite"]):
        return random.choice(respostas_cumprimentos)

    # Perguntas genéricas
    if "tudo bem" in mensagem:
        return random.choice(respostas_tudo_bem)

    if "quem é você" in mensagem:
        return "Sou um chatbot simples feito em Python! 🤖"

    # Aleatório
    return random.choice(respostas_padrao)

# Respostas pré-definidas
respostas_cumprimentos = [
    "Oi! Tudo certo? 😊",
    "Olá! Como posso te ajudar hoje?",
    "E aí! 👋",
    "Fala aí, beleza?",
]

respostas_tudo_bem = [
    "Tudo ótimo, obrigado por perguntar!",
    "Estou funcionando 100%! E você?",
    "Tudo na paz. 🤖",
]

respostas_padrao = [
    "Hmmm... não entendi muito bem. Pode repetir?",
    "Interessante... continue!",
    "Fale mais sobre isso!",
    "Uau, me conta mais!",
]

respostas_piadas = [
    "Por que o Python foi ao terapeuta? Porque tinha muitos loops na cabeça! 😂",
    "O que o zero disse para o oito? Belo cinto! 😆",
    "Como o programador se despede? 'Vou dar um commit aqui.'",
]

respostas_elogios = [
    "Você é incrível! 💖",
    "Sua presença já melhora tudo. 🌟",
    "Você é muito inteligente, sério!",
]

# Inicializa sessão
if "mensagens" not in st.session_state:
    st.session_state["mensagens"] = []

# Interface
st.set_page_config(page_title="Chatbot IA", layout="centered")
st.title("💬 Chatbot em Python")
st.write("Converse comigo! Sou um bot simples mas simpático 😄")

# Campo de entrada
entrada_usuario = st.text_input("Digite sua mensagem aqui 👇", "")

# Processamento
if entrada_usuario:
    st.session_state["mensagens"].append(("Você", entrada_usuario))
    resposta = gerar_resposta(entrada_usuario)
    st.session_state["mensagens"].append(("Bot", resposta))

# Exibe histórico
for autor, texto in reversed(st.session_state["mensagens"]):
    if autor == "Você":
        st.markdown(f"**🧑 {autor}:** {texto}")
    else:
        st.markdown(f"**🤖 {autor}:** {texto}")

# Rodapé
st.divider()
st.markdown("Desenvolvido com ❤️ em Python + Streamlit")
