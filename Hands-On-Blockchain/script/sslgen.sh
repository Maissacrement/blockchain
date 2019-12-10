function gensslkey() {
  openssl genrsa -out ${private_repo}/$1.pem 1024
  openssl rsa -in ${private_repo}/$1.pem -pubout > ${public_repo}/$1.pub
}

function main() {
  public_repo="../keys"
  private_repo="../private"

  gensslkey $1
}

main $1
