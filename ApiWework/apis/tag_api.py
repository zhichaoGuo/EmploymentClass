from we_work_TagApi.apis.utils import Utils
from we_work_TagApi.apis.wework import WeWork


class TagApi(WeWork):

    def create_tag(self,data):
        '''
        创建标签
        :param data: 通过接口传递的参数
        :return: json格式接口返回值
        '''
        url = Utils.get_url('create_tag')
        req = {
            "method": "post",
            "url": url,
            "params":{
                "access_token":self.token
            },
            "json": data
        }
        r=self.run_api(req)
        return r.json()

    def update_tag(self,data):
        '''
        更新标签
        :param data: 通过接口传递的参数
        :return: json格式接口返回值
        '''
        url = Utils.get_url('update_tag')
        req = {
            "method": "post",
            "url": url,
            "params": {
                "access_token": self.token
            },
            "json": data
        }
        r = self.run_api(req)
        return r.json()

    def delete_tag(self,tagid):
        url = Utils.get_url('delete_tag')
        req = {
            "method": "get",
            "url": url,
            "params": {
                "access_token": self.token,
                "tagid": tagid
            }
        }
        r = self.run_api(req)
        return r.json()

    def list_tag(self):
        url = Utils.get_url('list_tag')
        req = {
            "method": "get",
            "url": url,
            "params": {
                "access_token": self.token
            }
        }
        r = self.run_api(req)
        return r.json()
