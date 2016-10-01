# Consolidate blender datablocks

Purpose: To consolidate duplicate datablocks in a blend into one single reference.

Currently, this script will just conolidate images. The aim is so that after running, any duplicate datablocks like "image.001" and "image.002" will be consoldiated down to just "image", remapping existing references to this single image

An optional input also allows you to immedaitely remove the old *.001 etc datablocks outright; default is false

Future goals: automate this to the degree of being able to consolidate more datatypes. Also, currently only supports blender 2.78+ due to the inclusion of the user_remap funciton on image blocks. 

