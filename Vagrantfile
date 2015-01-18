# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

#bootload script to get chef-solo installed
$script = <<SCRIPT
sudo su
echo "deb http://mirror-fpt-telecom.fpt.net/ubuntu/ precise main" > /etc/apt/sources.list
echo "deb http://mirror-fpt-telecom.fpt.net/ubuntu/ precise-updates main" >> /etc/apt/sources.list
echo "deb http://mirror-fpt-telecom.fpt.net/ubuntu/ precise-security main" >> /etc/apt/sources.list
apt-get update
apt-get install curl -y
curl -L https://www.opscode.com/chef/install.sh | bash
SCRIPT

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
   #Set the virtual machine 'box' to use
   config.vm.box = "hashicorp/precise64"
   #Set the vm name
   config.vm.define :elkStack2 do |t|
   end
   #Set the host name
   config.vm.hostname = "elkStack2"
   
   #run the script near the top of this file
   config.vm.provision "shell", inline: $script

   #run through the chef recipies
   config.vm.provision "chef_solo" do |chef|
     chef.cookbooks_path = "cookbooks"
     chef.add_recipe "ss_nginx"
	 chef.add_recipe "ss_elasticsearch"
	 chef.add_recipe "ss_kibana"
	 chef.add_recipe "ss_logstash"
   end

   #run a shell script that updates the elasticsearch mappings for proper viewing in elasticsearch (kibana) queries
   config.vm.provision "shell", path: "updatedEsMappings.sh"
   
end
