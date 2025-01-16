from pathlib import Path
from typing import get_args

import pytest

import matrix_market
from matrix_market.browse import download_matrix, Formats, MATH_MNIST_URL, MATRIX_NAMES


formats = get_args(Formats)

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


@pytest.mark.parametrize("matrix_name", matrix_names)
@pytest.mark.parametrize("format", formats)
def test_by_matrix_name_no_save_dir_no_cache(
    matrix_name, format, tmp_path, monkeypatch
):
    cache_dir = tmp_path / ".cache" / "matrix_market"
    cache_dir.mkdir(exist_ok=True, parents=True)
    monkeypatch.setattr(matrix_market.browse, "CACHE_DIR", cache_dir)
    matrix_market.browse.by_matrix_name(matrix_name, format=format)
    assert (cache_dir / f"{matrix_name}{format}").exists()


@pytest.mark.parametrize("matrix_name", matrix_names)
@pytest.mark.parametrize("format", formats)
def test_by_matrix_name_yes_save_dir_no_cache(
    matrix_name, format, tmp_path, monkeypatch
):
    cache_dir = tmp_path / ".cache" / "matrix_market"
    cache_dir.mkdir(exist_ok=True, parents=True)
    monkeypatch.setattr(matrix_market.browse, "CACHE_DIR", cache_dir)
    save_dir = tmp_path / "data"
    save_dir.mkdir(exist_ok=True, parents=True)
    save_path = save_dir / f"{matrix_name}{format}"
    # TODO: check this does download data
    matrix_market.browse.by_matrix_name(matrix_name, save_dir, format)
    assert save_path.exists()


@pytest.mark.parametrize("matrix_name", matrix_names)
@pytest.mark.parametrize("format", formats)
def test_by_matrix_name_yes_save_dir_warm_cache(
    matrix_name, format, tmp_path, monkeypatch
):
    cache_dir = tmp_path / ".cache" / "matrix_market"
    cache_dir.mkdir(exist_ok=True, parents=True)
    monkeypatch.setattr(matrix_market.browse, "CACHE_DIR", cache_dir)
    cache_path = cache_dir / f"{matrix_name}{format}"
    save_dir = tmp_path / "data"
    save_dir.mkdir(exist_ok=True, parents=True)
    save_path = save_dir / cache_path.name
    download_matrix(
        MATH_MNIST_URL.copy_with(
            path=str(Path(MATRIX_NAMES[matrix_name]).with_suffix(format))
        ),
        save_path,
    )
    # TODO: check this does not download anything
    matrix_market.browse.by_matrix_name(matrix_name, save_dir, format)
    assert save_path.exists()
