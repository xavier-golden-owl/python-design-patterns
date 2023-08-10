from abc import ABC, abstractmethod

# abstract class
class Button(ABC):
	@abstractmethod
	def render(self):
		pass

	@abstractmethod
	def click(self):
		pass


# concrete class
class WindowsButton(Button):
	def render(self):
		print("Windows Button")

	def click(self):
		print("Windows Button clicked")

# concrete class
class MacButton(Button):
	def render(self):
		print("Mac Button")

	def click(self):
		print("Mac Button clicked")
	

# creator
class Dialog(ABC):
	# factory method
	@abstractmethod
	def createButton(self) -> Button:
		pass

	def render(self):
		pass

class WindowsDialog(Dialog):
	def createButton(self) -> Button:
		return WindowsButton()

class MacDialog(Dialog):
	def createButton(self) -> Button:
		return MacButton()

if __name__ == "__main__":

	dialog_type = input("Windows or Mac? ")

	if dialog_type == "Windows":
		dialog = WindowsDialog()
	elif dialog_type == "Mac":
		dialog = MacDialog()

	button = dialog.createButton()
	button.render()
	button.click()