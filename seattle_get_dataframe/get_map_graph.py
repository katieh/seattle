import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np

## modified from https://plot.ly/python/choropleth-maps/

data = pd.read_csv('~/Documents/seattle_data/911_group_subset.csv')
groups = np.unique(data['Event Clearance Group'])

crimes = []

for i in range(len(groups)):
    crimes.append(go.Scattergeo(
        lon = data[data['Event Clearance Group'] == groups[i]]['Longitude'][:500],
        lat = data[data['Event Clearance Group'] == groups[i]]['Latitude'][:500],
        name = groups[i],
    ) )

crimes[0]['mode'] = 'markers'
crimes[0]['textposition'] = 'bottom center'


layout = go.Layout(
    title = 'Seattle Crime Plot',
    geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = 'rgb(217, 217, 217)',
            subunitcolor="rgb(255, 255, 255)",
            countrycolor="rgb(255, 255, 255)",
            lonaxis = dict( range= [ -122.45, -122.25 ] ),
            lataxis = dict( range= [ 47.47, 47.75 ] ),
        ),
    legend = dict(
           traceorder = 'reversed'
    )
)

print(layout.help('geo'))

fig = go.Figure(layout=layout, data=crimes)
url = py.plot(fig, validate=False, filename='West Africa Ebola cases 2014')