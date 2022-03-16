import pytest
from ruamel import yaml

from we_work_TagApi.apis.tag_api import TagApi
from we_work_TagApi.apis.utils import Utils


class TestTag:
    def setup_class(self):
        """
        清理测试环境
        """
        pass

    f = yaml.safe_load(open('test_case.yaml', encoding='utf-8'))

    @pytest.mark.parametrize("tagid,tagname", f["create_tag"])
    def test_create_tag(self, tagid, tagname):
        data = {
            "tagid": tagid,
            "tagname": tagname
        }
        r = TagApi()
        e = r.create_tag(data)
        print(e)
        # 断言接口返回状态码正确，且创建成功可查询
        assert (e['errcode'] is 0) and (Utils.find_in_json(r.list_tag(), "tagname", tagname))

    @pytest.mark.parametrize("tagid,tagname", f["update_tag"])
    def test_update_tag(self,tagid,tagname):
        data = {
            "tagid": tagid,
            "tagname": tagname
        }
        r = TagApi()
        e = r.update_tag(data)
        print(e)
        # 断言接口返回状态码正确，且原tagname不可查询，新tagname可查询
        assert (e['errcode'] is 0) and (Utils.find_in_json(r.list_tag(), "tagname", tagname))

    @pytest.mark.parametrize("tagid", f["delete_tag"])
    def test_delete_tag(self,tagid):
        tagid = tagid
        r = TagApi()
        e = r.delete_tag(tagid)
        print(e)
        # 断言接口返回状态码正确，且tagname不可查询
        assert (e['errcode'] is 0) and not (Utils.find_in_json(r.list_tag(), "tagid", tagid))

    def test_list_tag(self):
        r = TagApi()
        e = r.list_tag()
        print(e)
        assert e['errcode'] is 0
