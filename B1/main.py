from Obj.Blockchain import *
from Obj.Block import *

def main():
    # Init my Blockchain
    yanaCoin=Blockchain()

    # Create a block
    newBlock = Block(1, datetime.datetime.now().isoformat(), 100)
    yanaCoin.addBlock(newBlock)

    print(yanaCoin.chain[0].__dict__)
    print(yanaCoin.chain[1].__dict__)

    for el in yanaCoin.chain:
      print(el)

if __name__ == "__main__":
    # execute only if run as a script
    main()
