from abc import ABC, abstractmethod


class Os(ABC):
    @abstractmethod
    def click(self):
        pass


class Windows(Os):
    def click(self):
        print("Windows clicked")


class OSX(Os):
    def click(self):
        print("OSX clicked")


class Facade:
    def __init__(self, win, mac):
        self.win = win
        self.mac = mac

    def click(self):
        self.win.click()
        self.mac.click()


if __name__ == "__main__":
    facade = Facade(Windows(), OSX())
    facade.click()
