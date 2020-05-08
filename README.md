# SSWC Database Interface

This is a python GUI interface that allows you to interact with the Southern Sierra Wildflower Club's (SSWC) database, an organization whose members are interested in observing wildflowers in their native habitat in the southernpart of the Sierra Nevada mountains of California.

## SSWC Database Description:

* SIGHTINGS (NAME, PERSON, LOCATION, SIGHTED)
* FEATURES (LOCATION, CLASS, LATITUDE, LONGITUDE, MAP, ELEV)
* FLOWERS (GENUS, SPECIES, COMNAME)

The database tables have the following semantics:
* SIGHTINGS gives information that describes every time that a member of the club observes one of the wildflowers described in the table FLOWERS.NAME tells the name of the flower observed, PERSON describes who saw the flower,LOCATION tells the name of a nearby geographical feature where the flower was seen, and SIGHTED tells the day when the flower was seen.
* FEATURES lists the various locations where flowers have been observed.  LOCATION is the name of the place, CLASSis the type of place.  There are several types such as Summit, Mine, Locale, etc.  LATITUDE and LONGITUDE describe where on the surface of the earth the locations are found.MAP tells the name of the topographic map where the feature can be found and ELEV tells the height of the feature.
* FLOWERS lists all of the flowers that the members of the SSWC try to find.  GENUS and SPECIES give the scientific name for the flower, and COMNAME gives the non-scientific name (SIGHTING.NAME is a foreign key into FLOWER.COMNAME)

## File Descriptions

### /SSWC_Flower_Pics/

This directory holds pictures of all the flowers in the database.  They are displayed within the pyhton GUI when you are querying for them.  All the pictures are in the format of: "Genus Species.jpg" 

### /Table Logs/

In the python GUI you are able to export the audit logs of any of the tables.  When you export the files, the "<Table Name>_LOG.txt" will appear in the folder.  You can use these logs to see any changes you have made to the database and potentially revert actions in the database.

### Database_Interface.py