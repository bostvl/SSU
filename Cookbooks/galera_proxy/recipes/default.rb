#
# Cookbook Name:: galera_proxy
# Recipe:: default
#
# Copyright 2016, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#
package 'haproxy'
 template '/etc/haproxy/haproxy.cfg' do
    sensitive true
    source 'haproxy.cfg.erb'
    owner 'root'
    group 'root'
    mode '0644'
 end

service "haproxy" do
	action [:enable, :start]
end
