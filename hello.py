import click

@click.command(help="This is just a Hello python app. It does nothing")
@click.option("--name", prompt="Enter your name", help="Need name")
@click.option("--color", prompt="Enter your color", help="Need color")

def hello(name, color):
    if name == "Thor":
        click.echo("Hey Thor you are always red!!!")
        click.echo(click.style(f"Hello World, {name}", fg="red"))
    else:
        click.echo(click.style(f"Hello World, {name}", fg=color))

if __name__ == "__main__":
    hello()