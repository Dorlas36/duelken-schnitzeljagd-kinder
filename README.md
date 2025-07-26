# Dülken Schnitzeljagd Hosting

## Hosting via GitHub Pages
1. Erstelle ein neues GitHub Repository (öffentlich oder privat).
2. Kopiere alle Dateien aus diesem Verzeichnis in das Repo.
3. Aktiviere GitHub Pages für den Branch `main` (Settings → Pages).
4. Die URLs lauten dann:
   `https://<your-username>.github.io/<repo-name>/intro.html`
   usw.

## QR-Code Generierung
Nutze das beigefügte Script `generate_qr.py`:

```bash
pip install qrcode[pil]
python generate_qr.py --prefix "https://<your-username>.github.io/<repo-name>/"
```

Die PNGs werden im Ordner `qr_codes/` abgelegt.
