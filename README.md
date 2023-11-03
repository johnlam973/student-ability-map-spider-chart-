# student-ability-map-spider-chart-
【整理后的成绩数据要以csv来存储	并且只可以标题为‘数字与计算', '度量衡与几何', '统计与应用解决’】
文件header 以【名字，姓名,数字与计算,度量衡与几何,统计与应用解决】来排序
实在懒惰的话，可以利用excel先处理一次 把所有相同标题的方式利用【=SUM()】的方式来找到各个学生每项能力值
然后把文件保存为answer.csv
最好是一个年级一个年级做
保存后的文件从file path 复制一遍，然后修改一下py file的read.csv('file path')即可

ver2.py 
-适合用于单个数据，但是你要手动打数据，包括学生名字成绩，需要的格数
-最后会显示在网页上，可自行下载
+需要pip install plotly （从terminal 安装）

ver3.py
-很好看的其实
-把所有学生一次过在一张图上面展现出来比较

ver4.py
-这个是会把所有的图片通过网站一kali跟你开出来，然后可以下载自己所需的学生能力值就好
+需要安装pip install plotly
+需要安装pip install pandas

final.py
-适合用于较为懒惰的老师，可以直接帮你把所有图片下载到文件
-下载下来的图片会直接以学生的名字命名
-但是 一定！一定！一定！要先确保文件夹内有一个命名为images的文件夹
+需要安装pip install plotly
+需要安装pip install pandas

+我的能力平均值是取所有在csv file 中学生的成绩平均，如果后期需一次过做其他学校亦可，但是只要在csv 文件中添加学校名字在学生前面即可
