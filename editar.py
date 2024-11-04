import pandas as pd
import streamlit as st

def editar_planilha(usuario):
    usuario = st.session_state.usuario_logado  # Obtém o usuário logado

    st.write(f"Usuário logado: {usuario}")  # Debug
    file_path = f"dados_acumulados_{usuario}.xlsx"
    
    st.write(f"Tentando carregar: {file_path}")  # Debug

    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        st.error("A planilha não foi encontrada.")
        return

    st.header(f"Edição de Dados - {usuario}")
    df_editar = st.data_editor(df, height=300)

    if st.button("Salvar Alterações"):
        df_editar.to_excel(file_path, index=False)
        st.success("Alterações salvas com sucesso!")

    if st.button("Excluir Dados"):
        if st.button("Confirmar Exclusão"):
            df_editar = pd.DataFrame()  # Limpar o dataframe
            df_editar.to_excel(file_path, index=False)
            st.success("Dados excluídos com sucesso!")
