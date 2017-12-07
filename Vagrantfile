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
  config.vm.box = 'debian/jessie64'

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
