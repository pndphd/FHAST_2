if (FALSE) {
"

  
--------------------------------------------------------------------------------  
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@     @@@@   @@@@         @@@@@    @@@@@         @@@@@@         @@@
    @@@@           @@@@   @@@@        @@@@@@@    @@@     @@@@@@@@@@@@@     @@@@@
    @@@@@@@@@      @@@@@@@@@@@       @@@  @@@@    @@@@         @@@@@@@     @@@@@
    @@@@           @@@@   @@@@      @@@@@@@@@@@   @@    @@@     @@@@@@     @@@@@
    @@@@           @@@@   @@@@     @@@@     @@@@  @@@@@      @@@@@@@@@     @@@@@
                                                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@               &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   @@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                                         
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                     
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
-------------------------------------------------------------------------------- 

Version 2.1.4-beta (Sharp Scale) 2025-09-25

2.1.4-beta
Added in columns “Started” and “Completed” as required to the OHWM plugin. 
Changed the salmonid feeding algorithm to allow for search feeding. See section Feeding: Search in this document for details. 

2.1.4-beta
Changed formatting in the OHWM plugin report.

2.1.2-beta
Added in an adult spawning module

2.1.1
Code is restructured for efficiency in speed and memory use
Added in batch reprojection tool in gui
Added in report compare tool in gui
Added OHWM analysis

2.1.0
Code is restructured for efficiency in speed and memory use
Added in batch reprojection tool in gui
Added in report compare tool in gui
2.0.4
Added in the joint AOI feature. If two AOIs are supplied, a new AOI is created based on the intersection of the two supplied. 
Example files have also been updated with recommended food and predation levels.
These levels are recorded in the FHAST documentation.

2.0.3
Fixed flow raster bugs

2.0.2
Added in column remove feature
Prevented empty output folder name
fixed bug in raster flow list making procedure

2.0.1
Updated some error catches and design elements

2.0.0
FHAST 2 with QGIS GUI and example files.

  
  Development Team
    Peter N. Dudley (PI)
    Jesse A. Black
    Stephanie G. Diaz
    Ted W. Hermann
    Chris John  
    Kwanmok Kim
  
Contributions
    PD: Oversite, griding algorithm, sampling algorithm, summary procedures,
    shade algorithm
    JB: Metabolic algorithms and methods, food availability research
    SD: movement procedures, ABM structure coding, migration procedures
    TH: Adult migration algorithm, predation procedures
    CJ: GUI coding, pathfinding algorithm
    KK: Food availability research, feeding algorithm research
 
Notes
    -Using NetLogo 6.2.2 with vid extension disabled (removes log4*.jar files)

Citation
    Dudley, Peter N., Jesse A. Black, Stephanie G. Diaz, Ted W. Hermann, Chris John,
    Kwanmok Kim. FHAST: Fish Habitat Assessment and Simulation Tool. V2.1.4, 
    Released 2025. https://github.com/pndphd/FHAST_2.


"
}