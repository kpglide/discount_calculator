class Discount_Calculator(object):

	def calculate_discount(self, cart_amount, discount_amount, typ):
		if type(cart_amount) != int and type(cart_amount) != float:
			raise ValueError
		elif type(discount_amount) != int and type(discount_amount) != float:
			raise ValueError
		elif typ == 'percent':
			discount = (discount_amount / 100.0) * cart_amount
		else:
			discount = discount_amount
		return discount
