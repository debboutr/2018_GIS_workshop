# 2018_GIS_workshop

*SMU_workshop*
start w/ catchments, full
get centroids
plot
get NARS data
make shp from  csv
heatmap from NARS of NO3

plot together with mike's catchment summarizations

2 NBs one that shows the analysis, the other steps through it
    * analysis just shows folium output along with explanations
    * steps NB shows:
        * DL NARS all
        * print tables ( cmd line )
        * access to envs through User local, 
CREATE --
    instruction in Anacona NB on Anaconda 

#! DL github repo -- extract/navigate cmd to there

SETUP --
    DL Anaconda -- use curl??
    install -- figure commands  for install
    
RUN --
    conda info -- ?? where does conda envs install -- python version 2.7.12.final.0!
    conda add channel ioos
    conda create -n gis jupyter geopandas folium spyder
    ####### should prompt for Y, hit enter
    activate gis
#! LEAVE WINDOWS OPEN
BEGIN --
    show abspath in cell -- explain how relativ/abs differ
    DL NARS data -- extract inside 2018_GIS_workshop
   
   ### Download [Anaconda](https://www.anaconda.com/download)
### Download [git](https://git-scm.com/download/win)

### Download [2018_GIS_workshop](https://github.com/debboutr/2018_GIS_workshop)

** steps for anaconda install **

DL [NARS data]() do Ctrl + F here a search for 'all' then arrow down to:
    
   **| Survey | Indicator | Data | Metadata |**
   
   **| Streams 2004-2005 | All | WSA All Data (ZIP)(1 pg, 7 MB) | |**
   
### click the '.zip' link for a folder of all tables

### open spyder w/ 'super' key  #! navigate to 
### open in cmd w/ spyder --new-instance


print tree of local dir
