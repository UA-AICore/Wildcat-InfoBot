import scrapy

class ArizonaSpider(scrapy.Spider):
    """Spider for crawling Arizona.edu domain pages."""

    name = 'arizona'
    allowed_domains = ['arizona.edu']
    start_urls = ['https://www.arizona.edu/']

    def parse(self, response):
        """
        Parse the response, follow all internal links and save the page content.
        
        Args:
            response (scrapy.http.Response): The response object for the web request.
        """
        # Extract all links on the page and generate follow-up requests
        links = response.css('a::attr(href)').getall()
        for link in links:
            if link.startswith(('http:', 'https:')) and 'arizona.edu' in link:
                yield scrapy.Request(link, callback=self.parse)
            elif link.startswith('/'):  # Handle relative URLs
                full_link = response.urljoin(link)
                if 'arizona.edu' in full_link:
                    yield scrapy.Request(full_link, callback=self.parse)

        # Save the current page content to a file
        page = response.url.split('/')[-2] if '/' in response.url else response.url
        filename = f'data/arizona-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

