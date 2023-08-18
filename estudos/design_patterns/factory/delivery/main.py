from abc import ABC, abstractmethod

class DeliveryService():

	def __init__(self, frozen=False):
		self.frozen = frozen

	@abstractmethod
	def deliver_product(self):
		pass

	def factory_method(self):

		if self.frozen:
			return FrozenDeliveryService()
		else:
			return NonFrozenDeliveryService()

	def delivery_operation(self):
		service = self.factory_method()

		service.deliver_product()

class FrozenDeliveryService(DeliveryService):

	def deliver_product(self):

		print("Client wants delivery of frozen product")
		FrozenProduct().operation()
		print("Delivering frozen product")
		
class NonFrozenDeliveryService(DeliveryService):

	def deliver_product(self):

		print("Client wants delivery of non frozen product")
		NonFrozenProduct().operation()
		print("Delivering non-frozen product")

class Product(ABC):

	@abstractmethod
	def operation(self):
		pass

class FrozenProduct(Product):

	def operation(self):
		print("This is a frozen product")

class NonFrozenProduct(Product):

	def operation(self):
		print("This is a non-frozen product")

if __name__ == '__main__':

	delivery = DeliveryService(frozen=True)
	delivery.delivery_operation()
	delivery = DeliveryService(frozen=False)
	delivery.delivery_operation()