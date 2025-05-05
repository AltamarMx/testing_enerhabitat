# %%
import enerhabitat as eh 
import plotly.express as px
# %%

dia = eh.calculateTSA(
    convection_heat_transfer=13, ## por default 
    solar_absortance=0.8,
    inclination=90, 
    azimuth=90,
    month="04",
    year="2025", ##obligatorio por default
    epw_file_path="epw/USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw"
    )
# %%
px.scatter(
    data_frame=dia,
    x=dia.index,
    y=["Ta","Tsa"]
)
#%%
sc = [
    (0.001,"acero"),
    # (0.1, "adobe")
#     (0.02, "tabique"),
#     (0.1, "concreto"),
]

dia = eh.solveSC(sc, dia)

#%%

px.scatter(
    data_frame=dia,
    x=dia.index,
    y=["Ta","Tsa","Ti"]
)