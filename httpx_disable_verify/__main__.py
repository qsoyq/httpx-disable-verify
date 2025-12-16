import site
from pathlib import Path
import typer

app = typer.Typer()

PTH_FILE_PATH = Path(site.getsitepackages()[0]) / "http_disable_verify.pth"


@app.command()
def install():
    """将 pth 补丁安装到 sitepackages"""
    pth = PTH_FILE_PATH
    if pth.exists():
        typer.echo("pth already exists.")
        raise typer.Exit(-1)

    pth.write_text("import httpx_disable_verify")


@app.command()
def uninstall():
    """移除 sitepackages 下的 pth 补丁"""
    pth = PTH_FILE_PATH
    if not pth.exists():
        typer.echo("pth not exists.")
        raise typer.Exit(-1)
    if not pth.is_file():
        typer.echo("pth must be file.")
        raise typer.Exit(-2)

    pth.unlink()


if __name__ == "__main__":
    app()
