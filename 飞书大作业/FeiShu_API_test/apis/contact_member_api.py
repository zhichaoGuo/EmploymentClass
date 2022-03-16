from FeiShu_API_test.apis.feishu import FeiShu
from FeiShu_API_test.apis.utils import Utils


class ContactMemberApi(FeiShu):
    def __init__(self):
        # 实例化时获取token
        self.token = self.get_tenant_token('contact_member')

    # 创建用户 （输入姓名、手机号、以及部门编号department_ids）
    def create_user(self, name, mobile, department_ids):
        '''
        使用该接口向通讯录创建一个用户
        :param name:姓名
        :param mobile:手机号
        :param department_ids:部门编号
        :return:
        '''
        # 输入url
        url = Utils.get_url('create_user')
        # 拼接token
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        # 拼接json数据
        json_data = {
            "user_id": f'ou_{mobile}',
            "name": name,
            "mobile": mobile,
            "department_ids": [f"{department_ids}"],
            "employee_type": '1'

        }
        # 拼接请求参数
        req = {
            "method": "post",
            "url": url,
            "headers": headers,
            "json": json_data
        }
        # 发送请求
        r = self.run_api(req)
        # 返回值
        return r.json()

    # 获取授权的部门列表  主要是用于获取部门编号department_ids
    def get_contact_power_list(self):
        '''
        获取通讯录授权范围:主要用于查找部门编号
        '''
        # 输入url
        url = Utils.get_url('get_contact_power_list')
        # 拼接token
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        # 拼接请求参数
        req = {
            "method": "get",
            "url": url,
            "headers": headers
        }
        # 发送请求
        r = self.run_api(req)
        # 返回值
        return r.json()

    # 获取授权的用户列表
    def get_user_list(self):
        '''
        获取用户列表
        :return:
        '''
        # 输入url
        url = Utils.get_url('get_user_list')
        # 拼接token
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        # 输入请求值
        params = {
            "department_id": 'od-7ed7852a697f9aa3e7b7356eff9ccc38'
        }
        # 拼接请求参数
        req = {
            "method": "get",
            "url": url,
            "headers": headers,
            "params": params
        }
        # 发送请求
        r = self.run_api(req)
        return r.json()

    # 根据用户user_id获取用户信息
    def get_user_data(self, user_id):
        # 输入url
        url = Utils.get_url('get_user_data') + user_id
        # 拼接token
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        # 输入请求参数
        params = {
            'user_id_type': 'user_id'
        }
        # 拼接请求参数
        req = {
            "method": "get",
            "url": url,
            "headers": headers,
            "params": params
        }
        # 发送请求
        r = self.run_api(req)
        return r.json()

    # 根据用户user_id删除用户
    def delete_user(self, user_id):
        # 输入url
        url = Utils.get_url('delete_user') + user_id
        # 输入请求头
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        # 输入请求参数
        params = {
            'user_id_type': 'user_id'
        }
        # 拼接请求参数
        req = {
            "method": "DELETE",
            "url": url,
            "headers": headers,
            "params": params
        }
        # 发送请求
        r = self.run_api(req)
        return r.json()
