import json
import streamlit as st

from pathlib import Path
from streamlit import session_state as state
from streamlit_elements import elements, sync, event
from types import SimpleNamespace

# each dashboard item "type" that can be used is defined as a class that inherits from Dashboard.Item
# you will be able to instantiate multiple cards of a given class later in the code
from .dashboard import Dashboard, Editor, Card, DataGrid, Radar, Pie, Player


def main():
    st.write(
        """
        ✨ Streamlit Elements &nbsp; [![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link]
        =====================

        Create a draggable and resizable dashboard in Streamlit, featuring Material UI widgets,
        Monaco editor (Visual Studio Code), Nivo charts, and more!

        [github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
        [github_link]: https://github.com/okld/streamlit-elements

        [pypi_badge]: https://badgen.net/pypi/v/streamlit-elements?icon=pypi&color=black&label
        [pypi_link]: https://pypi.org/project/streamlit-elements
        """
    )

    # with st.expander("GETTING STARTED"):
    #     st.write((Path(__file__).parent/"README.md").read_text())

    st.title("")

    if "w" not in state:
        board = Dashboard()
        # register each card in the dashboard namespace and define its default location and size
        # you can instantiate a single card type multiple times but they need to have different names
        # coordinates: x, y, w, h (coordinates starting top left corner)
        # w = SimpleNamespace(
        #     dashboard=board,
        #     editor=Editor(board, 0, 0, 6, 6, minW=3, minH=3),
        #     player=Player(board, 0, 7, 6, 10, minH=5),
        #     pie=Pie(board, 6, 0, 6, 7, minW=3, minH=4),
        #     radar=Radar(board, 12, 7, 3, 7, minW=2, minH=4),
        #     card=Card(board, 6, 7, 3, 7, minW=2, minH=4),
        #     data_grid=DataGrid(board, 6, 13, 6, 7, minH=4),
        #     card2=Card(board, 0, 21, 6, 7, minW=2, minH=4),
        #     pie2=Pie(board, 6, 17, 6, 7, minW=3, minH=4),
        # )
        w = SimpleNamespace(
            dashboard=board,
            metabolomics=Pie(board, 0, 0, 6, 6, minW=3, minH=4),
            radar=Radar(board, 6, 0, 3, 6, minW=2, minH=4),
            clinicaldata=Card(board, 9, 0, 3, 6, minW=2, minH=4),

            editor=Editor(board, 0, 6, 6, 6, minW=3, minH=3),
            # player=Player(board, 6, 6, 6, 6, minH=5),

            data_grid=DataGrid(board, 0, 12, 6, 6, minH=4),
            card2=Card(board, 6, 12, 3, 6, minW=2, minH=4),
            flowcytometry=Pie(board, 9, 12, 3, 6, minW=3, minH=4),
        )
        state.w = w

        # some cards may have additional settings, like tabs, that can be defined here
        w.editor.add_tab("Card content", Card.DEFAULT_CONTENT, "plaintext")
        w.editor.add_tab("Data grid", json.dumps(DataGrid.DEFAULT_ROWS, indent=2), "json")
        w.editor.add_tab("Metabolomics", json.dumps(Radar.DEFAULT_DATA, indent=2), "json")
        w.editor.add_tab("Flow cytometry", json.dumps(Pie.DEFAULT_DATA, indent=2), "json")
    else:
        w = state.w

    with elements("demo"):
        event.Hotkey("ctrl+s", sync(), bindInputs=True, overrideDefault=True)

        with w.dashboard(rowHeight=57):

            # here is an example string that can be converted, it needs to be parsable by
            # json.loads()
            flowcytometry_data = [
                dict(id="Cytotoxic T cells", label="Cytotoxic T cells", value=465, color="hsl(128, 70%, 50%)"),
                dict(id="Memory T Cells", label="Memory T Cells", value=1140, color="hsl(178, 70%, 50%)"),
                dict(id="Effector Memory T Cells", label="Effector Memory T Cells", value=156, color="hsl(178, 70%, 50%)")
            ]
            metabolomics_data = [
                {"id": "Succinic Acid", "label": "Succinic Acid", "value": 465, "color": "hsl(128, 70%, 50%)"},
                {"id": "Oxoglutaric acid", "label": "Oxoglutaric acid", "value": 140, "color": "hsl(178, 70%, 50%)"},
                {"id": "SM 34:1", "label": "SM 34:1", "value": 40, "color": "hsl(322, 70%, 50%)"},
                {"id": "PS 38:0", "label": "PS 38:0", "value": 439, "color": "hsl(117, 70%, 50%)"},
                {"id": "Stearidonic Acid", "label": "Stearidonic Acid", "value": 366, "color": "hsl(286, 70%, 50%)"}
            ]
            card_text = "this is just some custom text that we want to put on a card"

            w.editor()
            # w.player()
            w.metabolomics(json_data=metabolomics_data, item_title="Metabolomics")
            w.radar(w.editor.get_content("Metabolomics"))
            w.clinicaldata(w.editor.get_content("Card content"))
            w.data_grid(w.editor.get_content("Data grid"))
            w.card2(card_text)
            w.flowcytometry(json_data=flowcytometry_data, item_title="Flow cytometry")


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
