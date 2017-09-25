
Python script (web app coming soon) to figure out what CS upper divs course you completed all prereqs for. Also tells you which one of those are 
being offered this quarter.  

Current status: Alpha  
Next epic: 1.0 Basic web interface

## Design:  
Parse uci cs course prequisites: https://www.reg.uci.edu/cob/prrqcgi?dept=COMPSCI&term=201792&action=view_all  
Parse uci cs course offering: https://www.reg.uci.edu/perl/WebSoc  
Get input for prequisites they already completed   
Calculate the courses user can take (show all or show only courses offered in upcoming quarter)  

## Usage
1) input courses completed in inputs.py 
2) TEMPORARY: run __main__.py to see console. Working on web interface!...

Example console output:  
  
*** Based on the course you completed ***  
  I&C SCI 6B    
  I&C SCI 6D    
  I&C SCI 6N  
  I&C SCI 23  
  I&C SCI 45C  
  I&C SCI 46  
  I&C SCI 23  
  I&C SCI 23  
  MATH 2A  
  MATH 2B  
  STATS 67  
  COMPSCI 121  
  COMPSCI 122A  
  COMPSCI 122B  
  COMPSCI 132  
  
*** CS upper div you can take ***   
  COMPSCI 111 - DIGITAL IMAGE PROC  
  COMPSCI 116 - COMP PHOTO & VISION  
  COMPSCI 133 - ADV COMPUTER NETWKS  
  COMPSCI 161 - DES&ANALYS; OF ALGOR  
  COMPSCI 162 - FORMAL LANG & AUTM  
  COMPSCI 164 - COMPUTATIONAL GEO  
  COMPSCI 169 - INTRO OPTIMIZATION  
  COMPSCI 171 - INTRO ARTIFCL INTEL  
  COMPSCI 177 - APP OF PROB IN CS  
  COMPSCI 178 - MACHINE/DATA MINING  
  COMPSCI 179 - ALGRTMS GRAPH MDLS  
  COMPSCI 184A - ALGRTHMS FOR MOLBIO  
  
*** CS upper div you can take in Fall 2017 ***  
  COMPSCI 161 - DES&ANALYS; OF ALGOR  
  COMPSCI 169 - INTRO OPTIMIZATION  
  COMPSCI 171 - INTRO ARTIFCL INTEL  
  COMPSCI 177 - APP OF PROB IN CS  
  COMPSCI 178 - MACHINE/DATA MINING  
  

