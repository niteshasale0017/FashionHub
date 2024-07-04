from django import template
register = template.Library()

@register.filter(name="create_id")
def create_id(pro,second):
    return str(pro.id) + second
    print(str(pro.id) + second)

@register.filter(name="product_price")
def product_price(pro):
    pro = pro.price-pro.discount/100*pro.price
    return '₹'+str(int(pro))
