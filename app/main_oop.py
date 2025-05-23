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

class DiscountStrategy:
  def apply_discount(self, store):
    return 0
  # add s string representation of the class
  def __str__(self):
    return self.__class__.__name__

class DeliveryDiscountStrategy(DiscountStrategy):
  def apply_discount(self, store):
    if store.delivery_discount_applicable and store.cart_sum() > store.cart_sum_threshold:
      return store.regular_delivery_fee #the discount is the delivery fee
    else:
      return 0 #elso - no discount, diminished by 0

class FirstOrderDiscountStrategy(DiscountStrategy):
  def apply_discount(self, store):
    if store.first_order_discount_applicable and store.order_count == 1:
      return store.first_order_discount_value #the discount is the first order discount value
    return 0 #elso - no discount, diminished by 0

class Store:
  def __init__(self, 
              name, 
              price, 
              quantity, 
              regular_delivery_fee,
              order_count = None,
              delivery_discount_applicable = False,
              cart_sum_threshold = None,
              first_order_discount_applicable = False,
              first_order_discount_value = None,
              **kwargs):
    self.name = name
    self.price = price
    self.quantity = quantity
    self.regular_delivery_fee = regular_delivery_fee
    self.order_count = order_count
    self.delivery_discount_applicable = delivery_discount_applicable
    self.cart_sum_threshold = cart_sum_threshold
    self.first_order_discount_applicable = first_order_discount_applicable
    self.first_order_discount_value = first_order_discount_value
    self.delivery_discount_strategy = DeliveryDiscountStrategy()
    self.first_order_discount_strategy = FirstOrderDiscountStrategy()
    self.discount_strategies = self.initialize_discount_strategies()

  def initialize_discount_strategies(self):
    strategies = []
    if self.delivery_discount_applicable:
      strategies.append(DeliveryDiscountStrategy())
    if self.first_order_discount_applicable:
      strategies.append(FirstOrderDiscountStrategy())
    return strategies

  def cart_sum(self):
    return self.price * self.quantity

  def delivery_fee(self):
      return self.regular_delivery_fee -self.delivery_discount_strategy.apply_discount(self)

  def order_sum(self):
      return self.cart_sum() + self.delivery_fee()

  def deal_price(self):
      return self.order_sum() - self.first_order_discount_strategy.apply_discount(self)
  
S1 = Store(**store1)
print(*S1.discount_strategies)
print(S1.deal_price())
