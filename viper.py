#!/usr/bin/env python3

import docker
from docker import DockerClient
from docker.models.containers import Container
from rich.console import Console
from rich.table import Table
import argparse

class ViperTable():
    def __init__(self) -> None:
        self._table = Table(title="\nUsers' Containers List", title_justify="center")
        self._table.add_column("Container", justify="center", style="green")
        self._table.add_column("User", justify="center", style="cyan")
        self._table.add_column("SSH", justify="center", style="blue")
        self._table.add_column("VNC", justify="center", style="blue")
    
    def display_password(self):
        self._table.add_column("Password", justify="center", style="red")        

class Viper():
    def __init__(self) -> None:
        self._DockerClient:DockerClient = docker.from_env()
        self._table = Table(title="User Docker List")
    
    def get_containers(self) -> list[Container]:
        return self._DockerClient.containers.list()

    def get_containers_with_name_filter(self, containers:list[Container], filter:str):
        return [container for container in containers if container.name.startswith(filter)]

    def get_host_port(self, container:Container, service:str):
        service_ports = {"ssh":"22/tcp", "vnc":"XXXX/udp"}
        return container.ports[service_ports[service]][0]["HostPort"] if service == "ssh" else None
    
    def get_container_user_info(self, container:Container) -> tuple[str,str]:
        config = container.attrs["Config"]["Cmd"]
        return config[0],config[1]


if __name__ == "__main__":
    
    VIPER = Viper()
    TABLE = ViperTable()
    
    parser = argparse.ArgumentParser(
        prog="Viper",
        description="Viper project is ..."
    )
    parser.add_argument("-p","--password",action='store_true', help="Display password")
    parser.add_argument("-u","--user",nargs="?", help="Display one user")
    parser.add_argument("--all",action='store_true', help="Display all users with their password")
    args = parser.parse_args()
    # print(args)
    
    if args.all or args.password:
        TABLE.display_password()
    
    table = TABLE._table
    if args.all or args.user:
        
        containers = VIPER.get_containers()
        stud_containers = VIPER.get_containers_with_name_filter(containers=containers, filter="stud")
        
        if args.user:
            for container in stud_containers:
                user, password = VIPER.get_container_user_info(container=container)
                if user == args.user:
                    ssh = VIPER.get_host_port(container,'ssh')
                    vnc = VIPER.get_host_port(container,'vnc')
                    if args.password:
                        table.add_row(container.name, user, ssh, vnc, password)
                    else:   
                        table.add_row(container.name, user, ssh, vnc)
        
        elif args.all:
            for container in stud_containers:
                user, password = VIPER.get_container_user_info(container=container)
                ssh = VIPER.get_host_port(container,'ssh')
                vnc = VIPER.get_host_port(container,'vnc')
                table.add_row(container.name, user, ssh, vnc, password)

console = Console()
console.print(table)

    
