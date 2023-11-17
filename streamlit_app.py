import streamlit as st

# from streamlit_gallery import apps
from streamlit_gallery import components
from streamlit_gallery.utils.page import page_group

def main():
    page = page_group("p")

    with st.sidebar:
        st.title("FusionViewer 2.0")

        # with st.expander("✨ APPS", True):
        #     page.item("Streamlit gallery", apps.gallery, default=True)

        with st.expander("🧩 COMPONENTS", True):
            #page.item("Ace editor", components.ace_editor)
            #page.item("Disqus", components.disqus)
            page.item("New Dashboard", components.elements, default=True)
            #page.item("Pandas profiling", components.pandas_profiling)
            page.item("Quill editor", components.quill_editor)
            # page.item("React player", components.react_player)

    page.show()

if __name__ == "__main__":
    st.set_page_config(page_title="FusionViewer 2.0", page_icon="⚛️", layout="wide", initial_sidebar_state="collapsed")
    main()
