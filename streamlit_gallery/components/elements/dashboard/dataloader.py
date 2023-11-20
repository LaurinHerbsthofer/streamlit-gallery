"""
this file contains functions for loading mockup data for the FusionViewer dashboard demo
"""

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
        {'id': "Cytotoxic T cells", 'label': "Cytotoxic T cells", 'value': 27,
         'color': "hsl(128, 70%, 50%)"},
        {'id': "Memory T Cells", 'label': "Memory T Cells", 'value': 61,
         'color': "hsl(178, 70%, 50%)"},
        {'id': "Effector Memory T Cells", 'label': "Effector Memory T Cells", 'value': 12,
         'color': "hsl(178, 70%, 50%)"}
    ]


def get_boxplot_data():
    return [
        {'id': "Cytotoxic T cells", 'label': "Cytotoxic T cells", 'value': 27,
         'color': "hsl(128, 70%, 50%)"},
        {'id': "Memory T Cells", 'label': "Memory T Cells", 'value': 61,
         'color': "hsl(178, 70%, 50%)"},
        {'id': "Effector Memory T Cells", 'label': "Effector Memory T Cells", 'value': 12,
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


def get_NGS_SNP_counts():
    return [
        {"id": "ALK", "label": "ALK", "value": 1, "color": "hsl(128, 70%, 50%)"},
        {"id": "EGRF", "label": "EGRF", "value": 3, "color": "hsl(128, 70%, 50%)"},
        {"id": "ERBB2", "label": "ERBB2", "value": 8, "color": "hsl(128, 70%, 50%)"},
        {"id": "ERBB3", "label": "ERBB3", "value": 4, "color": "hsl(128, 70%, 50%)"},
        {"id": "ESR1", "label": "ESR1", "value": 2, "color": "hsl(128, 70%, 50%)"},
        {"id": "KRAS", "label": "KRAS", "value": 1, "color": "hsl(178, 70%, 50%)"},
        {"id": "NRAS", "label": "NRAS", "value": 2, "color": "hsl(322, 70%, 50%)"},
        {"id": "PIK3CA", "label": "PIK3CA", "value": 2, "color": "hsl(117, 70%, 50%)"},
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

def get_bump_data():
    return [
  {
    "id": "ECOG",
    "data": [
      {
        "x": 2000,
        "y": 5
      },
      {
        "x": 2001,
        "y": 7
      },
      {
        "x": 2002,
        "y": 4
      },
      {
        "x": 2003,
        "y": 9
      },
      {
        "x": 2004,
        "y": 3
      }
    ]
  },
  {
    "id": "Body weight",
    "data": [
      {
        "x": 2000,
        "y": 12
      },
      {
        "x": 2001,
        "y": 11
      },
      {
        "x": 2002,
        "y": 1
      },
      {
        "x": 2003,
        "y": 7
      },
      {
        "x": 2004,
        "y": 1
      }
    ]
  },
  {
    "id": "Ca",
    "data": [
      {
        "x": 2000,
        "y": 6
      },
      {
        "x": 2001,
        "y": 2
      },
      {
        "x": 2002,
        "y": 3
      },
      {
        "x": 2003,
        "y": 6
      },
      {
        "x": 2004,
        "y": 9
      }
    ]
  },
  {
    "id": "CHOL",
    "data": [
      {
        "x": 2000,
        "y": 10
      },
      {
        "x": 2001,
        "y": 6
      },
      {
        "x": 2002,
        "y": 12
      },
      {
        "x": 2003,
        "y": 3
      },
      {
        "x": 2004,
        "y": 10
      }
    ]
  },
  {
    "id": "GLUC",
    "data": [
      {
        "x": 2000,
        "y": 1
      },
      {
        "x": 2001,
        "y": 10
      },
      {
        "x": 2002,
        "y": 5
      },
      {
        "x": 2003,
        "y": 2
      },
      {
        "x": 2004,
        "y": 6
      }
    ]
  }
]

def get_areabump_data():
    return [
  {
    "id": "Ca",
    "data": [
      {
        "x": 2000,
        "y": 15
      },
      {
        "x": 2001,
        "y": 21
      },
      {
        "x": 2002,
        "y": 11
      },
      {
        "x": 2003,
        "y": 22
      },
      {
        "x": 2004,
        "y": 21
      },
      {
        "x": 2005,
        "y": 12
      }
    ]
  },
  {
    "id": "CHOL",
    "data": [
      {
        "x": 2000,
        "y": 16
      },
      {
        "x": 2001,
        "y": 24
      },
      {
        "x": 2002,
        "y": 23
      },
      {
        "x": 2003,
        "y": 20
      },
      {
        "x": 2004,
        "y": 21
      },
      {
        "x": 2005,
        "y": 11
      }
    ]
  },
  {
    "id": "GLUC",
    "data": [
      {
        "x": 2000,
        "y": 12
      },
      {
        "x": 2001,
        "y": 20
      },
      {
        "x": 2002,
        "y": 14
      },
      {
        "x": 2003,
        "y": 23
      },
      {
        "x": 2004,
        "y": 24
      },
      {
        "x": 2005,
        "y": 11
      }
    ]
  },
  {
    "id": "HBA1IF",
    "data": [
      {
        "x": 2000,
        "y": 26
      },
      {
        "x": 2001,
        "y": 16
      },
      {
        "x": 2002,
        "y": 19
      },
      {
        "x": 2003,
        "y": 13
      },
      {
        "x": 2004,
        "y": 11
      },
      {
        "x": 2005,
        "y": 24
      }
    ]
  },
  {
    "id": "HDL",
    "data": [
      {
        "x": 2000,
        "y": 13
      },
      {
        "x": 2001,
        "y": 14
      },
      {
        "x": 2002,
        "y": 15
      },
      {
        "x": 2003,
        "y": 16
      },
      {
        "x": 2004,
        "y": 29
      },
      {
        "x": 2005,
        "y": 30
      }
    ]
  }
]
def get_boxplot_data():
    return [
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.349123488941434
        },
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 6.151749241067562
        },
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.593987513318862
        },
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.880919423789582
        },
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 6.36745109757427
        },
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.0158945618211845
        },
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.751331460122424
        },
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.758074687115144
        },
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.362136263793628
        },
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.883635642526908
        },
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 3.680951894527809
        },
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.194632712261644
        },
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.220760692520841
        },
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.351117312941202
        },
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.269173428316614
        },
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.864386432063807
        },
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 2.6592103338323634
        },
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 7.092189574771535
        },
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.6860482625172715
        },
        {
            "group": "T cells",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.758476893242824
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 6.09634057769023
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 5.393630648720473
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 5.534692726166843
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 6.692424543191319
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 6.675375659975229
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 5.798887716631256
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 7.329418217555768
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 5.308137103383694
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 5.055038466418877
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 5.70764882224717
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 3.998341194341981
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 6.307528757757395
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 5.327154404401608
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 5.574550412206173
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 5.056182987685064
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 6.5364196020926375
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 5.373065040214139
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 5.8525525997996715
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 6.998879351507891
        },
        {
            "group": "T cells",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 7.300555476776495
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 8.593207104845387
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 6.803805231627961
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 7.393827858628626
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 8.757124184877108
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 7.704816219737244
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 7.708208154709452
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 8.033208427076172
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 9.306907549019492
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 9.670181286681723
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 7.860837776552886
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 6.926771391656372
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 8.274940300495775
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 7.7658619062250125
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 7.219158787011299
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 7.552854111215449
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 7.898129365622752
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 8.654180170606008
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 6.158962928927249
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 8.912804031087532
        },
        {
            "group": "Succinic Acid",
            "subgroup": "responder",
            "mu": 8,
            "sd": 1.4,
            "n": 20,
            "value": 7.2720651623624
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 6.609174832361711
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 6.429917896380009
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 6.056644820938463
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 6.715526581861837
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 7.386750149551726
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 5.373761025510219
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 7.14784326105486
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 5.992974802510931
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 7.963978936691964
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 6.526514831187629
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 7.03924585666192
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 7.692359660821619
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 8.169867586637265
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 7.3255541635540595
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 5.277474752801549
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 7.23600156604916
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 8.835175694206704
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 6.781531104000324
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 8.085544525265554
        },
        {
            "group": "Succinic Acid",
            "subgroup": "non-responder",
            "mu": 7.5,
            "sd": 1.4,
            "n": 20,
            "value": 8.058456158054152
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 2.9296133286692494
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 3.6490374028374033
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.277377874464911
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.607498852033886
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 6.000287126478622
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.775136383435469
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.0858901117256865
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 7.06606707598189
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.874006381026506
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.767968570126194
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.533090436396612
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.707436415274839
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.253904425092803
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.4973039253836
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.617472181612674
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.350804456381212
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.13374422906633
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.786330013881678
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.568571837283549
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.476418659878074
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 8.06952315301382
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 8.023705530413254
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 7.669361093961307
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 7.880585369729961
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 5.072365113749138
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 7.71688536499242
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 8.763557944297098
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 5.583433866007992
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 1.934588438815826
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 9.286169716426471
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 6.638840175835807
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 8.43702951494565
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 10.083021839703424
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 5.613380697942182
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 10.176029311944236
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 8.937868796458357
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 7.358874320391635
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 7.9214632192282926
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 8.851602151323455
        },
        {
            "group": "CD4-CD8+ pop1",
            "subgroup": "non-responder",
            "mu": 7.2,
            "sd": 1.8,
            "n": 20,
            "value": 7.344463694837667
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 6.066553729419105
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 3.539117011655381
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 3.779393387804897
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 7.1969623742243085
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.058055074128554
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.772008054361306
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.842538428557226
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.791890150232596
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.197863184108862
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.533193853277447
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.9260145861596145
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 3.7209203291589885
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.305817940786989
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.42181302722615
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 4.434451097733401
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.11797402132471
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 3.9383175456252317
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.268020535990022
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 2.756104566753344
        },
        {
            "group": "ERBB2",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1,
            "n": 20,
            "value": 5.345626185734579
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 6.179803750773409
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 4.780200434153198
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 4.792331184039259
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 6.381792593910859
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 5.552356787873941
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 6.882108986032867
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 5.768244429381534
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 6.2318652312631295
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 6.4899740079357375
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 6.395966308037094
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 7.0735933363079235
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 4.368501474802013
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 6.005287559603644
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 7.552315949845929
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 6.103011794030221
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 6.522612233413192
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 3.788954730096808
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 7.569657573817494
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 8.678218774209126
        },
        {
            "group": "ERBB2",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 1,
            "n": 20,
            "value": 5.07347619915854
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 4.67718359349138
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 3.975687554253355
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 4.895184763732461
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 4.994929843915772
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 4.427922778641409
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 4.866127870570349
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 5.168231043024714
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 4.485957313099086
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 5.498375076839985
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 4.70507890728923
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 5.138043334161617
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 2.461237633951741
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 5.060387289145632
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 4.0343044256234535
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 6.092620705778971
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 4.565956060145201
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 5.527260533130536
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 2.5878236785815703
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 4.604119691639516
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "responder",
            "mu": 5,
            "sd": 1.4,
            "n": 20,
            "value": 5.082448827634411
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 4.321663094739084
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 7.18689888227933
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 6.054158647289736
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 6.630050245455329
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 4.918794703930794
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 7.235680943758366
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 5.5219915514484414
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 2.7725395294621045
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 4.187813317284514
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 9.984022298530254
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 4.549887301507367
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 7.5548617662920625
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 1.8307837952535815
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 7.874881853321
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 6.766116628702203
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 9.55617732042336
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 2.997796386488914
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 9.884144334569362
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 6.962993578966966
        },
        {
            "group": "Kyn:Trp ratio",
            "subgroup": "non-responder",
            "mu": 6,
            "sd": 3,
            "n": 20,
            "value": 7.995078310149756
        }
    ]

