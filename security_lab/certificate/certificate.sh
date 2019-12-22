#make required folder
mkdir certs crl newcerts private

#make required file
touch index.txt
echo '01' > serial

# ca authority
openssl genrsa -des3 -out private/cakey.pem
openssl req -new -x509 -key private/cakey.pem -out cacert.pem


#
openssl genrsa -des3 -out private/server.key
openssl req -new -key private/server.key -out server.csr
openssl ca -in server.csr -out server.crt


sudo cat virtualhost.txt > /etc/apache2/sites-available/000-default.conf
