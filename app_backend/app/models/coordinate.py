class Coordinate:
    def __init__(self,latitude,longitude):
        self.latitude=latitude
        self.longitude=longitude

    def __composite_values__(self):
        return self.latitude,self.longitude
    
    def __repe__(self):
        return f"Coordinates({self.latitude}, {self.longitude})"
    
    def __ep__(self, other):
        return (
            isinstance(other,Coordinate)and
            other.latitude == self.latitude and 
            other.longitude == self.longitude
        )