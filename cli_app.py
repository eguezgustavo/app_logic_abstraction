import click

from task_list import get_pending_tasks
from task_list import get_all_tasks


@click.command()
@click.option('--pending', '-p', is_flag=True)
def main(pending):
    if pending:
        click.echo('\nPending tasks')
        click.echo('=============\n')
        for task in get_pending_tasks():
            click.echo(f'- {task.description}')
    else:
        click.echo('\nAll tasks')
        click.echo('=========\n')
        for task in get_all_tasks():
            click.echo(f'- {task.description}')


if __name__ == "__main__":
    main()
