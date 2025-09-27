# %% 
import enerhabitat as eh
import pandas as pd 
import plotly.express as px

# %%
eh.materials('./eh_config/materials.ini')

#%%
dia_promedio = eh.meanDay(epw_file="epw/USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw")

#%%
dia_promedio

#%%
tsa_df = eh.Tsa(
    meanDay_dataframe=dia_promedio,
    solar_absortance=0.8,
    surface_tilt=90, 
    surface_azimuth=90,
    )

#%%
tsa_df

#%%
sc = [
    ("Adobe", 0.1),
    ("Acero", 0.1),
#    ("brick", 0.2),
#    ("concrete", 0.1),
]

#%%
dia = eh.solveCS(sc, tsa_df)

#%%
pd.concat([tsa_df, dia], axis=1)

#%%
px.scatter(
    data_frame=dia,
    x=dia.index,
    y=["Ta","Tsa","Ti"]
)
# %%
