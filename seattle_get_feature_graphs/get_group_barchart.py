import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

data = pd.read_csv('~/Documents/seattle_data/911.csv')

groups = np.unique(data['Event Clearance Group'])

counts = []
for group in groups:
  counts.append(data[data['Event Clearance Group'] == group].shape[0])


## modified from https://plot.ly/python/bar-charts/
data = [
    go.Bar(
        x=groups,
        y=counts
    )
]
layout = go.Layout(
          margin=go.Margin(
            b=100

        ))

plot_url = py.plot(data, filename='Barchart of Clearance Group Counts')
