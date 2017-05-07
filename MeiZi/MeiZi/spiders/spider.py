# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
from MeiZi.items import MeiziItem


class SpiderSpider(CrawlSpider):
    name = "spider"
    allowed_domains = ["mzitu.com"]
    start_urls = ['http://www.mzitu.com/']
    #start_urls=["http://www.mzitu.com/91684"]

    rules={
        Rule(LinkExtractor(allow="http://www.mzitu.com/page/\d+",restrict_xpaths='//div[@class="nav-links"]'),follow=True),
        Rule(LinkExtractor(allow="http://www.mzitu.com/\d+",restrict_xpaths='//div[@class="postlist"]'),follow=True),
        Rule(LinkExtractor(allow="http://www.mzitu.com/\d+/\d+",restrict_xpaths='//div[@class="pagenavi"]'),follow=True,callback='paser_nav')
    }

    def paser_nav(self,response):
        items=MeiziItem()
        # print "**********************************************************************************"
        # print response.url
        img_urls=response.xpath("//div/p/a/img/@src").extract()
        if img_urls:
            items['img_url']=img_urls[0]
        yield items


