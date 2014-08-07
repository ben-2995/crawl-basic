from scrapy.spider import Spider
from scrapy.selector import Selector

class flipSpider(Spider):
	name = "flipkart"
	allowed__domains = ["flipkart.com"]
	start_urls = ["http://www.flipkart.com"]
	
	def parse(self,response):
                sel = Selector(response)
