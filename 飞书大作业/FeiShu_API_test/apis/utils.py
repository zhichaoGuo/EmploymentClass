from jsonpath import jsonpath
import yaml


class Utils:

    @classmethod
    def get_url(cls, name):
        # 从文件中读取相应url
        with open('../data/url.yaml') as f:
            datas = yaml.safe_load(f)
            return datas[name]

    @classmethod
    def get_app_data(cls, name):
        # 从文件中读取应用信息
        with open('../data/app.yaml') as f:
            datas = yaml.safe_load(f)
            json_data = {
                "app_id": datas[name]['app_id'],
                "app_secret": datas[name]['app_secret']
            }

            return json_data

    @classmethod
    def find_in_json(cls, data, aim_key, aim_value):
        """
        在json中查找目标键值对
        :param data:查找目标源json
        :param aim_key:查找目标Key
        :param aim_value:查找目标Value
        :return:找到返回Ture，未找到返回False
        """
        list_info = jsonpath(data, f"$..{aim_key}")

        if aim_value in list_info:
            return True
        else:
            return False
