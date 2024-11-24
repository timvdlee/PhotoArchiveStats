from PIL import Image
import os
import glob
import PIL.ExifTags
from datetime import datetime
from tqdm import tqdm
import pickle

class ImageExifData:
    def __init__(self,imageExif,filePath) -> None:
        self.fileName = os.path.basename(filePath)
        self.parentFolder = os.path.basename(os.path.dirname(filePath))
        self.yearFolder = os.path.split(os.path.split(os.path.dirname(filePath))[0])[1]
        
        #File data
        self.filePath = filePath
        self.fileSizeBytes = os.path.getsize(filePath)
        self.fileSize = self.fileSizeBytes/1024/1024
        self.fileType = os.path.splitext(filePath)[1]
                
        #Exif Data
        self.hasExif = bool(imageExif)
        
        self.dateTime = imageExif.get("DateTimeOriginal")
        
        self.SubjectDistance = imageExif.get("SubjectDistance")
        
        if imageExif.get("DateTimeOriginal") is None and imageExif.get("DateTime") is not None:
            self.dateTime = imageExif.get("DateTime")
        
        if self.dateTime:
            self.dateTime = datetime.strptime(self.dateTime, '%Y:%m:%d %H:%M:%S')
        self.CameraModel = imageExif.get("Model")
        if self.CameraModel:
            self.CameraModel = self.CameraModel.replace('\x00','')
        
        self.CameraMake = imageExif.get("Make")
        if self.CameraMake:
            self.CameraMake = self.CameraMake.replace('\x00','')
        self.GPSInfo = imageExif.get("GPSInfo")
        self.ISO = imageExif.get("ISOSpeedRatings")
        self.ExposureTime = imageExif.get("ExposureTime")
        self.FNumber = imageExif.get("FNumber")
        self.FocalLength = imageExif.get("FocalLength")
        self.LensModel = imageExif.get("LensModel")
        self.LensMake = imageExif.get("LensMake")
        self.Artist = imageExif.get("Artist")
        if self.Artist:
            self.Artist = self.Artist.replace('\x00','')
            
            
    def __str__(self):
        return f"Exif({self.parentFolder}/{self.fileName})"

    def __repr__(self):
        return f"Exif({self.parentFolder}/{self.fileName})"
            
    def get_fileName(self):
        return self.fileName
    
    def get_distance(self):
        return self.SubjectDistance

    def get_parentFolder(self):
        return self.parentFolder

    def get_yearFolder(self):
        return self.yearFolder

    def get_filePath(self):
        return self.filePath

    def get_fileSizeBytes(self):
        return self.fileSizeBytes

    def get_fileSize(self):
        return self.fileSize

    def get_fileType(self):
        return self.fileType

    def get_dateTime(self):
        return self.dateTime
    
    def get_date(self):
        return self.dateTime.date()
    
    def get_time(self): 
        return self.dateTime.time()
    
    def get_year(self):
        if self.dateTime:
            return self.dateTime.year
    
    def get_month(self):
        if self.dateTime:
            return self.dateTime.month
    
    def get_day(self):
        if self.dateTime:
            return self.dateTime.day

    def get_dayOfWeek(self):
        if self.dateTime:
            return self.dateTime.strftime("%A")
    
    def get_hour(self):
        return self.dateTime.hour
    
    def get_minute(self):
        return self.dateTime.minute
    
    def get_second(self):
        return self.dateTime.second
    
    def get_time_hhmm(self):
        return self.dateTime.strftime("%H:%M")

    def get_CameraModel(self):
        return self.CameraModel

    def get_CameraMake(self):
        return self.CameraMake

    def get_GPSInfo(self):
        return self.GPSInfo

    def get_ISO(self):
        return self.ISO

    def get_ExposureTime(self):
        return self.ExposureTime

    def get_FNumber(self):
        return self.FNumber

    def get_FocalLength(self):
        return self.FocalLength

    def get_LensModel(self):
        return self.LensModel

    def get_LensMake(self):
        return self.LensMake

    def get_Artist(self):
        return self.Artist




def main(archivePath):
    archive = []
    for filename in tqdm(glob.iglob(archivePath + '**/**', recursive=True),total=sum([len(files) for r, d, files in os.walk(archivePath)]),unit='photos'):
         if os.path.isfile(filename):
            try:
                img = Image.open(filename)
                exif_data = {
                    PIL.ExifTags.TAGS[k]: v
                    for k, v in img._getexif().items()
                    if k in PIL.ExifTags.TAGS
                        }
                archive.append(ImageExifData(exif_data,filename))

            
            except Exception as e:
                archive.append(ImageExifData({},filename))
                
    return archive
    
if __name__ == '__main__':
    import time
    start_time = time.time()
    currentArchive = "SleutelstamFotoArchief"
    # currentArchive = "testArchive"
    archive = main(currentArchive)
    
    with open(f'{currentArchive}.pkl', 'wb') as output:
        pickle.dump(archive, output, pickle.HIGHEST_PROTOCOL)
    
    print('--- %s seconds ---' % (time.time() - start_time))