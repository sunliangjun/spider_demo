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

    """
    sort_keys：是否按照字典排序（a-z）输出，True代表是，False代表否。
    indent=4：设置缩进格数，一般由于Linux的习惯，这里会设置为4。
    separators：设置分隔符，在dic = {'a': 1, 'b': 2, 'c': 3}这行代码里可以看到冒号和逗号后面都带了个空格，这也是因为Python的默认格式也是如此，如果不想后面带有空格输出，那就可以设置成separators=(',', ':')，如果想保持原样，可以写成separators=(', ', ': ')
    ensure_ascii=False ：是否显示ascii这个码，默认是ture，改为False 即可
    """
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
