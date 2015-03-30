# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.provider "virtualbox" do |v|
  v.customize ["modifyvm", :id, "--cpus", "2", "--memory", "2048"]
end
  config.vm.define "minecraft" do |minecraft|
    minecraft.vm.network "private_network", ip: "192.168.50.10"
    minecraft.vm.network "forwarded_port", guest: 25565, host: 25565
    minecraft.vm.hostname = "minecraft.khome"
    minecraft.vm.box = "precise64"
    minecraft.vm.box_url = "http://files.vagrantup.com/precise64.box"
  end
  
  # -------- Enable provisioning with Ansible.  --------
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.verbose = 'vvv'
    ansible.groups = {
        "minecraftservers" => ["minecraft"]
    }
  end
end
