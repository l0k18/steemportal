#!/bin/bash
# This file currently is not in use, but will be implemented as the gtk3/glib2 parts
# are added
sudo cp steemportal.gschema.xml /usr/share/glib-2.0/schemas/
sudo glib-compile-schemas /usr/share/glib-2.0/schemas
