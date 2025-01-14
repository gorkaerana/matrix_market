import json
from pathlib import Path
import shutil

import httpx


# __all__ = ["by_matrix_name"]


MATH_MNIST_URL = httpx.URL("https://math.nist.gov")
CACHE_DIR = Path.home() / ".cache" / "matrix_market"
here = Path(__file__).parent
MATRIX_NAMES = json.loads((here / "matrix_names.json").read_text())


def download_matrix(url: httpx.URL, save_path: Path) -> Path:
    matrix_request = httpx.get(url)
    with open(save_path, "wb") as fp:
        fp.write(matrix_request.content)
    return save_path


# TODO: `matrix_name` could be a literal if all names are pre-downloaded
def by_matrix_name(matrix_name: str, save_dir: Path | None = None) -> Path:
    if save_dir is None:
        CACHE_DIR.mkdir(exist_ok=True, parents=True)
        save_dir = CACHE_DIR
    save_path = save_dir / f"{matrix_name}.mtx.gz"
    if save_path.exists():
        return save_path
    if matrix_name not in MATRIX_NAMES:
        raise ValueError(f"{repr(matrix_name)} is incorrect, options are {', '.join(map(repr, matrix_name.keys()))}")
    # A cache of downloaded matrices is maintained in `~/.cache/matrix_market`
    cache_path = CACHE_DIR / save_path.name
    if cache_path.exists():
        if save_dir == CACHE_DIR:
            return cache_path
        else:
            shutil.copy2(cache_path, save_path)
    else:
        download_matrix(MATH_MNIST_URL.copy_with(path=MATRIX_NAMES[matrix_name]), save_path)
    return save_path
