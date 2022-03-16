from we_work_TagApi.apis.baseapi import BaseApi


class WeWork(BaseApi):
    def __init__(self):
        params = {
            'corpid': "wwb3f04477da71390c",
            'corpsecret': "Xai8x-ZNkLzCfzbW7ujMRdsG8JXZnBW4qxv1akaxB5k"
        }
        self.token=self.get_token(params)

    def get_token(self, params):
        """
        获取对应token
        :param params:
                params = {
                            'corpid': corp_id,
                            'corpsecret': corp_secret
                        }
        :return: token
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        req = {
            "method": "get",
            "url": url,
            "params": params
        }
        r = self.run_api(req)
        token = r.json()['access_token']
        return token

