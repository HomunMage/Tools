docker build -t ubuntu-ssh --build-arg SSH_USERNAME=<name> --build-arg SSH_PASSWORD=<password> .
docker create -it -p 5566:22 -v "$(pwd)":<mnt_source_path> -w /home/<name>/app --name ubuntu-container ubuntu-ssh /bin/bash
docker start ubuntu-container
ssh -i /path/to/your/private_key -p 5566 <name>@127.0.0.1
