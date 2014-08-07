from scrapy.spider import Spider
class InstSpider(Spider):
	name = "google"
	allowed_domains = ["google.com"]
	start_urls = ["http://www.google.com#q=benith"]
	
	def parse(self,response):
		filename = response.url.split("/")[-2]
        	open(filename, 'wb').write(response.body)
	

