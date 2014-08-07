from scrapy.spider import Spider
from scrapy.selector import Selector
from blog.items import BlogItem

class ndtvSpider(Spider):
        
	name = "ndtvtopnews"
	allowed_domains = ["ndtv.com"]
	start_urls = ["http://www.ndtv.com"]
	
	
	def parse(self,response):
                sel = Selector(response)
                divs = sel.xpath('//div[@class="topst_listing"]/ul/li/a')
                items = []
                for divi in divs:
                        item = BlogItem()
                        item['tnews'] = divi.xpath('@href').extract()
                        items.append(item)
                return items
