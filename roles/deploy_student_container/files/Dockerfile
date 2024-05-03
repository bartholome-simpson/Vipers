FROM debian

RUN apt update -y
RUN apt install openssh-server neovim vim openssl tmux figlet python3-pip curl -y
RUN apt install nmap -y

RUN curl https://raw.githubusercontent.com/xero/figlet-fonts/master/Bloody.flf > /usr/share/figlet/Bloody.flf

COPY ./create_user.sh /
RUN chmod +x /create_user.sh

ENTRYPOINT ["/create_user.sh"]

EXPOSE 22
