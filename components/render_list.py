import streamlit as st
import json
from components.base_renderer import BaseRenderer 

def render_list_input(container, label_singular, list_data_raw, item_key_prefix, index, subitem_name, column_name, tlist):
    renderer = BaseRenderer(container, list_data_raw, index, subitem_name, tlist, item_key_prefix)
    renderer.initialize_state()
    container.markdown(f"**{column_name}:**")

    count_key = f"{renderer.state_key}_count"
    if count_key not in st.session_state:
        st.session_state[count_key] = len(st.session_state[renderer.state_key])

    if container.button(f"Adicionar {label_singular} +", key=f"{renderer.state_key}_add"):
        st.session_state[count_key] += 1
        st.rerun() 

    current_list = st.session_state[renderer.state_key]
    while len(current_list) < st.session_state[count_key]:
        current_list.insert(0, "")  

    if st.session_state[count_key] > 0:
        first_index = 0  
        if first_index < len(current_list):
            current_list[first_index] = container.text_input(
                f"{label_singular} {first_index+1}", 
                value=current_list[first_index], 
                key=f"{renderer.state_key}_{first_index}", 
                label_visibility="collapsed"
            )
        else:
            new_val = container.text_input(
                f"{label_singular} {first_index+1}", 
                value="", 
                key=f"{renderer.state_key}_{first_index}", 
                label_visibility="collapsed"
            )
            current_list.insert(0, new_val)

    for j in range(1, st.session_state[count_key]):  
        if j < len(current_list):
            current_list[j] = container.text_input(
                f"{label_singular} {j+1}", 
                value=current_list[j], 
                key=f"{renderer.state_key}_{j}", 
                label_visibility="collapsed"
            )
        else:
            new_val = container.text_input(
                f"{label_singular} {j+1}", 
                value="", 
                key=f"{renderer.state_key}_{j}", 
                label_visibility="collapsed"
            )
            current_list.append(new_val)

    st.session_state[renderer.state_key] = current_list
    renderer.update_tlist()