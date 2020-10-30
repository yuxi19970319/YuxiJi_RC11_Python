import csv
import requests
from PIL import Image
from io import BytesIO

class ArtMoMA:
    def __init__(self, id, width, depth, height, imageUrl, artist):
        self.id = id
        self.width = width
        self.depth = depth
        self.height = height
        self.imageUrl = imageUrl
        self.artist = artist
        self.imagePath = ''

        if self.width:
            self.width = float(self.width) * 10
        else:
            self.width = 10

        if self.height:
            self.height = float(self.height) * 10
        else:
            self.height = 10

        if self.depth:
            self.depth = float(self.depth) * 10
        else:
            self.depth = 10

    def describe(self):
        print("artist:" + self.artist, "id:" + self.id, "width:" + str(self.width), "depth:" + str(self.depth), "height:" + str(self.height))

    def getImageFile(self):
        if self.imageUrl:
            response = requests.get(self.imageUrl)
            try:
                im = Image.open(BytesIO(response.content))
            except OSError:
                return None
            path = "ArtImages\ "+ self.artist +"_" +self.id+ ".jpg"
            self.imagePath = path
            im.save(path, "JPEG")

artPieces = []
with open("CSVFiles\Artworks.csv", encoding = 'utf-8-sig') as artFile:
    artReader = csv.DictReader(artFile)

    for row in artReader:
        id = row['ObjectID']
        width = row['Width (cm)']
        height = row['Height (cm)']
        depth = row['Depth (cm)']
        imageUrl = row['ThumbnailURL']
        artist = row['Artist']
        if width or depth or height:
            artPiece = ArtMoMA(id, width, depth, height, imageUrl, artist)
            artPieces.append(artPiece)

for art in artPieces:
    if "Pollock" in art.artist:
        art.getImageFile()
