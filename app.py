import streamlit as st

st.set_page_config(page_title="Sistema de Atalhos", layout="wide")

# Inicialização
if "pagina" not in st.session_state:
    st.session_state.pagina = "Início"
if "atalhos" not in st.session_state:
    st.session_state.atalhos = {}

# Função para mudar de página (sem rerun)
def ir_para(pagina):
    st.session_state.pagina = pagina

# Barra de navegação
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("🏠 Início", key="nav_inicio"):
        ir_para("Início")
with col2:
    if st.button("📝 Gerenciar Textos", key="nav_textos"):
        ir_para("Textos")
with col3:
    if st.button("💼 Planos", key="nav_planos"):
        ir_para("Planos")
with col4:
    if st.button("📞 Suporte", key="nav_suporte"):
        ir_para("Suporte")
st.markdown("---")

# CONTEÚDO DAS PÁGINAS

if st.session_state.pagina == "Início":
    st.title("Bem-vindo ao Sistema de Atalhos")
    st.write("Escolha uma das opções abaixo:")
    if st.button("📝 Gerenciar Textos", key="home_textos"):
        ir_para("Textos")
    if st.button("💼 Ver Planos", key="home_planos"):
        ir_para("Planos")
    if st.button("📞 Suporte", key="home_suporte"):
        ir_para("Suporte")

elif st.session_state.pagina == "Textos":
    st.title("Gerenciar Atalhos de Texto")

    st.subheader("Atalhos atuais:")
    if st.session_state.atalhos:
        for tecla, texto in st.session_state.atalhos.items():
            st.markdown(f"**{tecla}** → {texto}")
    else:
        st.write("Nenhum atalho cadastrado.")

    st.subheader("Adicionar novo atalho")
    nova_tecla = st.text_input("Tecla", key="nova_tecla")
    novo_texto = st.text_input("Texto", key="novo_texto")
    if st.button("Adicionar", key="adicionar_atalho"):
        if nova_tecla and novo_texto:
            st.session_state.atalhos[nova_tecla] = novo_texto
            st.success(f"Atalho '{nova_tecla}' adicionado!")

    st.subheader("Remover atalho")
    if st.session_state.atalhos:
        tecla_remover = st.selectbox("Escolha a tecla", list(st.session_state.atalhos.keys()), key="tecla_remover")
        if st.button("Remover", key="remover_atalho"):
            del st.session_state.atalhos[tecla_remover]
            st.success(f"Atalho '{tecla_remover}' removido!")

    if st.button("🔙 Voltar para o Início", key="voltar_textos"):
        ir_para("Início")

elif st.session_state.pagina == "Planos":
    st.title("Plano Atual")
    st.info("Seu plano: **Grátis**")
    st.markdown("Em breve: upgrades e mais funcionalidades!")

    if st.button("🔙 Voltar para o Início", key="voltar_planos"):
        ir_para("Início")

elif st.session_state.pagina == "Suporte":
    st.title("Suporte")
    st.markdown("Entre em contato conosco:")
    st.markdown("📧 Email: suporte@example.com")
    st.markdown("📞 Telefone: (11) 99999-9999")

    if st.button("🔙 Voltar para o Início", key="voltar_suporte"):
        ir_para("Início")
