# mail_validator
###################

#Enable Pod Balance
------------------

Router -> edit YAML

    haproxy.router.openshift.io/balance: roundrobin
    haproxy.router.openshift.io/disable_cookies: 'true'
