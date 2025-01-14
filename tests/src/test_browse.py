import pytest

import matrix_market
from matrix_market.browse import download_matrix, MATH_MNIST_URL, MATRIX_NAMES


# Just the smallest matrices
matrix_names = [
    "bcsstm05",
    "can___96",
    "bcsstm03",
    "bcsstm04",
    "bcspwr03",
    "dwt___87",
    "can___61",
    "curtis54",
    "ash85",
    "will57",
    "can___73",
    "resources",
    "browse",
    "search",
    "dwt___66",
    "bcsstm02",
    "dwt___59",
    "can___62",
    "dwt___72",
    "ibm32",
    "bcspwr02",
    "bcsstm01",
    "can___24",
    "bcspwr01",
    "rgg010",
    "jgl011",
    "jgl009",
]
matrix_name = "bcspwr01"  # Just a small matrix


@pytest.mark.parametrize("matrix_name", matrix_names)
def test_by_matrix_name_no_save_dir_no_cache(matrix_name, tmp_path, monkeypatch):
    cache_dir = tmp_path / ".cache" / "matrix_market"
    cache_dir.mkdir(exist_ok=True, parents=True)
    monkeypatch.setattr(matrix_market.browse, "CACHE_DIR", cache_dir)
    matrix_market.browse.by_matrix_name(matrix_name)
    assert (cache_dir / f"{matrix_name}.mtx.gz").exists()


@pytest.mark.parametrize("matrix_name", matrix_names)
def test_by_matrix_name_yes_save_dir_no_cache(matrix_name, tmp_path, monkeypatch):
    cache_dir = tmp_path / ".cache" / "matrix_market"
    cache_dir.mkdir(exist_ok=True, parents=True)
    monkeypatch.setattr(matrix_market.browse, "CACHE_DIR", cache_dir)
    save_dir = tmp_path / "data"
    save_dir.mkdir(exist_ok=True, parents=True)
    save_path = save_dir / f"{matrix_name}.mtx.gz"
    # TODO: check this does download data
    matrix_market.browse.by_matrix_name(matrix_name, save_dir)
    assert save_path.exists()


@pytest.mark.parametrize("matrix_name", matrix_names)
def test_by_matrix_name_yes_save_dir_warm_cache(matrix_name, tmp_path, monkeypatch):
    cache_dir = tmp_path / ".cache" / "matrix_market"
    cache_dir.mkdir(exist_ok=True, parents=True)
    monkeypatch.setattr(matrix_market.browse, "CACHE_DIR", cache_dir)
    cache_path = cache_dir / f"{matrix_name}.mtx.gz"
    save_dir = tmp_path / "data"
    save_dir.mkdir(exist_ok=True, parents=True)
    save_path = save_dir / cache_path.name
    download_matrix(MATH_MNIST_URL.copy_with(path=MATRIX_NAMES[matrix_name]), cache_path)
    # TODO: check this does not download anything
    matrix_market.browse.by_matrix_name(matrix_name, save_dir)
    assert save_path.exists()
