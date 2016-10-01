"""
Consolidate datablocks

Currently, this script will just consolidate images. The aim is so that after
running, any duplicate datablocks like "image.001" and "image.002" will be
consolidated down to just "image", remapping existing references to this 
single image

An optional input also allows you to immediately remove the old *.001 etc
datablocks outright; default is false

Future goals: automate this to the degree of being able to consolidate 
more datatypes.

Written by Patrick W. Crawford, MIT license
"""


import bpy


def consolidateImages(removeold=False):
	nameCat = {}

	for im in bpy.data.images:
		# get list of other names
		base = getBaseName(im.name)
		if base not in nameCat:
			nameCat[base] = [im.name]
		elif im.name not in nameCat[base]:
			nameCat[base].append(im.name)
		else:
			print("Skipping, already added image")

	print(list(nameCat))
	for base in nameCat:
		if len(base)<2: continue
		# loop over every name group
		nameCat[base].sort() # in-place sorting
		baseImg = bpy.data.images[ nameCat[base][0] ]
		#print("Base img is: ",baseImg.name)
		
		for imgname in nameCat[base][1:]:
			#print("remapping:", bpy.data.images[imgname].name, " # ", baseImg.name)
			remap_users(bpy.data.images[imgname],baseImg)
			if removeold==True and bpy.data.images[imgname].users==0:
				bpy.data.images.remove( bpy.data.images[imgname] )
		
		# Final step.. rename to not have .001 if it does
		if baseImg.name != getBaseName(baseImg.name):
			if getBaseName(baseImg.name) in bpy.data.images and bpy.data.images[getBaseName(baseImg.name)].users!=0:
				pass
			else:
				baseImg.name = getBaseName(baseImg.name)
		else:
			baseImg.name = getBaseName(baseImg.name)


# determines if name has duplicate extension, e.g. jpeg.002
def duped(name):
	try:
		if name[-4]!=".": return False
		int(name[-3:])
		return True
	except:
		return False


# gets base name from datablock name
def getBaseName(name):
	if duped(name) == True:
		return name[:-4]
	else:
		return name


# todo: write equivalent function of user_remap for older blender versions
def remap_users(old, new):
	if bpy.app.version[0]==2 and bpy.app.version[1] < 78:
		raise ValueError("Error: not available prior to blender 2.78")
		return
	
	old.user_remap( new )


# run the main script
consolidateImages(True) # false or empty to not auto-remove old references

