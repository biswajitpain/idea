 #-*- m: ruby -*-
 # vi: set ft=ruby :
 VAGRANTFILE_API_VERSION = "2" 
 Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
     config.ssh.insert_key = false
     config.ssh.forward_agent = true
     #iconfig.vm.provider :virtualbox do |vb|
     #vb.customize ["modifyvm", :id, "--memory", "256"]
     # Application server 1.
     config.vm.define "ubuntua" do |box1|
        box1.vm.hostname = "ubuntua"
        box1.vm.box = "ubuntu/trusty64"
        box1.vm.network :private_network, ip: "192.168.33.20"
        #box1.vm.synced_folder "../..", "/vagrant_data"
        #box1.vm.provision "shell", path: "build.sh"
        box1.vm.provider :virtualbox do |vb|
            vb.customize ["modifyvm", :id, "--memory", "256"]
        end
     end 
end
