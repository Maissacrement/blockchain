import json
import hashlib
import datetime

class Block():
  def __init__(self, nonce, tstamp, transaction, prevHash=''):
    self.nonce = nonce
    self.tstamp = tstamp
    self.transaction = transaction
    self.prevHash= prevHash
    self.hash = self.calcHash()

  def calcHash(self):
    block_string=json.dumps({
      "nonce": self.nonce, "tstamp": self.tstamp,
      "transaction": self.transaction, "prevHash": self.prevHash
    }, sort_keys=True).encode()

    return hashlib.sha256(block_string).hexdigest()

  def __str__(self):
    string="nonce"+ str(self.nonce) + "\n"
    string+= "tstamp"+ str(self.tstamp) + "\n"
    string+="transaction" + str(self.transaction) + "\n"
    string+="prevHash" + str(self.prevHash) + "\n"
    string+="hash" + str(self.hash) + "\n"

    return string
