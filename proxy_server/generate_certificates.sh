#!/bin/bash

mkdir -p ./certs
openssl req -nodes -days 3650 -new -x509 -newkey rsa:2048 -keyout ./certs/mitmproxy-ca-key.pem -out ./certs/mitmproxy-ca-cert.pem -subj "/C=RU/ST=Moscow/L=Moscow/O=Security Inc/OU=Security Inc DLP Root CA/CN=www.securityinc.com"
openssl pkcs12 -export -in ./certs/mitmproxy-ca-cert.pem -inkey ./certs/mitmproxy-ca-key.pem -name "DLP Root Cert" -out ./certs/mitmproxy-ca-cert.p12

cat ./certs/mitmproxy-ca-cert.pem ./certs/mitmproxy-ca-key.pem > ./certs/mitmproxy-ca.pem
cp ./certs/mitmproxy-ca-cert.pem ./certs/mitmproxy-ca-cert.cer
