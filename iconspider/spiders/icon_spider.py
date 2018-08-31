import scrapy
import io
import sys
from iconspider.items import IconspiderItem

class IconSpider(scrapy.Spider):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
    name = "iconspider"
    allowed_domains = ["qqtn.com"]
    i = 0
    start_urls = [
        "https://www.qqtn.com/tx/nvshengtx_1.html",
        "https://www.qqtn.com/tx/nvshengtx_2.html",
        "https://www.qqtn.com/tx/nvshengtx_3.html",
        "https://www.qqtn.com/tx/nvshengtx_4.html",
        "https://www.qqtn.com/tx/nvshengtx_5.html",
        "https://www.qqtn.com/tx/nvshengtx_6.html",
        "https://www.qqtn.com/tx/nvshengtx_7.html",
        "https://www.qqtn.com/tx/nvshengtx_8.html",
        "https://www.qqtn.com/tx/nvshengtx_9.html",
        "https://www.qqtn.com/tx/nvshengtx_10.html",
        "https://www.qqtn.com/tx/nvshengtx_11.html",
        "https://www.qqtn.com/tx/nvshengtx_12.html",
        "https://www.qqtn.com/tx/nvshengtx_13.html",
        "https://www.qqtn.com/tx/nvshengtx_14.html",
        "https://www.qqtn.com/tx/nvshengtx_15.html",
        "https://www.qqtn.com/tx/nvshengtx_16.html",
        "https://www.qqtn.com/tx/nvshengtx_17.html",
        "https://www.qqtn.com/tx/nvshengtx_18.html",
        "https://www.qqtn.com/tx/nvshengtx_19.html",
        "https://www.qqtn.com/tx/nvshengtx_20.html",
        "https://www.qqtn.com/tx/nvshengtx_21.html",
        "https://www.qqtn.com/tx/nvshengtx_22.html",
        "https://www.qqtn.com/tx/nvshengtx_23.html",
        "https://www.qqtn.com/tx/nvshengtx_24.html",
        "https://www.qqtn.com/tx/nvshengtx_25.html",
        "https://www.qqtn.com/tx/nvshengtx_26.html",
        "https://www.qqtn.com/tx/nvshengtx_27.html",
        "https://www.qqtn.com/tx/nvshengtx_28.html",
        "https://www.qqtn.com/tx/nvshengtx_29.html",
        "https://www.qqtn.com/tx/nvshengtx_30.html",
        "https://www.qqtn.com/tx/nvshengtx_31.html",
        "https://www.qqtn.com/tx/nvshengtx_32.html",
        "https://www.qqtn.com/tx/nvshengtx_32.html",
        "https://www.qqtn.com/tx/nvshengtx_33.html",
        "https://www.qqtn.com/tx/nvshengtx_34.html",
        "https://www.qqtn.com/tx/nvshengtx_35.html",
    ]


    def parse(self, response):
        print (response.url)
        items = response.xpath('//div[@class="g-gxlist-box g-box-1200 m-margin15 clearfix"]/div[@class="g-gxlist-left g-left-title f-fl g-main-bg"]/ul[@class="g-gxlist-imgbox"]/li/a/img/@src').extract()
        item = IconspiderItem()
        item['image_urls'] = items
        return item
