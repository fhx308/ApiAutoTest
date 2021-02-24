'''
Cookie 用来识别客户
'''
import requests

# 没有登录时调用，返回跳转到登录页面
url = "https://www.bagevent.com/account/dashboard"
r = requests.get(url)
print(r.text)

# 发送请求时，带上cookie信息
head = {
    "Cookie": '_ga=GA1.2.1348882891.1611732367; _gid=GA1.2.1617367296.1611732367; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1611732369; __auc=6f0d4f6c17742bc4ec47519c0ea; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38; JSESSIONID=EC8EE3AD393D7E5DEE4F8F832B096009; BAGSESSIONID=fd45cc04-643c-441d-b1c9-876d465ac8df'
}
r = requests.get(url, headers=head)
print(r.text)
'''
缺点：1、cookie会失效，失效后需要重新获取
     2、登陆后的每个接口，都要带着cookie
'''