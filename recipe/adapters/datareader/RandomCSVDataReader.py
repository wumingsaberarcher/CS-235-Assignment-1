# datareader/RandomCSVDataReader.py
import pandas as pd
import random
import os

class RandomCSVDataReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.load_data()

    def load_data(self):
        """加载 CSV 文件"""
        if os.path.exists(self.file_path):
            self.data = pd.read_csv(self.file_path)
        else:
            raise FileNotFoundError(f"文件 {self.file_path} 不存在")

    def get_random_recipe(self):
        """随机返回一条食谱记录"""
        if self.data is None or self.data.empty:
            return None
        return self.data.sample(1).to_dict(orient='records')[0]