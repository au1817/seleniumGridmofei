from selenium.webdriver.common.by import By

# 首页URL
login_url = "http://www.monph.com/"

# 登录链接
login_link = By.XPATH, "//* [text()='登录']"
# 切换账号密码登录
login_userandpwd_link = By.CSS_SELECTOR, ".toggleRight"
# 用户名
login_username = By.CSS_SELECTOR, "#mobile"
# 密码
login_pwd = By.CSS_SELECTOR, "#password"
# 登录按钮
login_btn = By.CSS_SELECTOR, "#submitButton"
# 昵称
login_nickname = By.CSS_SELECTOR, " a[class='phonelink'] span"

"""以下为租房 搜索 筛选 选择商品 点击收藏 查看收藏 配置"""
rent_url = "http://www.monph.com/"
# 我要租房链接
rent_link = By.CSS_SELECTOR, "[title='我要租房']"
# 搜索框
rent_search = By.CSS_SELECTOR, "#searchtxt"
# 搜索按钮
rent_search_btn = By.CSS_SELECTOR, ".btn-submit "
# 筛选 朝向
# 房源展示的第一个信息
rent_info = By.XPATH, "//*[@id='list-content-ul']/li[1]/a/img"
# 收藏
rent_collection = By.CSS_SELECTOR, ".icons_rt70"
# 筛选 更多 朝向不限
rent_direction = "朝向不限"
# 筛选 更多 朝向 南
rent_direction_text = "南"
# 收藏成功
rent_collection_result = By.XPATH, "//*[contains(text(),'收藏成功')]"

"""以下为删除收藏数据配置"""
# 手机号链接
del_phonelink = By.CSS_SELECTOR, ".phonelink"
# 收藏房源
del_coll_room = By.LINK_TEXT, "收藏房源"
# 批量删除
del_all = By.LINK_TEXT, "批量删除"
# 选择框
del_allcheck = By.CSS_SELECTOR, ".box_check"
# 批量删除图标
del_btn = By.CSS_SELECTOR, "#del_all"
# 删除确定按钮
del_ok_btn = By.CSS_SELECTOR, "a[class='layui-layer-btn0']"
# 暂无记录
del_no_exit = By.CSS_SELECTOR, "div[class='person_centermain clearfix nocontent'] img"
# 图片的src属性
del_src = "http://tp.monph.com/public/pc_v3/img/nocontent_03.jpg"
""""以下为App应用元素配置信息"""
# 包名    cn.monph.app/.ui.activity.MainActivity
appPackage = "cn.monph.app"
# 界面名
appActivity = ".ui.activity.MainActivity"
# 我的
app_my = By.XPATH, "//*[@index='4' and @class='android.widget.FrameLayout']"
# 头像image
app_image = By.XPATH, "//*[@index='2' and @class='android.widget.ImageView']"
# 切换账号登录
app_account = By.XPATH, "//*[@text='账号登录' and @class='android.widget.TextView']"
# 用户名
app_phone = By.XPATH, "//*[@text='请填写用户名/手机号' and @class='android.widget.EditText']"
# 密码
app_pwd = By.XPATH, "//*[@index='0' and @class='android.widget.EditText']"
# 登录按钮
app_login_btn = By.XPATH, "//*[@text='登录' and @class='android.widget.TextView']"
# 账号名称
app_nickname = By.XPATH, "//*[@index='1' and @class='android.widget.TextView']"
# 首页
app_index = By.XPATH, "//*[@index='0' and @class='android.widget.FrameLayout']"
# 地铁沿线房源
app_subway = By.XPATH, "//*[@text='地铁沿线房源' and @class='android.widget.TextView']"
# 地铁线路区域
app_channel_area = By.XPATH, "//*[@index='1' and @class='android.widget.HorizontalScrollView']"
# 房源展示区域
app_room_area = By.XPATH, "//*[@index='3' and @bounds='[0,1478][1440,2560]']"




"""以下为登录数据配置数据"""
"""
# 首页URL
login_url = "http://cd.jiwu.com/"

# 登录链接
login_link = By.CSS_SELECTOR, "#login_header"
# 切换账号密码登录
login_userandpwd_link = By.CSS_SELECTOR, ".tologin"
# 用户名
login_username = By.CSS_SELECTOR, "#username"
# 密码
login_pwd = By.CSS_SELECTOR, "#password"
# 登录按钮
login_btn = By.XPATH, "//li[@class='li-btn']/a"
# 置业管家
login_butler = By.XPATH, "//* [text()='置业管家']"
# 昵称
login_nickname = By.XPATH, "//*[@id='zfwy']/a"
"""
