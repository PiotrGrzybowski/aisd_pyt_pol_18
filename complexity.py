import plotly.graph_objects as go
import math

length = 100
domain = list(range(1, length + 1))
mode = 'lines+markers'

figure = go.Figure()
figure.add_trace(go.Scatter(x=domain, y=[x for x in domain], mode=mode, name='O(N)'))

figure.show()