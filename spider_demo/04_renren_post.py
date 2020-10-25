import requests


class Renren(object):

    def ren_session_post(self):
        url = "http://www.renren.com/PLogin.do"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
        data = {"email": "15385691275", "password": "1314520zqquau"}
        session = requests.session()
        response = session.post(url, headers=headers, data=data)
        # print(response.content.decode())
        with open("./renren.html", "w", encoding="utf-8") as f:
            f.write(response.content.decode())

    def ren_session_cookie(self):
        url = "http://www.renren.com/974631264/profile"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
        cookies = "anonymid=kfb6u5ja-2y1oh3; _r01_=1; taihe_bi_sdk_uid=22c61e7966e79a39cb7fb00ed1568949; depovince=GW; JSESSIONID=abchqthghN6pycpRbqEvx; ick_login=5414c0aa-1a01-4916-a338-e31c2f48bfef; taihe_bi_sdk_session=e3ee9edf02bff8c8122749a40f1a1555; first_login_flag=1; ln_uact=15385691275; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebecookies=86647446-24a7-4439-9ac0-62760182f9fd|||||; _de=E47BC117E66A21B8FAE3C1E79B0B041C; p=2a437ae6cf0bf501e689fae262e461874; t=8a46f8969632cc5adbe1cdfe8debddae4; societyguester=8a46f8969632cc5adbe1cdfe8debddae4; id=974631264; xnsid=a17f0869; ver=7.0; loginfrom=null; wp_fold=0"
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
        print(cookies)
        response = requests.get(url, headers=headers, cookies=cookies)
        with open("renren2.html", "w", encoding="utf-8") as f:
            f.write(response.content.decode())


if __name__ == '__main__':
    ren = Renren()
    ren.ren_session_cookie()
