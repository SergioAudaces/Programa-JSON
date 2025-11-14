import streamlit as st

class BaseRenderer:
    def __init__(self, container, data, index, subitem_name, tlist, component_type):
        self.container = container
        self.data = data if isinstance(data, list) else []
        self.index = index
        self.subitem_name = subitem_name
        self.tlist = tlist
        self.component_type = component_type
        self.state_key = f"{component_type}_{subitem_name}_{index}"

    def initialize_state(self):
        if self.state_key not in st.session_state:
            st.session_state[self.state_key] = self.data[:]

        count_key = f"{self.state_key}_count"  
        if count_key not in st.session_state:
            st.session_state[count_key] = len(self.data)

    def render_header(self, headers):
        cols = st.columns([1]*len(headers))
        for col, header in zip(cols, headers):
            with col:
                st.markdown(f"**{header}**")
        return cols

    def update_tlist(self):
        self.tlist[self.index][self.component_type] = st.session_state[self.state_key]

    def add_new_item(self, default_item):
        count_key = f"{self.state_key}_count"

        if self.container.button(f"Adicionar {self.component_type}", key=f"add_{self.state_key}"):
            st.session_state[count_key] += 1

            if self.state_key not in st.session_state:
                st.session_state[self.state_key] = []

            while len(st.session_state[self.state_key]) < st.session_state[count_key]:
                st.session_state[self.state_key].append(default_item)
            self.update_tlist()
            st.rerun()
