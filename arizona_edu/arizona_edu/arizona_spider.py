import scrapy

class ArizonaSpider(scrapy.Spider):
    name = 'arizona'
    allowed_domains = ['arizona.edu']
    start_urls = ['http://www.arizona.edu/']

    def parse(self, response):
        for href in response.css('a::attr(href)').getall():
            url = response.urljoin(href)
            if 'arizona.edu' in url:
                yield scrapy.Request(url, callback=self.parse)

        page = response.url.split("/")[-1]
        filename = f'data/{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

