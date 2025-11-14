import streamlit as st
import json
from streamlit import set_page_config
from dashboard import display_dashboard
from editor import edit_json

def main():
    set_page_config(layout="wide")
    uploaded_file = st.sidebar.file_uploader("Escolha um arquivo JSON", type="json")
    if uploaded_file is None:
        st.session_state.clear()  
        
    if uploaded_file is not None:   
        try:
            source_data = json.load(uploaded_file)
            uploaded_file.seek(0)
            valid_keys = {"TRANSFORMS", "SOURCES", "DESTINIES"}

            if not any(key in source_data for key in valid_keys):
                st.warning("Arquivo JSON inválidos no Sistema.  \nRecarregue novamente o arquivo, pois usam as chaves: TRANSFORMS, SOURCES ou DESTINIES.", icon="⚠️")
            else:
                st.sidebar.header("Editar JSON")
                if "source_data" not in st.session_state or st.session_state["uploaded_file_name"] != uploaded_file.name:
                    st.session_state["source_data"] = source_data
                    st.session_state["uploaded_file_name"] = uploaded_file.name
                page = st.sidebar.selectbox("Escolha uma seção:", ["Edit JSON", "Dashboard"])

                if page == "Dashboard":
                    display_dashboard(st.session_state["source_data"], uploaded_file)
                elif page == "Edit JSON":
                    edit_json(st.session_state["source_data"], st.session_state["uploaded_file_name"])
        except json.JSONDecodeError:
            st.error("Erro ao decodificar o arquivo. Verifique se é um JSON")
        except Exception as e:
            st.error(f"Ocorreu um erro inesperado: {e}")    

if __name__ == "__main__":
    main()