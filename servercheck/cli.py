import click
import json
import sys

@click.command()
@click.option("--filename", "-f", default=None) # default is none, because it is optional
@click.option("--server", "-s", default=None, multiple=True) # multiple is true as there can be multiple servers
def cli(filename, server):
    if not filename and not server:
        raise click.UsageError("Must provide a JSON fle or servers")
    
    # Create a set of servers to prevent duplicates
    servers = set()

    # If --filename or -f option is used then attempt to open file before making requests.
    if filename:
        try:
            with open(filename) as f:
                json_servers = json.load(f)
                for s in json_servers:
                    servers.add(s)
        except:
            print("Error: Unable to open or read JSON file")
            sys.exit(1)

    if server:
        for s in server:
            servers.add(s)

    print(servers)

if __name__ == "__main__":
    cli()
