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
              order_count, 
              delivery_discount_applicable, 
              cart_sum_threshold, 
              first_order_discount_applicable, 
              first_order_discount_value):
    self.name = name
    self.price = price
    self.quantity = quantity
    self.regular_delivery_fee = regular_delivery_fee
    self.order_count = order_count
    self.delivery_discount_applicable = delivery_discount_applicable  
    self.cart_sum_threshold = cart_sum_threshold
    self.first_order_discount_applicable = first_order_discount_applicable
    self.first_order_discount_value = first_order_discount_value

  def cart_sum(self):
    return self.price * self.quantity

  def delivery_fee(self):
    if self.delivery_discount_applicable and self.cart_sum() > self.cart_sum_threshold:
      return 0
    else:
      return self.regular_delivery_fee

  def order_sum(self):
      return self.cart_sum() + self.delivery_fee()

  def deal_price(self):
    if self.first_order_discount_applicable and self.order_count == 1:
      return self.order_sum() - self.first_order_discount_value
    else:
      return self.order_sum()


S1 = Store(**store1)
print(S1.deal_price())


