# CI and deployment

## Package checks

The [Python package workflow](.github/workflows/python-package.yml) runs on pull requests to `main`, pushes to `main`, and release tags. It tests Python 3.10–3.13 on Linux, Windows, and macOS. The build job checks for undefined names, builds a wheel and source distribution, checks their metadata, and tests the installed wheel outside the checkout. Both distributions are available in the workflow run under **Artifacts**.

Run the checks locally from the repository root in an activated virtual environment.

```bash
python -m pip install -e .
python -m pip install build twine ruff
python -m pip check
python -m unittest discover -s tests -v
ruff check --select F UsableFunctions tests
python -m build
python -m twine check --strict dist/*
```

## Package release

1. Update `__version__` in [UsableFunctions/_metadata.py](UsableFunctions/_metadata.py) and merge the change to `main`.
2. Update your local `main` and push a tag matching that version. For example, use these commands for version 2.0.1.

   ```bash
   git switch main
   git pull --ff-only origin main
   git tag -a 2.0.1 -m "UsableFunctions 2.0.1"
   git push origin refs/tags/2.0.1
   ```

3. Check the workflow run for the tag. After the checks pass, the release job creates a GitHub Release with the wheel, source archive, and generated release notes.

Tags use `X.Y.Z` without a prefix, as in `2.0.0`. The tagged commit must be on `main`. Publication uses the workflow's GitHub token and targets [GitHub Releases](https://github.com/Artemon0/UsableFunctions/releases).

## Documentation site

The [Documentation workflow](.github/workflows/deploy.yml) checks changes to `docs/` and publishes that directory to [GitHub Pages](https://artemon0.github.io/UsableFunctions/) on `main`.

To switch the repository from branch-based deployment, merge the workflow first. Then select **Settings → Pages → Build and deployment → Source → GitHub Actions**. In the **Actions** tab, run **Documentation** once on `main` to verify the switch. Later changes under `docs/` deploy automatically.

For a local preview, run `python -m http.server 8000 --directory docs` from the repository root and open [localhost:8000](http://localhost:8000/).
