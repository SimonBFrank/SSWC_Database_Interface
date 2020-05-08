import sqlite3
import os

def initialize():
	print('Currently initializing tables and setting up triggers...')
	connection = sqlite3.connect('flowers2019.db')
	c = connection.cursor()
	c.execute("""
	CREATE table if not EXISTS SIGHTINGS_LOG(
	Change text NOT NULL,
	OldName varchar(30) NULL,
	NewName varchar(30) NULL,
	OldPerson varchar(30) NULL,
	NewPerson varchar(30) NULL,
	OldLocation varchar(30) NULL,
	NewLocation varchar(30) NULL,
	OldSighted date NULL,
	NewSighted date NULL
	)		
	""")

	c.execute("""
	CREATE TRIGGER sighting_insert
	After INSERT on SIGHTINGS
	begin
	INSERT into SIGHTINGS_LOG VALUES ("Insert", NULL, NEW.name, NULL, NEW.person, NULL, NEW.location, NULL, NEW.sighted);
	END;""")

	c.execute("""
	CREATE TRIGGER sighting_delete
	After DELETE on SIGHTINGS
	begin
	INSERT into SIGHTINGS_LOG VALUES ("Delete", OLD.name, NULL, OLD.person, NULL, OLD.location, NULL, OLD.sighted, NULL);
	END;""")

	c.execute("""
	CREATE TRIGGER sighting_update
	After UPDATE on SIGHTINGS
	begin
	INSERT into SIGHTINGS_LOG VALUES ("Update", OLD.name, NEW.name, OLD.person, NEW.person, OLD.location, NEW.location, OLD.sighted, NEW.sighted);
	END;""")
	print('1.) Tables and triggers associated with SIGHTINGS are complete.')
	c.execute("""
	CREATE table if not EXISTS MEMBERS_LOG(
	Change text NOT NULL,
	OldName varchar(30) NULL,
	NewName varchar(30) NULL,
	OldMemberSince Date NULL,
	NewMemberSince date NULL,
	OldNumSightings int NULL,
	NewNumSightings int NULL
	)
		""")

	c.execute("""
	CREATE TRIGGER member_insert
	After INSERT on MEMBERS
	begin
	INSERT into MEMBERS_LOG VALUES ("Insert", NULL, NEW.name, NULL, NEW.membersince, NULL, NEW.numsightings);
	END;""")

	c.execute("""
	CREATE TRIGGER member_delete
	After DELETE on MEMBERS
	begin
	INSERT into MEMBERS_LOG VALUES ("Delete", OLD.name, NULL, OLD.membersince, NULL, OLD.numsightings, NULL);
	END;""")

	c.execute("""
	CREATE TRIGGER member_update
	After UPDATE on MEMBERS
	begin
	INSERT into MEMBERS_LOG VALUES ("Update", OLD.name, NEW.name, OLD.membersince, NEW.membersince, OLD.numsightings, NEW.numsightings);
	END;""")

	print('2.) Tables and triggers associated with MEMBERS are complete.')

	c.execute("""
	CREATE table if not EXISTS FLOWERS_LOG(
	Change text NOT NULL,
	OldGenus varchar(30) NULL,
	NewGenus varchar(30) NULL,
	OldSpecies varchar(30) NULL,
	NewSpecies varchar(30) NULL,
	OldComname varchar(30) NULL,
	NewComname varchar(30) NULL
	)""")

	c.execute("""
	CREATE TRIGGER flower_insert
	After INSERT on FLOWERS
	begin
	INSERT into FLOWERS_LOG VALUES ("Insert", NULL, NEW.genus, NULL, NEW.species, NULL, NEW.comname);
	END;""")

	c.execute("""
	CREATE TRIGGER flower_delete
	After DELETE on FLOWERS
	begin
	INSERT into FLOWERS_LOG VALUES ("Delete", OLD.genus, NULL, OLD.species, NULL, OLD.comname, NULL);
	END;""")

	c.execute("""
	CREATE TRIGGER flower_update
	After UPDATE on FLOWERS
	begin
	INSERT into FLOWERS_LOG VALUES ("Update", OLD.genus, NEW.genus, OLD.species, NEW.species, OLD.comname, NEW.comname);
	END;""")

	print('3.) Tables and triggers associated with FLOWERS are complete.')

	c.execute("""
	CREATE table if not EXISTS FEATURES_LOG(
	Change text NOT NULL,
	OldLocation varchar(30) NULL,
	NewLocation varchar(30) NULL,
	OldClass varchar(30) NULL,
	NewClass varchar(30) NULL,
	OldLatitude int NULL,
	NewLatitude int NULL,
	OldLongitude int null,
	NewLongitude int NULL,
	OldMap varchar(30) NULL,
	NewMap Varchar(30) NULL,
	OldElev int NULL,
	NewElev int NULL
	)""")

	c.execute("""
	CREATE TRIGGER feature_insert
	After INSERT on FEATURES
	begin
	INSERT into FEATURES_LOG VALUES ("Insert", NULL, NEW.location, NULL, NEW.class, NULL, NEW.latitude, NULL, NEW.longitude, NULL, NEW.map, NULL, NEW.elev);
	END;""")

	c.execute("""
	CREATE TRIGGER feature_delete
	After DELETE on FEATURES
	begin
	INSERT into FEATURES_LOG VALUES ("Delete", OLD.location, NULL, OLD.class, NULL, OLD.latitude, NULL, OLD.longitude, NULL, OLD.map, NULL, OLD.elev, NULL);
	END;""")

	c.execute("""
	CREATE TRIGGER feature_update
	After UPDATE on FEATURES
	begin
	INSERT into FEATURES_LOG VALUES ("Update", OLD.location, NEW.location, OLD.class, NEW.class, OLD.latitude, NEW.latitude, OLD.longitude, NEW.longitude, OLD.map, NEW.map, OLD.elev, NEW.elev);
	END;
	""")

	print('4.) Tables and triggers associated with FEATURES are complete.')

	c.execute("""
	CREATE INDEX sightingDate
	on SIGHTINGS(name);""")

	c.execute("""	
	CREATE INDEX sightingLocation
	on SIGHTINGS(name);""")

	c.execute("""
	CREATE INDEX sightingPerson
	on SIGHTINGS(name);""")

	c.execute("""
	CREATE INDEX sightedFlowers
	on SIGHTINGS(name);""")

	print('5.) Indices for the columns of SIGHTINGS are created.')

	connection.commit()
	connection.close()

initialize()