# Consolidate blender datablocks

Purpose: To consolidate duplicate datablocks in a blend into one single reference.

[Demo gif](/demo.gif)


Currently, this script will just consolidate images. The aim is so that after running, any duplicate datablocks like "image.001" and "image.002" will be consolidated down to just "image", remapping existing references to this single image. It will NOT remove/modify any images that have fake user enabled. This may be used as a skipping flag in case modifications are done to any individual image. The script does *not* check that the actual data is the same, just if the name is the same. 

An optional input also allows you to immediately remove the old *.001 etc datablocks outright; default is false

Future goals: automate this to the degree of being able to consolidate more datatypes. Also, currently only supports blender 2.78+ due to the inclusion of the user_remap function on image blocks. 

