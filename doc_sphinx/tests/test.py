import sys
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor

not_found_urls = []
non_templated_urls = []

ignored_extensions = [".png", ".jpg", "mailto"]
substitutions = ["|api_url|", "|cdn_url|", "|bimdata_connect|"]


class NotFoundSpider(scrapy.Spider):
    name = "404"
    allowed_domains = ["developers-staging.bimdata.io"] + substitutions
    start_urls = ["https://developers-staging.bimdata.io"]
    handle_httpstatus_list = [404]

    def parse(self, response):
        url = response.url
        referer = response.request.headers.get("Referer", None)
        if any(extension in url for extension in ignored_extensions):
            print("IGNORING " + url)
            return
        if any(substitution in url for substitution in substitutions):
            non_templated_urls.append((url, referer))
            return

        # if any(domain in url for domain in allowed_domains):
        if response.status in self.handle_httpstatus_list:
            not_found_urls.append((url, referer))
            return
        for href in response.css("a::attr(href)"):
            link_url = href.extract()
            if any(substitution in link_url for substitution in substitutions):
                non_templated_urls.append((link_url, url))
                continue
            yield response.follow(href, self.parse)


process = CrawlerProcess()

process.crawl(NotFoundSpider)
process.start()

if non_templated_urls or not_found_urls:
    print()
    print("Non templated errors:")
    for error, parent in non_templated_urls:
        print(error + " from " + parent)
    print()
    print("404 errors:")
    for error, parent in not_found_urls:
        print(error + " from " + parent.decode("utf-8"))

    sys.exit(1)
