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
    
    // Get input elements
    const facilityCountInput = document.getElementById("facilityCountValue");
    const povertyInput = document.getElementById("povertyValue");
    const incomeInput = document.getElementById("incomeValue");
    const unemploymentInput = document.getElementById("unemploymentValue");
    
    // Function to set facility count
    window.setFacilityCount = function(count) {
        facilityCountInput.value = count;
        updateFacilityButtonStyles();
        reloadData();
    };
    
    // Function to update facility button styles to show which is active
    function updateFacilityButtonStyles() {
        const facilityCount = facilityCountInput.value;
        const buttons = document.querySelectorAll('.facility-btn');
        
        buttons.forEach(button => {
            const buttonValue = button.textContent;
            if (buttonValue === facilityCount) {
                button.classList.add('active');
            } else {
                button.classList.remove('active');
            }
        });
    }
    
    // Function to increment a value
    window.incrementValue = function(inputId) {
        const input = document.getElementById(inputId);
        const currentValue = parseInt(input.value);
        if (currentValue < 2) {
            input.value = currentValue + 1;
            reloadData();
        }
    };
    
    // Function to decrement a value
    window.decrementValue = function(inputId) {
        const input = document.getElementById(inputId);
        const currentValue = parseInt(input.value);
        if (currentValue > 0) {
            input.value = currentValue - 1;
            reloadData();
        }
    };
    
    // Function to load data based on current input values
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
        
        // Get current input values
        const facilityCount = facilityCountInput.value;
        const povertyValue = povertyInput.value;
        const incomeValue = incomeInput.value;
        const unemploymentValue = unemploymentInput.value;
        
        // Load the data for the selected values
        loadDataset(facilityCount, povertyValue, incomeValue, unemploymentValue);
    }
    
    // Function to load a specific dataset
    function loadDataset(facilityCount, povertyValue, incomeValue, unemploymentValue) {
        // Clear any previous error messages
        const errorMessageDiv = document.getElementById("errorMessage");
        if (errorMessageDiv) {
            errorMessageDiv.textContent = '';
            errorMessageDiv.style.display = 'none';
        }

        // Construct file paths based on facility count
        let destinationsFileName, linesFileName;
        if (facilityCount === "20") {
            destinationsFileName = `data/destinations_${povertyValue}_${incomeValue}_${unemploymentValue}.csv`;
            linesFileName = `data/lines_${povertyValue}_${incomeValue}_${unemploymentValue}.csv`;
        } else { // For 5 or 10 facilities
            destinationsFileName = `data/destinations_${facilityCount}_${povertyValue}_${incomeValue}_${unemploymentValue}.csv`;
            linesFileName = `data/lines_${facilityCount}_${povertyValue}_${incomeValue}_${unemploymentValue}.csv`;
        }

        console.log("Attempting to load:", destinationsFileName, linesFileName);

        // Load highlighted facilities first
        loadHighlightedFacilities(destinationsFileName)
            .then(facilities => {
                // If facilities loaded successfully, load nodes
                if (facilities.length > 0) {
                    return loadNodes(facilities);
                } else {
                    // If facilities file failed, stop processing this dataset
                    throw new Error(`Facilities file ${destinationsFileName} could not be loaded or is empty.`);
                }
            })
            .then(result => {
                // If nodes loaded, load lines
                loadLines(linesFileName, result.nodeCoordinates, result.bounds);
            })
            .catch(error => {
                console.error("Error loading dataset:", error);
                // Show error message
                if (errorMessageDiv) {
                    errorMessageDiv.textContent = "Failed to load data for the selected parameters. Please try a different combination.";
                    errorMessageDiv.style.display = 'block';
                }
                // Clear layers again in case partial data was loaded before error
                nodesLayer.removeAll();
                linesLayer.removeAll();
                highlightedFacilitiesLayer.removeAll();
            });
    }
    
    // Function to load highlighted facilities from the specified file
    function loadHighlightedFacilities(fileName) {
        console.log("Loading facilities file:", fileName);
        return esriRequest(fileName, {
            responseType: "text"
        }).then(function(response) {
            const data = response.data.trim();
            if (!data) {
                console.warn(`Facilities file ${fileName} is empty.`);
                highlightedFacilities = [];
                return highlightedFacilities;
            }
            highlightedFacilities = data.split(',').map(id => parseInt(id.trim())).filter(id => !isNaN(id));
            console.log(`Highlighted facilities from ${fileName}:`, highlightedFacilities);
            return highlightedFacilities;
        }).catch(function(error) {
            console.error(`Error loading highlighted facilities from ${fileName}:`, error.message || error);
            highlightedFacilities = []; // Ensure it's empty on error
             // Display error message to user
             const errorMessageDiv = document.getElementById("errorMessage");
             if(errorMessageDiv) {
                 errorMessageDiv.textContent = `Error: Could not load data for the selected criteria (${fileName}). Please try different parameters.`;
                 errorMessageDiv.style.display = 'block'; // Make it visible
             } else {
                 console.error("Error message container not found.");
             }
             // Clear the map
             nodesLayer.removeAll();
             linesLayer.removeAll();
             highlightedFacilitiesLayer.removeAll();
            return highlightedFacilities; // Return empty array to allow promise chain to potentially continue or be caught
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
                
                // The index in the file corresponds to both OriginID and DestinationID
                const nodeId = index + 1;

                // Skip specific node IDs requested by the user
                if ([668, 611, 612].includes(nodeId)) {
                    console.log(`Skipping filtered node ID: ${nodeId}`);
                    return; // Skip the rest of the processing for this node
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
                nodeCoordinates[nodeId] = {
                    longitude: longitude,
                    latitude: latitude
                };

                // Check if this node is in the highlighted facilities list
                const isHighlighted = facilities.includes(nodeId);

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
    
    // Function to load lines data from the specified file
    function loadLines(fileName, nodeCoords, bounds) {
        console.log("Loading lines file:", fileName);
        const batchSize = 2000; // Adjust batch size based on performance

        esriRequest(fileName, {
            responseType: "text"
        }).then(function(response) {
            const csvData = parseCSV(response.data);
            let graphicsBatch = [];
            let processedCount = 0;
            let validLines = 0;
            let skippedLines = 0;

            console.log("CSV headers:", Object.keys(csvData[0] || {}));

            function processBatch() {
                const batchEnd = Math.min(processedCount + batchSize, csvData.length);
                for (let i = processedCount; i < batchEnd; i++) {
                    const row = csvData[i];
                    
                    // Skip rows without valid data
                    if (!row) continue;

                    // Get the origin and destination IDs
                    const originId = parseInt(row.OriginID);
                    const destinationId = parseInt(row.DestinationID);
                    
                    // Skip if we don't have valid IDs
                    if (isNaN(originId) || isNaN(destinationId)) {
                        skippedLines++;
                        continue;
                    }

                    // Get length from appropriate field - files can have different column names
                    let length = 0;
                    if (row.Shape_Length) {
                        length = parseFloat(row.Shape_Length);
                    } else if (row.Total_Length) {
                        length = parseFloat(row.Total_Length);
                    } else if (row.Total_Kilometers) {
                        length = parseFloat(row.Total_Kilometers);
                    }

                    // Check if both origin and destination coordinates exist
                    if (!nodeCoords[originId] || !nodeCoords[destinationId]) {
                        skippedLines++;
                        continue;
                    }

                    // Get coordinates for both points
                    const origin = nodeCoords[originId];
                    const destination = nodeCoords[destinationId];
                    
                    // Validate coordinates
                    if (!isCoordinateValid(origin, bounds) || !isCoordinateValid(destination, bounds)) {
                        skippedLines++;
                        continue;
                    }

                    // Create polyline connecting the two points
                    const polyline = new Polyline({
                        paths: [[[origin.longitude, origin.latitude], [destination.longitude, destination.latitude]]]
                    });

                    // Line color and thickness
                    const lineWidth = Math.max(0.5, Math.min(2.5, 3 - (length / 5000)));
                    
                    const lineSymbol = {
                        type: "simple-line",
                        color: [50, 50, 50, 0.75],  // More transparent for better visualization
                        width: lineWidth
                    };

                    const polylineGraphic = new Graphic({
                        geometry: polyline,
                        symbol: lineSymbol,
                        attributes: {
                            OriginID: originId,
                            DestinationID: destinationId,
                            Length: length.toFixed(2)
                        }
                    });
                    
                    graphicsBatch.push(polylineGraphic);
                    validLines++;
                }

                // Add the batch to the layer
                if (graphicsBatch.length > 0) {
                    linesLayer.addMany(graphicsBatch);
                    graphicsBatch = []; // Clear the batch
                }

                processedCount = batchEnd;

                // If more data to process, continue in the next frame
                if (processedCount < csvData.length) {
                    requestAnimationFrame(processBatch);
                } else {
                    console.log(`Finished loading lines: ${validLines} valid, ${skippedLines} skipped`);
                    // Zoom to highlighted facilities after lines are loaded
                    zoomToHighlightedFacilities(view, nodeCoords, highlightedFacilities);
                    
                    // Clear any previous error messages if successful
                    const errorMessageDiv = document.getElementById("errorMessage");
                    if (errorMessageDiv) {
                        errorMessageDiv.textContent = '';
                        errorMessageDiv.style.display = 'none'; // Hide it
                    }
                }
            }

            // Start processing the first batch
            requestAnimationFrame(processBatch);

        }).catch(function(error) {
            console.error(`Error loading lines from ${fileName}:`, error.message || error);
            // Display error message to user
            const errorMessageDiv = document.getElementById("errorMessage");
            if (errorMessageDiv) {
                errorMessageDiv.textContent = `Error: Could not load data for the selected criteria (${fileName}). Please try different parameters.`;
                errorMessageDiv.style.display = 'block'; // Make it visible
            } else {
                console.error("Error message container not found.");
            }
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
    
    // Set initial active state for facility count buttons
    updateFacilityButtonStyles();
    
    // Load initial dataset
    reloadData();
});
