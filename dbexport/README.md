# Easy Data Transformation

- [x] Download a centos docker image
- [] Create a centos docker container
```
docker run --name cloud_playground -p 8080:80 -i -t centos /bin/bash
```
- [] curl `db_setup.sh` into container
```
curl -O https://raw.githubusercontent.com/linuxacademy/content-python-use-cases/master/helpers/db_setup.sh
```

- [] Change permissions and run setup (script contains commands run as sudo)
```
chmod +x db_setup.sh
./db_setup.sh
```