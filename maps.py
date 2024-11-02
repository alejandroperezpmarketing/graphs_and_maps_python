#Authon:Alejandro Perez

############ libraries
import numpy as np
from math import floor
from pyproj import Proj, transform

class CoordinatesOperations():
    
    def __init__(self,latitude,longitude) -> None:
        map = None
        self.latitude = latitude
        self.longitude = longitude
    
        
    def degrees_to_radians(self,latitude,longitude):
        
        latitude_rad = np.radians(latitude)
        longitude_rad = np.radians(latitude)
        degrees = [latitude, longitude]
        radians = [latitude_rad,longitude_rad]
        
        print(f"{degrees} degrees is equal to {radians} radians")
        
        return latitude_rad, longitude_rad

    def radians_to_degrees(latitude_rad,longitude_rad):
        
        latitude = np.degrees(latitude_rad)
        longitude = np.degrees(longitude_rad)
        
        degrees = [latitude, longitude]
        radians = [latitude_rad,longitude_rad]
        
        print(f"latitude and longitude {radians} radians is equal to {degrees} degrees")

        return latitude, longitude

    # Function to convert decimal degrees to DMS
    def decimal_to_dms(self,decimal_degree):
        degrees = int(decimal_degree)
        minutes_full = abs((decimal_degree - degrees) * 60)
        minutes = int(minutes_full)
        seconds = (minutes_full - minutes) * 60
        return degrees, minutes, seconds

        # # Example latitude and longitude
        # latitude = 40.748817
        # longitude = -73.985428

        # # Convert to DMS format
        # lat_dms = decimal_to_dms(latitude)
        # lon_dms = decimal_to_dms(longitude)

        # # Print the result
        # print(f"Latitude DMS: {lat_dms[0]}° {lat_dms[1]}' {lat_dms[2]:.2f}\"")
        # print(f"Longitude DMS: {lon_dms[0]}° {lon_dms[1]}' {lon_dms[2]:.2f}\"")


    """
    Decimal Degrees=D+M/60+S/3600
    D = degrees
    M = minutes
    S = seconds
    """


    # Function to convert DMS to Decimal Degrees
    def dms_to_decimal(self, degrees, minutes, seconds):
        decimal_degree = degrees + minutes / 60 + seconds / 3600
        return decimal_degree

    # Convert Decimal Degrees to Hexadecimal
    def decimal_to_hex(self, decimal_degree):
        # Convert to absolute hex (ignoring sign), and preserve 6 decimal places if necessary
        hex_value = float.hex(decimal_degree)
        return hex_value

        #####################################

        # # Example DMS values (latitude and longitude)
        # dms_lat = (40, 44, 55.74)  # Latitude DMS: 40° 44' 55.74"
        # dms_lon = (-73, 59, 7.54)  # Longitude DMS: -73° 59' 7.54"

        # # Convert DMS to Decimal Degrees
        # decimal_lat = dms_to_decimal(*dms_lat)
        # decimal_lon = dms_to_decimal(*dms_lon)

        # # Convert Decimal Degrees to Hexadecimal
        # hex_lat = decimal_to_hex(decimal_lat)
        # hex_lon = decimal_to_hex(decimal_lon)

        # # Print the results
        # print(f"Latitude (Decimal): {decimal_lat}, Latitude (Hexadecimal): {hex_lat}")
        # print(f"Longitude (Decimal): {decimal_lon}, Longitude (Hexadecimal): {hex_lon}")

    def latlon_to_utm(self,latitude, longitude):
        # Define the UTM zone based on the longitude
        self.utm_zone = int((longitude + 180) / 6) + 1
        # Define the UTM projection with WGS84 datum and calculated zone
        self.utm_proj = Proj(proj='utm', zone=self.utm_zone, datum='WGS84')
        # Define the geographic coordinate system for latitude and longitude
        self.geo_proj = Proj(proj='latlong', datum='WGS84')
        # Transform latitude and longitude to UTM
        self.easting, self.northing = transform(self.geo_proj, self.utm_proj, latitude, longitude)
        
        return self.easting, self.northing, self.utm_zone

    """     # Example usage
        lat = 40.7486   # Latitude of a location
        lon = -73.9864  # Longitude of a location
        easting, northing, zone = latlon_to_utm(lat, lon)
        print(f"Easting: {easting}, Northing: {northing}, UTM Zone: {zone}")
 """


class CreateMaps():
    
    def __init__(self) -> float:
        CoordinatesOperations.__init__(self,self.latitude,self.longitude)
        