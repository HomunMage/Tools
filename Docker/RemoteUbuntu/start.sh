docker build -t ubuntu-ssh --build-arg SSH_USERNAME=<name> --build-arg SSH_PASSWORD=<pw> .
docker create -it -p 5566:22 -v /path/to/your/public_key_folder:/home/<name>/.ssh --name ubuntu-bash ubuntu-ssh /bin/bash
docker start ubuntu-bash
docker exec -it ubuntu-bash ps aux | grep sshd
docker exec -it ubuntu-bash sudo service ssh start
ssh -i /path/to/your/private_key -p 5566 <name>@127.0.0.1
