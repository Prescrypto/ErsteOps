# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "hashicorp/bionic64"


  # Open ports:
  #
  # 1080  - MailCatcher
  # 3000  - Rails
  # 3005  - BrowserSync
  # 5432  - Postgres
  # 6379  - Redis
  # 35729 - Livereload
  # 5316  - Jasmine
  # 8000 - Django
  # 8888 - daphne (Django Channels)
  [1080, 3000, 3005, 5432, 6379, 5316, 8000, 8001].each do |p|
    config.vm.network :forwarded_port, guest: p, host: p
  end

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
   config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
     vb.memory = "2048"
   end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL
  # Provision application
  config.vm.provision "shell", privileged: false, run: "always", path: "config/vagrantvars.sh"
  #config.vm.provision "shell", privileged: false, run: "always", path: "bin/setup_box.sh"

end
=======
# -*- mode: django -*-
# vi: set ft=python :

# Module to know the host platform
# Based on BernardoSilva's answer in http://stackoverflow.com/questions/26811089/vagrant-how-to-have-host-platform-specific-provisioning-steps
module OS
    def OS.mac?
        (/darwin/ =~ RUBY_PLATFORM) != nil
    end
    def OS.linux?
      not OS.mac?
    end
end

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = '2'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Every Vagrant virtual environment requires a box to build off of.
  #config.vm.box = 'debian/jessie64'
  config.vm.box = "debian/stretch64"

  # Open ports:
  #
  # 1080  - MailCatcher
  # 3000  - Rails
  # 3005  - BrowserSync
  # 5432  - Postgres
  # 6379  - Redis
  # 35729 - Livereload
  # 5316  - Jasmine
  # 8000 - Django
  # 8888 - daphne (Django Channels)
  [1080, 3000, 3005, 5432, 6379, 5316, 8000].each do |p|
    config.vm.network :forwarded_port, guest: p, host: p
  end

  # NFS ---- NFS improves speed of VM if supported by your OS
  # It does not work with encrypted volumes
  # Linux Need a plugin for Virtualbox to shared files `vagrant plugin install vagrant-vbguest`
  if OS.linux?
    puts "Vagrant launched from linux."
    config.vm.synced_folder '.', '/vagrant', type: 'virtualbox'
  elsif OS.mac?
    puts "Vagrant launched from mac."
    config.vm.network 'private_network', ip: '192.168.50.4'
    config.vm.synced_folder '.', '/vagrant', type: 'nfs'
  end

  # Provider-specific configuration so you can fine-tune various
  # backing providers for rant. These expose provider-specific options.
  config.vm.provider 'virtualbox' do |vb|
    vb.customize ['modifyvm', :id, '--memory', '2048']
  end

  # Provision application
  config.vm.provision "shell", privileged: false, run: "always", path: "config/vagrantvars.sh"
  config.vm.provision "shell", privileged: false, run: "always", path: "bin/setup_box.sh"


  # Deployment (Legacy code, now deploys with every push!)
  config.push.define "staging", strategy: "heroku" do |push|
    push.app = "ersteops-staging"
  end
  # Production (Still used)
  config.push.define "production", strategy: "heroku" do |push|
    push.app = "ersteops"
  end

end
