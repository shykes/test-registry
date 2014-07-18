#!/bin/sh

openssl genrsa -out client.key 1024
openssl req -new -x509 -text -key client.key -out client.cert
