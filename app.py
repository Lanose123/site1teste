import streamlit as st
import json
import os
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Sistema de Atalhos", layout="wide")

# Função de inicialização e carregamento de dados
def carregar_dados():
    # Verifica se os arquivos existem, caso contrário, cria-os com conteúdo inicial
    if not os.path.exists("usuarios.json"):
        with open("usuarios.json", "w") as f:
            json.dump([], f)

    if not os.path.exists("acessos.json"):
        with open("acessos.json", "w") as f:
            json.dump({}, f)

    if not os.path.exists("atalhos.json"):
        with open("atalhos.json", "w") as f:
            json.dump({}, f)

    # Tenta carregar os dados dos arquivos JSON
    try:
        with open("usuarios.json", "r") as f:
            usuarios = json.load(f)

        with open("acessos.json", "r") as f:
            acessos = json.load(f)

        with open("atalhos.json", "r") as f:
            atalhos = json.load(f)

    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        usuarios, acessos, atalhos = [], {}, {}

    return usuarios, acessos, atalhos

# Carregar os dados
usuarios, acessos, atalhos = carregar_dados()

# Função para salvar os dados atualizados
def salvar_dados():
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f)
    with open("acessos.json", "w") as f:
        json.dump(acessos, f)
    with open("atalhos.json", "w") as f:
        json.dump(atalhos, f)

# Função de login
def login():
    st.title("Início - Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        usuario_encontrado = next((u for u in usuarios if u["usuario"] == usuario), None)
        if usuario_encontrado and usuario_encontrado["senha"] == senha:
            st.session_state.usuario_logado = usuario
            st.session_state.is_logado = True
            acessos[str(datetime.now())] = {
                "usuario": usuario,
                "senha": senha,
                "data": str(datetime.now())
            }
            salvar_dados()
            st.success("Login bem-sucedido!")
        else:
            st.error("Usuário ou senha inválidos.")

# Função de cadastro
def cadastrar_usuario():
    st.title("Cadastro de Novo Usuário")
    nome_usuario = st.text_input("Nome de Usuário")
    senha_usuario = st.text_input("Senha", type="password")
    email_usuario = st.text_input("Email")
    telefone_usuario = st.text_input("Telefone")
    
    if st.button("Cadastrar"):
        if nome_usuario and senha_usuario and email_usuario and telefone_usuario:
            usuarios.append({
                "usuario": nome_usuario,
                "senha": senha_usuario,
                "email": email_usuario,
                "telefone": telefone_usuario
            })
            salvar_dados()
            st.success("Usuário cadastrado com sucesso!")
        else:
            st.error("Todos os campos devem ser preenchidos.")

# Função de exibição de painel de admin
def painel_admin():
    if st.session_state.usuario_logado == "admin":
        st.title("Painel de Administração")
        st.write("Usuários Cadastrados:")
        for u in usuarios:
            st.write(f"Usuário: {u['usuario']}, Email: {u['email']}, Telefone: {u['telefone']}")
        st.write("---")
        st.write("Logins Registrados:")
        for data, info in acessos.items():
            st.write(f"Data: {data}, Usuário: {info['usuario']}, IP: {info['senha']}")
    else:
        st.error("Você não tem permissão para acessar esta página.")

# Função de exibição e manipulação de atalhos
def gerenciar_atalhos():
    st.title("Gerenciar Atalhos de Texto")
    st.subheader("Atalhos atuais:")
    if atalhos:
        for tecla, texto in atalhos.items():
            st.markdown(f"**{tecla}** → {texto}")
    else:
        st.write("Nenhum atalho cadastrado.")
    
    st.subheader("Adicionar novo atalho")
    nova_tecla = st.text_input("Tecla")
    novo_texto = st.text_input("Texto")
    if st.button("Adicionar"):
        if nova_tecla and novo_texto:
            atalhos[nova_tecla] = novo_texto
            salvar_dados()
            st.success(f"Atalho '{nova_tecla}' adicionado!")

    st.subheader("Remover atalho")
    if atalhos:
        tecla_remover = st.selectbox("Escolha a tecla", options=list(atalhos.keys()))
        if st.button("Remover"):
            del atalhos[tecla_remover]
            salvar_dados()
            st.success(f"Atalho '{tecla_remover}' removido!")

# Função para navegação
def ir_para(pagina):
    st.session_state.pagina = pagina

# Controle de navegação
if "pagina" not in st.session_state:
    st.session_state.pagina = "Início"
if "is_logado" not in st.session_state:
    st.session_state.is_logado = False
if "usuario_logado" not in st.session_state:
    st.session_state.usuario_logado = None

# Barra de navegação
st.sidebar.title("Menu")
menu = st.sidebar.radio("Navegar:", ["Início", "Cadastrar Usuário", "Login", "Admin", "Gerenciar Textos"])

if menu == "Início":
    if not st.session_state.is_logado:
        st.title("Bem-vindo ao Sistema de Atalhos!")
        if st.button("Login"):
            ir_para("Login")
        if st.button("Cadastrar"):
            ir_para("Cadastrar Usuário")
    else:
        st.write(f"Bem-vindo, {st.session_state.usuario_logado}")
        if st.button("Sair"):
            st.session_state.is_logado = False
            ir_para("Início")

elif menu == "Cadastrar Usuário":
    cadastrar_usuario()

elif menu == "Login":
    login()

elif menu == "Admin":
    painel_admin()

elif menu == "Gerenciar Textos":
    gerenciar_atalhos()
