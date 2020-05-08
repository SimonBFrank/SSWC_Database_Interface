# SSWC Database Interface

This is a python GUI that allows you to interact with the Southern Sierra Wildflower Club's (SSWC) database, an organization whose members are interested in observing wildflowers in their native habitat in the southernpart of the Sierra Nevada mountains of California.

## Functionality

* Login system that requires you to signup and login using username and password.  There are no requirements for the username and password and there is no encryption on the password.  This system is not secure and should not be used to hold any important data
* Allows you to insert new flower sightings by adding the flower's name, person's name, location, and date it was sighted
* Update the flower information by choosing from a list of flowers and changing the flower's genus, species, or common name
* Query for all flower sightings by selecting which flower you want to see where it was sighted from a list and then you can see who saw it, the location, and date
* Delete a sighting using a atomic transaction by choosing which flower had the sighting and then selecting the person who saw it
* Export all the changes made to a table by selecting it from a menu

## SSWC Database Description:

Database Schema:
* SIGHTINGS (NAME, PERSON, LOCATION, SIGHTED)
* FEATURES (LOCATION, CLASS, LATITUDE, LONGITUDE, MAP, ELEV)
* FLOWERS (GENUS, SPECIES, COMNAME)

The database tables have the following semantics:
* SIGHTINGS gives information that describes every time that a member of the club observes one of the wildflowers described in the table FLOWERS.NAME tells the name of the flower observed, PERSON describes who saw the flower,LOCATION tells the name of a nearby geographical feature where the flower was seen, and SIGHTED tells the day when the flower was seen.
* FEATURES lists the various locations where flowers have been observed.  LOCATION is the name of the place, CLASSis the type of place.  There are several types such as Summit, Mine, Locale, etc.  LATITUDE and LONGITUDE describe where on the surface of the earth the locations are found.MAP tells the name of the topographic map where the feature can be found and ELEV tells the height of the feature.
* FLOWERS lists all of the flowers that the members of the SSWC try to find.  GENUS and SPECIES give the scientific name for the flower, and COMNAME gives the non-scientific name (SIGHTING.NAME is a foreign key into FLOWER.COMNAME)

## Required packages

* tkinter
* sqlite3
* PIL
* pandas
* data
* os

## File Descriptions

### /SSWC_Flower_Pics/

This directory holds pictures of all the flowers in the database.  They are displayed within the pyhton GUI when you are querying for them.  All the pictures are in the format of: "Genus Species.jpg" 

### /Table Logs/

In the python GUI you are able to export the audit logs of any of the tables.  When you export the files, the "<Table Name>_LOG.txt" will appear in the folder.  You can use these logs to see any changes you have made to the database and potentially revert actions in the database.

### Database_Interface.py

Creates and runs the tkinter GUI.

### flowers2019.db

SSWC SQL database.

### Initialized_Tables.py

Initializes the audit log tables and the triggers for the database.

### Login_Info.txt

Holds the username and password information for login.

## Author

Simon Frank
linkedin.com/in/simon-frank/
github.com/SimonBFrank/
