#video tutorial link
# https://youtu.be/2vcp0fKq3aw?list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t
# user agents : # https://youtu.be/GOjuQ9IgSfI?list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t
# Proxies     : # https://youtu.be/090tLVr0l7s?list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t
import scrapy
from ..items import AmazonItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    page_number =2

    start_urls = ['https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&qid=1612338673&rnid=1250225011&ref=lp_1000_nr_p_n_publication_date_0']

    def parse(self, response):
        items = AmazonItem()

        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
        product_price = response.css('.a-price-fraction , .a-price-whole').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items

        next_page = 'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page='+ str(AmazonItem.page_number) +'&qid=1612338690&rnid=1250225011&ref=sr_pg_2'
        if AmazonItem.page_number <= 75:
            AmazonItem.page_number +=1
            yield response.follow(next_page,callback = self.parse)


