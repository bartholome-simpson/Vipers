#!/bin/bash

cat <<'EOF' >> /etc/bash.bashrc
RED="\e[31m"
STOP="\e[0m"

printf "${RED}"
figlet -w 1000 Project Viper
printf "${STOP}"
printf "Created by: TheHackdes"
echo -e "\n"
alias shared='tmux -S /tmp/shareds attach -t shared'
EOF

cat <<'EOF' >> /etc/ssh/sshd_config
Match User *
        ForceCommand tmux attach-session -t shared || tmux -S /tmp/shareds new -s shared
EOF

/etc/init.d/ssh restart &> /dev/null
useradd $1 -m -s /bin/bash -p $(echo "$2" | openssl passwd -1 -stdin)

echo "Username : ${1}"
echo "Password : ${2}"
su - $1
