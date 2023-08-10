from abc import ABC, abstractmethod

class Component(ABC):
	@abstractmethod
	def size(self) -> int:
		pass

class File(Component):
	def __init__(self, name, size):
		self.__name = name
		self.__size = size

	def size(self) -> int:
		return self.__size

	

class Folder(Component):
	def __init__(self, name, components):
		self.__name = name
		self.__components = components

	def size(self) -> int:
		totalSize = 0
		for component in self.__components:
			totalSize += component.size()

		return totalSize


	def add(self, component: Component) -> None:
		self.__components.append(component)



file1 = File("file1", 100)
file2 = File("file2", 200)
folder1 = Folder("folder1", [file1, file2])
print(folder1.size())
folder1.add(File("file3", 300))
print(folder1.size())
print(folder1._Folder__components)
