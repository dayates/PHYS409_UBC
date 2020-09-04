# Positron Emission Tomography

## Format of individual data files

Data is collected in a file with the following naming format:

[DATE], [TIME], [SCAN#], [ANGLE IN DEGREES] Deg.dat

For example:

Aug-01-20, 1_30 PM, Scan1, -50_4 Deg.dat

The data within these files is of the following format:

Distance (mm)	Counts
0.0	130.0
0.2	178.0
0.4	170.0
0.6	176.0
0.8	184.0
1.0	167.0
.
.
.

where the distance is the lateral distance that the source has been moved.

## Which run is which?

The following table provides relevant information regarding the configurations used for each of the data runs. runs 001-004 have not been labelled in this table. As it is up to you to identify the data sets with their respective parameter settings.

| Run # | Number of Sources | Detector separation [mm] | Lead slit width [mm] | Copper slit width [mm] | y distance moved [mm] | y distance step [mm] | total angular rotation [deg.] | angular rotation step [deg.] | number of collections per point | collection time [sec.] |
|-------|-------------------|--------------------------|----------------------|------------------------|-----------------------|----------------------|-------------------------------|------------------------------|---------------------------------|------------------------|
| ???   | 1                 | 122 +/- 3                | 4                    | 4                      | 20                    | 0.5                  | N/A                           | N/A                          | 1                               | 30                     |
| ???   | 1                 | 122 +/- 3                | 2                    | 2                      | 20                    | 0.5                  | N/A                           | N/A                          | 1                               | 30                     |
| ???   | 1                 | 122 +/- 3                | 0                    | 2                      | 20                    | 0.5                  | N/A                           | N/A                          | 1                               | 30                     |
| ???   | 1                 | 244 +/- 3                | 2                    | 2                      | 20                    | 0.5                  | N/A                           | N/A                          | 1                               | 30                     |
| 005   | 2                 | 122 +/- 3                | 2                    | 2                      | 20                    | 0.5                  | 180                           | 3.6                          | 1                               | 30                     |
| 006   | 1                 | 122 +/- 3                | Not in place         | 9.82 +/- 0.05          | N/A                   | N/A                  | N/A                           | N/A                          | 4                               | 30                     |
| 007   | 1                 | 122 +/- 3                | 0                    | 9.82 +/- 0.05          | N/A                   | N/A                  | N/A                           | N/A                          | 4                               | 30                     |
| 008   | 1                 | 122 +/- 3                | Not in place         | 0                      | N/A                   | N/A                  | N/A                           | N/A                          | 4                               | 30                     |
| 009   | 1                 | 122 +/- 3                | 0                    | 0                      | N/A                   | N/A                  | N/A                           | N/A                          | 4                               | 30                     |
