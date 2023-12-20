from streamlit_vizzu import VizzuChart, Data, Config, Style
import pandas as pd

d_types = {
    "Region": str,
    "Subregion": str,
    "Country": str,
    "Year": str,
    "Period": str,
    "Pop_Medium": float,
    "Pop_High": float,
    "Pop_Low": float,
}
df = pd.read_csv("worldpopulation.csv", dtype=d_types)
data = Data()
data.add_df(df)

chart = VizzuChart()
chart.feature("tooltip", True)
chart.animate(data)

chart.animate(
    Data.filter(
        "(record['Region'] == 'Africa'||record['Region'] == 'Asia'||record['Region'] == 'Europe'||record['Region'] == 'America'||record['Region'] == 'Oceania')"
    ),
    Config(
        {
            "coordSystem": "cartesian",
            "geometry": "line",
            "x": "Year",
            "y": {"set": "Pop_Medium", "range": {"min": None, "max": "110%"}},
            "color": "Region",
            "lightness": None,
            "size": None,
            "noop": None,
            "split": False,
            "align": "none",
            "orientation": "horizontal",
            "label": None,
            "sort": "none",
        }
    ),
    Style(
        {
            "plot": {
                "yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                "xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
                "marker": {
                    "label": {
                        "numberFormat": "prefixed",
                        "maxFractionDigits": "1",
                        "numberScale": "shortScaleSymbolUS",
                    },
                    "rectangleSpacing": None,
                    "circleMinRadius": 0.005,
                    "borderOpacity": 1,
                    "colorPalette": "#03ae71 #f4941b #f4c204 #d49664 #f25456 #9e67ab #bca604 #846e1c #fc763c #b462ac #f492fc #bc4a94 #9c7ef4 #9c52b4 #6ca2fc #5c6ebc #7c868c #ac968c #4c7450 #ac7a4c #7cae54 #4c7450 #9c1a6c #ac3e94 #b41204",
                },
            }
        }
    ),
)

chart.show()