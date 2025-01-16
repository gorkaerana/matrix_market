# matrix_market

`matrix_market` is a CLI and Python API to interact with our dearly beloved [Matrix Market](https://math.nist.gov/MatrixMarket/). 

The Python API mimics the Matrix Market webpage. E.g., matrices can be downloaded by their name via the `matrix_market.browse.by_matrix_name` function.

The CLI can be used to download matrices by name.
```bash
$ matrix_market
Usage: matrix_market [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  download
```

```bash
$ matrix_market download
Usage: matrix_market download [OPTIONS]

Options:
  -n, --matrix-name TEXT  Name of the matrix to download
  -d, --save-dir PATH     Directory to which to save the matrix
  -f, --format TEXT       Format in which to download the matrix
  --help                  Show this message and exit.
```

## Further development
Ideally the Python API would implement one-to-one all of the Matrix Market webpage's functionalities under "Browse" and "Search"; and CLI would surface most of that behaviour. I.e., the Python API would implement `matrix_market.browse.by_generator_name`, `matrix_market.search.by_matrix_properties`, `matrix_market.search.by_application_area`, etc.; and CLI would idiomatically surface them. I don't plan to do that in the near future unless I need it. Contributions are welcome, feel free to open your own branch :)
