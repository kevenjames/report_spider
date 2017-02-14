#coding:gb2312
'''
    Create on 2017年2月14日
    @author: 雷佐天
'''
from szxx_spider import html_downloader, url_manager, html_parser, pdf_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_parser.HtmlParser()
        self.outputer = pdf_outputer.HtmlOutputer()
    
    def craw(self, url_domain):
        self.downloader.def_domain(url_domain)
        urls = self.downloader.get_last_reports_urls()
        self.urls.add_new_report_urls(urls)
        while self.urls.has_new_report_url():
            try:
                new_report_url = self.urls.get_new_report_url()
                pdf_data = self.downloader.download(new_report_url)
                #new_urls, new_data = self.parser.parse(new_report_url, pdf_data)
                #self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(pdf_data)
            except:
                print "发生异常！"
        
        self.outputer.output_pdf()


if __name__=="__main__":
    url_domain = "http://disclosure.szse.cn"
    obj_spider = SpiderMain()
    obj_spider.craw(url_domain);



