# include_recipe 'yum::default'
# include_recipe 'yum-epel::default'

#Creating repository ****************************************************************
 if node['use_default_repository']
     target_platform = "#{node['platform']}#{node['platform_version'].to_i}"
     yum_repository "mariadb-#{node['mariadb_version']}" do
       description 'MariaDB Official Repository'
       baseurl 'http://yum.mariadb.org/' + \
		node['mariadb_version'] + "/#{target_platform}-amd64"
       gpgkey 'https://yum.mariadb.org/RPM-GPG-KEY-MariaDB'
       action :create
      end  
   else
     yum_repository "mariadb-#{node['mariadb_version']}" do
       description 'MariaDB Official Repository'
       baseurl node['repo_base_url']
       gpgkey 'https://yum.mariadb.org/RPM-GPG-KEY-MariaDB'
       action :create
     end
  end

#Installing packages ****************************************
package 'MariaDB-Galera-server' 
package 'MariaDB-client' 
package 'galera'

#Change root password for mysql serevr *********
if node['allow_root_pass_change']
 service "mysql" do 
  action :start
 end

 include_recipe "#{cookbook_name}::rootpassch"

 service "mysql" do
  action :stop
 end
end

#Adding template for server.cnf file   *******************
 template '/etc/my.cnf.d/server.cnf' do
    sensitive true
    source 'server.cnf.erb'
    owner 'root'
    group 'root'
    mode '0644'
 end

#Start cluster master ***********************
if node['cluster_is_master']
 execute 'start_cluster' do
  command '/etc/init.d/mysql bootstrap'
 end
else
 service "mysql" do
  action :start
 end
end

 service "mysql" do
  action :enable
 end


