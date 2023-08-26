from pathlib import Path
from urllib.parse import urlparse

import click
import requests
from retry import retry

from . import utils

# User-Agent used when fetching robots.txt.
USER_AGENT = "NewsHomepagesBot (https://github.com/palewire/news-homepages)"


@click.command()
@click.argument("handle")
@click.option("-o", "--output-dir", "output_dir", default="./")
@click.option("--timeout", "timeout", default="5")
def cli(handle: str, output_dir: str, timeout: str = "5"):
    """Save the raw robots.txt of the provided site."""
    site = utils.get_site(handle)

    # Set the output path
    output_path = Path(output_dir) / f"{handle.lower()}.robots.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    robotstxt = _get_robotstxt(site["url"], int(timeout))
    with output_path.open("w+") as f:
        f.write(robotstxt)


@retry(tries=3, delay=5, backoff=2)
def _get_robotstxt(site_url: str, timeout: int = 180):
    robotstxt_url = urlparse(site_url)._replace(path="robots.txt").geturl()
    response = requests.get(
        robotstxt_url,
        headers={
            "User-Agent": USER_AGENT,
        },
        timeout=timeout,
    )
    return response.text


if __name__ == "__main__":
    cli()
