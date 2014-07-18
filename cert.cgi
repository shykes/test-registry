 #!/bin/bash
 if [ "$HTTPS" != "on" ]; then
     echo "Status: 403 Not using SSL"
     echo "x-docker-registry-version: 0.6.2"
     echo
     exit 0
 fi
 if [ "$SSL_CLIENT_VERIFY" == "NONE" ]; then
     echo "Status: 403 Client certificate invalid"
     echo "x-docker-registry-version: 0.6.2"
     echo
     exit 0
 fi
 echo "Content-length: $(stat --printf='%s' $PATH_TRANSLATED)"
 echo "x-docker-registry-version: 0.6.2"
 echo "X-Docker-Endpoints: $SERVER_NAME"
 echo "X-Docker-Size: 0"
 echo

 cat $PATH_TRANSLATED
