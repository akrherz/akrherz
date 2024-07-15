#!/usr/bin/env python
"""Run a command over all hosts with some parallelism."""

import subprocess
from functools import partial
from multiprocessing.pool import ThreadPool

import click

HOSTSFN = "/home/akrherz/Documents/HOSTS"


def read_hosts() -> list:
    """Read the hosts file."""
    hosts = []
    with open(HOSTSFN) as f:
        for line in f:
            line = line.strip()
            port = 22
            host = line
            if line.find(":") > 0:
                host, port = line.split(":")
            if host.find(".") == -1:
                host = f"{host}.agron.iastate.edu"
            hosts.append((host, port))
    return hosts


def run_command(command, config):
    """Run a command on a host."""
    host, port = config
    try:
        output = subprocess.check_output(
            [
                "ssh",
                "-o",
                "ConnectTimeout=5",
                "-o",
                "StrictHostKeyChecking=no",
                "-p",
                f"{port}",
                f"root@{host}",
                command,
            ],
            stderr=subprocess.STDOUT,
        ).decode("utf-8")
    except Exception as e:
        output = repr(e)
    return (host, output)


@click.command()
@click.option("--command", "-c", help="Command to run on each host.")
def main(command):
    print(f"Running command: {command}")
    hosts = read_hosts()
    f = partial(run_command, command)
    with ThreadPool(5) as pool:
        for host, output in pool.imap_unordered(f, hosts):
            print(f"----> {host}")
            print("\n".join([f"  {line}" for line in output.split("\n")]))


if __name__ == "__main__":
    main()
