 sudo timedatectl set-timezone Asia/Tokyo
 sudo yum -y update
 sudo yum -y install git gcc ncurses-devel readline-devel openssl-devel zlib-devel
 curl -L -O https://github.com/SoftEtherVPN/SoftEtherVPN_Stable/releases/download/v4.32-9731-beta/softether-src-v4.32-9731-beta.tar.gz
 tar xvzf softether-src-v4.32-9731-beta.tar.gz
 cd v4.32-9731
 ./configure
 make
 sudo make install
 sudo vim /etc/systemd/system/vpnserver.service
 cd ../
 ll
 sudo mv v4.32-9731 /opt/vpnserver
 sudo chmod 755 /etc/systemd/system/vpnserver.service
 sudo systemctl daemon-reload
 sudo systemctl start vpnserver
 sudo systemctl enable vpnserver
 sudo vpncmd
 sudo systemctl start vpnserver
 service vpnserver status
 sudo systemctl enable vpnserver
 vpnserver start
 vpnbridge start
 vpnclient start
 vpnserver status
 vpnserver
 vpnserver start