def get_NGS_SNPs():
    return [
  {
    "country": "ALK",
    "Transition": 1,
    "TransitionColor": "hsl(29, 70%, 50%)",
    "Transversion": None,
    "TransversionColor": "hsl(300, 70%, 50%)",
    ">1 Nucleotide": None,
    ">1 NucleotideColor": "hsl(129, 70%, 50%)",
  },
  {
    "country": "EGRF",
    "Transition": 2,
    "TransitionColor": "hsl(55, 70%, 50%)",
    "Transversion": 1,
    "TransversionColor": "hsl(292, 70%, 50%)",
    ">1 Nucleotide": None,
    ">1 NucleotideColor": "hsl(120, 70%, 50%)",
  },
  {
    "country": "ERBB2",
    "Transition": 4,
    "TransitionColor": "hsl(77, 70%, 50%)",
    "Transversion": 3,
    "TransversionColor": "hsl(95, 70%, 50%)",
    ">1 Nucleotide": 1,
    ">1 NucleotideColor": "hsl(336, 70%, 50%)",
  },
  {
    "country": "ERBB3",
    "Transition": 4,
    "TransitionColor": "hsl(117, 70%, 50%)",
    "Transversion": None,
    "TransversionColor": "hsl(137, 70%, 50%)",
    ">1 Nucleotide": None,
    ">1 NucleotideColor": "hsl(309, 70%, 50%)",
  },
  {
    "country": "ESR1",
    "Transition": 2,
    "TransitionColor": "hsl(339, 70%, 50%)",
    "Transversion": None,
    "TransversionColor": "hsl(326, 70%, 50%)",
    ">1 Nucleotide": None,
    ">1 NucleotideColor": "hsl(34, 70%, 50%)",
  },
  {
    "country": "KRAS",
    "Transition": 1,
    "TransitionColor": "hsl(256, 70%, 50%)",
    "Transversion": None,
    "TransversionColor": "hsl(98, 70%, 50%)",
    ">1 Nucleotide": None,
    ">1 NucleotideColor": "hsl(104, 70%, 50%)",
  },
  {
    "country": "NRAS",
    "Transition": 2,
    "TransitionColor": "hsl(104, 70%, 50%)",
    "Transversion": None,
    "TransversionColor": "hsl(309, 70%, 50%)",
    ">1 Nucleotide": None,
    ">1 NucleotideColor": "hsl(101, 70%, 50%)",
  },
    {
        "country": "PIK3CA",
        "Transition": 1,
        "TransitionColor": "hsl(104, 70%, 50%)",
        "Transversion": 1,
        "TransversionColor": "hsl(309, 70%, 50%)",
        ">1 Nucleotide": None,
        ">1 NucleotideColor": "hsl(101, 70%, 50%)",
    }

]

def get_chord_data():
    return [
      [
        321,
        64,
        488,
        1438,
        1907
      ],
      [
        467,
        235,
        448,
        1665,
        1260
      ],
      [
        43,
        141,
        128,
        1549,
        509
      ],
      [
        15,
        1462,
        1996,
        405,
        185
      ],
      [
        1142,
        345,
        207,
        385,
        308
      ]
    ]