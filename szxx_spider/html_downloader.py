#coding:gb2312
'''
    Create on 2017��2��14��
    @author: ������
'''
import urllib2

con_stocklist = "/m/js/stocklist_zb_zxb.js"
con_url_lastreports = "/disclosure/fulltext/plate/szlatest_24h.js?ver=yyyymmddhhmm"

class HtmlDownLoader(object):
    
    
    def def_domain(self, url):
        self.domain_url = url
    
    def get_last_reports_urls(self):
        #��ȡ���й�Ʊ�����
        stocklist_url = self.domain_url + con_stocklist
        response = urllib2.urlopen(stocklist_url)
    
        if response.getcode() != 200:
            return None
        
        ret = response.read()
        print ret
        #ret.split('|')
        


