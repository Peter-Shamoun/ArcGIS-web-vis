# Project Documentation

## Overview

This project displays an ArcGIS map visualizing nodes (locations) and lines (connections) based on selected socioeconomic factors and a specified number of facilities. Data is loaded from CSV files and filtered based on user input.

## Decisions and Reasoning

*   **Technology:** ArcGIS API for JavaScript 4.28 is used for map rendering and interaction. Standard HTML, CSS, and JavaScript handle the UI and logic.
*   **Data Loading:** CSV files are fetched using `esri/request`. Data is processed asynchronously to avoid blocking the UI.
*   **Data Filtering:**
    *   Socioeconomic importance (Poverty, Income, Unemployment) and the Number of Facilities are selected by the user. These selections determine which specific `destinations_*.csv` and `lines_*.csv` files are loaded.
    *   Specific Node IDs (668, 611, 612) are hardcoded to be excluded from the visualization in the `loadNodes` function. This was done based on a direct user request to remove these points.
*   **Visualization:**
    *   Nodes are represented by points (`Graphic` with `SimpleMarkerSymbol`).
    *   Facilities selected by the algorithm (from `destinations_*.csv`) are highlighted with a different color and size.
    *   Connections are represented by lines (`Graphic` with `SimpleLineSymbol`). Line thickness is slightly varied based on length for visual differentiation.
    *   The map automatically zooms to the extent of the highlighted facilities after data loading.
*   **Error Handling:** Basic error handling is implemented to catch issues during file loading (e.g., file not found) and display a message to the user. Invalid coordinates or data rows are skipped with console warnings.
*   **UI:** Simple controls allow users to select the number of facilities and adjust the importance weights for socioeconomic factors. Buttons are used for facility count, and +/- buttons for importance weights.

## File Structure

*   `index.html`: Main HTML structure, includes map container and UI controls.
*   `styles.css`: CSS for styling the UI elements.
*   `main.js`: Core JavaScript logic using ArcGIS API, handles data loading, map setup, and UI interactions.
*   `data/`: Directory containing CSV data files.
    *   `destinations.csv`: Contains coordinates and names for all possible node locations.
    *   `destinations_*.csv`: Contains IDs of selected facilities for specific parameter combinations.
    *   `lines_*.csv`: Contains origin/destination pairs and lengths for lines connecting nodes, specific to parameter combinations.
*   `DOCUMENTATION.md`: This file.

## Setup

1.  Ensure you have a web server to serve the files (e.g., using Python's `http.server` or VS Code Live Server).
2.  Place the `data` directory with all necessary CSV files alongside `index.html`, `styles.css`, and `main.js`.
3.  Open `index.html` in a web browser.

## Potential Improvements

*   More robust error handling and user feedback.
*   Performance optimization for very large datasets (consider server-side processing or different data formats).
*   Add more sophisticated UI controls (e.g., sliders).
*   Refactor CSV parsing for better handling of edge cases. 