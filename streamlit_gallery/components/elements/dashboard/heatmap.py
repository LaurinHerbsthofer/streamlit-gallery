import json

from streamlit_elements import nivo, mui
from .dashboard import Dashboard


class Heatmap(Dashboard.Item):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._theme = {
            "dark": {
                "background": "#252526",
                "textColor": "#FAFAFA",
                "tooltip": {
                    "container": {
                        "background": "#3F3F3F",
                        "color": "FAFAFA",
                    }
                }
            },
            "light": {
                "background": "#FFFFFF",
                "textColor": "#31333F",
                "tooltip": {
                    "container": {
                        "background": "#FFFFFF",
                        "color": "#31333F",
                    }
                }
            }
        }

    def __call__(self, json_data=None, title="Heatmap chart"):
        try:
            data = json.loads(json_data)
        except Exception as e:
            data = json_data

        with mui.Paper(key=self._key, sx={"display": "flex", "flexDirection": "column",
                                          "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            with self.title_bar():
                mui.icon.PieChart()
                mui.Typography(title, sx={"flex": 1})

            with mui.Box(sx={"flex": 1, "minHeight": 0}):
                nivo.HeatMap(
                    data=data,
                    theme=self._theme["dark" if self._dark_mode else "light"],
                    margin={"top": 40, "right": 80, "bottom": 80, "left": 80},
                    innerRadiusRatio=0.96,
                    innerRadiusOffset=0.02,
                    inactiveArcOpacity=0.25,
                    padAngle=0,
                    cornerRadius=3,
                    activeOuterRadiusOffset=8,
                    borderWidth=1,
                    borderColor={
                        "from": "color",
                        "modifiers": [
                            [
                                "darker",
                                0.2,
                            ]
                        ]
                    },
                    axisTop={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": -45,
                        "legend": '',
                        "legendOffset": 46
                    },
                    axisRight={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": 'Cancer',
                        "legendPosition": 'middle',
                        "legendOffset": 70
                    },
                    axisLeft={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": 'country',
                        "legendPosition": 'middle',
                        "legendOffset": -72
                    },
                    colors={
                        "type": 'diverging',
                        "scheme": 'red_yellow_blue',
                        "divergeAt": 0.5,
                        "minValue": -100000,
                        "maxValue": 100000
                    },
                    emptyColor="#555555",
                    arcLinkLabelsSkipAngle=10,
                    arcLinkLabelsTextColor="grey",
                    arcLinkLabelsThickness=2,
                    arcLinkLabelsColor={ "from": "color" },
                    arcLabelsSkipAngle=10,
                    arcLabelsTextColor={
                        "from": "color",
                        "modifiers": [
                            [
                                "darker",
                                2
                            ]
                        ]
                    },
                    defs=[
                        {
                            "id": "dots",
                            "type": "patternDots",
                            "background": "inherit",
                            "color": "rgba(255, 255, 255, 0.3)",
                            "size": 4,
                            "padding": 1,
                            "stagger": True
                        },
                        {
                            "id": "lines",
                            "type": "patternLines",
                            "background": "inherit",
                            "color": "rgba(255, 255, 255, 0.3)",
                            "rotation": -45,
                            "lineWidth": 6,
                            "spacing": 10
                        }
                    ],
                    fill=[
                        { "match": { "id": "ruby" }, "id": "dots" },
                        { "match": { "id": "c" }, "id": "dots" },
                        { "match": { "id": "go" }, "id": "dots" },
                        { "match": { "id": "python" }, "id": "dots" },
                        { "match": { "id": "scala" }, "id": "lines" },
                        { "match": { "id": "lisp" }, "id": "lines" },
                        { "match": { "id": "elixir" }, "id": "lines" },
                        { "match": { "id": "javascript" }, "id": "lines" }
                    ],
                    legends=[
                        {
                            "anchor": 'bottom',
                            "translateX": 0,
                            "translateY": 30,
                            "length": 400,
                            "thickness": 8,
                            "direction": 'row',
                            "tickPosition": 'after',
                            "tickSize": 3,
                            "tickSpacing": 4,
                            "tickOverlap": False,
                            "tickFormat": '>-.2s',
                            "title": 'Value →',
                            "titleAlign": 'start',
                            "titleOffset": 4
                        }
                    ]
                )
