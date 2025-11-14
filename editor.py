import streamlit as st
import json
from components.render_dimensions import render_dimensions_input
from components.render_list import render_list_input
from components.render_transforms import render_transforms_input
from components.render_measures import render_measures_input
from components.render_keyrefs import render_keyrefs_input

def edit_json(source_data, uploaded_file):
    st.subheader("Chaves do JSON")
    keys = list(source_data.keys())
    if len(keys) > 3:
        keys = keys[:3]
        col_key, col_subitem = st.columns(2)
        with col_key:
            selected_key = st.selectbox("Escolha uma chave", keys) 
        valor = source_data[selected_key]

        if isinstance(valor, list) and all(isinstance(item, str) for item in valor):           
            default_subitem = st.session_state.get("current_subitem")          
            default_index = 0  
            
            if default_subitem in valor:
                default_index = valor.index(default_subitem)           
            with col_subitem:
                new_subitem = st.selectbox(
                    f"Selecione um item de {selected_key}", 
                    valor, 
                    key="subitem_selector",
                    index=default_index
                )

        if new_subitem != st.session_state.get("current_subitem"):
            st.session_state["current_subitem"] = new_subitem
            for key in list(st.session_state.keys()):
                if key.startswith(("hsf_", "sid_list_", "lookupatts_", "columns_name_", "transforms_", "fixes_", "dimensions_", "transform_list_", "multiple_files_")):
                    del st.session_state[key]
            st.rerun() 

        if new_subitem in source_data:
            if selected_key == "TRANSFORMS":
                col_novo_item, col_espaco, col_novo_etl = st.columns([1, 1, 1])
                with col_novo_item:
                    if 'transform_list' not in source_data[new_subitem]:
                        source_data[new_subitem]['transform_list'] = []
                    tlist = source_data[new_subitem]['transform_list']
                    
                    if st.button("➕ Adicionar Novo Item", use_container_width=True, ):
                        tlist.append({})
                        st.rerun()               
                with col_espaco:
                    st.write("") 
                with col_novo_etl:
                    with st.expander("➕ Adicionar Novo ETL", expanded=False):
                        novo_nome = st.text_input("Nome do novo ETL", key="novo_etl_nome")

                        if st.button(" Criar Novo ETL", key="criar_novo_etl"):

                            if not novo_nome or not isinstance(novo_nome, str) or not novo_nome.strip():
                                st.warning("Digite um nome válido para o novo ETL.")
                            else:
                                novo_nome = novo_nome.strip()

                                if novo_nome in source_data.get(selected_key, []):
                                    st.warning("Já existe um ETL com esse nome.")
                                else:

                                    if selected_key not in source_data or not isinstance(source_data[selected_key], list):
                                        source_data[selected_key] = []
                                    source_data[selected_key].append(novo_nome)

                                    if novo_nome not in source_data:
                                        source_data[novo_nome] = {"transform_list": []}
                                    else:
                                        source_data.setdefault(novo_nome, {"transform_list": []})

                                    st.session_state["current_subitem"] = novo_nome
                                    st.success(f"Novo ETL '{novo_nome}' criado com sucesso!")
                                    st.rerun()

                if not tlist:
                    st.info("Este ETL ainda não possui itens. Clique em '➕ Adicionar Novo Item' acima para começar.")
                else:
                    abas = st.tabs([f"Item {i+1}" for i in range(len(tlist))])
                    for i, aba in enumerate(abas):
                        with aba:
                            st.markdown(f"### Item {i+1}")                           
                            # Grupo 1: SQL Files
                            with st.expander("Expandir item do SQL", expanded=False):
                                render_sql_input(st, tlist[i], i, new_subitem, tlist)
                            # Grupo 2: Detalhes do Item
                            with st.expander("Expandir detalhes do item", expanded=False):
                                render_detail_inputs(st, tlist[i], i)
                            # Grupo 3: Tabela
                            with st.expander("Expandir item da tabela", expanded=False):
                                render_table_input(st, tlist[i], i, new_subitem, tlist)
                            # Grupo 4: Key, IdFinder, Lookupatts e Columns_name
                            with st.expander("Expandir Key, IdFinder, Lookupatts e Columns_name", expanded=False):                               
                                row4_col1, row4_col2 = st.columns([1, 1])
                                with row4_col1:
                                    tlist[i]["key"] = st.text_input("Key", value=tlist[i].get("key", ""), key=f"key_{new_subitem}_{i}")
                                with row4_col2:   
                                    tlist[i]["idfinder"] = st.text_input("IdFinder", value=tlist[i].get("idfinder", ""), key=f"idfinder_{new_subitem}_{i}")
                                # Linha2 Lookupatts e Columns_name
                                row4_col1, row4_col2 = st.columns([1, 1])
                                with row4_col1:
                                    render_list_input(st, "Lookupatts", tlist[i].get("lookupatts", []), "lookupatts", i, new_subitem, "lookupatts", tlist)
                                with row4_col2:
                                    render_list_input(st, "Columns_name", tlist[i].get("columns_name", []), "columns_name", i, new_subitem, "columns_name", tlist)
                            # Grupo 5: Measures e Keyrefs
                            with st.expander("Expandir Measures e Keyrefs", expanded=False):
                                row3_col1, row3_col2 = st.columns([1, 1])
                                with row3_col1:
                                    render_measures_input(st, tlist[i].get("measures", []), i, new_subitem, tlist)
                                with row3_col2:
                                    render_keyrefs_input(st, tlist[i].get("keyrefs", []), i, new_subitem, tlist)
                            # Grupo 6: Dimensions
                            with st.expander("Expandir Dimensions", expanded=False):
                                render_dimensions_input(st, tlist[i].get("dimensions", []), i, new_subitem, tlist)
                            # Grupo 7: Transforms
                            with st.expander("Expandir Transforms", expanded=False):
                                    render_transforms_input(st, tlist[i].get("transforms", []), i, new_subitem, tlist)                
            else:
                st.subheader(f"Chave: {selected_key}")
            json_str = json.dumps(source_data[new_subitem], indent=2, ensure_ascii=False)        

            with st.expander("Expandir o Editor do JSON", expanded=False):
                st.caption("💡 Dica: Use 'Ctrl + F' no editor abaixo para localizar os caminhos encontrados na busca acima.")            

                if selected_key == "TRANSFORMS":   

                    edited_json_str = st.text_area("Edite o JSON abaixo:", value=json_str, height=800, key=f"json_editor_{new_subitem}")
                else:

                    edited_json_str = st.text_area("Edite o JSON abaixo:", value=json_str, height=300, key=f"json_editor_{new_subitem}")    

                if st.button("Salvar alterações", key=f"save_button_{new_subitem}"):
                    try:
                        edited_data = json.loads(edited_json_str)
                        source_data[new_subitem] = edited_data
                        st.success(f"{new_subitem} atualizado com sucesso!")
                        st.download_button(
                            label="Baixar JSON editado",
                            data=json.dumps(source_data, indent=2,
                                            ensure_ascii=False),
                            file_name="edited_" + uploaded_file,                            
                            mime="application/json",
                            key=f"download_button_{new_subitem}"
                        )
                    except Exception as e:
                        st.error(f"Erro ao salvar alterações: {e}")

            with st.expander(" Expandir a Visualização do JSON Formatada", expanded=False):
                st.json(source_data[new_subitem], expanded=False)
        else:
            st.warning(f"O item '{new_subitem}' não tem dados detalhados no JSON.")
    else:
        st.subheader(f"Valor de: {selected_key}")
        st.write(valor)

