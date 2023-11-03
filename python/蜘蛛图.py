import plotly.graph_objects as go

categories = ['numbers & operations','measurement & geometric','statistic & application']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[6,4,5],
      theta=categories,
      fill='toself',
      name='CAITLYN'
))
fig.add_trace(go.Scatterpolar(
      r=[3,2.45,3.27],
      theta=categories,
      fill='toself',
      name='AVG'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 6]
    )),
  showlegend=False
)

fig.show()
