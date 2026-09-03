# Publishing the canonical icon bundle

The repository is configured so that publishing or updating the complete icon set requires pushing **one binary file**:

```text
dist/source-icons.zip
```

The GitHub Actions workflow `.github/workflows/sync-icons.yml` then performs the remaining work automatically.

## Git command line

From a clone of the repository:

```bash
mkdir -p dist
cp /path/to/NuoveICO.zip dist/source-icons.zip
git add dist/source-icons.zip
git commit -m "feat: publish Weather Icons v2 source bundle"
git push origin main
```

## Windows PowerShell

```powershell
New-Item -ItemType Directory -Force .\dist | Out-Null
Copy-Item "C:\Path\To\NuoveICO.zip" ".\dist\source-icons.zip" -Force
git add .\dist\source-icons.zip
git commit -m "feat: publish Weather Icons v2 source bundle"
git push origin main
```

## GitHub web interface

1. Open the `dist` directory in the repository.
2. Choose **Add file → Upload files**.
3. Upload the icon archive renamed exactly to `source-icons.zip`.
4. Commit directly to `main` (or use a branch/PR if desired).
5. Wait for the **Sync source bundle** workflow.

## What the workflow publishes

The workflow validates the ZIP and then:

- copies PNG files into `icons/`;
- copies `aeris-icon-list.json` into `mappings/`;
- validates every mapping target;
- generates `manifest.json` with file hashes and dimensions;
- generates `docs/ICON_CATALOG.md`;
- generates `docs/GALLERY.md`;
- commits the generated files back to `main`.

The ZIP may contain a top-level directory such as `NuoveICO/`; the synchronization script normalizes that automatically.
