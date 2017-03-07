###
### init.pp: start webserver, and ensure all client services exist, and
###          properly configured.
###

class webserver {
    ## install mariadb
    contain database::client
    contain database::bindings

    ## install redis client
    contain package::redis_client

    ## install webserver
    contain package::gunicorn
    contain webserver::service
}