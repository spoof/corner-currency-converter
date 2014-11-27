# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.require_version ">= 1.4.0"

Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu1204"
    config.vm.box_url = "http://cloud-images.ubuntu.com/vagrant/precise/current/precise-server-cloudimg-amd64-vagrant-disk1.box"
    config.vm.hostname = "cornerapp-test.vm"

    config.vm.network :forwarded_port, guest:5000, host:5000
    config.vm.network :private_network, ip:"192.168.100.24"

    config.vm.provider :vmware_fusion do |fusion|
        fusion.vmx["memsize"] = "512"
        fusion.vmx["numvcpus"] = "1"
    end

    config.vm.provider :virtualbox do |vbox|
        vbox.name = "cornerapp-test"
        vbox.customize ["modifyvm", :id, "--memory", "512"]
        vbox.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    end

    config.vm.provision :ansible do |ansible|
        ansible.limit = 'vagrant'
        ansible.verbose = 'vvvv'
        ansible.host_key_checking = false
        ansible.inventory_path = "vagrant/hosts_vagrant"
        ansible.playbook = "vagrant/initial-setup.yaml"
    end


end

