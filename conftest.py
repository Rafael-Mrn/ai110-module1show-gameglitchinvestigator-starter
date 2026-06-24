# Placing conftest.py at the repo root makes pytest add this directory to
# sys.path, so tests under tests/ can `import logic_utils` regardless of
# whether you run `pytest` or `python -m pytest`.
