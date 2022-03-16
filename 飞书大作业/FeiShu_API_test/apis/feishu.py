from FeiShu_API_test.apis.base_api import BaseApi
from FeiShu_API_test.apis.utils import Utils


class FeiShu(BaseApi):

    # 获取租户token
    def get_tenant_token(self,app_name):
        # 输入url
        url = Utils.get_url('get_tenant_access_token')
        # 获取应用信息
        app_data = Utils.get_app_data(app_name)
        # 拼接请求参数
        req = {
            "method": "post",
            "url": Utils.get_url('get_tenant_access_token'),
            "json": app_data
        }
        # 发送请求
        r = self.run_api(req)
        # 返回返回值中的token
        return r.json()['tenant_access_token']