from abc import ABC, abstractmethod


class Miner(ABC):
    def mine(self):
        self.openFile()
        self.extractData()
        self.analyzeFile()
        self.sendReport()
        self.closeFile()

    def openFile(self):
        print("open file")

    def closeFile(self):
        print("close file")

    def analyzeFile(self):
        print("analyze file")

    def sendReport(self):
        print("send report")

    @abstractmethod
    def extractData(self):
        pass


class DocDataMiner(Miner):
    def extractData(self):
        print("extract doc data")


class CSVDataMiner(Miner):
    def extractData(self):
        print("extract csv data")


class PDFDataMiner(Miner):
    def extractData(self):
        print("extract pdf data")


if __name__ == "__main__":
    docMiner = DocDataMiner()
    docMiner.mine()

    csvMiner = CSVDataMiner()
    csvMiner.mine()

    pdfMiner = PDFDataMiner()
    pdfMiner.mine()
