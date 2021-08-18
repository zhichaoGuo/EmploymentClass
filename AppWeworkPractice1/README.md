# 课后作业
完成企业微信移动端添加联系人删除联系人用例
# 项目结构
- test_case:`测试用例文件夹`
    - test_addmember.py:`添加联系人用例`
    - test_delmenmber.py:`删除联系人用例`
- test_page:`页面元素`
    - AddmemberPage.py:`添加成员页面`
    - app.py:`基础配置，后期可通过参数化来优化掉`
    - BasePage.py:`公用方法`
    - ContactPage.py:`通讯录页面`
    - EdimemberPage.py:`编辑成员页面`
    - EdiPersonalPage.py:`编辑成员页面2`
    - main.py:`登录后主页面，主要用于跳转`
    - PersonalPage.py:`编辑成员界面`
    - PersonalPageMore.py:`编辑成员-更多界面`