#scrapy crawl quotes

#scrapy crawl quotes -o items.csv

import scrapy
from ..items import QuotescraperItem


class QuoteSpider(scrapy.Spider):
	name = 'quotes'
	page_num = 2
	start_urls = ['http://quotes.toscrape.com/']

	def parse(self,response):
		items = QuotescraperItem()
		all_div = response.css('div.quote')
		for content in all_div:

			title = content.css('span.text::text').extract()
			author = content.css('.author::text').extract()
			tag = content.css('.tag::text').extract()
			items['title'] = title
			items['author'] =author
			items['tag'] =tag
			yield items

		next_page = 'http://quotes.toscrape.com/page/'+str(QuoteSpider.page_num)+'/'

		if QuoteSpider.page_num < 11:
			QuoteSpider.page_num += 1
			yield response.follow(next_page,callback = self.parse)