openssl genrsa -out privateKey.pem
openssl rsa -in privateKey.pem -outform pem -pubout -out pubKey.pem 

echo $1

openssl dgst -sha256 -sign privateKey.pem -out signature.sha256 $1
openssl enc -base64 -in signature.sha256 -out signature.sha256.base64


openssl enc -base64 -d -in signature.sha256.base64 -out sign.sha256-v
openssl dgst -sha256 -verify pubKey.pem -signature sign.sha256-v $1