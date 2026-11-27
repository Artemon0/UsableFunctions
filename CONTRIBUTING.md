# Contributing

1. Fork and clone the repository, then create a branch from `main`.
2. In a Python 3.10+ virtual environment, run `python -m pip install -e .` from the repository root.
3. Use the [project structure](README.md#project-structure) to find the module to edit. Update both READMEs when changing a documented function.
4. Run `python -m unittest discover -s tests -v`. See the [deployment guide](DEPLOYMENT.md) for the full checks and release steps.
5. Push your branch and open a pull request against `main`.
