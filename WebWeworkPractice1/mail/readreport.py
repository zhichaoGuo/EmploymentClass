import os


class NewReport():
    """获取最新的测试报告"""
    path = Config.BasePath + "\\report\\"

    def report(self):
        # 获取文件夹中所有的文件名，以列表形式返回
        lists = os.listdir(self.path)
        # 按照key的关键字进行升序排列，lambda入参x作为lists列表元素，获取文件最后的修改日期
        # 最后对lists以文件时间从小到大排列
        lists.sort(key=lambda x:os.path.getmtime((self.path+x)))
        # 获取最新文件的绝度路径，列表中最后与一个值，文件夹+文件名
        new_report = os.path.join(self.path,lists[-1])
        return new_report