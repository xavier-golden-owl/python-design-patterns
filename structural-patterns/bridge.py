class Device:
	def __init__(self, channel, volume):
		self.__channel = channel
		self.__volume = volume
		self.__enable = False
	
	def isEnable(self):
		return self.__enable

	def enable(self):
		self.__enable = True
		self.__channel = 1
		self.__volume = 50

	def disable(self):
		self.__enable = False

	def getVolume(self):
		return self.__volume
	
	def setVolume(self, percent):
		self.__volume = percent

	def getChannel(self):
		return self.__channel

	def setChannel(self, channel):
		self.__channel = channel

class Radio(Device):
	def __init__(self, channel, volume):
		super().__init__(channel, volume)
		self.__name = "Radio"

class TV(Device):
	def __init__(self, channel, volume):
		super().__init__(channel, volume)
		self.__name = "TV"

class Remote:
	def __init__(self, device):
		self.__device = device

	def togglePower(self):
		if not self.__device.isEnable():
			self.__device.enable()
		else:
			self.__device.disable()

	def volumeDown(self):
		self.__device.setVolume(self.__device.getVolume() - 10)

	def volumeUp(self):
		self.__device.setVolume(self.__device.getVolume() + 10)

	def channelDown(self):
		self.__device.setChannel(self.__device.getChannel() - 1)

	def channelUp(self):
		self.__device.setChannel(self.__device.getChannel() + 1)

	def setVolume(self, volume):
		self.__device.setVolume(volume)

	
class AdvanceRemote(Remote):
	def __init__(self, device):
		super().__init__(device)
	
	def mute(self):
		self.setVolume(0)
	
	def unmute(self):
		self.setVolume(100)



if __name__ == "__main__":
	radio = Radio(1, 50)
	tv = TV(1, 50)
	radioRemote = Remote(radio)
	radioRemote.togglePower()
	radioRemote.volumeDown()
	radioRemote.channelDown()

	advanceRemoteTV = AdvanceRemote(tv)
	advanceRemoteTV.togglePower()
	advanceRemoteTV.volumeDown()
	advanceRemoteTV.mute()
	advanceRemoteTV.unmute()
