# Imports:
# use python --version to check what version of python your standard installation is
# if this is 2.x you will have to use pip3 install otherwise pip install

import csv
import requests
from PIL import Image
from io import BytesIO

class ArtTate:
    def __init__(self, title, id, width, depth, height, imageUrl, artist):
        self.title = title
        self.id = id
        self.width = width
        self.depth = depth
        self.height = height
        self.imageUrl = imageUrl
        self.artist = artist
        self.imagePath = ''

        if self.width:
            self.width = width
        else:
            self.width = 1

        if self.height:
            self.height = height
        else:
            self.height = 1

        if self.depth:
            self.depth = depth
        else:
            self.depth = 1
    # Define a function that prints a description
    def describe(self):
        print("artist:" + self.artist, "title:" + self.title, "id:" + self.id, "width:" + str(self.width), "depth:" + str(self.depth), "height:" + str(self.height))


    # implement the get image function that saves the image to the specified folder
    def getImageFile(self):
        if self.imageUrl:
            response = requests.get(self.imageUrl)
            try:
                im = Image.open(BytesIO(response.content))
            except OSError:
                return None
            path = "Thumbnails\ "+self.artist +"_" +self.id+ ".jpg"
            self.imagePath = path
            im.save(path, "JPEG")

artPieces = []
with open("D:\\assignment\python\\file\YuxiJi_RC11_Python\Assignment1\csvFiles\\artwork_data.csv", encoding = 'utf-8-sig') as dataFile:
    artReader = csv.DictReader(dataFile)

    for row in artReader:
        title = row['title']
        id = row['id']
        width = row['width']
        height = row['height']
        depth = row['depth']
        imageUrl = row['thumbnailUrl']
        artist = row['artist']
        if width or depth or height:
            artPiece = ArtTate(id, title, width, depth, height, imageUrl, artist)
            artPieces.append(artPiece)

for art in artPieces:
    if "Leighton" in art.artist:
        art.getImageFile()
# Read in the rows of the artwork_data.csv file into a list of ArtTate objects

# write a loop that saves all artwork thumbnails of an artist to a specific folder
