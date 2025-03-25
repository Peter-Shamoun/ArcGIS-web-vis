require([
    "esri/Map",
    "esri/views/MapView",
    "esri/Graphic",
    "esri/geometry/Point",
    "esri/geometry/Polyline",
    "esri/request",
    "esri/layers/GraphicsLayer"
], function(Map, MapView, Graphic, Point, Polyline, esriRequest, GraphicsLayer) {
    // Create a new map instance
    const map = new Map({
        basemap: "streets-navigation-vector"
    });

    // Create a new map view centered on San Diego
    const view = new MapView({
        container: "mapContainer",
        map: map,
        center: [-116.7611, 32.88], // San Diego coordinates (longitude, latitude)
        zoom: 9
    });

    // Create graphics layers
    const nodesLayer = new GraphicsLayer();
    const linesLayer = new GraphicsLayer();
    const highlightedFacilitiesLayer = new GraphicsLayer(); // Layer for highlighted facilities
    map.add(linesLayer);
    map.add(nodesLayer);
    map.add(highlightedFacilitiesLayer); // Add layer for highlighted facilities

    // Store node coordinates and valid coordinate bounds
    let nodeCoordinates = {};
    let minLon = Infinity, maxLon = -Infinity;
    let minLat = Infinity, maxLat = -Infinity;
    
    // Load highlighted facilities
    let highlightedFacilities = [];
    
    // Current dataset number
    let currentDataset = "1";
    
    // Get dataset selector element
    const datasetSelect = document.getElementById("datasetSelect");
    
    // Add event listener to dataset selector
    datasetSelect.addEventListener("change", function(event) {
        currentDataset = event.target.value;
        reloadData();
    });
    
    // Function to load data based on current dataset selection
    function reloadData() {
        // Clear existing graphics layers
        nodesLayer.removeAll();
        linesLayer.removeAll();
        highlightedFacilitiesLayer.removeAll();
        
        // Reset data structures
        nodeCoordinates = {};
        highlightedFacilities = [];
        minLon = Infinity;
        maxLon = -Infinity;
        minLat = Infinity;
        maxLat = -Infinity;
        
        // Load the data for the selected dataset
        loadDataset(currentDataset);
    }
    
    // Function to load a specific dataset
    function loadDataset(datasetNumber) {
        // Load highlighted facilities
        loadHighlightedFacilities(datasetNumber)
            .then(facilities => {
                // Load nodes data
                return loadNodes(facilities);
            })
            .then(result => {
                // Load lines data
                loadLines(datasetNumber, result.nodeCoordinates, result.bounds);
            })
            .catch(error => {
                console.error("Error loading dataset:", error);
            });
    }
    
    // Function to load highlighted facilities for the specified dataset
    function loadHighlightedFacilities(datasetNumber) {
        return esriRequest(`data/highlighted_facilities_sample_${datasetNumber}.csv`, {
            responseType: "text"
        }).then(function(response) {
            const data = response.data.trim();
            highlightedFacilities = data.split(',').map(id => parseInt(id.trim()));
            console.log(`Highlighted facilities (Dataset ${datasetNumber}):`, highlightedFacilities);
            return highlightedFacilities;
        }).catch(function(error) {
            console.error(`Error loading highlighted facilities (Dataset ${datasetNumber}):`, error);
            return [];
        });
    }

    // Function to load nodes data
    function loadNodes(facilities) {
        return esriRequest("data/destinations.csv", {
            responseType: "text"
        }).then(function(response) {
            // Parse CSV text into array of objects
            const csvData = parseCSV(response.data);
            
            // Create a marker for each node and store its coordinates
            csvData.forEach(function(row, index) {
                // Skip the header row or any row without coordinates
                if (!row.SnapX || !row.SnapY || isNaN(parseFloat(row.SnapX)) || isNaN(parseFloat(row.SnapY))) {
                    console.log("Skipping row with invalid coordinates:", row);
                    return;
                }
                
                const longitude = parseFloat(row.SnapX);
                const latitude = parseFloat(row.SnapY);
                
                // Add basic coordinate validation to filter out obviously wrong values
                // San Diego area is roughly longitude -118 to -116, latitude 32 to 34
                if (longitude < -120 || longitude > -115 || latitude < 31 || latitude > 35) {
                    console.log(`Skipping point with out-of-bounds coordinates: (${longitude}, ${latitude})`);
                    return;
                }
                
                // Update min/max coordinates to establish valid bounds
                minLon = Math.min(minLon, longitude);
                maxLon = Math.max(maxLon, longitude);
                minLat = Math.min(minLat, latitude);
                maxLat = Math.max(maxLat, latitude);
                
                const point = new Point({
                    longitude: longitude,
                    latitude: latitude
                });

                // Store coordinates by index (starting from 1)
                // The index in the file corresponds to both OriginID and DestinationID
                const nodeId = index + 1;
                nodeCoordinates[nodeId] = {
                    longitude: longitude,
                    latitude: latitude
                };

                // Check if this node is in the highlighted facilities list
                const isHighlighted = highlightedFacilities.includes(nodeId);

                // Create different symbols for regular and highlighted nodes
                const markerSymbol = {
                    type: "simple-marker",
                    color: isHighlighted ? [0, 204, 255] : [0, 119, 200],  // Bright cyan blue for highlighted, regular blue for others
                    size: isHighlighted ? 8 : 6,
                    outline: {
                        color: [255, 255, 255],
                        width: isHighlighted ? 1 : 0.5
                    }
                };

                const nodeGraphic = new Graphic({
                    geometry: point,
                    symbol: markerSymbol,
                    attributes: {
                        Name: row.Name,
                        ID: nodeId,
                        Highlighted: isHighlighted
                    },
                    popupTemplate: {
                        title: "{Name}",
                        content: [
                            {
                                type: "fields",
                                fieldInfos: [
                                    { fieldName: "Name", label: "Name" },
                                    { fieldName: "ID", label: "ID" },
                                    { fieldName: "Highlighted", label: "Chosen Facility" }
                                ]
                            }
                        ]
                    }
                });

                // Add to appropriate layer
                nodesLayer.add(nodeGraphic);
            });
            
            // Expand bounds slightly to account for rounding errors
            const boundBuffer = 0.1;
            
            // Highlight nodes on map that match the highlighted facilities
            facilities.forEach(id => {
                if (nodeCoordinates[id]) {
                    const coord = nodeCoordinates[id];
                    
                    const point = new Point({
                        longitude: coord.longitude,
                        latitude: coord.latitude
                    });
                    
                    // Create a highlight effect (larger circle behind the node)
                    const highlightSymbol = {
                        type: "simple-marker",
                        color: [0, 204, 255, 0.8],  // Bright cyan blue with some transparency
                        size: 12,
                        outline: {
                            color: [255, 255, 255],
                            width: 2
                        }
                    };
                    
                    const highlightGraphic = new Graphic({
                        geometry: point,
                        symbol: highlightSymbol,
                        attributes: {
                            ID: id,
                            Type: "Highlighted Facility"
                        }
                    });
                    
                    highlightedFacilitiesLayer.add(highlightGraphic);
                }
            });
            
            return {
                nodeCoordinates,
                bounds: {
                    minLon: minLon - boundBuffer,
                    maxLon: maxLon + boundBuffer,
                    minLat: minLat - boundBuffer,
                    maxLat: maxLat + boundBuffer
                }
            };
        }).catch(function(error) {
            console.error("Error loading destinations CSV:", error);
            return { nodeCoordinates: {}, bounds: null };
        });
    }
    
    // Function to load lines data for the specified dataset
    function loadLines(datasetNumber, nodeCoords, bounds) {
        // If we couldn't determine valid bounds, use San Diego area as fallback
        const validBounds = bounds || {
            minLon: -118.0, maxLon: -115.0,
            minLat: 32.0, maxLat: 34.0
        };
        
        console.log("Valid coordinate bounds:", validBounds);
        
        // Load the lines CSV file
        esriRequest(`data/lines_sample_${datasetNumber}.csv`, {
            responseType: "text"
        }).then(function(response) {
            // Parse CSV text into array of objects
            const linesData = parseCSV(response.data);
            
            // Process lines in smaller batches to avoid browser hanging
            const batchSize = 1000;
            let processed = 0;
            let validLines = 0;
            let skippedLines = 0;
            
            function processBatch() {
                const batch = linesData.slice(processed, processed + batchSize);
                processed += batchSize;
                
                batch.forEach(function(row) {
                    const originId = parseInt(row.OriginID);
                    const destId = parseInt(row.DestinationID);
                    const shapeLength = parseFloat(row.Shape_Length);
                    
                    // Skip if we don't have coordinates for either point
                    if (!nodeCoords[originId] || !nodeCoords[destId]) {
                        skippedLines++;
                        console.log(`Skipped line: Origin=${originId}, Destination=${destId}, Reason=Missing node data`);
                        return;
                    }
                    
                    // Get coordinates for both points
                    const originCoord = nodeCoords[originId];
                    const destCoord = nodeCoords[destId];
                    
                    // Validate coordinates - ensure they're within reasonable bounds
                    if (!isCoordinateValid(originCoord, validBounds) || 
                        !isCoordinateValid(destCoord, validBounds)) {
                        skippedLines++;
                        console.log(`Skipped line: Origin=${originId}, Destination=${destId}, Reason=Out of bounds`);
                        return;
                    }
                    
                    // Use Total_Kilometers from the CSV instead of calculating the distance
                    const distance = parseFloat(row.Total_Kilometers) || 0;
                    
                    // Skip lines that are too long (adjust this threshold as needed)
                    const maxLineDistance = 100; // km
                    if (distance > maxLineDistance) {
                        skippedLines++;
                        console.log(`Skipped line: Origin=${originId}, Destination=${destId}, Reason=Excessive distance`);
                        return;
                    }
                    
                    // Create polyline connecting the two points
                    const polyline = new Polyline({
                        paths: [
                            [
                                [originCoord.longitude, originCoord.latitude],
                                [destCoord.longitude, destCoord.latitude]
                            ]
                        ]
                    });
                    
                    // Determine line width based on Shape_Length
                    const lineWidth = Math.max(0.5, Math.min(2.5, 3 - (shapeLength / 5000)));
                    
                    const lineSymbol = {
                        type: "simple-line",
                        color: [50, 50, 50, 1],  // Make more transparent for better visualization
                        width: lineWidth,
                        outline: {
                            color: [1, 1, 1],
                            width: 2
                        }
                    };
                    
                    const lineGraphic = new Graphic({
                        geometry: polyline,
                        symbol: lineSymbol,
                        attributes: {
                            OriginID: originId,
                            DestinationID: destId,
                            Length: shapeLength.toFixed(2),
                            Distance: distance.toFixed(2) + " km"
                        },
                        popupTemplate: {
                            title: "Connection",
                            content: [
                                {
                                    type: "fields",
                                    fieldInfos: [
                                        { fieldName: "OriginID", label: "Origin ID" },
                                        { fieldName: "DestinationID", label: "Destination ID" },
                                        { fieldName: "Length", label: "Shape Length" },
                                        { fieldName: "Distance", label: "Distance" }
                                    ]
                                }
                            ]
                        }
                    });
                    
                    linesLayer.add(lineGraphic);
                    validLines++;
                });
                
                // Process next batch if there are more lines
                if (processed < linesData.length) {
                    setTimeout(processBatch, 0);
                } else {
                    console.log(`Processed ${processed} lines: ${validLines} valid, ${skippedLines} skipped`);
                    
                    // After all data is loaded, adjust the map view to focus on highlighted facilities
                    if (highlightedFacilities.length > 0) {
                        zoomToHighlightedFacilities(view, nodeCoords, highlightedFacilities);
                    }
                }
            }
            
            // Start processing lines in batches
            processBatch();
        }).catch(function(error) {
            console.error(`Error loading lines CSV (Dataset ${datasetNumber}):`, error);
        });
    }

    // Function to zoom the map to show all highlighted facilities
    function zoomToHighlightedFacilities(view, nodeCoordinates, highlightedIds) {
        // Get coordinates of all highlighted facilities
        const validHighlightedCoords = highlightedIds.filter(id => nodeCoordinates[id])
            .map(id => nodeCoordinates[id]);
        
        if (validHighlightedCoords.length === 0) {
            console.log("No valid coordinates for highlighted facilities");
            return;
        }
        
        // Find extents
        let minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity;
        
        validHighlightedCoords.forEach(coord => {
            minX = Math.min(minX, coord.longitude);
            maxX = Math.max(maxX, coord.longitude);
            minY = Math.min(minY, coord.latitude);
            maxY = Math.max(maxY, coord.latitude);
        });
        
        // Add some padding
        const padding = 0.1;
        minX -= padding;
        maxX += padding;
        minY -= padding;
        maxY += padding;
        
        // Zoom to extent
        view.goTo({
            center: [(minX + maxX) / 2, (minY + maxY) / 2],
            zoom: Math.min(10, view.zoom) // Limit zoom level to avoid zooming too far out
        });
    }

    // Helper function to check if coordinates are valid
    function isCoordinateValid(coord, bounds) {
        if (!coord || typeof coord.longitude !== 'number' || typeof coord.latitude !== 'number') {
            console.log("Invalid coordinate format:", coord);
            return false;
        }
        
        const valid = (
            coord.longitude >= bounds.minLon && 
            coord.longitude <= bounds.maxLon &&
            coord.latitude >= bounds.minLat && 
            coord.latitude <= bounds.maxLat
        );
        
        if (!valid) {
            console.log(`Coordinate out of bounds: (${coord.longitude}, ${coord.latitude}), bounds:`, bounds);
        }
        
        return valid;
    }
    
    // Helper function to calculate distance between two coordinates in kilometers
    function calculateDistance(lat1, lon1, lat2, lon2) {
        const R = 6371; // Earth's radius in km
        const dLat = (lat2 - lat1) * Math.PI / 180;
        const dLon = (lon2 - lon1) * Math.PI / 180;
        const a = 
            Math.sin(dLat/2) * Math.sin(dLat/2) +
            Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) * 
            Math.sin(dLon/2) * Math.sin(dLon/2);
        const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
        return R * c;
    }
    
    // Function to parse CSV text into array of objects
    function parseCSV(csvText) {
        const lines = csvText.split("\n");
        const headers = lines[0].split(",");
        const result = [];

        for (let i = 1; i < lines.length; i++) {
            if (lines[i].trim() === "") continue;
            
            // Handle quoted values that may contain commas
            const values = [];
            let currentValue = "";
            let insideQuotes = false;
            
            for (let char of lines[i]) {
                if (char === '"') {
                    insideQuotes = !insideQuotes;
                } else if (char === ',' && !insideQuotes) {
                    values.push(currentValue);
                    currentValue = "";
                } else {
                    currentValue += char;
                }
            }
            values.push(currentValue); // Add the last value
            
            const row = {};
            for (let j = 0; j < headers.length; j++) {
                // Remove any surrounding quotes and trim whitespace
                let value = values[j] || "";
                value = value.trim().replace(/^"|"$/g, "");
                row[headers[j]] = value;
            }
            
            result.push(row);
        }

        return result;
    }
    
    // Load initial dataset
    loadDataset(currentDataset);
});
