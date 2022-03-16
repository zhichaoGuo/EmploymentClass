import pytest
import requests
import yaml

from FeiShu_API_test.apis.contact_member_api import ContactMemberApi


class TestContactMemberApi:
    f = yaml.safe_load(open('test_case.yaml', encoding='utf-8'))

    # 创建用户
    @pytest.mark.skip
    @pytest.mark.parametrize("name,mobile,department_ids", f["create_user"])
    def test_create_user(self, name, mobile, department_ids):
        test_api = ContactMemberApi()
        r = test_api.create_user(name, mobile, department_ids)
        print(r)
        assert (r['code'] is 0)

    # 删除用户
    # @pytest.mark.skip
    @pytest.mark.parametrize("user_id", f["delete_user"])
    def test_delete_user(self, user_id):
        test_api = ContactMemberApi()
        r = test_api.delete_user(user_id)
        print(r)
        assert (r['code'] is 0)

    # 创建部门
    @pytest.mark.skip
    def test_create_department(self):
        url = 'https://open.feishu.cn/open-apis/contact/v3/departments'
        headers = {
            "Authorization": "Bearer t-f3e5f96004aaae8df008c6f0be894fdcf86bab58"
        }
        json_data = {
            "name": 'test-1',
            "parent_department_id": '0',
            "department_id": 'od-1'
        }
        req = {
            "method": 'post',
            "url": url,
            "headers": headers,
            'json': json_data
        }
        r = requests.request(**req)
        print(r)

    # 获取授权的部门列表
    @pytest.mark.skip
    def test_get_contact_power_list(self):
        test_api = ContactMemberApi()
        r = test_api.get_contact_power_list()
        print(r)
        assert (r['code'] is 0)

    # 获取授权的用户列表
    @pytest.mark.skip
    def test_get_user_list(self):
        test_api = ContactMemberApi()
        r = test_api.get_user_list()
        print(r)
