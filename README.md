# moongas-py-mediascan
Python library for working with moongas mediascan database files and metadata files

## Installation 

### (User) Install from GitHub repo

```bash
pip install "git+https://github.com/bretttolbert/moongas-py-mediascan.git[stats]"
```

### (Developer) Clone GitHub repo and install (editable)

```bash
git clone git@github.com:bretttolbert/moongas-py-mediascan.git && cd mediascan
python -m pip install -e ".[dev,stats]"
```

### Optional dependency groups

- `[dev]` - development dependencies (includes `pytest` and `ruff`)
- `[stats]` - statistics script dependencies (includes `matplotlib` and `numpy`)

