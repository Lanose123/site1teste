import streamlit as st

# Dados fixos
USUARIO_FIXO = "admin"
SENHA_FIXA = "1234"
PLANO_ATUAL = "Grátis"

# Inicializar sessão
if "logado" not in st.session_state:
    st.session_state.logado = False
if "atalhos" not in st.session_state:
    st.session_state.atalhos = {}

# Função de login
def login():
    st.title("Início - Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if usuario == USUARIO_FIXO and senha == SENHA_FIXA:
            st.session_state.logado = True
            st.success("Login bem-sucedido!")
        else:
            st.error("Usuário ou senha inválidos")

# Menu lateral
st.sidebar.title("Menu")
menu = st.sidebar.radio(
    "Navegar:",
    options=["Início"] + (["Configurar Textos", "Planos"] if st.session_state.logado else []),
)

# Página: Início
if menu == "Início":
    if not st.session_state.logado:
        login()
    else:
        st.success("Você já está logado!")

# Página: Configurar Textos
elif menu == "Configurar Textos":
    st.title("Configurar Textos")

    st.subheader("Atalhos atuais:")
    for tecla, texto in st.session_state.atalhos.items():
        st.markdown(f"**{tecla}** → {texto}")

    st.subheader("Adicionar novo atalho")
    nova_tecla = st.text_input("Tecla")
    novo_texto = st.text_input("Texto")
    if st.button("Adicionar"):
        if nova_tecla and novo_texto:
            st.session_state.atalhos[nova_tecla] = novo_texto
            st.success(f"Atalho '{nova_tecla}' adicionado!")
            st.experimental_rerun()

    st.subheader("Remover atalho")
    tecla_remover = st.selectbox("Escolha a tecla", options=list(st.session_state.atalhos.keys()))
    if st.button("Remover"):
        del st.session_state.atalhos[tecla_remover]
        st.success(f"Atalho '{tecla_remover}' removido!")
        st.experimental_rerun()

# Página: Planos
elif menu == "Planos":
    st.title("Plano Atual")
    st.info(f"Seu plano: **{PLANO_ATUAL}**")
    st.markdown("Em breve: upgrades e mais funcionalidades!")