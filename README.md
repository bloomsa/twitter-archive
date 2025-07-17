# Twitter Archive Analysis

A Python project for analyzing [Twitter/X data archives](https://x.com/settings/download_your_data).

## Features

- **Data Conversion**: Converts Twitter's JavaScript data files to JSON format
- **Ad Analysis**: Analyzes ad impressions, targeting, and engagement data
- **Visualizations**: Creates charts showing targeting types, impressions over time, and more

## Files

- `convert-js.py` - Converts Twitter export JS files to JSON
    - they are in a loosely wrapped javascript file originally for use with an html page included in the export.
- `explore.ipynb` - Jupyter notebook for data exploration and visualization
- `export/` - Contains Twitter archive data (HTML viewer, JSON data, media)
    - this is ignored by git, the only file strictly required is `ad-engagements.json` nested under `export/data/json` but everything in `json/` will be converted from js.

## Usage

1. Install dependencies: `uv sync`
2. Run conversion script: `uv run convert-js.py`
3. Explore data in `explore.ipynb`. VSCode of Jupyter work here but make sure the notebook kernel is in the same created by uv.

## Data Sources

Analyzes Twitter archive data including:
- Ad impressions and engagements
- Targeting criteria
- Tweet content and metadata
- Media files

Built with Python, pandas, matplotlib, and Jupyter.