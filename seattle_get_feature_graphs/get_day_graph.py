import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

data_911 = pd.read_csv('~/Documents/seattle_data/911_with_hour_month.csv')

groups = ['ASSAULTS', 'BURGLARY', 'DISTURBANCES', 'MENTAL HEALTH',
'MOTOR VEHICLE COLLISION INVESTIGATION', 'NARCOTICS COMPLAINTS',
'SHOPLIFTING', 'THREATS, HARASSMENT', 'TRAFFIC RELATED CALLS',
'TRESPASS']

days = range(1, 32)

total = []
day_counts = []

for group in groups:
  group_subset = data_911[data_911['Event Clearance Group'] == group]
  total.append(len(group_subset))

  y_vals = []
  for day in days:
    y_vals.append(len(group_subset[group_subset['day'] == day]))

  day_counts.append(y_vals)

data = []
for i in range(len(groups)):
  data.append(
    go.Scatter(
      x = days,
      y = day_counts[i],
      mode = 'lines+markers',
      name = groups[i]
    )
  )

url = py.plot(data, filename = 'Number of Crimes per Day')

day_prop = []
for i in range(len(day_counts)):
  day_prop.append(
    [float(x) / total[i] for x in day_counts[i]]
  )

data = []
for i in range(len(groups)):
  data.append(
    go.Scatter(
      x = days,
      y = day_prop[i],
      mode = 'lines+markers',
      name = groups[i]
    )
  )

url = py.plot(data, filename = 'Proportion of Crimes per Day')