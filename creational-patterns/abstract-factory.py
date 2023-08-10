from abc import ABC, abstractmethod


# abstract product
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def click(self):
        pass


# concrete product
class WinButton(Button):
    def render(self):
        print("Windows Button rendered")

    def click(self):
        print("Windows Button clicked")


# concrete product
class MacButton(Button):
    def render(self):
        print("Mac Button rendered")

    def click(self):
        print("Mac Button clicked")


# abstract product
class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def click(self):
        pass


# concrete product
class WinCheckbox(Checkbox):
    def render(self):
        print("Windows Checkbox rendered")

    def click(self):
        print("Windows Checkbox clicked")


# concrete product
class MacCheckbox(Checkbox):
    def render(self):
        print("Mac Checkbox rendered")

    def click(self):
        print("Mac Checkbox clicked")


# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def createButton(self) -> Button:
        pass

    @abstractmethod
    def createCheckbox(self) -> Checkbox:
        pass


# concrete factory
class WinFactory(GUIFactory):
    def createButton(self) -> Button:
        return WinButton()

    def createCheckbox(self) -> Checkbox:
        return WinCheckbox()


# concrete factory
class MacFactory(GUIFactory):
    def createButton(self) -> Button:
        return MacButton()

    def createCheckbox(self) -> Checkbox:
        return MacCheckbox()


class Application:
    def __init__(self, factory: GUIFactory):
        self.__factory = factory
        self.__button = None
        self.__checkbox = None

    def createUI(self):
        self.__button = self.__factory.createButton()
        self.__checkbox = self.__factory.createCheckbox()

    def paint(self):
        self.__button.render()
        self.__checkbox.render()

    def action(self):
        self.__button.click()
        self.__checkbox.click()


if __name__ == "__main__":
    factory_type = input("Enter factory type (win or mac)? ")

    if factory_type == "win":
        factory = WinFactory()
    elif factory_type == "mac":
        factory = MacFactory()
    else:
        print("Invalid factory type")
        exit()

    app = Application(factory)
    print("-----------")
    print("creating UI")
    app.createUI()
    print("-----------")
    print("painting")
    app.paint()
    print("-----------")
    print("action")
    app.action()
