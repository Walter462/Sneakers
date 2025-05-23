#=========
# DATA
#=========
store1 = {
  'name':'Store1', 
  'price':97.89,
  'quantity':1,
  'regular_delivery_fee': 3.16,
  'order_count': 1,
  'delivery_discount_applicable': True,
  'cart_sum_threshold': 105.26,
  'first_order_discount_applicable': False,
  'first_order_discount_value': None
}

def deal_price(store_copy: dict)->dict:
  """
  Calculates the following keys to the returned dict:
    - 'cart_sum'
    - 'delivery_fee'
    - 'order_sum'
    - 'deal_price'
  The returned dict contains all original keys plus these.
  """
  store_copy = order_sum(store_copy)
  if store_copy['first_order_discount_applicable'] is True and store_copy['order_count']==1:
    store_copy['deal_price'] = store_copy['order_sum'] - store_copy['first_order_discount_value'] #10.53
    return store_copy
  else:
    store_copy['deal_price'] = store_copy['order_sum']
    return store_copy

def order_sum(store_copy: dict)->dict:
  """
  Calculates the following keys to the returned dict:
    - 'cart_sum'
    - 'delivery_fee'
    - 'order_sum'
  The returned dict contains all original keys plus these.
  """
  store_copy = delivery_fee(store_copy)
  store_copy['order_sum'] = store_copy['delivery_fee'] + store_copy['cart_sum']
  return store_copy

def delivery_fee(store_copy: dict)->dict:
  """
  Calculates the following keys to the returned dict:
    - 'cart_sum'
    - 'delivery_fee'
  The returned dict contains all original keys plus these.
  """
  store_copy = cart_sum(store_copy)
  if store_copy['delivery_discount_applicable'] is True and store_copy['cart_sum'] > store_copy['cart_sum_threshold']: # 105.26
    store_copy['delivery_fee'] = 0
    return store_copy
  else:
    store_copy['delivery_fee'] = store_copy['regular_delivery_fee']
    return store_copy

def cart_sum(store: dict)->dict:
  """
  Calculates the following keys to the returned dict:
    - 'cart_sum'
  The returned dict contains all original keys plus this.
  """
  store_copy = store.copy()   
  cart_sum = 0
  cart_sum = store['price'] * store['quantity']
  store_copy['cart_sum'] = cart_sum
  return store_copy

print(cart_sum(store1))

