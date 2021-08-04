# 课后作业
通过 Cookie 或者 Remote 浏览器复用完成添加联系人测试用例
# 项目结构
 - get_cookie
    - cookies.yaml:`储存cookies的yaml文件`
    - MainLogin.py:`通过复用浏览器的形式登录获取cookies`
 - test_case
   - test_addmember
      - case_addmember.yaml:`储存测试用例的yaml文件`
      - cookies.yaml:`储存cookies的yaml文件`
      - test_addmember.yaml:`添加用户的自动化用例`
   - test_delmember
      - test_delmember.py:`删除用户的自动化用例`
 - test_page
   - add_member_page.py:`封存添加成员页面元素`
   - base_page.py:`封存页面基本操作`
   - contact_page.py:`封存联系人页面元素`
   - main_page.py:`封存主页面元素`