from Obj.Block import *

def main():
    # First block
    block_A = Block(
      1, 'Nelson likes cat'
    )
    print(block_A.__dict__)

    # Second block
    block_B = Block(
      2, 'Marie likes dog', block_A.id
    )
    print(block_B.__dict__)

    block_C = Block(
      2, 'Sky hates dog', block_B.id
    )
    print(block_C.__dict__)

if __name__ == "__main__":
    # execute only if run as a script
    main()
