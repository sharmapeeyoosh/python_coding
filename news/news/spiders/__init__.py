# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from news.items import NewsItem

class ToiSpider(CrawlSpider):
  name = "toinews"
  allowed_domains = ["timesofindia.indiatimes.com"]
  start_urls = ["http://www.timesofindia.indiatimes.com/tech", ]

  rules = [Rule(LinkExtractor(allow=['/smartphones-\d+']), 'parse_story')]
  
  def parse_story(self, response):
    story = NewsItem()
    story['url'] = response.url
    story['headline'] = response.xpath("//title/text()").extract()
    story['intro']  = response.css('p.introductoin::text').extract();
    return story 

  