def render_sql_input(container, tlist_item, index, subitem_name, tlist):
    """Processar inputs relacionados a SQL"""
    container.markdown("**hana_sql_file:**")
    hana_sql_value = tlist_item.get("hana_sql_file", "")
    hana_sql_key = f"hana_sql_file_{subitem_name}_{index}"
    if hana_sql_key not in st.session_state:
        st.session_state[hana_sql_key] = hana_sql_value
    
    new_value = container.text_input(
        "Hana SQL File",
        value=st.session_state[hana_sql_key],
        key=f"input_{hana_sql_key}",
        label_visibility="collapsed"
    )

    st.session_state[hana_sql_key] = new_value 
    tlist[index]["hana_sql_file"] = new_value
    render_list_input(container, "SQL Increment Drop", tlist_item.get("sql_increment_drop", []), "sql_increment_drop", index, subitem_name, "sql_increment_drop", tlist)
    render_list_input(container, "SQL Create Fact", tlist_item.get("sql_create_fact", []), "sql_create_fact", index, subitem_name, "sql_create_fact", tlist)
    render_list_input(container, "SQL Full Drop", tlist_item.get("sql_full_drop", []), "sql_full_drop", index, subitem_name, "sql_full_drop", tlist)


def render_detail_inputs(container, tlist_item, index):
    """Renderiza inputs de detalhes do item"""
    container.text_input("DataFrame", value=str(tlist_item.get("dataFrame", "")), key=f"dataFrame_{index}")
    container.checkbox("Multiple Files", value=tlist_item.get("multiple_files", False), key=f"multiple_files_{index}", help="Marque se for verdadeiro, desmarque se for falso")
   
    # Sep
    sep_options_list = [";", ",", "|", "\t", " "]
    current_sep = tlist_item.get("sep")

    if f"sep_{index}" not in st.session_state:
        st.session_state[f"sep_{index}"] = current_sep if current_sep in sep_options_list else None


    sep_options = st.selectbox(
        "Sep",
        sep_options_list,
        key=f"sep_{index}",

    )
    tlist_item["sep"] = sep_options
    # Decimal
    decimal_options_list = [None, ".", ","]
    current_decimal = tlist_item.get("decimal")

    if f"decimal_{index}" not in st.session_state:
        st.session_state[f"decimal_{index}"] = current_decimal if current_decimal in decimal_options_list else None
       

    decimal_options = st.selectbox(
        "Decimal",
        decimal_options_list,
        key=f"decimal_{index}",               
    )
    tlist_item["decimal"] = decimal_options

    # Type
    type_options_list = ["Fact", "Dimension", "Stage"]
    current_type = tlist_item.get("type")

    if f"type_{index}" not in st.session_state:
        st.session_state[f"type_{index}"] = current_type if current_type in type_options_list else None


  
    type_options = st.selectbox(
        "Type",
        type_options_list,
        key=f"type_{index}",

    )
    tlist_item["type"] = type_options

    st.checkbox("Batch", value=tlist_item.get("batch", False), key=f"batch_{index}", help="Marque se for verdadeiro, desmarque se for falso")
    
    # Class     
    class_options_list = ["SQLBatchFact", "SQLBatchDimension", "SQLBatchStage"]
    current_class = tlist_item.get("class")


    if f"class_{index}" not in st.session_state:
        st.session_state[f"class_{index}"] = current_class if current_class in class_options_list else None 



    class_options = st.selectbox(
        "Class",
        class_options_list,
        key=f"class_{index}",

    )
    tlist_item["class"] = class_options

    # Methods"

    if f"methods_{index}" not in st.session_state:
        st.session_state[f"methods_{index}"] = tlist_item.get("methods", [])
    options = st.multiselect(
        "Methods",
        ["toStage", "populate_dimensions", "populate_fact"],
        key=f"methods_{index}"
    )
    tlist_item["methods"] = options

