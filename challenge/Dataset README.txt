PEMS-BAY This traffic dataset is collected by California Transportation Agencies (CalTrans) Performance Measurement System (PeMS). We select 325 sensors in the San Fransisco Bay Area and collect 6 months of data ranging from Jan 1st 2017 to May 31th 2017 for the experiment.

The dataset provided consists of 3 files.

1. speed_sensor_data.csv
The average speed captured by each traffic sensor [mph]

Columns:
- Column 1 shows the timestamp of which 5 min interval the corresponding speed was captured. 
- Column 2-n is the unique traffic sensor IDs.
Rows:
- Each row is a timestamp with 5 min intervals having data from Jan 1st 2017 to June 30st 2017.


2. geo_sensor_locations_bay.csv
Contains the geo location information of the traffic sensor [lat/long]

Columns:
- Unique traffic sensor ID
- Latitude 
- Longitude 
Rows:
- One row for each unique traffic sensor id.


3. adjacent_sensor_distances_bay.csv
Contains information regarding the distances between the traffic sensors [feet]

Columns: 
- From (sensor ID)
- To (sensor ID)
- Distance (between the two sensors)
Rows:
- There exist multiple rows for each sensor ID depending on which other sensors are adjacent to it. Do note that not all sensor combinations are found in the dataset, as only distance information exists for sensors in proximity to each other.


