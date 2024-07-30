# data.py

import random

def generate_random_data():
    names = [
        "Microsoft", "Apple iPhone Pro Max 15", "Amazon Web Services", "Google Search",
        "Tesla Model S", "Facebook", "Netflix Streaming Service", "Samsung Galaxy S21",
        "IBM Cloud", "Intel Processors", "Nike Shoes", "Adidas Sportswear",
        "Sony PlayStation 5", "Microsoft Office 365", "Slack", "Zoom Video Communications",
        "Dropbox", "Spotify Music Service", "Uber Ridesharing", "Lyft", "Airbnb", "Twitter",
        "LinkedIn", "Pinterest", "Salesforce CRM", "Oracle Database", "SAP ERP",
        "Dell Laptops", "HP Printers", "Cisco Networking", "AMD Graphics Cards", "NVIDIA GPUs",
        "Asus Motherboards", "LG Televisions", "Panasonic Home Appliances", "Bose Audio Systems",
        "JBL Speakers", "Canon Cameras", "GoPro Action Cameras", "Fitbit Fitness Trackers",
        "Garmin GPS Devices", "Nest Smart Home", "Ring Doorbell", "Philips Hue Lighting",
        "Sony Headphones", "Beats by Dre", "Xiaomi Smartphones", "OnePlus Phones",
        "Huawei Technologies", "Pepsi", "Coca-Cola", "McDonald's", "Burger King",
        "KFC", "Starbucks", "Subway", "Domino's Pizza", "Pizza Hut", "Taco Bell",
        "Chick-fil-A", "Wendy's", "Dunkin'", "Panera Bread", "Chipotle",
        "Sonic Drive-In", "Little Caesars", "Panda Express", "Five Guys", "Arby's",
        "Jack in the Box", "Papa John's Pizza", "Zaxby's", "Wingstop", "In-N-Out Burger",
        "Buffalo Wild Wings", "Baskin-Robbins", "Cold Stone Creamery", "Dairy Queen",
        "Krispy Kreme", "Ben & Jerry's", "Häagen-Dazs", "Einstein Bros. Bagels", "Caribou Coffee",
        "The Coffee Bean & Tea Leaf", "Peet's Coffee", "Tim Hortons", "Pret A Manger", "D'Angelo Grilled Sandwiches",
        "Taco John's", "El Pollo Loco", "Moe's Southwest Grill", "Del Taco", "Qdoba Mexican Eats",
        "Boston Market", "Blaze Pizza", "MOD Pizza", "Marco's Pizza", "Cicis Pizza",
        "California Pizza Kitchen", "Papa Murphy's", "Schlotzsky's", "Jersey Mike's Subs",
        "Jimmy John's", "Firehouse Subs", "Potbelly Sandwich Shop", "Which Wich", "McAlister's Deli",
        "Jason's Deli", "Sweetgreen", "Just Salad", "Chopt Creative Salad Co.", "Saladworks",
        "Freshii", "Einstein Bagels", "Bruegger's Bagels", "La Madeleine",
        "Au Bon Pain", "Corner Bakery Café", "Zoe's Kitchen", "Le Pain Quotidien", "Boudin Bakery",
        "Hale and Hearty Soups", "Soup Kitchen International", "Cosi", "Gourmet Garage",
        "Balducci's", "Dean & DeLuca", "Trader Joe's", "Whole Foods Market", "Wegmans",
        "Safeway", "Kroger", "Albertsons", "Publix", "WinCo Foods", "Meijer", "H-E-B",
        "Hy-Vee", "Sprouts Farmers Market", "Fresh Thyme Farmers Market", "The Fresh Market",
        "Natural Grocers", "New Seasons Market", "Earth Fare", "Lucky's Market", "Sunflower Farmers Market",
        "Amazon Fresh", "Walmart", "Target", "Costco", "Sam's Club", "BJ's Wholesale Club",
        "Aldi", "Lidl", "Save-A-Lot", "Dollar General", "Family Dollar", "Dollar Tree",
        "Big Lots", "Five Below", "Ollie's Bargain Outlet", "Ross Dress for Less", "T.J. Maxx",
        "Marshalls", "HomeGoods", "Sierra Trading Post", "At Home", "Bed Bath & Beyond",
        "The Container Store", "IKEA", "Wayfair", "Ashley HomeStore", "Rooms To Go",
        "American Signature Furniture", "Bob's Discount Furniture", "Havertys Furniture", "Crate & Barrel",
        "Pottery Barn", "West Elm", "CB2", "Restoration Hardware", "Williams-Sonoma", "Sur La Table",
        "Pier 1 Imports", "World Market", "Cost Plus World Market", "Banana Republic", "Gap",
        "Old Navy", "Athleta", "H&M", "Zara", "Uniqlo", "Forever 21", "American Eagle Outfitters",
        "Aerie", "Hollister", "Abercrombie & Fitch", "Express", "New York & Company", "Ann Taylor",
        "LOFT", "Lane Bryant", "Torrid", "Hot Topic", "Urban Outfitters", "Anthropologie",
        "Free People", "Madewell", "J.Crew", "J.Jill", "Talbots", "Chico's", "White House Black Market",
        "Soma Intimates", "Victoria's Secret", "PINK", "Bath & Body Works", "L Brands", "The Body Shop",
        "Lush", "Sephora", "Ulta Beauty", "Macy's", "Nordstrom", "Neiman Marcus", "Saks Fifth Avenue",
        "Bloomingdale's", "Dillard's", "Lord & Taylor", "JCPenney", "Kohl's", "Belk",
        "Bealls", "Stage Stores", "Gordmans", "Bon-Ton", "Boscov's", "Carson's", "Herberger's",
        "Younkers", "Harris Teeter", "ShopRite", "Food Lion", "Winn-Dixie", "Piggly Wiggly",
        "Ingles Markets", "Giant Eagle", "Stop & Shop", "King Soopers", "Fry's Food Stores",
        "QFC", "Smith's Food & Drug", "Ralphs", "Food 4 Less", "Fred Meyer"
    ]
    types = ["Company", "Product", "Service"]
    data = []

    for i in range(400):
        name = f"{random.choice(names)}"
        data_type = random.choice(types)
        ethics_index = random.randint(50, 100)
        sustainable = random.choice([True, False])
        data.append({
            "name": name,
            "type": data_type,
            "ethics_index": ethics_index,
            "sustainable": sustainable
        })

    return data


companies_services_products = generate_random_data()
