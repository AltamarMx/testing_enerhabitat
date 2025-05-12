# %% 
import enerhabitat as eh 
import plotly.express as px

# %%
eh.materials('./eh_config/doblecarpeta/materiales_nuevos.ini')

#%%
dia = eh.Tsa(
    solar_absortance=0.8,
    surface_tilt=90, 
    surface_azimuth=90,
    month="04",
    year="2025",
    epw_file="epw/USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw"
    )

#%%
sc = [
    (0.001,"steel"),
#    (0.1, "adobe")
#    (0.02, "brick"),
#    (0.1, "concrete"),
]

dia = eh.solveCS(sc, dia)

#%%
px.scatter(
    data_frame=dia,
    x=dia.index,
    y=["Ta","Tsa","Ti"]
)
# %%
