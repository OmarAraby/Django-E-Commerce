from product.models import Product

class Cart():
	def __init__(self,request):
		self.session = request.session


		# Get the cuurent session Key if it exists

		cart = self.session.get('session_key')


		# if USer is New , No Session key , create one

		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}



		# Making Sure that cart is available on all pages of site

		self.cart = cart


	def add(self,product):
		product_id = str(product.id)

		## Logic

		if product_id in self.cart:
			pass

		else:
			self.cart[product_id] = {'price':str(product.PRDPrice)}


		self.session.modified = True



	# Count anything in the cart

	def __len__(self):
		return len(self.cart)


	def get_prods(self):
		# Get ids from cart
		product_id = self.cart.keys()

		# Use ids to lookup product in database model

		products = Product.objects.filter(id__in=product_id)

		return products





