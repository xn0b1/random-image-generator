# cli.py
import typer
from gen import generate_images

app = typer.Typer()

@app.command()
def run(output_dir: str = "random_images", size_gb: int = 1):
    generate_images(output_dir, size_gb)

if __name__ == "__main__":
    app()
