'''cli'''
from pathlib import Path
import logging
from typing import Any, Annotated
import typer
import helpers
from rich.console import Console
from rich.table import Table
from todo import db, config, todos, __version__, TITLE, ERRORS
from todo.helpers import add_your_task, hello, make_your_choice, bye, help_me, choose_category
from todo.model import Todo


app = typer.Typer()
console = Console()
header = Todo.make_header()

def show(tasks: Any) -> None:
    """a list of tasks in the form of a table"""
    table = Table(show_header=True, header_style="bold blue")
    for item in header:
        table.add_column(item['name'], style=item['style'], width=item['width'],
        min_width=item['min_width'],justify=item['justify'])

    for index, task in enumerate(tasks, start=1):
        c = Todo.get_category_color(task['category'])
        is_done = Todo.DONE if task['status'] == 2 else Todo.PENDING
        table.add_row(str(index), task['task'], f'[{c}]{task['category']}[/{c}]', is_done)

        console.print(table)

def get_todo_list() -> todos.TodoList:
    """a list of tasks in the form of a table"""
    if config.CONFIG_FILE_PATH.exists():
        db_path = db.get_database_path(config.CONFIG_FILE_PATH)
    else:
        typer.secho('Config file not found. Please, run "todo init"', fg=typer.colors.RED, )
        raise typer.Exit(1)
    if db_path.exists():
        return todos.TodoList(db_path)
    else:
        typer.secho('Database not found. Please, run "todo init"', fg=typer.colors.RED, )
        raise typer.Exit(1)


@app.command()
def init(
        db_path: Annotated[str, typer.Option("--db-path", "-db",
            prompt="to-do database location?"),] = str(
            db.DEFAULT_DB_FILE_PATH), ) -> None:
    app_init_error = config.init_app(db_path)

    if app_init_error:
        typer.secho(f"Creating config file failed with {ERRORS[app_init_error]}",
        fg=typer.colors.RED)
        logging.error(F"Exception {ERRORS[app_init_error]} occurred.", exc_info=True)
        raise typer.Exit(1)

    db_init_error = db.init_database(Path(db_path))
    if db_init_error:
        typer.secho(f"Creating database failed with {ERRORS[app_init_error]}", fg=typer.colors.RED)
        logging.error(F"Exception {ERRORS[app_init_error]} occurred.", exc_info=True)
        raise typer.Exit(1)

    typer.secho(f"The todo database is {db_path}", fg=typer.colors.GREEN)
    logging.info(f"The todo database is {db_path}")


@app.command()
def run() -> None:
    hello()
    todo_list = get_todo_list()

    while True:
        match make_your_choice():
            case 'a':
                category = choose_category()
                task = add_your_task()

                write_error = todo_list.add(task, category)

                if write_error:
                    typer.secho(f"Added task failed with {write_error}", fg=typer.colors.RED)
                    logging.error(F"Exception {write_error} occurred.", exc_info=True)
                    raise typer.Exit(1)
                else:
                    typer.secho(f"Task {task} was added to todo database with {category}",
                    fg=typer.colors.GREEN)
                    logging.info(f"Task {task} was added to todo database with {category}")

            case 'l':
                tasks, error = todo_list.get_todo()
                if error:
                    typer.secho(f"Fetching tasks failed with {ERRORS[error]}", fg=typer.colors.RED)
                    raise typer.Exit(1)
                else:
                    if len(tasks) == 0:
                        typer.secho("There are no tasks in the to-do list yet", fg=typer.colors.RED)
                        raise typer.Exit()
                    show(tasks)
            case 'u':
                task_id = helpers.choose_id()
                task, error = todo_list.complete(task_id)
                if error:
                    typer.secho(f"Completing task failed with {ERRORS[error]}", fg = typer.colors.RED)
                    logging.error("Completing task with id %d failed with %s", task_id, ERRORS[error])
                    raise typer.Exit(1)
                show(tasks)
                logging.info("Task with id %d completed", task_id)
            case 'r':
                task_id = helpers.choose_id()
                task, error = todo_list.delete(task_id)
                if error:
                    typer.secho(f"Deleting task failed with {ERRORS[error]}", fg = typer.colors.RED)
                    logging.error("Deleting task with id %d failed with %s", task_id, ERRORS[error])
                    raise typer.Exit(1)
                show(tasks)
                logging.info("Task with id %d deleted", task_id)

                id = helpers.choose_id()
                tasks, error = todo_list.delete(id)
                show(tasks)
            case 'q':
                bye(TITLE)
                break

            case _:
                help_me()
