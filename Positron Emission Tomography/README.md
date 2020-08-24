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

The following table provides relevant information regarding the configurations used for each of the data runs.

| Run # | Number of Sources | Detector separation [mm] | Lead slit width [mm] | Copper slit width [mm] | y distance moved [mm] | y distance step [mm] | total angular rotation [deg.] | angular rotation step [deg.] | collection time [sec.] |
|-------|-------------------|--------------------------|----------------------|------------------------|-----------------------|----------------------|-------------------------------|------------------------------|------------------------|
| 001   | 1                 | ?                        |                      |                        |                       |                      |                               |                              |                        |
| 002   | 1                 | ?                        |                      |                        |                       |                      |                               |                              |                        |
| 003   | 1                 | ?                        |                      |                        |                       |                      |                               |                              |                        |
| 004   | 1                 | ?                        |                      |                        |                       |                      |                               |                              |                        |
| 005   | 2                 | ?                        |                      |                        |                       |                      |                               |                              |                        |
| 006   | 2                 |                          |                      |                        |                       |                      |                               |                              |                        |
| 007   | 1                 |                          | max?                 | max?                   |                       |                      |                               |                              |                        |
| 008   | 1                 |                          | 0                    | max?                   |                       |                      |                               |                              |                        |
| 009   | 1                 |                          | max?                 | 0                      |                       |                      |                               |                              |                        |
| 010   | 1                 |                          | 0                    | 0                      |                       |                      |                               |                              |                        |
