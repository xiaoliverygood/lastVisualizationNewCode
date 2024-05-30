from file_util import read_csv_file
from pyecharts.charts import Bar, Pie, Boxplot, Radar
from pyecharts import options as opts

df = read_csv_file("./input.csv")

# 检查每个类别的数据数量
category_sales_amount = [df[df['大类名称'] == cat]['销售金额'].tolist() for cat in df['大类名称'].unique()]
for idx, data in enumerate(category_sales_amount):
    if len(data) < 4:
        print(f"类别 {df['大类名称'].unique()[idx]} 的数据不足，无法绘制箱型图。")


# 1. 柱状图：展示销量前5的商品
top5_products = df.nlargest(5, '销售数量')
bar = (
    Bar()
    .add_xaxis(top5_products['中类名称'].tolist())
    .add_yaxis("销售数量", top5_products['销售数量'].tolist())
    .set_global_opts(title_opts=opts.TitleOpts(title="销量前5的商品"))
)
bar.render("bar_chart.html")

# 2. 饼图：展示不同商品类别的销售金额占比
category_sales = df.groupby('大类名称')['销售金额'].sum().reset_index()
pie = (
    Pie()
    .add("", [list(z) for z in zip(category_sales['大类名称'], category_sales['销售金额'])])
    .set_global_opts(title_opts=opts.TitleOpts(title="商品类别销售金额占比"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
)
pie.render("pie_chart.html")

# 移除数据不足的类别
category_sales_amount = [data for data in category_sales_amount if len(data) >= 4]
# 3. 箱型图：展示不同商品类别的销售金额分布情况
if category_sales_amount:
    boxplot = Boxplot()
    boxplot.add_xaxis(df['大类名称'].unique().tolist())
    boxplot.add_yaxis("销售金额", boxplot.prepare_data(category_sales_amount))
    boxplot.set_global_opts(title_opts=opts.TitleOpts(title="商品类别销售金额分布"))
    boxplot.render("boxplot_chart.html")
else:
    print("数据不足，无法绘制箱型图。")

