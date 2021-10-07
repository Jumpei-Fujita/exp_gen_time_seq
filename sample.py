import plotly.graph_objs as go
import numpy as np

a = np.random.rand(100)
fig = go.Figure(go.Histogram(x = a, nbinsx=4))
fig.write_image('figure/image.png')
fig.show()