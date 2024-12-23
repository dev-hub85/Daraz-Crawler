import scrapy
import time
from scrapy.http import Request, Response
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from ecom_crawler.items import EcomItem

class EcomspiderSpider(scrapy.Spider):
    name = "ecomspider"
    allowed_domains = ["daraz.pk"]
    start_urls = ["https://www.daraz.pk/Category/"]    
    
    custom_settings ={
        'FEED':{
            'itmedata.json':{'format':'json', 'overwrite': True, 'indent': 4}
        }
    }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.index = 1
        self.index2 =0
        self.all_data = []
        self.subcategory_links = []
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def parse(self, response):
        all_url_data = [
    {
        "id": "Level_1_Category_No1",
        "name": "Groceries & Pets",
        "categories": [
            {
                "name": "Frozen Food",
                "link": "/www.daraz.pk/groceries-frozen",
                "subcategories": [
                    {
                        "name": "Other Frozen Food",
                        "link": "/www.daraz.pk/other-frozen-food"
                    },
                    {
                        "name": "Chicken",
                        "link": "/www.daraz.pk/groceries-frozen-meat-chicken"
                    },
                    {
                        "name": "Beef",
                        "link": "/www.daraz.pk/groceries-frozen-meat-beef"
                    }
                ]
            },
            {
                "name": "Dog",
                "link": "/www.daraz.pk/dogs-supplies",
                "subcategories": [
                    {
                        "name": "Bowls & Feeders",
                        "link": "/www.daraz.pk/dog-bowls-feeders"
                    },
                    {
                        "name": "Beds, Mats & Houses",
                        "link": "/www.daraz.pk/dog-beds-mats-houses"
                    },
                    {
                        "name": "Cages, Crates & Doors",
                        "link": "/www.daraz.pk/dog-cages-pens-doors"
                    },
                    {
                        "name": "Fleas & Ticks",
                        "link": "/www.daraz.pk/dog-flea-tick"
                    },
                    {
                        "name": "Leashes, Collars & Muzzles",
                        "link": "/www.daraz.pk/dog-leashes-collars-muzzles"
                    },
                    {
                        "name": "Carriers & Travel",
                        "link": "/www.daraz.pk/dog-carriers-travel"
                    },
                    {
                        "name": "Treats",
                        "link": "/www.daraz.pk/dog-treats"
                    },
                    {
                        "name": "Food",
                        "link": "/www.daraz.pk/dog-food"
                    },
                    {
                        "name": "Grooming",
                        "link": "/www.daraz.pk/dog-grooming-supplies"
                    },
                    {
                        "name": "Toys",
                        "link": "/www.daraz.pk/toys"
                    }
                ]
            },
            {
                "name": "Cat",
                "link": "/www.daraz.pk/cats-supplies",
                "subcategories": [
                    {
                        "name": "Trees, Condos & Scratchers",
                        "link": "/www.daraz.pk/cat-condo-tree-scratchers"
                    },
                    {
                        "name": "Bowls & Feeders",
                        "link": "/www.daraz.pk/cat-bowls-feeders"
                    },
                    {
                        "name": "Beds, Mats & Houses",
                        "link": "/www.daraz.pk/cat-beds-mats-houses"
                    },
                    {
                        "name": "Cages, Crates & Doors",
                        "link": "/www.daraz.pk/cat-cages-crates-doors"
                    },
                    {
                        "name": "Carriers & Travel",
                        "link": "/www.daraz.pk/cat-carriers-travel"
                    },
                    {
                        "name": "Toys",
                        "link": "/www.daraz.pk/cats-toys"
                    },
                    {
                        "name": "Cat Treats",
                        "link": "/www.daraz.pk/cat-treats"
                    },
                    {
                        "name": "Grooming",
                        "link": "/www.daraz.pk/cat-grooming-supplies"
                    },
                    {
                        "name": "Food",
                        "link": "/www.daraz.pk/cat-food"
                    },
                    {
                        "name": "Litter & Toilet",
                        "link": "/www.daraz.pk/cat-clean-up-toilets"
                    }
                ]
            },
            {
                "name": "Breakfast, Choco & Snacks",
                "link": "/www.daraz.pk/breakfast",
                "subcategories": [
                    {
                        "name": "Cakes & Sweets",
                        "link": "/www.daraz.pk/groceries-bakery-cakes-sweet-pies-cakes"
                    },
                    {
                        "name": "Jams, Honey & Spreads",
                        "link": "/www.daraz.pk/groceries-breakfast-jams-honey-spreads"
                    },
                    {
                        "name": "Oatmeals",
                        "link": "/www.daraz.pk/oats-porridge"
                    },
                    {
                        "name": "Breakfast Cereals",
                        "link": "/www.daraz.pk/cereal"
                    },
                    {
                        "name": "Pancake & Waffle Mixes",
                        "link": "/www.daraz.pk/pancake-waffle-mixes"
                    },
                    {
                        "name": "Breakfast Bars",
                        "link": "/www.daraz.pk/protein-bars"
                    },
                    {
                        "name": "Instant Breakfast Drinks",
                        "link": "/www.daraz.pk/instant-breakfast-drinks"
                    },
                    {
                        "name": "Nuts & Legumes",
                        "link": "/www.daraz.pk/nuts-2"
                    },
                    {
                        "name": "Biscuit & Cookies",
                        "link": "/www.daraz.pk/biscuits-cookies"
                    },
                    {
                        "name": "Chocolate & Candy",
                        "link": "/www.daraz.pk/chocolates"
                    },
                    {
                        "name": "Chewing Gums & Mints",
                        "link": "/www.daraz.pk/chewing-bubble-gum"
                    },
                    {
                        "name": "Chips & Crisps",
                        "link": "/www.daraz.pk/chips-crisps"
                    }
                ]
            },
            {
                "name": "Beverages",
                "link": "/www.daraz.pk/beverages",
                "subcategories": [
                    {
                        "name": "Soft Drinks",
                        "link": "/www.daraz.pk/groceries-beverages-soft-drinks"
                    },
                    {
                        "name": "Water",
                        "link": "/www.daraz.pk/groceries-beverages-water"
                    },
                    {
                        "name": "UHT, Milk & Milk Powder",
                        "link": "/www.daraz.pk/groceries-beverages-uht-milk-milk-powder"
                    },
                    {
                        "name": "Juices",
                        "link": "/www.daraz.pk/groceries-beverages-juices"
                    },
                    {
                        "name": "Coffee",
                        "link": "/www.daraz.pk/coffee-espresso"
                    },
                    {
                        "name": "Powdered Drinks",
                        "link": "/www.daraz.pk/milk-powder-and-milk-modifiers"
                    },
                    {
                        "name": "Tea",
                        "link": "/www.daraz.pk/tea"
                    },
                    {
                        "name": "Flavoring Syrup",
                        "link": "/www.daraz.pk/syrups"
                    }
                ]
            },
            {
                "name": "Food Staples",
                "link": "/www.daraz.pk/baking-and-cooking",
                "subcategories": [
                    {
                        "name": "Condiment Dressing",
                        "link": "/www.daraz.pk/condiment-dressing"
                    },
                    {
                        "name": "Home Baking & Sugar",
                        "link": "/www.daraz.pk/groceries-baking-cooking-home-baking-sugar"
                    },
                    {
                        "name": "Cooking Ingredients",
                        "link": "/www.daraz.pk/groceries-baking-cooking-cooking-ingredients"
                    },
                    {
                        "name": "Noodles & Pasta",
                        "link": "/www.daraz.pk/noodles"
                    },
                    {
                        "name": "Jarred Food",
                        "link": "/www.daraz.pk/groceries-canned-dry-packaged-food-jarred-food"
                    },
                    {
                        "name": "Canned Food",
                        "link": "/www.daraz.pk/groceries-canned-dry-packaged-food-canned-food"
                    },
                    {
                        "name": "Instant & Ready-to-Eat",
                        "link": "/www.daraz.pk/groceries-canned-dry-packaged-food-instant-ready-to-eat"
                    },
                    {
                        "name": "Grains, Beans & Pulses",
                        "link": "/www.daraz.pk/groceries-canned-dry-packaged-food-grains-beans-pulses"
                    },
                    {
                        "name": "Rice",
                        "link": "/www.daraz.pk/rice"
                    },
                    {
                        "name": "Oil",
                        "link": "/www.daraz.pk/oil-ghee"
                    }
                ]
            },
            {
                "name": "Laundry & Household",
                "link": "/www.daraz.pk/laundry-and-home-care-4",
                "subcategories": [
                    {
                        "name": "Laundry",
                        "link": "/www.daraz.pk/laundry-products"
                    },
                    {
                        "name": "Pest Control",
                        "link": "/www.daraz.pk/groceries-laundry-household-pest-control"
                    },
                    {
                        "name": "Tissue Paper",
                        "link": "/www.daraz.pk/groceries-laundry-household-paper-towels"
                    },
                    {
                        "name": "Air Fresheners",
                        "link": "/www.daraz.pk/groceries-laundry-household-air-fresheners"
                    },
                    {
                        "name": "Cleaning Supplies",
                        "link": "/www.daraz.pk/cleaning-supplies"
                    }
                ]
            }
        ]
    },
    {
        "id": "Level_1_Category_No2",
        "name": "Health & Beauty",
        "categories": [
            {
                "name": "Men's Care",
                "link": "/www.daraz.pk/mens-grooming",
                "subcategories": [
                    {
                        "name": "Shaving & Grooming",
                        "link": "/www.daraz.pk/mens-shaving-grooming"
                    }
                ]
            },
            {
                "name": "Medical Supplies",
                "link": "/www.daraz.pk/health-beauty-care",
                "subcategories": [
                    {
                        "name": "Stethoscopes",
                        "link": "/www.daraz.pk/stethoscopes"
                    },
                    {
                        "name": "Surgical Masks",
                        "link": "/www.daraz.pk/surgical-masks"
                    },
                    {
                        "name": "Health Monitors & Tests",
                        "link": "/www.daraz.pk/health-monitors-tests"
                    },
                    {
                        "name": "Ointments and Creams",
                        "link": "/www.daraz.pk/ointments-creams"
                    },
                    {
                        "name": "Nebulizer & Aspirators",
                        "link": "/www.daraz.pk/nebulizers"
                    },
                    {
                        "name": "Health Accessories",
                        "link": "/www.daraz.pk/health-aid-supplies"
                    },
                    {
                        "name": "First Aid Supplies",
                        "link": "/www.daraz.pk/first-aid-supplies"
                    }
                ]
            },
            {
                "name": "Personal Care",
                "link": "/www.daraz.pk/personal-care",
                "subcategories": [
                    {
                        "name": "Adult Diapers",
                        "link": "/www.daraz.pk/adult-diapers-incontinence"
                    },
                    {
                        "name": "Oral Care",
                        "link": "/www.daraz.pk/oral-care-products"
                    },
                    {
                        "name": "Eye Care",
                        "link": "/www.daraz.pk/eye-creams"
                    },
                    {
                        "name": "Pads & Tampons",
                        "link": "/www.daraz.pk/tampons"
                    },
                    {
                        "name": "Menstrual Cups",
                        "link": "/www.daraz.pk/tampons"
                    },
                    {
                        "name": "Deodorants",
                        "link": "/www.daraz.pk/deodorants"
                    },
                    {
                        "name": "Personal Safety & Security",
                        "link": "/www.daraz.pk/personal-safety-security"
                    },
                    {
                        "name": "Ear Care",
                        "link": "/www.daraz.pk/ear-care"
                    }
                ]
            },
            {
                "name": "Hair Care",
                "link": "/www.daraz.pk/hair-care",
                "subcategories": [
                    {
                        "name": "Oil & Serums",
                        "link": "/www.daraz.pk/hair%20care-hair-oils-322"
                    },
                    {
                        "name": "Hair Care Accessories",
                        "link": "/www.daraz.pk/hair-care-accessories"
                    },
                    {
                        "name": "Shampoo & Conditioner",
                        "link": "/www.daraz.pk/hair-shampoo"
                    },
                    {
                        "name": "Hair Treatments",
                        "link": "/www.daraz.pk/treatments"
                    },
                    {
                        "name": "Hair Styling",
                        "link": "/www.daraz.pk/hair-styling"
                    },
                    {
                        "name": "Hair Coloring",
                        "link": "/www.daraz.pk/hair-color"
                    }
                ]
            },
            {
                "name": "Beauty Tools",
                "link": "/www.daraz.pk/health-beauty-tools",
                "subcategories": [
                    {
                        "name": "Foot Relief Tools",
                        "link": "/www.daraz.pk/foot-relief"
                    },
                    {
                        "name": "Slimming & Electric Massagers",
                        "link": "/www.daraz.pk/massage-relaxation"
                    },
                    {
                        "name": "Hair Removal Appliances",
                        "link": "/www.daraz.pk/hair-removal-appliances"
                    },
                    {
                        "name": "Hair Styling Appliances",
                        "link": "/www.daraz.pk/hair-styling-appliances"
                    },
                    {
                        "name": "Skin Care Tools",
                        "link": "/www.daraz.pk/hb-skin-care-tools"
                    }
                ]
            },
            {
                "name": "Makeup",
                "link": "/www.daraz.pk/womens-make-up",
                "subcategories": [
                    {
                        "name": "Bulk Deals",
                        "link": "/www.daraz.pk/makeup-bulk-deals"
                    },
                    {
                        "name": "Eyes",
                        "link": "/www.daraz.pk/eye-makeup"
                    },
                    {
                        "name": "Makeup Accessories",
                        "link": "/www.daraz.pk/makeup-accessories"
                    },
                    {
                        "name": "Lips",
                        "link": "/www.daraz.pk/lips"
                    },
                    {
                        "name": "Nails",
                        "link": "/www.daraz.pk/nails-makeup"
                    },
                    {
                        "name": "Makeup Removers",
                        "link": "/www.daraz.pk/womens-make-up-remover"
                    },
                    {
                        "name": "Makeup Palettes & Sets",
                        "link": "/www.daraz.pk/makeup-kits-palettes"
                    },
                    {
                        "name": "Face",
                        "link": "/www.daraz.pk/blush"
                    }
                ]
            },
            {
                "name": "Fragrances",
                "link": "/www.daraz.pk/fragrances",
                "subcategories": [
                    {
                        "name": "Women",
                        "link": "/www.daraz.pk/womens-fragrance"
                    },
                    {
                        "name": "Men",
                        "link": "/www.daraz.pk/mens-fragrance"
                    },
                    {
                        "name": "Unisex",
                        "link": "/www.daraz.pk/unisex-fragrance"
                    }
                ]
            },
            {
                "name": "Bath & Body",
                "link": "/www.daraz.pk/bath-body",
                "subcategories": [
                    {
                        "name": "Hand Care",
                        "link": "/www.daraz.pk/hand-care"
                    },
                    {
                        "name": "Talcum Powder",
                        "link": "/www.daraz.pk/womans-hygiene-talcum-powder"
                    },
                    {
                        "name": "Foot Care",
                        "link": "/www.daraz.pk/foot-care"
                    },
                    {
                        "name": "Body Moisturizers",
                        "link": "/www.daraz.pk/body-lotion-butter"
                    },
                    {
                        "name": "Hair Removal",
                        "link": "/www.daraz.pk/hair-removal-tools"
                    },
                    {
                        "name": "Body Soaps & Shower Gels",
                        "link": "/www.daraz.pk/soaps-wash"
                    },
                    {
                        "name": "Body Scrubs",
                        "link": "/www.daraz.pk/body-wash-scrubs"
                    },
                    {
                        "name": "Bath & Body Accessories",
                        "link": "/www.daraz.pk/bath-body-accessories"
                    },
                    {
                        "name": "Body & Massage Oils",
                        "link": "/www.daraz.pk/body-oils"
                    }
                ]
            },
            {
                "name": "Sexual Wellness",
                "link": "/www.daraz.pk/sexual-wellness",
                "subcategories": [
                    {
                        "name": "Lubricants",
                        "link": "/www.daraz.pk/lubricants-sexual-health"
                    },
                    {
                        "name": "Condoms",
                        "link": "/www.daraz.pk/shop-condoms"
                    }
                ]
            },
            {
                "name": "Skin Care",
                "link": "/www.daraz.pk/skincare",
                "subcategories": [
                    {
                        "name": "Moisturizers and Cream",
                        "link": "/www.daraz.pk/moisturizers-creams"
                    },
                    {
                        "name": "Lip Balm & Treatment",
                        "link": "/www.daraz.pk/lip-balms-treatments"
                    },
                    {
                        "name": "Sunscreen & Aftersun",
                        "link": "/www.daraz.pk/mens-sun-care"
                    },
                    {
                        "name": "Face Mask & Packs",
                        "link": "/www.daraz.pk/facial-masks-peels"
                    },
                    {
                        "name": "Face Scrubs & Exfoliators",
                        "link": "/www.daraz.pk/mens-face"
                    },
                    {
                        "name": "Facial Cleansers",
                        "link": "/www.daraz.pk/face-wash"
                    },
                    {
                        "name": "Toner & Mists",
                        "link": "/www.daraz.pk/toner"
                    },
                    {
                        "name": "Anti-aging",
                        "link": "/www.daraz.pk/anti-aging"
                    }
                ]
            }
        ]
    },
    {
        "id": "Level_1_Category_No3",
        "name": "Men's Fashion",
        "category": [
            {
                "name": "Boy's Shoes",
                "link": "/www.daraz.pk/boys-shoes"
            },
            {
                "name": "Kurtas & Shalwar Kameez",
                "link": "/www.daraz.pk/mens-traditional-clothing",
                "subcategories": [
                    {
                        "name": "Kurtas",
                        "link": "/www.daraz.pk/mens-kurtas"
                    },
                    {
                        "name": "Shalwar",
                        "link": "/www.daraz.pk/mens-lungi"
                    },
                    {
                        "name": "Unstitched Fabric",
                        "link": "/www.daraz.pk/mens-unstitched-fabric"
                    },
                    {
                        "name": "Shawls",
                        "link": "/www.daraz.pk/mens-shawls"
                    }
                ]
            },
            {
                "name": "Winter Clothing",
                "link": "/www.daraz.pk/men-sweaters-cardigans",
                "subcategories": [
                    {
                        "name": "Jackets & Coats",
                        "link": "/www.daraz.pk/men-jackets-coats"
                    },
                    {
                        "name": "Hoodies & Sweatshirts",
                        "link": "/www.daraz.pk/mens-hoodies"
                    }
                ]
            },
            {
                "name": "Shorts, Joggers & Sweats",
                "link": "/www.daraz.pk/mens-shorts",
                "subcategories": [
                    {
                        "name": "Joggers & Sweats",
                        "link": "/www.daraz.pk/mens-sweat-pants"
                    }
                ]
            },
            {
                "name": "Shirts & Polo",
                "link": "/www.daraz.pk/mens-shirts",
                "subcategories": [
                    {
                        "name": "Polos",
                        "link": "/www.daraz.pk/mens-polo-shirts"
                    },
                    {
                        "name": "Casual Shirts",
                        "link": "/www.daraz.pk/mens-casual-shirts"
                    },
                    {
                        "name": "Formal Shirts",
                        "link": "/www.daraz.pk/mens-formal-shirts"
                    }
                ]
            },
            {
                "name": "T-Shirts & Tanks",
                "link": "/www.daraz.pk/mens-t-shirts"
            },
            {
                "name": "Boy's Accessories",
                "link": "/www.daraz.pk/fashion-boys-accessories",
                "subcategories": [
                    {
                        "name": "Socks",
                        "link": "/www.daraz.pk/boys-socks"
                    },
                    {
                        "name": "Belts",
                        "link": "/www.daraz.pk/boys-belts-ties-bow-ties"
                    },
                    {
                        "name": "Hats & Caps",
                        "link": "/www.daraz.pk/hats-scarves"
                    }
                ]
            },
            {
                "name": "Boy's Clothing",
                "link": "/www.daraz.pk/boys-clothing",
                "subcategories": [
                    {
                        "name": "Kurtas & Shalwar Kameez",
                        "link": "/www.daraz.pk/boys-kurtas"
                    },
                    {
                        "name": "Shorts",
                        "link": "/www.daraz.pk/boys-shorts"
                    },
                    {
                        "name": "T-Shirts & Shirts",
                        "link": "/www.daraz.pk/boys-t-shirts"
                    },
                    {
                        "name": "Pants & Jeans",
                        "link": "/www.daraz.pk/fashion-boys-clothing-pants-jeans"
                    },
                    {
                        "name": "Underwear & Socks",
                        "link": "/www.daraz.pk/fashion-boys-clothing-underwear"
                    }
                ]
            },
            {
                "name": "Accessories",
                "link": "/www.daraz.pk/men-accessories",
                "subcategories": [
                    {
                        "name": "Socks",
                        "link": "/www.daraz.pk/mens-socks"
                    },
                    {
                        "name": "Sunglasses",
                        "link": "/www.daraz.pk/eyewear-sunglasses-168"
                    },
                    {
                        "name": "Gloves",
                        "link": "/www.daraz.pk/mens-gloves"
                    },
                    {
                        "name": "Hats & Caps",
                        "link": "/www.daraz.pk/men-accessories-hats"
                    },
                    {
                        "name": "Belts",
                        "link": "/www.daraz.pk/mens-belt"
                    },
                    {
                        "name": "Scarves",
                        "link": "/www.daraz.pk/mens-scarves-mufflers"
                    },
                    {
                        "name": "Ties & Bows",
                        "link": "/www.daraz.pk/mens-ties-cufflinks"
                    }
                ]
            },
            {
                "name": "Shoes",
                "link": "/www.daraz.pk/mens-shoes",
                "subcategories": [
                    {
                        "name": "Shoes Accessories",
                        "link": "/www.daraz.pk/mens-shoe-care"
                    },
                    {
                        "name": "Slip-Ons & Loafers",
                        "link": "/www.daraz.pk/mens-slip-ons"
                    },
                    {
                        "name": "Khusa & Kolapuri",
                        "link": "/www.daraz.pk/mens-khusa-kolapuri"
                    },
                    {
                        "name": "Formal Shoes",
                        "link": "/www.daraz.pk/mens-formal-shoes"
                    },
                    {
                        "name": "Flip Flops & Sandals",
                        "link": "/www.daraz.pk/mens-sandals-slippers"
                    },
                    {
                        "name": "Sneakers",
                        "link": "/www.daraz.pk/mens-sneakers"
                    },
                    {
                        "name": "Boots",
                        "link": "/www.daraz.pk/mens-boots"
                    }
                ]
            },
            {
                "name": "Inner Wear",
                "link": "/www.daraz.pk/clothing-men-underwear",
                "subcategories": [
                    {
                        "name": "Thermal",
                        "link": "/www.daraz.pk/mens-thermal"
                    },
                    {
                        "name": "Nightwear",
                        "link": "/www.daraz.pk/mens-sleepwear"
                    },
                    {
                        "name": "Vests",
                        "link": "/www.daraz.pk/mens-waistcoats"
                    },
                    {
                        "name": "Socks",
                        "link": "/www.daraz.pk/mens-socks"
                    },
                    {
                        "name": "Briefs",
                        "link": "/www.daraz.pk/mens-briefs"
                    },
                    {
                        "name": "Trunk & Boxers",
                        "link": "/www.daraz.pk/mens-boxers"
                    }
                ]
            },
            {
                "name": "Pants & Jeans",
                "link": "/www.daraz.pk/mens-pants-trousers",
                "subcategories": [
                    {
                        "name": "Jeans",
                        "link": "/www.daraz.pk/mens-jeans"
                    },
                    {
                        "name": "Cargo",
                        "link": "/www.daraz.pk/mens-lounge-pants"
                    },
                    {
                        "name": "Chinos",
                        "link": "/www.daraz.pk/mens-khakis-chinos"
                    }
                ]
            }
        ]
    },
    {
        "id": "Level_1_Category_No4",
        "name": "Women's Fashion",
        "category": [
            {
                "name": "Girls Shoes",
                "link": "/www.daraz.pk/girls-shoes"
            },
            {
                "name": "Girls Clothing",
                "link": "/www.daraz.pk/girls-clothing",
                "subcategories": [
                    {
                        "name": "Socks & Tights",
                        "link": "/www.daraz.pk/girls-socks"
                    },
                    {
                        "name": "Jackets & Coats",
                        "link": "/www.daraz.pk/jackets-coats"
                    },
                    {
                        "name": "Underwear & Sleepwear",
                        "link": "/www.daraz.pk/girls-undergarments"
                    },
                    {
                        "name": "Hats & Caps",
                        "link": "/www.daraz.pk/girls-hats-scarves"
                    },
                    {
                        "name": "Belts",
                        "link": "/www.daraz.pk/fashion-girls-accessories-belts"
                    },
                    {
                        "name": "Gloves, Scarves & Cold Weather",
                        "link": "/www.daraz.pk/gloves-scarves-cold-weather"
                    },
                    {
                        "name": "Dresses",
                        "link": "/www.daraz.pk/girls-jumpsuits-rompers"
                    },
                    {
                        "name": "Tops",
                        "link": "/www.daraz.pk/girls-clothing-tops"
                    },
                    {
                        "name": "Bottoms",
                        "link": "/www.daraz.pk/girls-clothing-bottoms"
                    },
                    {
                        "name": "Swimsuits",
                        "link": "/www.daraz.pk/girls-swimsuits"
                    },
                    {
                        "name": "Hair Accessories",
                        "link": "/www.daraz.pk/girls-hair-accessories"
                    },
                    {
                        "name": "Hoodies",
                        "link": "/www.daraz.pk/girls-hoodies-2"
                    }
                ]
            },
            {
                "name": "Sleepwear & Innerwear",
                "link": "/www.daraz.pk/womens-nightwear",
                "subcategories": [
                    {
                        "name": "Tanks & Camisoles",
                        "link": "/www.daraz.pk/womens-tops-vests-camisoles"
                    },
                    {
                        "name": "Robe and Gown sets",
                        "link": "/www.daraz.pk/women-robes"
                    },
                    {
                        "name": "Shapewear",
                        "link": "/www.daraz.pk/womens-shapewear"
                    },
                    {
                        "name": "Nightwear",
                        "link": "/www.daraz.pk/fashion-nightwear"
                    }
                ]
            },
            {
                "name": "Bras, Panties & Lingerie",
                "link": "/www.daraz.pk/womens-lingerie-sleepwear",
                "subcategories": [
                    {
                        "name": "Beachwear and Bikinis",
                        "link": "/www.daraz.pk/swimwear-beachwear"
                    },
                    {
                        "name": "Lingerie Sets",
                        "link": "/www.daraz.pk/womens-lingerie"
                    },
                    {
                        "name": "Socks & Tights",
                        "link": "/www.daraz.pk/womens-socks-stockings"
                    },
                    {
                        "name": "Bras",
                        "link": "/www.daraz.pk/womens-bras"
                    },
                    {
                        "name": "Panties",
                        "link": "/www.daraz.pk/womens-panties"
                    }
                ]
            },
            {
                "name": "Unstitched Fabric",
                "link": "/www.daraz.pk/womens-lawn",
                "subcategories": [
                    {
                        "name": "Sarees",
                        "link": "/www.daraz.pk/womens-sarees"
                    },
                    {
                        "name": "Branded Unstitched",
                        "link": "/www.daraz.pk/womens-dresses"
                    }
                ]
            },
            {
                "name": "Kurtas & Shalwar Kameez",
                "link": "/www.daraz.pk/womens-kurtas-shalwar-kameez",
                "subcategories": [
                    {
                        "name": "Kurtis",
                        "link": "/www.daraz.pk/womens-kurtis"
                    },
                    {
                        "name": "Shalwar Kameez",
                        "link": "/www.daraz.pk/womens-shalwar-kameez"
                    },
                    {
                        "name": "Trousers & Palazzos",
                        "link": "/www.daraz.pk/palazzos-capris"
                    }
                ]
            },
            {
                "name": "Dresses & Skirts",
                "link": "/www.daraz.pk/womens-dresses",
                "subcategories": [
                    {
                        "name": "Skirts",
                        "link": "/www.daraz.pk/womens-skirts"
                    },
                    {
                        "name": "Formal Wear",
                        "link": "/www.daraz.pk/womens-formal-wear"
                    },
                    {
                        "name": "Ethnic Dresses",
                        "link": "/www.daraz.pk/womens-dresses"
                    }
                ]
            },
            {
                "name": "Winter Clothing",
                "link": "/www.daraz.pk/womens-sweaters",
                "subcategories": [
                    {
                        "name": "Jackets & Coats",
                        "link": "/www.daraz.pk/women-jackets-coats"
                    },
                    {
                        "name": "Shrugs",
                        "link": "/www.daraz.pk/shrugs"
                    },
                    {
                        "name": "Hoodies & Sweatshirts",
                        "link": "/www.daraz.pk/womens-hoodies-sweatshirts"
                    }
                ]
            },
            {
                "name": "Pants, Jeans & Leggings",
                "link": "/www.daraz.pk/womens-pants-trousers",
                "subcategories": [
                    {
                        "name": "Jeggings",
                        "link": "/www.daraz.pk/womens-jeggings"
                    },
                    {
                        "name": "Shorts",
                        "link": "/www.daraz.pk/clothing-shorts"
                    },
                    {
                        "name": "Leggings",
                        "link": "/www.daraz.pk/womens-tights-leggings"
                    },
                    {
                        "name": "Pants",
                        "link": "/www.daraz.pk/women-pants"
                    },
                    {
                        "name": "Jeans",
                        "link": "/www.daraz.pk/womens-jeans"
                    }
                ]
            },
            {
                "name": "Tops",
                "link": "/www.daraz.pk/tops",
                "subcategories": [
                    {
                        "name": "Tunics",
                        "link": "/www.daraz.pk/tops-tunics"
                    },
                    {
                        "name": "Blouses & Shirts",
                        "link": "/www.daraz.pk/womens-shirts"
                    }
                ]
            },
            {
                "name": "Muslim Wear",
                "link": "/www.daraz.pk/womens-abayas-and-hijabs",
                "subcategories": [
                    {
                        "name": "Dupattas, Stoles & Shawls",
                        "link": "/www.daraz.pk/womens-dupattas-stoles-shawls"
                    },
                    {
                        "name": "Scarves",
                        "link": "/www.daraz.pk/womens-scarves-mufflers"
                    },
                    {
                        "name": "Abayas & Hijabs",
                        "link": "/www.daraz.pk/womens-hijabs"
                    },
                    {
                        "name": "Hair Accessories",
                        "link": "/www.daraz.pk/women-hair-accessories"
                    }
                ]
            }
        ]
    },
    {
        "id": "Level_1_Category_No5",
        "name": "Mother & Baby",
        "categories": [
            {
                "name": "Clothing & Accessories",
                "link": "/www.daraz.pk/baby-clothings-accessories",
                "subcategories": [
                    {
                        "name": "Newborn",
                        "link": "/www.daraz.pk/new-born-baby-clothing"
                    },
                    {
                        "name": "Accessories",
                        "link": "/www.daraz.pk/new-born-baby-clothing-accessories"
                    },
                    {
                        "name": "New born sets & Packs",
                        "link": "/www.daraz.pk/sets-packs"
                    },
                    {
                        "name": "Girls (Under 3 Years)",
                        "link": "/www.daraz.pk/baby-girls-clothing-and-accessories"
                    },
                    {
                        "name": "Boys (Under 3 Years)",
                        "link": "/www.daraz.pk/baby-boys-clothing-and-accessories"
                    },
                    {
                        "name": "New born bodysuits",
                        "link": "/www.daraz.pk/boys-jumpsuits-rompers"
                    }
                ]
            },
            {
                "name": "Maternity Care",
                "link": "/www.daraz.pk/womens-maternity-care",
                "subcategories": [
                    {
                        "name": "Pregnancy Pillows",
                        "link": "/www.daraz.pk/maternity-pregnancy-pillows"
                    },
                    {
                        "name": "Maternity Accessories",
                        "link": "/www.daraz.pk/baby-toddler-maternity-accessories"
                    },
                    {
                        "name": "Breast Pumps",
                        "link": "/www.daraz.pk/breast-pumps"
                    },
                    {
                        "name": "Nursing Covers",
                        "link": "/www.daraz.pk/nursing-covers"
                    },
                    {
                        "name": "Maternity Wear",
                        "link": "/www.daraz.pk/maternity-care-wear"
                    },
                    {
                        "name": "Nipple Care",
                        "link": "/www.daraz.pk/nipple-care"
                    },
                    {
                        "name": "Breast Shells",
                        "link": "/www.daraz.pk/breast-shells-creams"
                    }
                ]
            },
            {
                "name": "Baby Gear",
                "link": "/www.daraz.pk/baby-gear",
                "subcategories": [
                    {
                        "name": "Backpacks & Carriers",
                        "link": "/www.daraz.pk/baby-toddler-carriers"
                    },
                    {
                        "name": "Swings, Jumpers & Bouncers",
                        "link": "/www.daraz.pk/baby-walkers"
                    },
                    {
                        "name": "Harnesses & Leashes",
                        "link": "/www.daraz.pk/baby-harnesses-leashes"
                    },
                    {
                        "name": "Walkers",
                        "link": "/www.daraz.pk/baby-toddler-walkers"
                    },
                    {
                        "name": "Car Seats",
                        "link": "/www.daraz.pk/baby-car-seats"
                    },
                    {
                        "name": "Strollers",
                        "link": "/www.daraz.pk/baby-toddler-strollers"
                    },
                    {
                        "name": "Highchairs & Booster Seats",
                        "link": "/www.daraz.pk/high-chairs"
                    },
                    {
                        "name": "Baby Safety",
                        "link": "/www.daraz.pk/baby-safety"
                    },
                    {
                        "name": "Baby Monitor",
                        "link": "/www.daraz.pk/baby-toddler-monitors"
                    },
                    {
                        "name": "Kids Bag",
                        "link": "/www.daraz.pk/boys-bags"
                    }
                ]
            },
            {
                "name": "Remote Control & Vehicles",
                "link": "/www.daraz.pk/remote-control-toys-and-play-vehicles",
                "subcategories": [
                    {
                        "name": "Play Vehicles",
                        "link": "/www.daraz.pk/play-vehicles-toys"
                    },
                    {
                        "name": "RC Vehicles & Batteries",
                        "link": "/www.daraz.pk/vehicles-batteries"
                    },
                    {
                        "name": "Drones & Accessories",
                        "link": "/www.daraz.pk/drones-and-accessories"
                    },
                    {
                        "name": "Die-Cast Vehicles",
                        "link": "/www.daraz.pk/die-cast-cars"
                    },
                    {
                        "name": "Play Trains & Railway Sets",
                        "link": "/www.daraz.pk/model-railway-and-train-sets"
                    }
                ]
            },
            {
                "name": "Feeding",
                "link": "/www.daraz.pk/feeding",
                "subcategories": [
                    {
                        "name": "Bottle-Feeding",
                        "link": "/www.daraz.pk/bottle-feeding"
                    },
                    {
                        "name": "Breastfeeding",
                        "link": "/www.daraz.pk/breast-feeding"
                    },
                    {
                        "name": "Food Blenders",
                        "link": "/www.daraz.pk/baby-food-blenders"
                    },
                    {
                        "name": "Utensils",
                        "link": "/www.daraz.pk/baby-utensils"
                    },
                    {
                        "name": "Pacifiers & Teethers",
                        "link": "/www.daraz.pk/baby-pacifiers-accessories"
                    }
                ]
            },
            {
                "name": "Milk Formula & Baby Food",
                "link": "/www.daraz.pk/formula-milk",
                "subcategories": [
                    {
                        "name": "Toddler Milk (1 - under 3 yrs)",
                        "link": "/www.daraz.pk/toddler-milk"
                    },
                    {
                        "name": "Maternal",
                        "link": "/www.daraz.pk/maternal-milk"
                    },
                    {
                        "name": "Infant Milk (0-6 Months)",
                        "link": "/www.daraz.pk/milk-formula"
                    },
                    {
                        "name": "Infant Milk (6-12 Months)",
                        "link": "/www.daraz.pk/followon-milk-formula"
                    },
                    {
                        "name": "Growing-up Milk (3yrs +)",
                        "link": "/www.daraz.pk/growth-milk"
                    },
                    {
                        "name": "Baby & Toddler Foods",
                        "link": "/www.daraz.pk/baby-n-toddler-food"
                    }
                ]
            },
            {
                "name": "Diapering & Potty",
                "link": "/www.daraz.pk/baby-toddler-diapers-potties",
                "subcategories": [
                    {
                        "name": "Disposable diapers",
                        "link": "/www.daraz.pk/baby-diapers"
                    },
                    {
                        "name": "Diaper Bags",
                        "link": "/www.daraz.pk/diaper-bags"
                    },
                    {
                        "name": "Diapering Care",
                        "link": "/www.daraz.pk/diapering-care"
                    },
                    {
                        "name": "Changing Tables, Pads & Kits",
                        "link": "/www.daraz.pk/baby-changing"
                    },
                    {
                        "name": "Cloth Diapers & Accessories",
                        "link": "/www.daraz.pk/cloth-diapers-and-accessories"
                    },
                    {
                        "name": "Wipes & Holders",
                        "link": "/www.daraz.pk/wipes-holders"
                    },
                    {
                        "name": "Potty Training",
                        "link": "/www.daraz.pk/potty-training"
                    }
                ]
            },
            {
                "name": "Nursery",
                "link": "/www.daraz.pk/baby-toddler-nursery",
                "subcategories": [
                    {
                        "name": "Storage & Organization",
                        "link": "/www.daraz.pk/storage-organization"
                    },
                    {
                        "name": "Nursery Decor",
                        "link": "/www.daraz.pk/nursery-decor"
                    },
                    {
                        "name": "Baby Furniture",
                        "link": "/www.daraz.pk/baby-furniture"
                    },
                    {
                        "name": "Mattresses & Bedding",
                        "link": "/www.daraz.pk/mattresses-bedding"
                    }
                ]
            },
            {
                "name": "Sports & Outdoor Play",
                "link": "/www.daraz.pk/sports-and-outdoor-play",
                "subcategories": [
                    {
                        "name": "Inflatable Bouncers",
                        "link": "/www.daraz.pk/inflatable-bouncers"
                    },
                    {
                        "name": "Fidget Spinners",
                        "link": "/www.daraz.pk/fidget-spinners"
                    },
                    {
                        "name": "Swimming Pool & Water Toys",
                        "link": "/www.daraz.pk/swimming-pool-and-water-toys"
                    }
                ]
            },
            {
                "name": "Baby & Toddler Toys",
                "link": "/www.daraz.pk/baby-toddler-toys-games",
                "subcategories": [
                    {
                        "name": "Developmental Toys",
                        "link": "/www.daraz.pk/developmental-toys"
                    },
                    {
                        "name": "Plush Toys",
                        "link": "/www.daraz.pk/plush-toys"
                    },
                    {
                        "name": "Musical Toys",
                        "link": "/www.daraz.pk/musical-toys"
                    }
                ]
            }
        ]
    },
    {
        "id": "Level_1_Category_No6",
        "name": "Home & Lifestyle",
        "categories": [
            {
                "name": "Laundry & Cleaning",
                "link": "/www.daraz.pk/laundry-cleaning",
                "subcategories": [
                    {
                        "name": "Brushes, Sponges & Wipers",
                        "link": "/www.daraz.pk/household-supplies"
                    },
                    {
                        "name": "Brooms, Mops & Sweepers",
                        "link": "/www.daraz.pk/mops-refills-mop-sets"
                    },
                    {
                        "name": "Clothes Line & Drying Racks",
                        "link": "/www.daraz.pk/pegs-clothes-lines"
                    },
                    {
                        "name": "Ironing Boards",
                        "link": "/www.daraz.pk/ironing-boards-covers"
                    },
                    {
                        "name": "Laundry Baskets & Hampers",
                        "link": "/www.daraz.pk/bathroom-baskets-trays"
                    }
                ]
            },
            {
                "name": "Tools, DIY & Outdoor",
                "link": "/www.daraz.pk/home-improvement-tools",
                "subcategories": [
                    {
                        "name": "Paints",
                        "link": "/www.daraz.pk/paints"
                    },
                    {
                        "name": "Fixtures & Plumbing",
                        "link": "/www.daraz.pk/plumbing"
                    },
                    {
                        "name": "Lawn & Garden",
                        "link": "/www.daraz.pk/lawn-garden"
                    },
                    {
                        "name": "Power Tools",
                        "link": "/www.daraz.pk/power-tools"
                    },
                    {
                        "name": "Security",
                        "link": "/www.daraz.pk/security-system-hardware"
                    },
                    {
                        "name": "Electrical",
                        "link": "/www.daraz.pk/electrical-equipment"
                    },
                    {
                        "name": "Primers",
                        "link": "/www.daraz.pk/supplies-paints"
                    },
                    {
                        "name": "Hand Tools",
                        "link": "/www.daraz.pk/engine-hand-tools"
                    },
                    {
                        "name": "Home Build Up",
                        "link": "/www.daraz.pk/home-build-up"
                    }
                ]
            },
            {
                "name": "Bath",
                "link": "/www.daraz.pk/bath",
                "subcategories": [
                    {
                        "name": "Bathroom Scales",
                        "link": "/www.daraz.pk/bathroom-scales"
                    },
                    {
                        "name": "Towel Rails & Warmers",
                        "link": "/www.daraz.pk/bathroom-towel-racks-warmers"
                    },
                    {
                        "name": "Shower Caddies & Hangers",
                        "link": "/www.daraz.pk/shower-holders-hangers"
                    },
                    {
                        "name": "Bathroom Shelving",
                        "link": "/www.daraz.pk/shower-curtains"
                    },
                    {
                        "name": "Bath Towels",
                        "link": "/www.daraz.pk/bath-towels"
                    },
                    {
                        "name": "Bathrobes",
                        "link": "/www.daraz.pk/bathrobes"
                    },
                    {
                        "name": "Bath Mats",
                        "link": "/www.daraz.pk/bath-mats-rugs"
                    }
                ]
            },
            {
                "name": "Stationery & Craft",
                "link": "/www.daraz.pk/stationery-craft",
                "subcategories": [
                    {
                        "name": "Paper Products",
                        "link": "/www.daraz.pk/paper-products"
                    },
                    {
                        "name": "Writing & Correction",
                        "link": "/www.daraz.pk/writing-utensils"
                    },
                    {
                        "name": "Art Supplies",
                        "link": "/www.daraz.pk/art-supplies"
                    },
                    {
                        "name": "Packaging & Cartons",
                        "link": "/www.daraz.pk/packaging-products"
                    },
                    {
                        "name": "School & Office Equipment",
                        "link": "/www.daraz.pk/school-supplies"
                    },
                    {
                        "name": "Gifts & Wrapping",
                        "link": "/www.daraz.pk/gifts-wrapping"
                    },
                    {
                        "name": "School Uniforms",
                        "link": "/www.daraz.pk/school-uniforms"
                    }
                ]
            },
            {
                "name": "Furniture",
                "link": "/www.daraz.pk/furniture",
                "subcategories": [
                    {
                        "name": "Kitchen Furniture",
                        "link": "/www.daraz.pk/kitchen-dining-furniture"
                    },
                    {
                        "name": "Gaming Furniture",
                        "link": "/www.daraz.pk/game-room-furniture"
                    },
                    {
                        "name": "Home Office",
                        "link": "/www.daraz.pk/office-furniture"
                    },
                    {
                        "name": "Living Room",
                        "link": "/www.daraz.pk/living-room-furniture"
                    },
                    {
                        "name": "Bedroom",
                        "link": "/www.daraz.pk/bedroom-furniture"
                    }
                ]
            },
            {
                "name": "Bedding",
                "link": "/www.daraz.pk/bedding-2",
                "subcategories": [
                    {
                        "name": "Comforters, Quilts & Duvets",
                        "link": "/www.daraz.pk/comforters-quilts"
                    },
                    {
                        "name": "Blankets & Throws",
                        "link": "/www.daraz.pk/blankets-throws"
                    },
                    {
                        "name": "Pillows & Bolsters",
                        "link": "/www.daraz.pk/anti-allergy-pillows"
                    },
                    {
                        "name": "Pillow Cases",
                        "link": "/www.daraz.pk/pillows"
                    },
                    {
                        "name": "Bedding Accessories",
                        "link": "/www.daraz.pk/bedding-accessories"
                    },
                    {
                        "name": "Bed Sheets",
                        "link": "/www.daraz.pk/bedsheets"
                    },
                    {
                        "name": "Mattress Protectors",
                        "link": "/www.daraz.pk/bedding-mattress-pads-protectors"
                    }
                ]
            },
            {
                "name": "Decor",
                "link": "/www.daraz.pk/home-decoration",
                "subcategories": [
                    {
                        "name": "Mirrors",
                        "link": "/www.daraz.pk/mirrors"
                    },
                    {
                        "name": "Cushions & Covers",
                        "link": "/www.daraz.pk/cushions"
                    },
                    {
                        "name": "Rugs & Carpets",
                        "link": "/www.daraz.pk/carpets-rugs"
                    },
                    {
                        "name": "Wall Stickers & Decals",
                        "link": "/www.daraz.pk/wall-stickers"
                    },
                    {
                        "name": "Curtains",
                        "link": "/www.daraz.pk/curtains-blinds-shades"
                    },
                    {
                        "name": "Artificial Flowers & Plants",
                        "link": "/www.daraz.pk/artificial-flowers-plants"
                    },
                    {
                        "name": "Candles & Candleholders",
                        "link": "/www.daraz.pk/candles-candle-holders"
                    },
                    {
                        "name": "Clocks",
                        "link": "/www.daraz.pk/clocks"
                    },
                    {
                        "name": "Vases & Vessels",
                        "link": "/www.daraz.pk/vases"
                    },
                    {
                        "name": "Picture Frames",
                        "link": "/www.daraz.pk/picture-frames"
                    }
                ]
            },
            {
                "name": "Lighting",
                "link": "/www.daraz.pk/lighting",
                "subcategories": [
                    {
                        "name": "Wall Lights & Sconces",
                        "link": "/www.daraz.pk/wall-lights"
                    },
                    {
                        "name": "Ceiling Lights",
                        "link": "/www.daraz.pk/ceiling-lights"
                    },
                    {
                        "name": "Lighting Fixtures & Components",
                        "link": "/www.daraz.pk/lighting-components"
                    },
                    {
                        "name": "Light Bulbs",
                        "link": "/www.daraz.pk/lighting-bulbs"
                    },
                    {
                        "name": "Lamp Shades",
                        "link": "/www.daraz.pk/bedside-lamps"
                    },
                    {
                        "name": "Outdoor Lighting",
                        "link": "/www.daraz.pk/outdoor-lighting"
                    },
                    {
                        "name": "Table Lamps",
                        "link": "/www.daraz.pk/table-lamps"
                    },
                    {
                        "name": "Floor Lamps",
                        "link": "/www.daraz.pk/floor-lamps"
                    }
                ]
            },
            {
                "name": "Media, Music & Books",
                "link": "/www.daraz.pk/books-games-music",
                "subcategories": [
                    {
                        "name": "eBooks",
                        "link": "/www.daraz.pk/ebooks"
                    },
                    {
                        "name": "Music",
                        "link": "/www.daraz.pk/music"
                    },
                    {
                        "name": "Movies & TV Shows",
                        "link": "/www.daraz.pk/movies-tv"
                    },
                    {
                        "name": "Board Games",
                        "link": "/www.daraz.pk/board-games"
                    },
                    {
                        "name": "Books",
                        "link": "/www.daraz.pk/books"
                    }
                ]
            },
            {
                "name": "Toys, Kids & Babies",
                "link": "/www.daraz.pk/toys-kids-babies",
                "subcategories": [
                    {
                        "name": "Toys",
                        "link": "/www.daraz.pk/toys"
                    },
                    {
                        "name": "Educational Toys",
                        "link": "/www.daraz.pk/educational-toys"
                    },
                    {
                        "name": "Games & Puzzles",
                        "link": "/www.daraz.pk/puzzles"
                    },
                    {
                        "name": "Kids Furniture",
                        "link": "/www.daraz.pk/kids-room-furniture"
                    },
                    {
                        "name": "Baby & Toddler",
                        "link": "/www.daraz.pk/baby-products"
                    },
                    {
                        "name": "Kids Clothing",
                        "link": "/www.daraz.pk/kids-clothing"
                    }
                ]
            }
        ]
    },
    {
        "id": "Level_1_Category_No7",
        "name": "Electronic Devices",
        "categories": [
            {
                "name": "Feature Phones",
                "link": "/www.daraz.pk/featurephones"
            },
            {
                "name": "Daraz Like New",
                "link": "/www.daraz.pk/like-new-phones",
                "subcategories": [
                    {
                        "name": "Like New Phones",
                        "link": "/www.daraz.pk/like-new-phones"
                    },
                    {
                        "name": "Like New Smartwatches",
                        "link": "/www.daraz.pk/like_new_smartwatches"
                    },
                    {
                        "name": "Like New Laptops",
                        "link": "/www.daraz.pk/like-new-laptops"
                    },
                    {
                        "name": "Like New Tablets",
                        "link": "/www.daraz.pk/like-new-tablets"
                    },
                    {
                        "name": "Like New Speakers",
                        "link": "/www.daraz.pk/like-new-speakers"
                    },
                    {
                        "name": "Like New Airbuds",
                        "link": "/www.daraz.pk/like_new_airpods"
                    }
                ]
            },
            {
                "name": "Security Cameras",
                "link": "/www.daraz.pk/security-cameras",
                "subcategories": [
                    {
                        "name": "IP Security Cameras",
                        "link": "/www.daraz.pk/security-surveillance"
                    }
                ]
            },
            {
                "name": "Gaming Consoles",
                "link": "/www.daraz.pk/gaming-consoles",
                "subcategories": [
                    {
                        "name": "Playstation Games",
                        "link": "/www.daraz.pk/playstation-games"
                    },
                    {
                        "name": "PlayStation Consoles",
                        "link": "/www.daraz.pk/playstation-consoles"
                    },
                    {
                        "name": "Playstation Controllers",
                        "link": "/www.daraz.pk/gaming-controllers"
                    },
                    {
                        "name": "Nintendo Games",
                        "link": "/www.daraz.pk/nintendo-games"
                    },
                    {
                        "name": "Xbox Games",
                        "link": "/www.daraz.pk/xbox-games"
                    }
                ]
            },
            {
                "name": "Smart Phones",
                "link": "/www.daraz.pk/smartphones/mi",
                "subcategories": [
                    {
                        "name": "Nokia Mobiles",
                        "link": "/www.daraz.pk/smartphones/nokia"
                    },
                    {
                        "name": "Honor Mobiles",
                        "link": "/www.daraz.pk/smartphones/honor"
                    },
                    {
                        "name": "Infinix Mobiles",
                        "link": "/www.daraz.pk/smartphones/infinix"
                    },
                    {
                        "name": "Realme Mobiles",
                        "link": "/www.daraz.pk/smartphones/realme"
                    },
                    {
                        "name": "Redmi Mobiles",
                        "link": "/www.daraz.pk/smartphones/redmi"
                    },
                    {
                        "name": "Oneplus Mobiles",
                        "link": "/www.daraz.pk/catalog/?q=oneplus&_keyori=ss&from=input"
                    },
                    {
                        "name": "Oppo Mobile Phones",
                        "link": "/www.daraz.pk/smartphones/oppo"
                    },
                    {
                        "name": "Apple iPhones",
                        "link": "/www.daraz.pk/smartphones/apple"
                    },
                    {
                        "name": "Tecno Mobiles",
                        "link": "/www.daraz.pk/smartphones/?q=tecno&from=input"
                    },
                    {
                        "name": "Samsung Mobile Phones",
                        "link": "/www.daraz.pk/catalog/?q=samsung%20%20mobile"
                    },
                    {
                        "name": "Vivo Mobiles",
                        "link": "/www.daraz.pk/smartphones/vivo"
                    }
                ]
            },
            {
                "name": "Cameras & Drones",
                "link": "/www.daraz.pk/camera",
                "subcategories": [
                    {
                        "name": "Drones",
                        "link": "/www.daraz.pk/camera-drones"
                    },
                    {
                        "name": "Point & Shoot",
                        "link": "/www.daraz.pk/point-shoot-plain-digital"
                    },
                    {
                        "name": "DSLR",
                        "link": "/www.daraz.pk/dslr-hybrid-cameras"
                    },
                    {
                        "name": "Instant Cameras",
                        "link": "/www.daraz.pk/instant-camera"
                    },
                    {
                        "name": "Video Camera",
                        "link": "/www.daraz.pk/video-camera"
                    }
                ]
            },
            {
                "name": "Smart Watches",
                "link": "/www.daraz.pk/smart-watches"
            },
            {
                "name": "Monitors",
                "link": "/www.daraz.pk/monitors"
            },
            {
                "name": "Landline Phones",
                "link": "/www.daraz.pk/corded-phones"
            },
            {
                "name": "Laptops",
                "link": "/www.daraz.pk/laptops",
                "subcategories": [
                    {
                        "name": "Refurbished Laptops",
                        "link": "/www.daraz.pk/refurbished-laptops"
                    },
                    {
                        "name": "Traditional Laptops",
                        "link": "/www.daraz.pk/traditional-laptops"
                    }
                ]
            },
            {
                "name": "Desktops",
                "link": "/www.daraz.pk/desktop-computer",
                "subcategories": [
                    {
                        "name": "All-In-One",
                        "link": "/www.daraz.pk/computer-all-in-ones"
                    }
                ]
            }
        ]
    },
    {
        "id": "Level_1_Category_No8",
        "name": "Electronic Accessories",
        "categories": [
            {
                "name": "Mobile Accessories",
                "link": "/www.daraz.pk/mobiles-tablets-accessories",
                "subcategories": [
                    {
                        "name": "Tablet Accessories",
                        "link": "/www.daraz.pk/accessories-tablet"
                    },
                    {
                        "name": "Cables & Converters",
                        "link": "/www.daraz.pk/other-phone-tablet-accessories"
                    },
                    {
                        "name": "Phone Cases",
                        "link": "/www.daraz.pk/mobile-cases-covers"
                    },
                    {
                        "name": "Car Mounts",
                        "link": "/www.daraz.pk/car-mounts"
                    },
                    {
                        "name": "Parts & Tools",
                        "link": "/www.daraz.pk/mobiles-tablets-parts-tools"
                    },
                    {
                        "name": "Screen Protectors",
                        "link": "/www.daraz.pk/mobile-surface-screen-protectors"
                    },
                    {
                        "name": "Power Banks",
                        "link": "/www.daraz.pk/mobile-power-banks"
                    },
                    {
                        "name": "Phone Camera Flash Lights",
                        "link": "/www.daraz.pk/phone-camera-flash-lights"
                    },
                    {
                        "name": "Wireless Chargers",
                        "link": "/www.daraz.pk/bluetooth-accessories"
                    },
                    {
                        "name": "Selfie Sticks",
                        "link": "/www.daraz.pk/selfie-sticks"
                    },
                    {
                        "name": "Car Chargers",
                        "link": "/www.daraz.pk/car-chargers"
                    },
                    {
                        "name": "Wall Chargers",
                        "link": "/www.daraz.pk/phone-tablet-chargers"
                    }
                ]
            },
            {
                "name": "Camera Accessories",
                "link": "/www.daraz.pk/camera-accessories",
                "subcategories": [
                    {
                        "name": "Gimbals & Stabilizers",
                        "link": "/www.daraz.pk/gimbals-stabilizer"
                    },
                    {
                        "name": "Action Camera Accessories",
                        "link": "/www.daraz.pk/sport-action-camera-accessories"
                    },
                    {
                        "name": "Lenses",
                        "link": "/www.daraz.pk/camera-lenses"
                    },
                    {
                        "name": "Tripods & Monopods",
                        "link": "/www.daraz.pk/tripods-monopods"
                    },
                    {
                        "name": "Memory Cards",
                        "link": "/www.daraz.pk/camera-memory-cards"
                    },
                    {
                        "name": "Batteries",
                        "link": "/www.daraz.pk/camera-batteries"
                    },
                    {
                        "name": "Lighting & Studio Equipment",
                        "link": "/www.daraz.pk/lighting-studio-equipment"
                    },
                    {
                        "name": "Camera Cases, Covers and Bags",
                        "link": "/www.daraz.pk/camera-bags"
                    }
                ]
            },
            {
                "name": "Wearable",
                "link": "/www.daraz.pk/wearable-technology",
                "subcategories": [
                    {
                        "name": "Fitness & Activity Trackers",
                        "link": "/www.daraz.pk/fitness-trackers"
                    },
                    {
                        "name": "Virtual Reality",
                        "link": "/www.daraz.pk/virtual-reality"
                    }
                ]
            },
            {
                "name": "Network Components",
                "link": "/www.daraz.pk/networking",
                "subcategories": [
                    {
                        "name": "Access Points",
                        "link": "/www.daraz.pk/access-points"
                    }
                ]
            },
            {
                "name": "Computer Components",
                "link": "/www.daraz.pk/components-spare-parts",
                "subcategories": [
                    {
                        "name": "Motherboards",
                        "link": "/www.daraz.pk/motherboard"
                    },
                    {
                        "name": "Processors",
                        "link": "/www.daraz.pk/processor"
                    },
                    {
                        "name": "Fans & Heatsinks",
                        "link": "/www.daraz.pk/fans-heatsinks"
                    },
                    {
                        "name": "Graphic Cards",
                        "link": "/www.daraz.pk/computer-graphic-cards"
                    },
                    {
                        "name": "Desktop Casings",
                        "link": "/www.daraz.pk/casing"
                    }
                ]
            },
            {
                "name": "Headphones & Headsets",
                "link": "/www.daraz.pk/headphones-headsets",
                "subcategories": [
                    {
                        "name": "Bluetooth Headsets",
                        "link": "/www.daraz.pk/audio-bluetooth-headsets"
                    },
                    {
                        "name": "Wired Headsets",
                        "link": "/www.daraz.pk/audio-wired-headsets"
                    },
                    {
                        "name": "In-Ear Headphones",
                        "link": "/www.daraz.pk/earphones-headsets"
                    },
                    {
                        "name": "Over-The-Ear Headphones",
                        "link": "/www.daraz.pk/over-the-ear-headphones"
                    },
                    {
                        "name": "Headphones & Headsets Access.",
                        "link": "/www.daraz.pk/headphones-headsets-accessories"
                    },
                    {
                        "name": "Wireless Earbuds",
                        "link": "/www.daraz.pk/wireless-earbuds"
                    },
                    {
                        "name": "Mono Headsets",
                        "link": "/www.daraz.pk/mono-headsets"
                    }
                ]
            },
            {
                "name": "Printers",
                "link": "/www.daraz.pk/multi-function-printers",
                "subcategories": [
                    {
                        "name": "Ink & Toners",
                        "link": "/www.daraz.pk/printer-ink"
                    },
                    {
                        "name": "Fax Machines",
                        "link": "/www.daraz.pk/fax-machines"
                    }
                ]
            },
            {
                "name": "Storage",
                "link": "/www.daraz.pk/computing-storage",
                "subcategories": [
                    {
                        "name": "Internal Hard Drives",
                        "link": "/www.daraz.pk/internal-hard-drives"
                    },
                    {
                        "name": "Storage for Mac",
                        "link": "/www.daraz.pk/storage-mac"
                    },
                    {
                        "name": "Flash Drives",
                        "link": "/www.daraz.pk/usb-flash-drives"
                    },
                    {
                        "name": "OTG Drives",
                        "link": "/www.daraz.pk/storage-otg-drives"
                    },
                    {
                        "name": "External Hard Drives",
                        "link": "/www.daraz.pk/external-hard-drives"
                    }
                ]
            },
            {
                "name": "Portable Speakers",
                "link": "/www.daraz.pk/portable-speakers"
            },
            {
                "name": "Gaming Accessories",
                "link": "/www.daraz.pk/gaming",
                "subcategories": [
                    {
                        "name": "Gaming Mouse",
                        "link": "/www.daraz.pk/gaming-mouse"
                    },
                    {
                        "name": "Gaming Keyboards",
                        "link": "/www.daraz.pk/gaming-keyboard"
                    },
                    {
                        "name": "Gaming Headsets",
                        "link": "/www.daraz.pk/gaming-headset"
                    }
                ]
            },
            {
                "name": "Monitors & Accessories",
                "link": "/www.daraz.pk/monitor-accessories"
            },
            {
                "name": "Computer Accessories",
                "link": "/www.daraz.pk/computing-peripherals-accessories",
                "subcategories": [
                    {
                        "name": "Mac Accessories",
                        "link": "/www.daraz.pk/mac-accessories"
                    },
                    {
                        "name": "Mouse",
                        "link": "/www.daraz.pk/mouse"
                    },
                    {
                        "name": "Adapters & Cables",
                        "link": "/www.daraz.pk/computer-adapters"
                    },
                    {
                        "name": "PC Audio",
                        "link": "/www.daraz.pk/pc-audio"
                    },
                    {
                        "name": "Cooling Pads/Cooling Stands",
                        "link": "/www.daraz.pk/other-computer-accessories"
                    },
                    {
                        "name": "Keyboards",
                        "link": "/www.daraz.pk/keyboard"
                    }
                ]
            }
        ]
    },
    {
        "id": "Level_1_Category_No9",
        "name": "TV & Home Appliances",
        "categories": [
            {
                "name": "Air Conditioner",
                "link": "/www.daraz.pk/air-conditioners"
            },
            {
                "name": "Washing Machine",
                "link": "/www.daraz.pk/washers-dryers"
            },
            {
                "name": "Refrigerators & Freezers",
                "link": "/www.daraz.pk/refrigerators",
                "subcategories": [
                    {
                        "name": "Freezers",
                        "link": "/www.daraz.pk/freezers"
                    }
                ]
            },
            {
                "name": "Cooling & Heating",
                "link": "/www.daraz.pk/cooling-heating",
                "subcategories": [
                    {
                        "name": "Air Cooler",
                        "link": "/www.daraz.pk/portable-ac"
                    },
                    {
                        "name": "Air Purifier",
                        "link": "/www.daraz.pk/air-purifiers"
                    },
                    {
                        "name": "Dehumidifier",
                        "link": "/www.daraz.pk/dehumidifiers"
                    },
                    {
                        "name": "Humidifier",
                        "link": "/www.daraz.pk/air-purifiers-humidifiers"
                    },
                    {
                        "name": "Fan",
                        "link": "/www.daraz.pk/fans"
                    },
                    {
                        "name": "Room Heater",
                        "link": "/www.daraz.pk/heaters"
                    },
                    {
                        "name": "Water Heater",
                        "link": "/www.daraz.pk/hot-water-systems"
                    }
                ]
            },
            {
                "name": "Irons & Garment Care",
                "link": "/www.daraz.pk/garment-care",
                "subcategories": [
                    {
                        "name": "Irons",
                        "link": "/www.daraz.pk/ironing-laundry-appliances"
                    },
                    {
                        "name": "Garment Steamer",
                        "link": "/www.daraz.pk/steam-iron-systems"
                    },
                    {
                        "name": "Sewing Machine",
                        "link": "/www.daraz.pk/sewing-machines"
                    }
                ]
            },
            {
                "name": "Vacuums & Floor Care",
                "link": "/www.daraz.pk/floorcare-appliances",
                "subcategories": [
                    {
                        "name": "Electric Brooms",
                        "link": "/www.daraz.pk/electric-brooms"
                    },
                    {
                        "name": "Steam Mops",
                        "link": "/www.daraz.pk/steam-mops"
                    },
                    {
                        "name": "Floor Polisher",
                        "link": "/www.daraz.pk/floor-polishers1"
                    },
                    {
                        "name": "Vacuum Cleaner",
                        "link": "/www.daraz.pk/vacuum-cleaners"
                    }
                ]
            },
            {
                "name": "Kitchen Appliances",
                "link": "/www.daraz.pk/home-appliances",
                "subcategories": [
                    {
                        "name": "Microwave",
                        "link": "/www.daraz.pk/microwaves"
                    },
                    {
                        "name": "Water Dispensers",
                        "link": "/www.daraz.pk/water-dispensers"
                    },
                    {
                        "name": "Dishwashers",
                        "link": "/www.daraz.pk/dishwashers-&-dryers"
                    },
                    {
                        "name": "Cooktop & Range",
                        "link": "/www.daraz.pk/cooktops-2"
                    },
                    {
                        "name": "Oven",
                        "link": "/www.daraz.pk/large-ovens"
                    },
                    {
                        "name": "Air & Deep Fryers",
                        "link": "/www.daraz.pk/fryers"
                    },
                    {
                        "name": "Specialty Cookware",
                        "link": "/www.daraz.pk/specialty-cookware-appliances"
                    },
                    {
                        "name": "Juicer & Fruit Extraction",
                        "link": "/www.daraz.pk/juicers"
                    },
                    {
                        "name": "Blender, Mixer & Grinder",
                        "link": "/www.daraz.pk/food-preparation"
                    },
                    {
                        "name": "Electric Kettle",
                        "link": "/www.daraz.pk/kettles"
                    },
                    {
                        "name": "Pressure Cookers",
                        "link": "/www.daraz.pk/pressure-cookers"
                    },
                    {
                        "name": "Rice Cooker",
                        "link": "/www.daraz.pk/rice-cookers"
                    }
                ]
            },
            {
                "name": "Home Audio & Theater",
                "link": "/www.daraz.pk/unuse-category-link-key-134",
                "subcategories": [
                    {
                        "name": "Soundbar Speakers",
                        "link": "/www.daraz.pk/sound-bars"
                    },
                    {
                        "name": "Live Sound & Stage Equipment",
                        "link": "/www.daraz.pk/live-sound-stage"
                    },
                    {
                        "name": "Home Entertainment",
                        "link": "/www.daraz.pk/audio-home-entertainment"
                    },
                    {
                        "name": "Home Theater Systems",
                        "link": "/www.daraz.pk/home-theater"
                    }
                ]
            },
            {
                "name": "Televisions",
                "link": "/www.daraz.pk/televisions",
                "subcategories": [
                    {
                        "name": "LED Televisions",
                        "link": "/www.daraz.pk/led-tvs"
                    },
                    {
                        "name": "Smart Televisions",
                        "link": "/www.daraz.pk/smart-tvs"
                    }
                ]
            },
            {
                "name": "Projectors & Players",
                "link": "/www.daraz.pk/%20tv_video",
                "subcategories": [
                    {
                        "name": "Projectors",
                        "link": "/www.daraz.pk/computing-projectors"
                    },
                    {
                        "name": "Blu Ray & DVD Players",
                        "link": "/www.daraz.pk/blu-ray-&-dvd-players"
                    }
                ]
            },
            {
                "name": "Generator, UPS & Solar",
                "link": "/www.daraz.pk/portable-power-supply",
                "subcategories": [
                    {
                        "name": "Solar Inverters",
                        "link": "/www.daraz.pk/solar-inverters"
                    },
                    {
                        "name": "Generators",
                        "link": "/www.daraz.pk/generators"
                    },
                    {
                        "name": "UPS",
                        "link": "/www.daraz.pk/ups-inverter"
                    }
                ]
            },
            {
                "name": "TV Accessories",
                "link": "/www.daraz.pk/tv-accessories",
                "subcategories": [
                    {
                        "name": "Antennas",
                        "link": "/www.daraz.pk/antennas"
                    },
                    {
                        "name": "TV Receivers",
                        "link": "/www.daraz.pk/tv-receivers"
                    },
                    {
                        "name": "Cables",
                        "link": "/www.daraz.pk/tv-cables"
                    },
                    {
                        "name": "3D Glasses",
                        "link": "/www.daraz.pk/3d-glasses"
                    },
                    {
                        "name": "TV Remote Controllers",
                        "link": "/www.daraz.pk/tv-remote-controllers"
                    },
                    {
                        "name": "Wall Mounts & Protectors",
                        "link": "/www.daraz.pk/projectors"
                    },
                    {
                        "name": "TV Adapters",
                        "link": "/www.daraz.pk/tv-adapters"
                    }
                ]
            }
        ]
    },
    {
        "id": "Level_1_Category_No10",
        "name": "Sports & Outdoor",
        "category": [
            {
                "name": "Sports & Outdoors",
                "link": "/www.daraz.pk",
                "subcategories": [
                    {
                        "name": "Racket Sports",
                        "link": "/www.daraz.pk/racket-sports",
                        "subcategories": [
                            {
                                "name": "Badminton",
                                "link": "/www.daraz.pk/badminton"
                            },
                            {
                                "name": "Tennis",
                                "link": "/www.daraz.pk/tennis"
                            },
                            {
                                "name": "Squash",
                                "link": "/www.daraz.pk/squash"
                            }
                        ]
                    },
                    {
                        "name": "Shoes & Clothing",
                        "link": "/www.daraz.pk/shoes-clothing",
                        "subcategories": [
                            {
                                "name": "Womens Shoes",
                                "link": "/www.daraz.pk/womens-sports-shoes"
                            },
                            {
                                "name": "Mens Shoes",
                                "link": "/www.daraz.pk/mens-sports-shoes"
                            },
                            {
                                "name": "Mens Clothing",
                                "link": "/www.daraz.pk/men-sports-clothing"
                            },
                            {
                                "name": "Womens Clothing",
                                "link": "/www.daraz.pk/women-sports-clothing"
                            },
                            {
                                "name": "Women Accessories",
                                "link": "/www.daraz.pk/women-sport-clothing-accessories"
                            },
                            {
                                "name": "Men Accessories",
                                "link": "/www.daraz.pk/men-sports-clothing-accessories"
                            },
                            {
                                "name": "Women Bags",
                                "link": "/www.daraz.pk/womens-sports-bags"
                            },
                            {
                                "name": "Men Bags",
                                "link": "/www.daraz.pk/mens-sports-bags"
                            }
                        ]
                    },
                    {
                        "name": "Sports Accessories",
                        "link": "/www.daraz.pk/sports-outdoors-accessories",
                        "subcategories": [
                            {
                                "name": "Water Bottles",
                                "link": "/www.daraz.pk/sports-water-bottles"
                            },
                            {
                                "name": "Home Gym",
                                "link": "/www.daraz.pk/home-gym"
                            }
                        ]
                    },
                    {
                        "name": "Fitness Gadgets",
                        "link": "/www.daraz.pk/fitness-gadgets",
                        "subcategories": [
                            {
                                "name": "Fitness Trackers",
                                "link": "/www.daraz.pk/fitness-trackers"
                            },
                            {
                                "name": "Fitness Trackers Accessories",
                                "link": "/www.daraz.pk/fitness-trackers-accessories"
                            }
                        ]
                    },
                    {
                        "name": "Outdoor Recreation",
                        "link": "/www.daraz.pk/outdoor-activities",
                        "subcategories": [
                            {
                                "name": "Fishing",
                                "link": "/www.daraz.pk/fishing"
                            },
                            {
                                "name": "Water Sports",
                                "link": "/www.daraz.pk/water-sports"
                            },
                            {
                                "name": "Skate Boards",
                                "link": "/www.daraz.pk/skateboarding"
                            },
                            {
                                "name": "Camping / Hiking",
                                "link": "/www.daraz.pk/camping-hiking"
                            },
                            {
                                "name": "Cycling",
                                "link": "/www.daraz.pk/bikes"
                            },
                            {
                                "name": "Cycle accessories",
                                "link": "/www.daraz.pk/cycling-accessories"
                            }
                        ]
                    },
                    {
                        "name": "Supplements",
                        "link": "/www.daraz.pk/sp-nutrition",
                        "subcategories": [
                            {
                                "name": "Fat Burners",
                                "link": "/www.daraz.pk/fat-burner"
                            },
                            {
                                "name": "Post Workouts and Recovery",
                                "link": "/www.daraz.pk/post-workout-supplements"
                            },
                            {
                                "name": "Pre Workouts",
                                "link": "/www.daraz.pk/pre-workout-supplements"
                            },
                            {
                                "name": "Proteins",
                                "link": "/www.daraz.pk/protein-supplements"
                            }
                        ]
                    },
                    {
                        "name": "Team Sports",
                        "link": "/www.daraz.pk/team-sports",
                        "subcategories": [
                            {
                                "name": "Baseballs",
                                "link": "/www.daraz.pk/sports-baseball"
                            },
                            {
                                "name": "Hockey",
                                "link": "/www.daraz.pk/sports-hockey"
                            },
                            {
                                "name": "Basket Ball",
                                "link": "/www.daraz.pk/sports-basketball"
                            },
                            {
                                "name": "Volley balls",
                                "link": "/www.daraz.pk/volleyball"
                            },
                            {
                                "name": "Cricket",
                                "link": "/www.daraz.pk/sports-cricket"
                            },
                            {
                                "name": "Football",
                                "link": "/www.daraz.pk/football"
                            }
                        ]
                    },
                    {
                        "name": "Exercise & Fitness",
                        "link": "/www.daraz.pk/exercise-fitness",
                        "subcategories": [
                            {
                                "name": "Fitness Accessories",
                                "link": "/www.daraz.pk/weights-accessories"
                            },
                            {
                                "name": "Treadmills",
                                "link": "/www.daraz.pk/treadmills"
                            },
                            {
                                "name": "Exercise Bikes",
                                "link": "/www.daraz.pk/exercise-bikes"
                            },
                            {
                                "name": "Boxing, Martial Arts & MMA",
                                "link": "/www.daraz.pk/boxing-martial-arts-mma"
                            },
                            {
                                "name": "Strength Training Equipments",
                                "link": "/www.daraz.pk/strength-training-equipment"
                            },
                            {
                                "name": "Weight",
                                "link": "/www.daraz.pk/weight-training"
                            },
                            {
                                "name": "Exercise Bands",
                                "link": "/www.daraz.pk/exercise-bands-accessories"
                            },
                            {
                                "name": "Cardio Training Equipment",
                                "link": "/www.daraz.pk/cardio-training-equipment"
                            },
                            {
                                "name": "Yoga",
                                "link": "/www.daraz.pk/yoga"
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "Level_1_Category_No11",
        "name": "Watches, Bags & Jewellery",
        "category": [
            {
                "name": "Watches & Accessories",
                "link": "/www.daraz.pk/watches-accessories",
                "subcategories": [
                    {
                        "name": "Women's Watches",
                        "link": "/www.daraz.pk/womens-watches",
                        "subcategories": [
                            {
                                "name": "Analog",
                                "link": "/www.daraz.pk/womens-casual-watches-wsj"
                            },
                            {
                                "name": "Digital",
                                "link": "/www.daraz.pk/womens-sports-watches-wsj"
                            },
                            {
                                "name": "Accessories",
                                "link": "/www.daraz.pk/womens-watch-accessories"
                            }
                        ]
                    }
                ]
            },
            {
                "name": "Men's Watches",
                "link": "/www.daraz.pk/mens-watches",
                "subcategories": [
                    {
                        "name": "Analog",
                        "link": "/www.daraz.pk/mens-digital"
                    },
                    {
                        "name": "Accessories",
                        "link": "/www.daraz.pk/mens-watch-accessories"
                    },
                    {
                        "name": "Digital",
                        "link": "/www.daraz.pk/mens-sports-watches"
                    },
                    {
                        "name": "Chronograph",
                        "link": "/www.daraz.pk/womens-fashion-watches-wsj"
                    },
                    {
                        "name": "Branded Watches",
                        "link": "/www.daraz.pk/mens-chronograph"
                    }
                ]
            },
            {
                "name": "Kid's Watches",
                "link": "/www.daraz.pk/kids-watches-wsj",
                "subcategories": [
                    {
                        "name": "Girls",
                        "link": "/www.daraz.pk/girls-watches"
                    },
                    {
                        "name": "Boys",
                        "link": "/www.daraz.pk/boys-watches"
                    }
                ]
            },
            {
                "name": "Mens Jewellery",
                "link": "/www.daraz.pk/mens-jewellery",
                "subcategories": [
                    {
                        "name": "Chains",
                        "link": "/www.daraz.pk/jewellery-necklaces-&-pendants-469"
                    },
                    {
                        "name": "Rings",
                        "link": "/www.daraz.pk/mens-rings"
                    },
                    {
                        "name": "Bracelets",
                        "link": "/www.daraz.pk/accessories-bracelets"
                    },
                    {
                        "name": "Studs",
                        "link": "/www.daraz.pk/jewellery-earrings-465"
                    }
                ]
            },
            {
                "name": "Womens Jewellery",
                "link": "/www.daraz.pk/womens-jewellery",
                "subcategories": [
                    {
                        "name": "Necklaces",
                        "link": "/www.daraz.pk/jewellery-necklaces-&-pendants-470"
                    },
                    {
                        "name": "Rings",
                        "link": "/www.daraz.pk/jewellery-rings-474"
                    },
                    {
                        "name": "Jewellery Sets",
                        "link": "/www.daraz.pk/jewellery-sets-&-others"
                    },
                    {
                        "name": "Anklets",
                        "link": "/www.daraz.pk/anklets"
                    },
                    {
                        "name": "Earrings",
                        "link": "/www.daraz.pk/jewellery-earrings-466"
                    },
                    {
                        "name": "Bracelets",
                        "link": "/www.daraz.pk/bracelets-&-bangles"
                    }
                ]
            },
            {
                "name": "Sunglasses & Eyewear",
                "link": "/www.daraz.pk/sunglasses",
                "subcategories": [
                    {
                        "name": "Lenses",
                        "link": "/www.daraz.pk/contact-lenses"
                    },
                    {
                        "name": "Men Sunglasses",
                        "link": "/www.daraz.pk/mens-sunglasses"
                    },
                    {
                        "name": "Women Sunglasses",
                        "link": "/www.daraz.pk/womens-sunglasses"
                    },
                    {
                        "name": "Kids Sunglasses",
                        "link": "/www.daraz.pk/kids-sunglasses"
                    },
                    {
                        "name": "Unisex Sunglasses",
                        "link": "/www.daraz.pk/unisex-sunglasses"
                    },
                    {
                        "name": "Men Eyeglasses",
                        "link": "/www.daraz.pk/mens-eyeglasses"
                    },
                    {
                        "name": "Kids Eyeglasses",
                        "link": "/www.daraz.pk/kids-eyewear"
                    },
                    {
                        "name": "Unisex Eyeglasses",
                        "link": "/www.daraz.pk/temporary-link-key-level4-12"
                    }
                ]
            },
            {
                "name": "Womens Bags",
                "link": "/www.daraz.pk/womens-bags",
                "subcategories": [
                    {
                        "name": "Wristlets",
                        "link": "/www.daraz.pk/bags-wristlets"
                    },
                    {
                        "name": "Wallets & Accessories",
                        "link": "/www.daraz.pk/wallets-accessories"
                    },
                    {
                        "name": "Clutches",
                        "link": "/www.daraz.pk/womens-clutch-bags"
                    },
                    {
                        "name": "Backpacks",
                        "link": "/www.daraz.pk/womens-backpacks"
                    },
                    {
                        "name": "Top-Handle Bags",
                        "link": "/www.daraz.pk/womens-office-digital"
                    },
                    {
                        "name": "Tote Bags",
                        "link": "/www.daraz.pk/tote-bags"
                    },
                    {
                        "name": "Cross Body & Shoulder Bags",
                        "link": "/www.daraz.pk/cross-body-shoulder-bags"
                    }
                ]
            },
            {
                "name": "Mens Bags",
                "link": "/www.daraz.pk/mens-bags",
                "subcategories": [
                    {
                        "name": "Backpacks",
                        "link": "/www.daraz.pk/men-bags-backpacks"
                    },
                    {
                        "name": "Crossbody Bags",
                        "link": "/www.daraz.pk/mens-formal-bags"
                    },
                    {
                        "name": "Messenger Bags",
                        "link": "/www.daraz.pk/men-messenger-bags"
                    },
                    {
                        "name": "Business Bags",
                        "link": "/www.daraz.pk/backpacks-and-briefcases"
                    },
                    {
                        "name": "Wallets & Cardholders",
                        "link": "/www.daraz.pk/mens-wallets-cardholders"
                    },
                    {
                        "name": "Cardholders & Keychains",
                        "link": "/www.daraz.pk/wallets-mens-card-holders"
                    }
                ]
            },
            {
                "name": "Luggage & Suitcase",
                "link": "/www.daraz.pk/catalog",
                "subcategories": [
                    {
                        "name": "Luggage",
                        "link": "/www.daraz.pk/luggage"
                    },
                    {
                        "name": "Laptop Bags",
                        "link": "/www.daraz.pk/laptop-bags-cover"
                    },
                    {
                        "name": "Travel Accessories",
                        "link": "/www.daraz.pk/travel-accessories"
                    }
                ]
            },
            {
                "name": "Women's Accessories",
                "link": "/www.daraz.pk/womens-accessories",
                "subcategories": [
                    {
                        "name": "Gloves",
                        "link": "/www.daraz.pk/womens-gloves"
                    },
                    {
                        "name": "Belts",
                        "link": "/www.daraz.pk/women-belts"
                    },
                    {
                        "name": "Hats & Caps",
                        "link": "/www.daraz.pk/womens-hats-caps-gloves"
                    }
                ]
            }
        ]
    },
    {
        "id": "Level_1_Category_No12",
        "name": "Automotive & Motorbike",
        "category": [
            {
                "name": "Loaders & Rickshaw",
                "link": "/www.daraz.pk/catalog",
                "subcategories": [
                    {
                        "name": "Loaders",
                        "link": "/www.daraz.pk/loaders"
                    },
                    {
                        "name": "Auto Rikshaw",
                        "link": "/www.daraz.pk/auto-rikshaw"
                    }
                ]
            },
            {
                "name": "Automotive",
                "link": "/www.daraz.pk/automotive",
                "subcategories": [
                    {
                        "name": "Car Tools & Equipment",
                        "link": "/www.daraz.pk/tools-equipment"
                    },
                    {
                        "name": "Car Tires & Wheels",
                        "link": "/www.daraz.pk/wheels-tires"
                    },
                    {
                        "name": "Car Oils & Fluids",
                        "link": "/www.daraz.pk/oils-fluids"
                    },
                    {
                        "name": "Car Care",
                        "link": "/www.daraz.pk/motors-car-care"
                    },
                    {
                        "name": "Car Exterior Accessories",
                        "link": "/www.daraz.pk/exterior-accessories"
                    },
                    {
                        "name": "Car Interior Accessories",
                        "link": "/www.daraz.pk/interior-accessories"
                    },
                    {
                        "name": "Car Safety & Security",
                        "link": "/www.daraz.pk/car-safety-security"
                    },
                    {
                        "name": "Car Electronics",
                        "link": "/www.daraz.pk/car-electronics-accessories"
                    },
                    {
                        "name": "Car Parts & Spares",
                        "link": "/www.daraz.pk/auto-parts-spares"
                    }
                ]
            },
            {
                "name": "Motorcycle",
                "link": "/www.daraz.pk/motorcycle",
                "subcategories": [
                    {
                        "name": "Motorcycle Helmets",
                        "link": "/www.daraz.pk/motorcycle-helmets"
                    },
                    {
                        "name": "Sports Bikes",
                        "link": "/www.daraz.pk/motorcycle-sportbikes"
                    },
                    {
                        "name": "Standard Bikes",
                        "link": "/www.daraz.pk/standard-bikes"
                    },
                    {
                        "name": "Electric Bikes",
                        "link": "/www.daraz.pk/electric-motor-bikes"
                    },
                    {
                        "name": "Motorcycle Parts & Spares",
                        "link": "/www.daraz.pk/motorcycle-parts-spares"
                    },
                    {
                        "name": "Motorcycle Oil & Fluids",
                        "link": "/www.daraz.pk/motorcycle-oils-fluids"
                    },
                    {
                        "name": "Riding Gear",
                        "link": "/www.daraz.pk/motorcycle-riding-gear"
                    },
                    {
                        "name": "Motorcycle Accessories",
                        "link": "/www.daraz.pk/motorcycle-exterior-accessories"
                    },
                    {
                        "name": "ATVs & UTVs",
                        "link": "/www.daraz.pk/atv-scooters"
                    },
                    {
                        "name": "Motorcycle Tires & Wheels",
                        "link": "/www.daraz.pk/moto-tires-wheels"
                    }
                ]
            }
        ]
    }
]
        for i in range(0, len(all_url_data)):
            name = all_url_data[i]['name']
            idofitem = all_url_data[i]['id']
            if "categories" in all_url_data[i]:
                for category in all_url_data[i]["categories"]:
                    if "subcategories" in category:
                        for subcategory in category["subcategories"]:
                            self.subcategory_links.append({
                                'name': name,
                                'id': idofitem,
                                'maincategory':category['name'], 
                                'subcategory' : subcategory['name'],
                                'url' : 'https:/' + subcategory['link'] + '/'})
                            
        if self.index2 < len(self.subcategory_links):
            yield Request(
                url=self.subcategory_links[self.index2]['url'],
                callback=self.parse_products,
                dont_filter=True,
                meta={
                    'category_data': self.subcategory_links[self.index2]
                }
            )

    def parse_products(self, response):
        self.driver.get(response.url)
        self.driver.implicitly_wait(0.30)
        
        try:
            html_page_content = self.driver.page_source
            self.logger.info("HTML successfully retrieved.")
        except Exception as e:
            self.logger.error(f"Error retrieving HTML: {e}")
            html_page_content = None
        if html_page_content is not None:
            selector = scrapy.Selector(text=html_page_content)
            all_product = selector.css('._17mcb .Bm3ON .Ms6aG .qmXQo')
            all_buttons = selector.css('.b7FXJ .e5J1n .ant-pagination')
            prev_button = all_buttons.css('.ant-pagination-prev::attr(aria-disabled)').get()
            next_button = all_buttons.css('.ant-pagination-next::attr(aria-disabled)').get()
            for products in all_product:
                product_url ='https:' + products.css('.ICdUp ._95X4G a::attr(href)').get()
                product_image = products.css('.ICdUp ._95X4G a .picture-wrapper img::attr(src)').get()
                product_title = products.css('.buTCk .RfADt a::text').get()
                product_price = products.css('.buTCk .aBrP0 span::text').get()
                sold_products= products.css('.buTCk ._6uN7R ._1cEkb span::text').get()
                rating_number = products.css('.buTCk ._6uN7R .mdmmT span::text').get()
                availability = products.css('.buTCk ._6uN7R .oa6ri::text').get()
                stars = products.css('.buTCk ._6uN7R .mdmmT .Dy1nx').getall()
                
                item_data = {
                    'url': product_url,
                    'img': product_image,
                    'title': product_title,
                    'price': product_price,
                    'sold': sold_products,
                    'comments': rating_number,
                    'stars': len(stars),
                    'availability': availability,
                    'main_link': response.url,
                    'category_data': [response.meta['category_data']],
                }
                
                yield Request(
                    url=product_url,
                    callback=self.parse_product_details,
                    dont_filter=True,
                    meta=item_data
                )
        
        if next_button == "false":
            self.index += 1
            new_link = response.meta['category_data']['url']+ '?page=' + str(self.index)
            yield Request(
            url=new_link,
            callback=self.parse_products,
            dont_filter=True,
            meta={
                'category_data': response.meta['category_data']
            }
            )
        else:
            self.index2 += 1
            self.index = 1
            self.all_data.clear()
            if self.index2 < len(self.subcategory_links):
                yield Request(
                    url=self.subcategory_links[self.index2]['url'],
                    callback=self.parse_products,
                    dont_filter=True,
                    meta={'category_data': self.subcategory_links[self.index2]}
            )
        

    def parse_product_details(self,response):
        ecom_item = EcomItem()
        ecom_item['img'] = response.meta.get('img')
        ecom_item['title'] = response.meta.get('title')
        ecom_item['price'] = response.meta.get('price')
        ecom_item['sold'] = response.meta.get('sold')
        ecom_item['comments'] = response.meta.get('rating')
        ecom_item['stars'] = response.meta.get('stars')
        ecom_item['availability'] = response.meta.get('availability')
        ecom_item['main_link'] = response.meta.get('main_link')
        ecom_item['category_data'] = response.meta.get('category_data')
        self.driver.get(response.url)
        self.driver.execute_script("window.scrollBy(0, 500);")
        self.driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(3)
        try:
            html_page_content = self.driver.page_source
            self.logger.info("HTML successfully retrieved.")
        except Exception as e:
            self.logger.error(f"Error retrieving HTML: {e}")
            html_page_content = None
        if html_page_content is not None:
            selector = scrapy.Selector(text=html_page_content)
            ecom_item['product_description'] = selector.xpath("//div[@class='html-content pdp-product-highlights']//ul/li/text()").getall()
            ecom_item['product_desc'] = selector.xpath("//div[@class='html-content detail-content']/p/text()").get()
            ecom_item['sku'] = selector.xpath("//ul[@class='specification-keys']//li[span[contains(text(), 'SKU')]]/div[@class='key-value']/text()").get()
            ecom_item['brand_name'] = selector.xpath("//div[@class='pdp-product-brand']//a[@class='pdp-link pdp-link_size_s pdp-link_theme_blue pdp-product-brand__brand-link']/text()").get()
            images_list = selector.css("#root #block-1zS9PxaSTs #block-7J1Jvz6odp #module_item_gallery_1 .item-gallery .item-gallery-slider .next-slick-inner .next-slick-list .next-slick-track .next-slick-slide")
            color_image_url = selector.xpath('//div[@class="sku-prop"][.//h6[text()="Color Family"]]//img[@class="image"]/@src').getall()
            ecom_item['disount_price'] = selector.xpath("//div[@class='pdp-product-price']//span[@class='pdp-product-price__discount']/text()").get()
            rating_score = selector.xpath("//div[@class='mod-rating']//div[@class='score']//span[@class='score-average']/text()").get()
            try:
                rating_score = float(rating_score) if rating_score else None
            except ValueError:
                rating_score = None
            total_score = selector.xpath("//div[@class='mod-rating']//div[@class='count']/text()").get()
            try:
                total_score = float(total_score.replace(" Ratings",'')) if total_score else None
            except ValueError:
                total_score = None
            fivestar = selector.xpath("//div[@class='mod-rating']//li[1]//span[@class='percent']/text()").get()
            try:
                fivestar= float(fivestar) if fivestar else None
            except ValueError:
                fivestar = None
            fourstar = selector.xpath("//div[@class='mod-rating']//li[2]//span[@class='percent']/text()").get()
            try:
                fourstar= float(fourstar) if fourstar else None
            except ValueError:
                fourstar = None
            threestar = selector.xpath("//div[@class='mod-rating']//li[3]//span[@class='percent']/text()").get()
            try:
                threestar= float(threestar) if threestar else None
            except ValueError:
                threestar = None
            twostar = selector.xpath("//div[@class='mod-rating']//li[4]//span[@class='percent']/text()").get()
            try:
                twostar= float(twostar) if twostar else None
            except ValueError:
                twostar = None
            onestar = selector.xpath("//div[@class='mod-rating']//li[5]//span[@class='percent']/text()").get()
            try:
                onestar= float(onestar) if onestar else None
            except ValueError:
                onestar = None
            fivewidth = selector.xpath("//div[@class='mod-rating']//li[1]//div[@class='pdp-review-progress']//div[@class='bar fg']/@style").get()
            try:
                fivewidth= float(fivewidth.replace("width: ",'').replace("%;",''))/100 if fivewidth else None
            except ValueError:
                fivewidth = None
            fourwidth = selector.xpath("//div[@class='mod-rating']//li[2]//div[@class='pdp-review-progress']//div[@class='bar fg']/@style").get()
            try:
                fourwidth= float(fourwidth.replace("width: ",'').replace("%;",''))/100 if fourwidth else None
            except ValueError:
                fourwidth = None
            threewidth = selector.xpath("//div[@class='mod-rating']//li[3]//div[@class='pdp-review-progress']//div[@class='bar fg']/@style").get()
            try:
                threewidth= float(threewidth.replace("width: ",'').replace("%;",''))/100 if threewidth else None
            except ValueError:
                threewidth = None
            twowidth = selector.xpath("//div[@class='mod-rating']//li[4]//div[@class='pdp-review-progress']//div[@class='bar fg']/@style").get()
            try:
                twowidth= float(twowidth.replace("width: ",'').replace("%;",''))/100 if twowidth else None
            except ValueError:
                twowidth = None
            onewidth = selector.xpath("//div[@class='mod-rating']//li[5]//div[@class='pdp-review-progress']//div[@class='bar fg']/@style").get()
            try:
                onewidth= float(onewidth.replace("width: ",'').replace("%;",''))/100 if onewidth else None
            except ValueError:
                onewidth = None
            self.images_url = []
            for image in images_list:
                image_url = image.css('.next-slick-slide .item-gallery__image-wrapper img::attr(src)').get()
                if image_url:
                    self.images_url.append(image_url)
            ecom_item['image_list'] = self.images_url
            ratings = selector.xpath("//div[@id='module_seller_info']/div[@class='seller-container']/div[@class='pdp-seller-info-pc']/div[@class='info-content']")
            ecom_item['positive_rating'] = ratings[0].css('.seller-info-value::text').get() if ratings[0] else None
            ecom_item['ship_on_time'] = ratings[1].css('.seller-info-value::text').get() if ratings[1] else None
            ecom_item['response_time'] = ratings[2].css('.seller-info-value::text').get() if ratings[2] else None
            ecom_item['delivery_location'] = selector.xpath("//div[@class='delivery__header']/div/div/div/div[@class='location__address']/text()").get()
            ecom_item['delivery_content'] = selector.xpath("//div[@class='delivery__content']/div/div/div/div/div[@class='delivery-option-item__info']/div/text()").get()
            ecom_item['out_of_stock'] = selector.xpath('//div[@class="sku-quantity-selection"]//span[@class="quantity-content-default"]/text()').get()
            ecom_item['return_policy'] = selector.xpath("//div[@class='warranty__option-item']//div[@class='delivery-option-item__title']/text()")[0].get()
            ecom_item['warranty_info'] = selector.xpath("//div[@class='warranty__option-item']//div[@class='delivery-option-item__title']/text()")[1].get()
            ecom_item['color_image_url']= color_image_url
            ecom_item['rating_data'] = {
                "rating_score": rating_score,
                "total_ratings": total_score,
                "star_rating_breakdown": {
                    "5_star_percent": fivestar,
                    "4_star_percent": fourstar,
                    "3_star_percent": threestar,
                    "2_star_percent": twostar,
                    "1_star_percent": onestar,
                },
                "star_rating_progress": {
                    "5_star_bar_width": fivewidth,
                    "4_star_bar_width": fourwidth,
                    "3_star_bar_width": threewidth,
                    "2_star_bar_width": twowidth,
                    "1_star_bar_width": onewidth,
                }
            }

        yield ecom_item