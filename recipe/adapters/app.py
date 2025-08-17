# app.py
from flask import Flask, render_template
from datareader.RandomCSVDataReader import RandomCSVDataReader
import os

app = Flask(__name__)

# 添加 zip 过滤器到 Jinja2 环境
app.jinja_env.filters['zip'] = zip

# CSV 文件路径
csv_file_path = os.path.join('data', 'recipes.csv')
data_reader = RandomCSVDataReader(csv_file_path)

@app.route('/')
def random_recipe():
    """显示随机食谱"""
    recipe = data_reader.get_random_recipe()
    if recipe:
        return render_template('RandomRecipe.html', recipe=recipe)
    else:
        return "无法加载食谱数据", 500

if __name__ == '__main__':
    app.run(debug=True)