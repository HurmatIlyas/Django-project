from MyApp.models import Product


def products_category(category):
    all_products = Product.objects.filter(category=category)
    products = []
    for product in all_products:
        product_dict = {}
        product_dict['brand'] = product.brand
        product_dict['care'] = product.care
        product_dict['category'] = product.category
        product_dict['currency'] = product.currency
        product_dict['description'] = product.description
        product_dict['image_urls'] = eval(product.image_urls)
        product_dict['lang'] = product.lang
        product_dict['name'] = product.name
        product_dict['price'] = product.price
        product_dict['retailer_sku'] = product.retailer_sku
        product_dict['skus'] = eval(product.skus)
        product_dict['url'] = product.url
        product_dict['trail'] = product.trail
        products.append(product_dict)

    return products


def product(retailer_sku):
    all_products = Product.objects.filter(retailer_sku=retailer_sku)
    products = []
    for product in all_products:
        product_dict = {}
        product_dict['brand'] = product.brand
        product_dict['care'] = product.care
        product_dict['category'] = product.category
        product_dict['currency'] = product.currency
        product_dict['description'] = product.description
        product_dict['image_urls'] = eval(product.image_urls)
        product_dict['lang'] = product.lang
        product_dict['name'] = product.name
        product_dict['price'] = product.price
        product_dict['retailer_sku'] = product.retailer_sku
        product_dict['skus'] = eval(product.skus)
        product_dict['url'] = product.url
        product_dict['trail'] = product.trail
        products.append(product_dict)

    return products


def products():
    all_products = Product.objects.all()
    products = []
    for product in all_products:
        product_dict = {}
        product_dict['brand'] = product.brand
        product_dict['care'] = product.care
        product_dict['category'] = product.category
        product_dict['currency'] = product.currency
        product_dict['description'] = product.description
        product_dict['image_urls'] = eval(product.image_urls)
        product_dict['lang'] = product.lang
        product_dict['name'] = product.name
        product_dict['price'] = product.price
        product_dict['retailer_sku'] = product.retailer_sku
        product_dict['skus'] = eval(product.skus)
        product_dict['url'] = product.url
        product_dict['trail'] = product.trail
        products.append(product_dict)

    return products
