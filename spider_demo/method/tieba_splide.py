import requests
import os


class TiebaSplide(object):

    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
        self.url = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"

    # 切换至保存数据的路劲文件当中
    def switch_path(self):
        os.chdir("./../response_result")
        if not os.path.exists(self.tieba_name):
            os.mkdir(self.tieba_name)
        os.chdir("./../response_result/{}".format(self.tieba_name))

    # 获取URL地址
    def url_temp(self):
        return [self.url.format(i * 50) for i in range(10)]

    # 发送请求获取响应数据
    def response_data(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    # 保存数据
    def save_response_data(self, response, page_num):
        save_name = "{}-第{}页.html".format(self.tieba_name, page_num)
        with open(save_name, "w", encoding="utf-8") as f:
            f.write(response)
        print(save_name)

    def run(self):
        # 1.获取访问地址的URL
        url_list = self.url_temp()
        # 切换至保存数据的路径文件当中
        self.switch_path()
        # 2.发送请求，获取响应
        for url in url_list:
            response = self.response_data(url)
            # 3.存储数据
            self.save_response_data(response, url_list.index(url) + 1)


if __name__ == '__main__':
    tiebasplide = TiebaSplide("dota")
    tiebasplide.run()
    # print(8000/21.75*17.75+8000/21.75*0.8)
