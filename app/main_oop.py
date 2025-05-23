#!/usr/bin/env python3

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

class Store:
  def __init__(self, 
              name, 
              price, 
              quantity, 
              regular_delivery_fee,
              **kwargs):
    self.name = name
    self.price = price
    self.quantity = quantity
    self.regular_delivery_fee = regular_delivery_fee

  def cart_sum(self):
    return self.price * self.quantity

  def delivery_fee(self):
      return self.regular_delivery_fee

  def order_sum(self):
      return self.cart_sum() + self.delivery_fee()

  def deal_price(self):
      return self.order_sum()
  
  # call class factory manually
  # S1 = Store.store_subclasses_factory(store1)
  @staticmethod
  def store_subclasses_factory(store_dict):
    """
    This method creates a subclass of Store based on the store_dict keys.
    """
    if store_dict.get('delivery_discount_applicable') is True:
      return DeliveryDiscount(**store_dict)
    elif store_dict.get('first_order_discount_applicable') is True:
      return FirstOrderDiscount(**store_dict)
    else:
      return NoDiscount(**store_dict)


class NoDiscount(Store):
  '''
  Use basic calculation logic
  '''
  pass

class DeliveryDiscount(Store):
  '''
  Apply delivery discount
  '''
  def __init__(self,
              delivery_discount_applicable,
              cart_sum_threshold,
              **kwargs):
    super().__init__(**kwargs)
    self.delivery_discount_applicable = delivery_discount_applicable
    self.cart_sum_threshold = cart_sum_threshold
  
  def delivery_fee(self):
    if self.delivery_discount_applicable and self.cart_sum() > self.cart_sum_threshold:
      return 0
    else:
      return self.regular_delivery_fee

class FirstOrderDiscount(Store):
  '''
  Apply first order discount logic
  '''
  def __init__(self,
              first_order_discount_applicable,
              first_order_discount_value,
              order_count,
              **kwargs):
    super().__init__(**kwargs)
    self.first_order_discount_applicable = first_order_discount_applicable
    self.first_order_discount_value = first_order_discount_value
    self.order_count = order_count

def deal_price(self):
  if self.first_order_discount_applicable and self.order_count == 1:
    return self.order_sum() - self.first_order_discount_value
  else:
    return self.order_sum()


S1 = Store.store_subclasses_factory(store1)
print(S1.deal_price())


