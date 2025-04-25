import streamlit as st

# Título e barra superior com navegação
st.set_page_config(page_title="Sistema de Atalhos", layout="wide")

# Inicializar variáveis da sessão
if "pagina" not in st.session_state:
    st.session_state.pagina = "Início"
if "atalhos" not in st.session_state:
    st.session_state.atalhos = {}

# Função para mudar de página
def ir_para(pagina):
    st.session_state.pagina = pagina
    st.experimental_rerun()

# Barra de navegação superior
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("🏠 Início"):
        ir_para("Início")
with col2:
    if st.button("📝 Gerenciar Textos"):
        ir_para("Textos")
with col3:
    if st.button("💼 Planos"):
        ir_para("Planos")
with col4:
    if st.button("📞 Suporte"):
        ir_para("Suporte")
st.markdown("---")

# PÁGINAS

### PÁGINA INICIAL
if st.session_state.pagina == "Início":
    st.title("Bem-vindo ao Sistema de Atalhos")
    st.write("Escolha uma das opções abaixo:")
    st.button("📝 Gerenciar Textos", on_click=lambda: ir_para("Textos"))
    st.button("💼 Ver Planos", on_click=lambda: ir_para("Planos"))
    st.button("📞 Suporte", on_click=lambda: ir_para("Suporte"))

### PÁGINA: GERENCIAR TEXTOS
elif st.session_state.pagina == "Textos":
    st.title("Gerenciar Atalhos de Texto")

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
    if st.session_state.atalhos:
        tecla_remover = st.selectbox("Escolha a tecla", options=list(st.session_state.atalhos.keys()))
        if st.button("Remover"):
            del st.session_state.atalhos[tecla_remover]
            st.success(f"Atalho '{tecla_remover}' removido!")
            st.experimental_rerun()
    else:
        st.warning("Nenhum atalho cadastrado ainda.")

    st.button("🔙 Voltar para o Início", on_click=lambda: ir_para("Início"))

### PÁGINA: PLANOS
elif st.session_state.pagina == "Planos":
    st.title("Plano Atual")
    st.info("Seu plano: **Grátis**")
    st.markdown("Em breve: upgrades e mais funcionalidades!")

    st.button("🔙 Voltar para o Início", on_click=lambda: ir_para("Início"))

### PÁGINA: SUPORTE
elif st.session_state.pagina == "Suporte":
    st.title("Suporte")
    st.markdown("Entre em contato conosco:")
    st.markdown("📧 Email: suporte@example.com")
    st.markdown("📞 Telefone: (11) 99999-9999")

    st.button("🔙 Voltar para o Início", on_click=lambda: ir_para("Início"))
