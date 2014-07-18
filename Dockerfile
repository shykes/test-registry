from ubuntu:14.04
run apt-get update
run apt-get install -y apache2
run apt-get install -y openssl
add v1.tar.gz /var/www/html/
add registry.conf /etc/httpd/conf.d/registry.conf
add cert.cgi /var/www/cgi-bin/cert.cgi
add mkcerts.sh /usr/local/bin/mkcerts.sh
expose 80
