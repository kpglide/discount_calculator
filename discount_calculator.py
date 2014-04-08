class Discount_Calculator(object):

	def calculate_discount(self, cart_amount, discount_amount, discount_type):
		
		if type(cart_amount) != int and type(cart_amount) != float:
			raise ValueError
		elif type(discount_amount) != int and type(discount_amount) != float:
			raise ValueError
		
		elif discount_type == 'percent':
			if discount_amount > 100:
				raise ValueError('Percentage must be 100 or less')
			else: 
				discount = (discount_amount / 100.0) * cart_amount
		
		elif discount_type == 'absolute':
			if discount_amount > cart_amount:
				raise ValueError('Discount cannot exceed cart total')
			else:
				discount = discount_amount
		
		else: raise ValueError('Invalid discount type')
		
		return discount
