# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class EcomCrawlerPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        # Process price field
        price_keys = ['price']
        for price_key in price_keys:
            value = adapter.get(price_key)
            value = value.replace('Rs. ', '')
            if ',' in value:
                value = value.replace(',', '')
            adapter[price_key] = float(value)
        
        # Process comments field
        comment_keys = ['comments']
        for comment_key in comment_keys:
            value = adapter.get(comment_key)
            if value:
                value = value.replace('(', '').replace(')', '')
                try:
                    value = float(value)
                except ValueError:
                    value = 0  # If conversion fails, set to 0
            else:
                value = 0
            adapter[comment_key] = float(value)
        
        # Process sold field
        sold_keys = ['sold']
        for sold_key in sold_keys:
            value = adapter.get(sold_key)
            if value:
                value = value.replace(" sold", "")
                if 'K' in value:
                    value = float(value.replace('K', '')) * 1000
                elif 'M' in value:
                    value = float(value.replace('M', '')) * 1000000
                else:
                    value = float(value)
            else:
                value = 0
            adapter[sold_key] = float(value)
        
        # Process ratings fields (positive_rating, ship_on_time, response_time)
        rating_keys = ['positive_rating', 'ship_on_time', 'response_time']
        for rating_key in rating_keys:
            value = adapter.get(rating_key)
            try:
                if value is not None:
                    value = float(value.replace("%",''))
                else:
                    value = 0.0 
            except ValueError:
                value = 0.0
            adapter[rating_key] = value
        
        
        
        return item



class Savedatatomongodb:
    def __init__(self):
        self.uri = "mongodb://localhost/27017"
        self.client = MongoClient(self.uri)
        try:
            self.product_database = self.client.get_database("Daraz")
            self.product_collection = self.product_database.get_collection("Products")
        except Exception as e:
            raise Exception("Unable to find the document due to the following error: ", e)
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        item_data = dict(adapter)
        product_url = item_data.get('title')
        try:
            existing_item = self.product_collection.find_one({"title": product_url})
            if existing_item:
                print(f"Item already exists in MongoDB: {item_data}")
            else:
                self.product_collection.insert_one(item_data)
            print(f"Inserted item into MongoDB: {item_data}")
        except Exception as e:
            print(f"Error inserting item into MongoDB: {e}")
        
        return item