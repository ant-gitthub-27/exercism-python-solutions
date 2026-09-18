class SpaceAge:
    EARTH_SECS = 31557600
    PLANETS_DATA = dict(Mercury = 0.2408467, Venus = 0.61519726, Earth = 1.0, Mars = 1.8808158, Jupiter = 11.862615, Saturn = 29.447498, Uranus = 84.016846, Neptune = 164.79132)
    def __init__(self, seconds):
        self.seconds = seconds
    def _calculate_age(self, planet):
        return round((self.seconds/self.EARTH_SECS)/self.PLANETS_DATA[planet], 2)
                    
                     
    def on_mercury(self) -> float:
        return self._calculate_age("Mercury")
    
    def on_venus(self):
        return self._calculate_age("Venus")

    def on_earth(self):
        return self._calculate_age("Earth")

    def on_mars(self):
        return self._calculate_age("Mars")

    def on_jupiter(self):
        return self._calculate_age("Jupiter")

    def on_saturn(self):
        return self._calculate_age("Saturn")

    def on_uranus(self):
        return self._calculate_age("Uranus")

    def on_neptune(self):
        return self._calculate_age("Neptune")