CampusCneipe
=====

Webseite der Campus Cneipe, `master:HEAD` wird automatisch nach https://www.c2.tum.de/ deployed.

[Aktuelle PDF-Version der Karte](https://www.c2.tum.de/menu.pdf)

## Setup locally
You need to have at least NodeJS 16 installed.

Run: `npm i`

Run locally: `npm run dev`

Compile for production: `npm run build`

In case it complains about missing file: `touch scripts/menu.pdf` to prevent broken symlink.

## Content Maintenance Tasks

### Manually Update Menu Data

* Generate ready2order API key and `export R2O_API_KEY=yourkey`
* `./scripts/update_menu.py > data/menu_data.json`
* add and commit `data/menu_data.json`

### Manually Update Calendar Data

* Make sure you have proper `credentials.json` for Google API
* `./scripts/update_calendar.py`
* add and commit `data/calendar_data.json`

### Build PDF Karte

* `./scripts/pdfmenu.sh`

## Tool Maintenance Tasks

### Update direnv / nix shell environment / CI container

* Make sure you are inside `nix shell`
* `niv update`
* `exit`
* `nix shell` or `direnv reload` (if you use direnv)

### Update npm packages

* Make changes to `package.json` (get latest versions from project pages / github)
* `npm update`
