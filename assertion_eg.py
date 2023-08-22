'''
1.Never use it for data validation
2.Asserts that never fail
'''


def apply_discount(product,discount):
    discounted_price = product['price']*discount
    assert 0 < discounted_price < product['price'] , "Wrong discount added"
    return discounted_price

shoes = { 'name' : 'fancy shoes' , 'price' : 15487}
print(apply_discount(shoes,0.2))
print(apply_discount(shoes,2))