import json
import streamlit as st
import datetime

from pathlib import Path
from streamlit import session_state as state
from streamlit_elements import elements, sync, event
from types import SimpleNamespace

# each dashboard item "type" that can be used is defined as a class that inherits from Dashboard.Item
# you will be able to instantiate multiple cards of a given class later in the code
from .dashboard import Dashboard, dataloader
# from .dashboard import Editor, DataGrid, Player
from .dashboard import Card, Radar, Pie, Bar, Boxplot, Bump, Areabump, Chord

# adding new plot types: the python code is just a wrapper around the javascript Nivo package https://nivo.rocks/bar/
# add a new python class for a new plot type that you need (make a copy e.g. of pie.py, rename the class, add it to the imports on top, add it to the dashboard/__init__.py file and use the respective Nivo plotting function)
# make sure to check the "data" tab on nivo.rocks to see in what format any given plot expects the input data
# finally, you might need to make changes to the call of the plot function itself, like adding a "keys=[]" argument, or something similar, just check the nivo.rocks example code

#todo add boxplots: boxplots were likely added to Nivo after April 2023 (https://github.com/plouc/nivo/issues/849), so they are maybe not yet in the code that streamlit and streamlit-elements depend on.
# if you search the PyCharm project for "ResponsiveBar" (C:\Users\ocherbstho\.virtualenvs\streamlit-gallery-fWSS-baO\Lib\site-packages\streamlit_elements\frontend\build\_next\static\chunks\pages) you will find some javascript files installed in the project environment that are likely the JS/React code snippets that are called from streamlit
#however, you will not find code for ResponsiveBoxplot (!) which is likely why boxplots don't work. One fix would likely be to install the nivo boxplot code in the local environment using npm i @nivo/boxplot (https://www.npmjs.com/package/@nivo/boxplot)
# the code for boxplots is available on npmjs so adding them to the environment folder mentioned above could work https://www.npmjs.com/package/@nivo/boxplot?activeTab=code but its unclear to me how to do this properly

#todo add pyanatomogram picture with real computation


