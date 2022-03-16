from jsonpath import jsonpath
from ruamel import yaml


class Utils:
    @classmethod
    def get_url(cls, name):
        with open('../data/url.yaml') as f:
            datas = yaml.safe_load(f)
            return datas[name]

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
