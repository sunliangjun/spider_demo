import requests


class Renren(object):
    def post_session(self):
        url = "http://www.renren.com/PLogin.do"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
        data = {"email": "15385691275", "password": "1314520zqquau"}
        session = requests.session()
        response = session.post(url, headers=headers, data=data)
        with open("renren.html", "w", encoding="utf-8") as f:
            f.write(response.content.decode())

    def post_cookies_data(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
        }
        cookie = "anonymid=kfb6u5ja-2y1oh3; _r01_=1; taihe_bi_sdk_uid=22c61e7966e79a39cb7fb00ed1568949; depovince=GW; ick_login=5414c0aa-1a01-4916-a338-e31c2f48bfef; taihe_bi_sdk_session=e3ee9edf02bff8c8122749a40f1a1555; first_login_flag=1; ln_uact=15385691275; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebecookies=41f1367d-fea9-4601-8aa0-5c917093ee11|||||; _de=E47BC117E66A21B8FAE3C1E79B0B041C; p=c965e890c2b92a42c62794e2835331994; t=d4cca696fb222a216d21d355f89d7d014; societyguester=d4cca696fb222a216d21d355f89d7d014; id=974631264; xnsid=a0c3ea80; ver=7.0; loginfrom=null"
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}
        url = "http://www.renren.com/974631264/profile"
        response = requests.get(url, headers=headers, cookies=cookies)
        with open("renren2.html", "w", encoding="utf-8") as f:
            f.write(response.content.decode())

    def post_cookies(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
            "Cookie": "anonymid=kfb6u5ja-2y1oh3; _r01_=1; taihe_bi_sdk_uid=22c61e7966e79a39cb7fb00ed1568949; depovince=GW; ick_login=5414c0aa-1a01-4916-a338-e31c2f48bfef; taihe_bi_sdk_session=e3ee9edf02bff8c8122749a40f1a1555; first_login_flag=1; ln_uact=15385691275; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebecookies=41f1367d-fea9-4601-8aa0-5c917093ee11|||||; _de=E47BC117E66A21B8FAE3C1E79B0B041C; p=c965e890c2b92a42c62794e2835331994; t=d4cca696fb222a216d21d355f89d7d014; societyguester=d4cca696fb222a216d21d355f89d7d014; id=974631264; xnsid=a0c3ea80; ver=7.0; loginfrom=null"
        }
        url = "http://www.renren.com/974631264/profile"
        response = requests.get(url, headers=headers)
        with open("renren1.html", "w", encoding="utf-8") as f:
            f.write(response.content.decode())


if __name__ == '__main__':
    ren = Renren()
    # 第三方登录，session保存请求中的cookie，下次直接登录
    # ren.post_session()
    # 先手动登录后，拿到cookie放在请求头里，后面请求其他页面的时候可以直接请求
    # ren.post_cookies()
    # cookie单独存为一个字典的形式，发送请求的时候带上需要的cookie
    ren.post_cookies_data()
