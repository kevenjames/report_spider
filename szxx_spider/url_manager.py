#coding:gb2312
'''
    Create on 2017年2月14日
    @author: 雷佐天
'''

class UrlManager(object):
    def __init__(self):
        self.new_report_urls = set()
        self.old_report_urls = set()
    
    def add_new_report_url(self, url):
        if url is None:
            return
        if url not in self.new_report_urls and url not in self.old_report_urls:
            self.new_report_urls.add(url)
            
    def add_new_report_urls(self, urls):
        if urls is None or len(urls) == 0:
            return;
        
        for url in urls:
            self.add_new_report_url(url);
        
         
    
    def has_new_report_url(self):
        return len(self.new_report_urls) != 0

    def get_new_report_url(self):
        new_report_url = self.new_urls.pop()
        self.old_report_urls.add(new_report_url)
        
        return new_report_url
    
    def get_stock_list(self):
        pass

    
    def get_last_reports_urls(self):
        pass
    
    

