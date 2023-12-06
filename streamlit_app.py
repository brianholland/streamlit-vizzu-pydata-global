from streamlit_vizzu import VizzuChart, Data, Config, Style

import streamlit as st
import pandas as pd

st.set_page_config(initial_sidebar_state="expanded")

df = pd.read_csv("sales.csv")
data = Data()
data.add_df(df)

chart = VizzuChart()
chart.feature("tooltip", True)
chart.animate(data)

chart.animate(
    Data.filter(None),
    Config(
        {
          # "coordSystem": "cartesian",
          # "geometry": "rectangle",
            "x": "Revenue[$]",
            "y": {"set": "Country"},
			"label": "Revenue[$]",
        }
    ),
	Style({
        "plot": {
			"yAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
			"xAxis": {"label": {"numberScale": "shortScaleSymbolUS"}},
			"marker": {
                "colorPalette": '#FF0000FF #BDAF10FF #9355e8FF ',
				"label": {
					"numberFormat": "prefixed",
					"maxFractionDigits": "1",
					"numberScale": "shortScaleSymbolUS",
				},
			}
		}
	})
)

st.title("Sales by country")

config = {}
if st.toggle("Order by total"):
    config["sort"] = "byValue"
else:
    config["sort"] = "none"

chart.animate(Config(config))

chart.show()
