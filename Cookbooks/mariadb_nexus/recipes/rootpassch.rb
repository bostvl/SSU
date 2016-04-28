
if node['allow_root_pass_change']
  # Used to change root password after first install
  # Still experimental
  if node['old_root_password'].empty?
    md5 = Digest::MD5.hexdigest('empty')
  else
    md5 = Digest::MD5.hexdigest(node['old_root_password'])
  end

  file '/etc/mysql_root_change' do
    content md5
    action :create
    notifies :run, 'execute[install-grants]', :immediately
  end
end

if  node['allow_root_pass_change'] ||
    node['forbid_remote_root']
  execute 'install-grants' do
    # Add sensitive true when foodcritic #233 fixed
    command '/bin/bash /etc/mariadb_grants \'' + \
      node['new_root_password'] + '\''
    only_if { File.exist?('/etc/mariadb_grants') }
    action :nothing
  end

  template '/etc/mariadb_grants' do
    sensitive true
    source 'mariadb_grants.erb'
    owner 'root'
    group 'root'
    mode '0600'
    notifies :run, 'execute[install-grants]', :immediately
  end
end

