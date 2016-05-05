import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

data_911 = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/911_w_parks.csv')

groups = ['ASSAULTS', 'BURGLARY', 'MENTAL HEALTH',
'MOTOR VEHICLE COLLISION INVESTIGATION', 'NARCOTICS COMPLAINTS',
'SHOPLIFTING', 'THREATS, HARASSMENT', 'TRESPASS', 'AUTO THEFTS']

hours = range(24)

total = []
hour_counts = []

for group in groups:
  group_subset = data_911[data_911['Event Clearance Group'] == group]
  total.append(len(group_subset))

  y_vals = []
  for hour in hours:
    y_vals.append(len(group_subset[group_subset['hour'] == hour]))

  hour_counts.append(y_vals)

data = []
for i in range(len(groups)):
  data.append(
    go.Scatter(
      x = hours,
      y = hour_counts[i],
      mode = 'lines+markers',
      name = groups[i]
    )
  )

url = py.plot(data, filename = 'Number of Crimes per Hour')

hour_prop = []
for i in range(len(hour_counts)):
  hour_prop.append(
    [float(x) / total[i] for x in hour_counts[i]]
  )

data = []
for i in range(len(groups)):
  data.append(
    go.Scatter(
      x = hours,
      y = hour_prop[i],
      mode = 'lines+markers',
      name = groups[i]
    )
  )

url = py.plot(data, filename = 'Proportion of Crimes per Hour')