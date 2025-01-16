from pathlib import Path

import click

from matrix_market import browse


@click.command(no_args_is_help=True)
@click.option("--matrix-name", "-n", help="Name of the matrix to download")
@click.option(
    "--save-dir",
    "-d",
    help="Directory to which to save the matrix",
    default=None,
    type=Path,
)
@click.option(
    "--format", "-f", help="Format in which to download the matrix", default=".mtx.gz"
)
def download(
    matrix_name: str, save_dir: Path | None = None, format: browse.Formats = ".mtx.gz"
):
    save_path = browse.by_matrix_name(matrix_name, save_dir, format)
    click.echo(f"Downloaded {repr(matrix_name)} to {save_path} :)")


if __name__ == "__main__":
    download()
