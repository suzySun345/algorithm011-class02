  
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Referer': 'https://shimo.im/login',
    'x-requested-with': 'XmlHttpRequest'
}

s = requests.session()

# 需将邮件地址和密码替换为实际真实用户信息
data = {
    'email': 'sunsunsisiyu@126.com',
    'password': 'ssy350009513'
}

url = 'https://shimo.im/lizard-api/auth/password/login'

# 登录结果
r = s.post(url, data=data, headers=headers)
print(r.status_code)