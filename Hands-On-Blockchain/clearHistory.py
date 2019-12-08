from Obj.Block import *

def main():
    # First block
    block_A = Block()
    block_A.id = 1
    block_A.history = 'Nelson likes cat'
    print(block_A.__dict__)

    # Second block
    block_B = Block()
    block_B.id = 2
    block_B.history = 'Marie likes dog'
    block_B.parent_id = block_A.id
    print(block_B.__dict__)

    block_C = Block()
    block_C.id = 3
    block_C.history = 'Sky hates dog'
    block_C.parent_id = block_B.id
    print(block_C.__dict__)

if __name__ == "__main__":
    # execute only if run as a script
    main()
