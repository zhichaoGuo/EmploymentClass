import requests


class BaseApi:

    def run_api(self,req):
        '''
        对requests进行二次封装，执行api
        :param req:
            req={
                    “method”：“get”
                    “url”：“xxxxx”
                    “params”：{}
                    “json”：{}
                }
        :return:返回requests的结果
        '''
        return requests.request(**req)
