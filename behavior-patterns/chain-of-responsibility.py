from abc import ABC, abstractmethod


class Handler(ABC):
	@abstractmethod
	def setNext(self, handler):
		pass

	@abstractmethod
	def handle(self, request: int):
		pass
	

class BaseHandler(Handler):
	_nextHandler = None

	def setNext(self, handler):
		self._nextHandler = handler
		return handler

	@abstractmethod
	def handle(self, request: int):
		if self._nextHandler:
			self._nextHandler.handle(request)


class PositiveHandler(BaseHandler):
	def handle(self, request: int):
		if request > 0:
			print(f'PositiveHandler: Handling request {request}')
		else:
			self._nextHandler.handle(request)

class NegativeHandler(BaseHandler):
	def handle(self, request: int):
		if request < 0:
			print(f'NegativeHandler: Handling request {request}')
		else:
			self._nextHandler.handle(request)
	
class ZeroHandler(BaseHandler):
	def handle(self, request: int):
		if request == 0:
			print(f'ZeroHandler: Handling request {request}')
		else:
			self._nextHandler.handle(request)



if __name__ == "__main__":

	positiveHandler = PositiveHandler()
	negativeHandler = NegativeHandler()
	zeroHandler = ZeroHandler()

	positiveHandler.setNext(negativeHandler).setNext(zeroHandler)

	for i in range(-2, 3, 1):
		print(i)
		print('-------------------')
		positiveHandler.handle(i)