def main():
    st.title("⚛️ FusionViewer 2.0 Dashboard")
    st.write(
        "Create a draggable and resizable dashboard in Streamlit, featuring Material UI widgets, Monaco editor (Visual Studio Code), Nivo charts, and more!")

    if "w" not in state:
        board = Dashboard()
        # register each card in the dashboard namespace and define its default location and size
        # you can instantiate a single card type multiple times but they need to have different names
        # coordinates: x, y, w, h (coordinates starting top left corner)
        #
        # DEFAULT LAYOUT 1
        # w = SimpleNamespace(
        #     dashboard=board,
        #     card_anatomogram=Card(board, 0, 0, 2, 10, minW=2, minH=9),
        #     card_warning1=Card(board, 2, 0, 2, 3, minW=2, minH=2),
        #     card_warning2=Card(board, 4, 0, 2, 3, minW=2, minH=3),
        #     card_warning3=Card(board, 6, 0, 2, 3, minW=2, minH=2),
        #     card_summary=Card(board, 8, 0, 4, 5, minW=2, minH=4),
        #
        #     radar_outliers=Radar(board, 2, 3, 6, 7, minW=2, minH=4),
        #     card_pathology=Card(board, 8, 5, 4, 9, minW=3, minH=4),
        #
        #     pie_flowcytometry=Pie(board, 0, 10, 4, 6, minW=3, minH=4),
        #     pie_metabolomics=Pie(board, 4, 10, 4, 6, minW=3, minH=4),
        #     card_clinicaldata=Card(board, 8, 14, 4, 5, minW=2, minH=4),
        #
        #     # editor=Editor(board, 0, 6, 6, 6, minW=3, minH=3),
        #     # player=Player(board, 6, 6, 6, 6, minH=5),
        #     fusion_report=DataGrid(board, 0, 19, 12, 6, minH=4),
        # )
        # DEFAULT LAYOUT 2
        w = SimpleNamespace(
            dashboard=board,
            card_anatomogram=Card(board, 0, 0, 2, 10, minW=2, minH=3),
            card_pathology=Card(board, 2, 0, 3, 10, minW=2, minH=3),

            card_warning1=Card(board, 5, 0, 2, 3, minW=2, minH=2),
            card_warning2=Card(board, 5, 3, 2, 4, minW=2, minH=2),
            card_warning3=Card(board, 5, 7, 2, 3, minW=2, minH=2),

            card_summary=Card(board, 7, 0, 5, 5, minW=2, minH=4),
            card_clinicaldata=Card(board, 7, 7, 5, 5, minW=2, minH=4),

            radar_outliers=Radar(board, 0, 11, 4, 5, minW=2, minH=4),
            pie_flowcytometry=Pie(board, 4, 11, 4, 5, minW=3, minH=4),
            pie_metabolomics=Bar(board, 8, 11, 4, 5, minW=3, minH=4),

            pie_NGS_SNPcounts=Pie(board, 0, 16, 3, 5, minW=3, minH=4),
            bar_NGS_SNPs=Bar(board, 3, 16, 6, 5, minW=3, minH=4),
            chord_demo=Chord(board, 9, 16, 3, 5, minW=3, minH=4),

            areabump_demo=Areabump(board, 0, 21, 6, 6, minW=3, minH=4),
            bump_demo=Bump(board, 6, 21, 6, 6, minW=3, minH=4),
            boxplot_demo=Boxplot(board, 0, 21, 6, 6, minW=3, minH=4),

            # editor=Editor(board, 0, 6, 6, 6, minW=3, minH=3),
            # player=Player(board, 6, 6, 6, 6, minH=5),
            # fusion_report=DataGrid(board, 0, 19, 12, 6, minH=4),
        )
        state.w = w

        # w.editor.add_tab("Notes", f"{datetime.date.today()}: ", "plaintext")
        # w.editor.add_tab("Previous notes", "2023-11-16: I found an interesting relationship between the BRAF mutations and an usual number of memory T cells.", "plaintext")
    else:
        w = state.w

    with elements("demo"):
        # event.Hotkey("ctrl+s", sync(), bindInputs=True, overrideDefault=True)

        with w.dashboard(rowHeight=57):
            # define some data to be shown on the cards

            w.card_anatomogram(title="Anatomogram",
                               subheader="Patient F_01029",
                               content="Primary tumor and metastasis locations",
                               media={"component": "img",
                                      "height": 700,
                                      "image": "https://www.cbmed.at/wp-content/uploads/2023/11/pyanatomogram.png",
                                      "alt": "Anatomogram"},
                               avatar={'letter': 'A', 'bgcolor': 'lightblue'})
            w.card_pathology(title="Digital pathology",
                             subheader="H&E slide",
                             content="",
                             avatar={'letter': 'DP', 'bgcolor': 'hotpink'},
                             media={"component": "img", "height": 600,
                                    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/Retina_--_high_mag.jpg/800px-Retina_--_high_mag.jpg",
                                    "alt": "H&E image"},
                             overflow="hidden")

            w.card_warning1(title="Allergies",
                            subheader="Warning",
                            content="Temozolomide",
                            avatar={'letter': 'W', 'bgcolor': 'red'})
            w.card_warning2(title="Weight-loss",
                            subheader="Warning",
                            content="Significant weight-loss in last 4 weeks during Bevacizumab treatment.",
                            avatar={'letter': 'W', 'bgcolor': 'orange'})
            w.card_warning3(title="Comorbidities",
                            subheader="Warning",
                            content="Cerebrovascular accident or transient ischemic attacks",
                            avatar={'letter': 'W', 'bgcolor': 'orange'})

            w.card_summary(title="Patient summary",
                           subheader="",
                           content=dataloader.get_card_summary_text(),
                           avatar={'letter': 'S', 'bgcolor': 'lightblue'})
            w.card_clinicaldata(title="Clinical report",
                                subheader="Last diskurs ambulant entry",
                                content=dataloader.get_card_clinicaldata_text(),
                                avatar={'letter': 'CR', 'bgcolor': 'lightblue'},
                                media=None)
            w.radar_outliers(json_data=dataloader.get_lab_overview_data()['data'],
                             title="Outliers in each lab",
                             indexBy="outliers",
                             keys=dataloader.get_lab_overview_data()['keys'])
            w.pie_flowcytometry(json_data=dataloader.get_flowcytometry_data(),
                                title="Flow cytometry populations")
            w.pie_metabolomics(json_data=dataloader.get_metabolomics_data(),
                               title="Metabolomics",
                               indexBy="id",
                               keys=["value"])
            w.pie_NGS_SNPcounts(json_data=dataloader.get_NGS_SNP_counts(),
                                title="NGS SNP counts")

            w.boxplot_demo(json_data=dataloader.get_boxplot_data())
            w.bar_NGS_SNPs(json_data=dataloader.get_NGS_SNPs(),
                           title="NGS SNP details",
                           keys=["Transition", "Transversion", ">1 Nucleotide"])
            w.areabump_demo(json_data=dataloader.get_areabump_data())
            w.bump_demo(json_data=dataloader.get_bump_data())
            w.chord_demo(json_data=dataloader.get_chord_data())

            # w.editor()
            # w.player()
            # w.fusion_report(json_data=get_fusion_report_rows(), data_cols=get_fusion_report_cols())
    return


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
