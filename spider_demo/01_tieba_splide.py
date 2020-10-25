import requests


class SplideTest:
    def __init__(self, page_name):
        self.page_name = page_name
        self.url = "https://tieba.baidu.com/f?kw=" + page_name + "&ie=utf-8&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}

    # 获取访问URL列表
    def url_list(self):
        # url_list = []
        # for i in range(10):
        #     url = self.url.format(i * 50)
        #     url_list.append(url)
        # return url_list
        return [self.url.format(i * 50) for i in range(1000)]

    # 发送request请求，获取响应
    def response_data(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    # 保存获取响应数据
    def response_result(self, page_number, response_result):
        page_name = self.page_name + "-" + "第{}页.html".format(page_number)
        with open(page_name, "w", encoding='utf-8') as f:
            f.write(response_result)

    def run(self):
        # 1. 获取访问地址URL
        url_list = self.url_list()
        # 2. 获取相应数据
        for url in url_list:
            response = self.response_data(url)
            # 3. 保存数据
            self.response_result(url_list.index(url) + 1, response)


if __name__ == '__main__':
    splide = SplideTest("dota")
    # splide.url_list()
    splide.run()
    # splide.response_data()
