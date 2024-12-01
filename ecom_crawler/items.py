# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EcomCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

class EcomItem(scrapy.Item):
    img = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    disount_price = scrapy.Field()
    sold = scrapy.Field()
    comments = scrapy.Field()
    color_image_url = scrapy.Field()
    out_of_stock = scrapy.Field()
    stars = scrapy.Field()
    availability = scrapy.Field()
    main_link = scrapy.Field()
    category_data = scrapy.Field()
    product_name = scrapy.Field()
    product_description = scrapy.Field()
    product_desc = scrapy.Field()
    sku = scrapy.Field()
    brand_name = scrapy.Field()
    image_list = scrapy.Field()
    positive_rating = scrapy.Field()
    ship_on_time = scrapy.Field()
    response_time = scrapy.Field()
    delivery_location = scrapy.Field()
    delivery_content = scrapy.Field()
    return_policy = scrapy.Field()
    warranty_info = scrapy.Field()
    rating_data = scrapy.Field()