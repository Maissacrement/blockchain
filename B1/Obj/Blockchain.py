from Obj.Block import *

class Blockchain():
    def __init__(self):
        self.chain = [self.initialFirstBlock()]

    def initialFirstBlock(self):
        return Block(0, datetime.datetime.now().isoformat(), 100)

    def getLastBlock(self):
        return self.chain[-1]

    def addBlock(self, newBlock):
        newBlock.prevHash=self.getLastBlock().hash
        newBlock.hash=newBlock.calcHash()
        self.chain.append(newBlock)
