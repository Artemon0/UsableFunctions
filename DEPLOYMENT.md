# Deployment Guide

## GitHub Pages Setup

1. **Enable GitHub Pages**
   - Go to Settings → Pages
   - Source: **GitHub Actions**
   - Save

2. **Push to main**
   ```bash
   git push origin main
   ```

3. **Done!** Visit: `https://artemon0.github.io/UsableFunctions/`

## Local Testing

```bash
cd docs
python -m http.server 8000
# Visit http://localhost:8000
```

## Workflows

- `deploy.yml` - Auto-deploy docs to GitHub Pages
- `python-package.yml` - Test package on multiple platforms
