openssl enc -aes-128-cbc -e -in $1 -out cipher -k $2 -iv $3
openssl dgst -sha256 -hmac $4 $1 | cat > mac1

openssl enc -aes-128-cbc -d -in cipher -out plain2.txt -k $2 -iv $3
openssl dgst -sha256 -hmac $4 plain2.txt | cat > mac2


diff <(sort mac1) <(sort mac2) >/dev/null
comp_value=$?


echo ""
echo ""

if [ $comp_value -eq 1 ]
then
    echo "result --->  same"
else
    echo "result --->  different"
fi