def render_table_input(container, tlist_item, index, subitem_name, tlist):
    # --- Campo 1: Stage Table Name ---
    field_name_stn = "stage_table_name"

    current_value_stn = tlist_item.get(field_name_stn, "")

    state_key_stn = f"{field_name_stn}_{subitem_name}_{index}"
    

    if state_key_stn not in st.session_state:
        st.session_state[state_key_stn] = current_value_stn
        

    new_value_stn = container.text_input(
        "Stage Table Name", 
        value=st.session_state[state_key_stn], 
        key=f"input_{state_key_stn}" 
    )
    

    st.session_state[state_key_stn] = new_value_stn
    if index < len(tlist):
        tlist[index][field_name_stn] = new_value_stn

    # --- Campo 2: Stage Key ---
    field_name_sk = "stage_key"
    current_value_sk = tlist_item.get(field_name_sk, "")
    state_key_sk = f"{field_name_sk}_{subitem_name}_{index}"
    
    if state_key_sk not in st.session_state:
        st.session_state[state_key_sk] = current_value_sk
        
    new_value_sk = container.text_input(
        "Stage Key", 
        value=st.session_state[state_key_sk], 
        key=f"input_{state_key_sk}"
    )
    

    st.session_state[state_key_sk] = new_value_sk
    if index < len(tlist):
        tlist[index][field_name_sk] = new_value_sk

    # --- Campo 3: Table Name ---
    field_name_tn = "table_name"
    current_value_tn = tlist_item.get(field_name_tn, "")
    state_key_tn = f"{field_name_tn}_{subitem_name}_{index}"
    
    if state_key_tn not in st.session_state:
        st.session_state[state_key_tn] = current_value_tn
        
    new_value_tn = container.text_input(
        "Table Name", 
        value=st.session_state[state_key_tn], 
        key=f"input_{state_key_tn}"
    )
    

    st.session_state[state_key_tn] = new_value_tn
    if index < len(tlist):
        tlist[index][field_name_tn] = new_value_tn