import scrapy

class AosFatosSpider(scrapy.Spider):
    name = 'aos_fatos'
    start_urls = ['https://www.aosfatos.org/']

    def parse(self, response):
        links = response.xpath('//nav//ul//li/a[re:test(@href, "checamos")]/@href').getall()
        for link in links:
            yield scrapy.Request(
                response.urljoin(link),
                callback=self.parse_category
            )

    def parse_category(self, response):
        news = response.css('a.card::attr(href)').getall()
        for new_url in news:
            yield scrapy.Request(
                response.urljoin()
                # callback=self.parse_new
            )

    def parse_new(self, response):
        pass