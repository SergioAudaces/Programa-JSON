import streamlit as st
import json
from components.base_renderer import BaseRenderer
   
def render_measures_input(container, measures_data, index, subitem_name, tlist):
    container.markdown("**Measures:**")  
    renderer = BaseRenderer(container, measures_data, index, subitem_name, tlist, "measures")
    renderer.initialize_state()

    if st.session_state[renderer.state_key] and isinstance(st.session_state[renderer.state_key][0], str):
        st.session_state[renderer.state_key] = [{'name': m} for m in st.session_state[renderer.state_key]]

    count_key = f"{renderer.state_key}_count"
    if count_key not in st.session_state:
        st.session_state[count_key] = len(st.session_state[renderer.state_key])        

    if container.button(f"Adicionar Measure +", key=f"{renderer.state_key}_add"):
        st.session_state[count_key] += 1
        st.rerun() 

    current_list = st.session_state[renderer.state_key]
    while len(current_list) < st.session_state[count_key]:
        current_list.append({'name': ''})

    if st.session_state[count_key] > 0:
        last_index = st.session_state[count_key] - 1
        if last_index < len(current_list):
            current_list[last_index]['name'] = container.text_input(
                f"Measure {last_index+1}", 
                value=current_list[last_index].get('name', ''), 
                key=f"{renderer.state_key}_{last_index}", 
                label_visibility="collapsed"
            )
        else:
            new_val = container.text_input(
                f"Measure {last_index+1}", 
                value="", 
                key=f"{renderer.state_key}_{last_index}", 
                label_visibility="collapsed"
            )
            current_list.append({'name': new_val})

    for j in range(st.session_state[count_key] - 1):
        if j < len(current_list):
            current_list[j]['name'] = container.text_input(
                f"Measure {j+1}", 
                value=current_list[j].get('name', ''), 
                key=f"{renderer.state_key}_{j}", 
                label_visibility="collapsed"
            )
        else:
            new_val = container.text_input(
                f"Measure {j+1}", 
                value="", 
                key=f"{renderer.state_key}_{j}", 
                label_visibility="collapsed"
            )
            if j == len(current_list):
                current_list.append({'name': new_val})
            else:
                current_list[j] = {'name': new_val}        

    st.session_state[renderer.state_key] = current_list
    renderer.update_tlist()