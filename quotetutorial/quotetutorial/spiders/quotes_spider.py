# This is login functionality and opens login page and fills the form and logged in and shows our page in browser
import scrapy

from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/login'
    ]


    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response,formdata={
            'csrf_token' : token,
            'username': 'ksreddykavali@gmail.com',
            'password': 'abcde'
        },callback=self.start_scraping)

    def start_scraping(self,response):
        open_in_browser(response)
        item = QuotetutorialItem()
        all_div_quotes = response.css('div.quote')  # all quote boxes will be come
        for quote in all_div_quotes:
            quotation = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tags = quote.css('.tag::text').extract()

            item['quotation'] = quotation
            item['author'] = author
            item['tags'] = tags
            """yield {
                'quotation' : quotation,
                'author'    : author,
                'tags'      : tags
            }"""
            yield item