from pathlib import Path
import json

from bs4 import BeautifulSoup
import fast_matrix_market as fmm
import httpx
from rich.progress import track

from matrix_market.browse import download_matrix


if __name__ == "__main__":
    here = Path(__file__).parent
    SAVE_DIR = here / "data"
    BASE_URL = httpx.URL("https://math.nist.gov")

    matrix_names = {}

    main_page = httpx.get(BASE_URL.copy_with(path="/MatrixMarket/matrices.html"))
    soup = BeautifulSoup(main_page.text, "html.parser")
    for tag in track(soup.find_all("a", href=True)):
        href = tag["href"]
        if href.startswith("/MatrixMarket") and href.endswith(".html"):
            path = Path(href)
            if path.stem in {"browse", "resources", "search"}:
                continue
            save_path = SAVE_DIR / path.with_suffix(".mtx.gz").name
            download_matrix(BASE_URL.copy_with(path=str(path.with_suffix(".mtx.gz"))), save_path)
            matrix_names[path.stem] = href

    (here / "src" / "matrix_market" / "matrix_names.json").write_text(json.dumps(matrix_names))
