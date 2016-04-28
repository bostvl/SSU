#  hope to have 'from_source' in the near future
default['mariadb_version'] = '5.5'
default['use_default_repository'] = false
default['repo_base_url'] = \
  'http://192.168.103.206:8081/nexus/content/repositories/Mariadb5.5_centos6'

default['allow_root_pass_change'] = true
default['old_root_password'] = 
default['new_root_password'] = '1q'
default['forbid_remote_root'] = false
default['bind_address'] = '0.0.0.0'
default['cluster_enabled'] = false
default['cluster_servers_ip'] = "192.168.121.212,192.168.121.213"
default['cluster_name'] = "galera_cluster"
default['cluster_node_ip'] = "192.168.121.211"
default['cluster_user_pass'] = "root:1q"
default['cluster_is_master'] = false

