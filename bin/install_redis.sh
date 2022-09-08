# Execute sudo ./install_redis.sh
# Add repository for Redis
# Uncomment this for debian 8
#echo deb http://ftp.utexas.edu/dotdeb/ stable all > /etc/apt/sources.list.d/dotdeb.list
#echo deb-src http://ftp.utexas.edu/dotdeb/ stable all >> /etc/apt/sources.list.d/dotdeb.list
# For debian 7
# echo deb http://packages.dotdeb.org jessie all > /etc/apt/sources.list.d/dotdeb.list
# echo deb-src http://packages.dotdeb.org jessie all >> /etc/apt/sources.list.d/dotdeb.list
# cd /tmp/
# wget https://www.dotdeb.org/dotdeb.gpg
# sudo apt-key add dotdeb.gpg
# sudo apt-get update
# sudo apt-get install -y redis-server
# cd /vagrant/


#https://redis.io/docs/getting-started/installation/install-redis-on-linux/
echo "Install Redis Server on ubuntu 18"
echo "Installs redis version 6"
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
sudo apt-get update

sudo apt install redis
echo "Instalation complete"
echo "run redis-cli for test."