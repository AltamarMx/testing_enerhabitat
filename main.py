# %% 
import enerhabitat as eh 
from matplotlib.pylab import e
import plotly.express as px

# %%
eh.get_list_materials()
# %%
eh.Nx = 200
sc1 = eh.Tsa(
    solar_absortance=0.8,
    surface_tilt=90, 
    surface_azimuth=90,
    month="04",
    epw_file="epw/USA_CA_San.Francisco.Intl.AP.724940_TMY3.epw"
    )

sc = [
    (0.3,"adobe")
]

sc1 = eh.solveCS(sc,sc1)


px.scatter(
    data_frame=sc1,
    x=sc1.index,
    y=["Ta","Ti"]
)

# %%
