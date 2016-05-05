import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np

labels = pd.read_csv('/Users/KatieHanss/Documents/424_seattle/seattle/seattle_data/crime_labels.csv')

groups = ['ASSAULTS', 'BURGLARY', 'MENTAL HEALTH',
'MOTOR VEHICLE COLLISION INVESTIGATION', 'NARCOTICS COMPLAINTS',
'SHOPLIFTING', 'THREATS, HARASSMENT', 'TRESPASS', 'AUTO THEFTS']

size = []
for label in np.unique(labels['2']):
  size.append(len(labels[labels['2'] == label]))


fig = {
    'data': [{'labels': groups,
              'values': size,
              'type': 'pie'}],
    'layout': {'title': 'Proportion of Crime Types'}
}

url = py.plot(fig, filename='Pie Chart of Crime Types')