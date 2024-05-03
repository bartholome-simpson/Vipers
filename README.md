![banner_0x02](./sources/banner_0x02.png)

**Project description**

This project aims to deploy individual containers easily and quickly for each student. They were originally designed for cybersecurity students. This allows them to have a laboratory available to work and learn basic commands.

A terminal sharing feature is included. A teacher can connect to the student's container and see in real time what the student is doing. They can also type on their behalf to help them.

## Contents

1. [Installation](#installation)
2. [Usage](#use)
3. [Contribute](#contribute)
4. [License](#license)

## Installation

### Edit the student name

Add or edit the file : 

```bash
vim roles/deploy_student_container/defaults/main.yml
```

## Use

```bash
ansible-playbook -i hosts deploy_student_container.yml
```

Connect to docker student with the below command :

```bash
docker exec -ti <CONTAINER_NAME> bash
```

To view the student screen type : 

```bash
root@MACHINE:~$ shared
```

## Contribute

As a reminder, this project is still only a draft, as we are still learning about this provision, any contribution and opinion /improvement of this provision is welcome.

The same goes for adding functionality, don’t hesitate to:

1. Project fork
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Added a new feature'`)
4. Branch push (`git push origin feature/new-feature`)
5. Create a pull request

## License

This project is distributed under the MIT License, a permissive open source license that allows anyone to use, modify and distribute the code, as long as the copyright notice and license are included in all copies or substantial parts of the software. This license is renowned for its simplicity and flexibility, offering great freedom to users.
