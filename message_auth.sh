openssl enc -aes-128-cbc -e -in plain.txt -out  ciphertext -k $1 -iv  $2
openssl dgst -sha256 -hmac $3 plain.txt | cat >> sig

openssl enc -aes-128-cbc -d -in ciphertext -out  plain2.txt -k $1 -iv $2
openssl dgst -sha256 -hmac $3 plain2.txt | cat >> sig2

diff --brief <(sort sig) <(sort sig2) >/dev/null
comp_value=$?


echo ""
echo ""

if [ $comp_value -eq 1 ]
then
    echo "result --->  same"
else
    echo "result --->  different"
fi
