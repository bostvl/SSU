heat stack-list
heat stack-delete elk
heat template-validate --template-file ElkNetWork.yml 

heat stack-create -f ElkNetWork.yml -e ElkParameters.yml  elk

heat stack-update -f ElkNetWork.yml -e ElkParameters.yml  elk

heat --os-username orest --os-password onlyfororest  --os-project-name elk --os-auth-url http://192.168.122.92:5000/v2.0 stack-list
heat --os-username orest --os-password onlyfororest  --os-project-name elk --os-auth-url http://192.168.122.92:5000/v2.0   stack-create -f ElkNetWork.yml -e ElkParameters.yml  elk

