import requests
import os.path
import json


class DoubanSplider(object):

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
        self.url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start={}"

    # 获取URL地址
    def parse_url(self):
        url_list = [self.url.format(i) for i in range(20)]
        return url_list

    # 发送请求，获取响应
    def report_url(self, url):
        response = requests.get(url, headers=self.headers)
        return json.loads(response.content.decode())

    # 保存数据
    def save_response(self, response, index):
        path = "豆瓣电影-第{}页.txt".format(index)
        response = json.dumps(response, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
        with open(path, "w", encoding="utf-8") as f:
            f.write(response)

    # 切换到保存数据文件夹
    def switch_path(self):
        os.chdir("./response_result/")
        if not os.path.exists("douban"):
            os.mkdir("douban")
        os.chdir("./douban")

    # 执行
    def run(self):
        # 获取URL地址
        url_list = self.parse_url()
        # 切换保存数据文件
        self.switch_path()
        # 发送请求，
        for url in url_list:
            response = self.report_url(url)
            # 保存数据
            self.save_response(response, url_list.index(url) + 1)


if __name__ == '__main__':
    douban_splide = DoubanSplider()
    douban_splide.run()
