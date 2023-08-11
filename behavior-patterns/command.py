from abc import ABC, abstractclassmethod


class Light:
	def lightOn(self):
		print('The light is on')
	
	def lightOff(self):
		print('The light is off')

class Command(ABC):

	@abstractclassmethod
	def execute(self):
		pass


class LightOnCommand(Command):
	def __init__(self, light):
		self.light = light

	def execute(self):
		self.light.lightOn()


class LightOffCommand(Command):
	def __init__(self, light):
		self.light = light
	
	def execute(self):
		self.light.lightOff()
		

class Invoker:
	def __init__(self):
		self.command = {}
		self.history = []

	def setCommand(self, commandStr, command):
		self.command[commandStr] = command

	def execute(self, commandStr):
		if commandStr in self.command:
			self.history.append(commandStr)
			self.command[commandStr].execute()
		else:
			print('Invalid command')

	def undo(self):
		print(f'Command history: {self.history}')
		if len(self.history) > 0:
			self.history.pop()
		else:
			print('history empty')
		

if __name__ == '__main__':
	light = Light()
	invoker = Invoker()
	invoker.setCommand('on', LightOnCommand(light))
	invoker.setCommand('off', LightOffCommand(light))

	print('Light is off')
	invoker.execute('on')
	invoker.execute('off')
	invoker.execute('on')
	invoker.execute('off')
	invoker.execute('on')

	# undo
	invoker.undo()
	invoker.undo()
	invoker.undo()

	

