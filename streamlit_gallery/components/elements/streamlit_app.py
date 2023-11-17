import json
import streamlit as st
import datetime

from pathlib import Path
from streamlit import session_state as state
from streamlit_elements import elements, sync, event
from types import SimpleNamespace

# each dashboard item "type" that can be used is defined as a class that inherits from Dashboard.Item
# you will be able to instantiate multiple cards of a given class later in the code
from .dashboard import Dashboard, Editor, Card, DataGrid, Radar, Pie, Player

#todo add barchart
#todo add boxplots
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

            radar_outliers=Radar(board, 0, 11, 3, 5, minW=2, minH=4),
            pie_flowcytometry=Pie(board, 3, 11, 3, 5, minW=3, minH=4),
            pie_metabolomics=Pie(board, 6, 11, 3, 5, minW=3, minH=4),
            pie_NGS=Pie(board, 9, 11, 3, 5, minW=3, minH=4),

            # editor=Editor(board, 0, 6, 6, 6, minW=3, minH=3),
            # player=Player(board, 6, 6, 6, 6, minH=5),
            fusion_report=DataGrid(board, 0, 19, 12, 6, minH=4),
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
                           content=get_card_summary_text(),
                           avatar={'letter': 'S', 'bgcolor': 'lightblue'})
            w.card_clinicaldata(title="Clinical report",
                                subheader="Last diskurs ambulant entry",
                                content=get_card_clinicaldata_text(),
                                avatar={'letter': 'CR', 'bgcolor': 'lightblue'},
                                media=None)
            w.radar_outliers(json_data=get_lab_overview_data()['data'],
                             title="Outliers in each lab",
                             indexBy="outliers",
                             keys=get_lab_overview_data()['keys'])
            w.pie_flowcytometry(json_data=get_flowcytometry_data(),
                                title="Flow cytometry populations")
            w.pie_metabolomics(json_data=get_metabolomics_data(),
                               title="Metabolomics")
            w.pie_NGS(json_data=get_NGS_data(),
                      title="NGS SNPs")

            # w.editor()
            # w.player()
            # w.fusion_report(json_data=get_fusion_report_rows(), data_cols=get_fusion_report_cols())
    return


def get_lab_overview_data(with_background_cohorts=False):
    if with_background_cohorts:
        data = {
            'data': [
                        {"outliers": "Flow Cytometry", "patient": 4, "responder avg": 2, "non-responder avg": 6},
                        {"outliers": "Metabolomics", "patient": 3, "responder avg": 6, "non-responder avg": 4},
                        {"outliers": "Digital Pathology", "patient": 6, "responder avg": 5, "non-responder avg": 7},
                        {"outliers": "NGS", "patient": 7, "responder avg": 5, "non-responder avg": 3},
                        {"outliers": "Microbiome", "patient": 10, "responder avg": 2, "non-responder avg": 4}
                    ],
            'keys': ["responder avg", "non-responder avg", "patient"]
        }
    else:
        data = {
            'data': [
                        {"outliers": "Flow Cytometry", "patient": 4},
                        {"outliers": "Metabolomics", "patient": 3},
                        {"outliers": "Digital Pathology", "patient": 6},
                        {"outliers": "NGS", "patient": 7},
                        {"outliers": "Microbiome", "patient": 10}
                    ],
            'keys': ["patient"]
        }
    return data


def get_flowcytometry_data():
    return [
        {'id': "Cytotoxic T cells", 'label': "Cytotoxic T cells", 'value': 465,
         'color': "hsl(128, 70%, 50%)"},
        {'id': "Memory T Cells", 'label': "Memory T Cells", 'value': 1140,
         'color': "hsl(178, 70%, 50%)"},
        {'id': "Effector Memory T Cells", 'label': "Effector Memory T Cells", 'value': 156,
         'color': "hsl(178, 70%, 50%)"}
    ]


def get_metabolomics_data():
    return [
        {"id": "Succinic Acid", "label": "Succinic Acid", "value": 465,
         "color": "hsl(128, 70%, 50%)"},
        {"id": "Oxoglutaric acid", "label": "Oxoglutaric acid", "value": 140,
         "color": "hsl(178, 70%, 50%)"},
        {"id": "SM 34:1", "label": "SM 34:1", "value": 40,
         "color": "hsl(322, 70%, 50%)"},
        {"id": "PS 38:0", "label": "PS 38:0", "value": 439,
         "color": "hsl(117, 70%, 50%)"},
        {"id": "Stearidonic Acid", "label": "Stearidonic Acid", "value": 366,
         "color": "hsl(286, 70%, 50%)"}
    ]


def get_NGS_data():
    return [
        {"id": "ALK", "label": "ALK", "value": 2,
         "color": "hsl(128, 70%, 50%)"},
        {"id": "KRAS", "label": "KRAS", "value": 1,
         "color": "hsl(178, 70%, 50%)"},
        {"id": "ERBB2", "label": "ERBB2", "value": 1,
         "color": "hsl(322, 70%, 50%)"},
        {"id": "BRAF", "label": "BRAF", "value": 3,
         "color": "hsl(117, 70%, 50%)"},
    ]

def get_card_summary_text():
    return """
Year of birth: 1958 (65 years)
Sex: female ♀️
BMI: 24.3 (healthy weight)
ECOG study start: 2
Cancer entity: Non-small cell lung cancer
Date of diagnosis: 2021-02
Histology: Adenocarcinoma
Gene mutations*: ALK (2), PDGFRA (1), KRAS (1), ERBB2 (3), EGFR (1), PIK3CA (2)
Primary tumour surgery: No
Palliative at diagnosis: Yes
Metastasis locations: 4
Radiotherapy: Yes
Tumour stage: IV
TNMG stage: nan/nan/nan/nan
Last treatment: pall. PCT mit Carboplatin AUC-2/Abraxane q1w
"""


def get_card_clinicaldata_text():
    return """
        14.11.2022
        Therapie FOLFIRI **** 4
        Befinden/NW:geht gut, min. Skin Tox G1
        ECOG:1
        Gewicht:idem
        Klinische Untersuchung:unauff.
        Labor:BB oB
        Stv.Lt. Assoz.Prof.PDDr ***** ******
        Staging:NA Tumortherapie:FOLFIRI/ **** Sonstige Medikation:idem Bemerkung:NA Plan:THX weiter, Stging vereinbart
        """

def get_fusion_report_cols():
    return [
        {"field": 'id', "headerName": 'ID', "width": 90},
        {"field": 'infotype', "headerName": 'Info type', "width": 150, "editable": False, },
        {"field": 'label', "headerName": 'Label', "width": 150, "editable": False, },
        {"field": 'text', "headerName": 'Text', "width": 500, "editable": False, },
    ]


def get_fusion_report_rows():
    return [
        {"id": 1, "infotype": 'Warning', "label": 'Allergy', "text": "Temozolomide"},
        {"id": 2, "infotype": 'Warning', "label": 'Comorbidity', "text": "Cerebrovascular accident or transient ischemic attacks"},
        {"id": 3, "infotype": 'Warning', "label": 'Weight-loss', "text": "Significant weight-loss in last 4 weeks during Bevacizumab treatment."},
        {"id": 4, "infotype": 'Clinical Clue', "label": 'Something', "text": "Some text describing an interesting finding."},
    ]

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
