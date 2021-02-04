import scrapy

from ..items import QuotetutorialItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        item = QuotetutorialItem()

        # title = response.css('title').extract()            #gives like {'titletext': ['<title>Quotes to Scrape</title>']}
        # title = response.css('title::text').extract()      #gives like {'titletext': ['Quotes to Scrape']}
        # title = response.xpath("//title").extract()        #gives like {'titletext': ['<title>Quotes to Scrape</title>']}
        # title = response.xpath("//title/text()").extract()  #gives like {'titletext': ['Quotes to Scrape']}
        # yield {'titletext' : title}
        # qts = response.xpath("//span[@class='text']/text()")[1].extract()
        # {'quotes': '“It is our choices, Harry, that show what we truly are, far more than our abilities.”'}
        # yield {'quotes' : qts}
        # page2 = response.css("li.next a").xpath("@href").extract()  #{'quotes': ['/page/2/']}
        # yield {'quotes' : page2}

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

        # next_page = response.css('li.next a::attr(href)').get()
        #
        # if next_page is not None:
        #     yield response.follow(next_page, callback= self.parse) # just like a recursive function
