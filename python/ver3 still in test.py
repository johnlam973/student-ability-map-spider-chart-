import plotly.graph_objects as go
import pandas as pd

# 假设你的数据以CSV格式存储在文件 'answer.csv' 中
data = pd.read_csv('C:\\Users\\User\\OneDrive\\Desktop\\web project\\python\\answer.csv')

categories = ['numbers & operations', 'measurement & geometric', 'statistic & application']

fig = go.Figure()

# 添加每个学生的雷达图
for index, row in data.iterrows():
    fig.add_trace(go.Scatterpolar(
        r=[row['数字与计算'], row['度量衡与几何'], row['统计与应用解决']],
        theta=categories,
        fill='toself',
        name=row['姓名']
    ))

# 添加平均能力值的雷达图
average_values = data[['数字与计算', '度量衡与几何', '统计与应用解决']].mean().tolist()
fig.add_trace(go.Scatterpolar(
    r=average_values,
    theta=categories,
    fill='toself',
    name='平均能力值'
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 6]
        )),
    showlegend=True
)

fig.show()
