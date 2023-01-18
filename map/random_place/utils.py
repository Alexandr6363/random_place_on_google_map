import random

Arr1 = ["S", "N"]
Arr2 = ["E", "W"]


class Coordinate:
        def __init__(self):
            self.meridian = round(random.uniform(0, 180), 5)
            self.palallels = round(random.uniform(0, 90), 5)
            self.meridian_degrees = random.randint(0, 180)
            self.meridian_minutes = random.randint(0, 60)
            self.meridian_seconds = round(random.uniform(0, 60), 1)
            self.side_SN = random.choice(Arr1)
            self.parallels_degrees = random.randint(0, 90)
            self.parallels_minutes = random.randint(0, 60)
            self.parallels_seconds = round(random.uniform(0, 60), 1)
            self.side_EW = random.choice(Arr2)
            self.coordinates = f"{self.side_SN} {str(self.palallels)} " \
               f"{self.side_EW} {str(self.meridian)}"
            self.coordinate_link = f"https://www.google.com/maps/place/" \
               f"{self.parallels_degrees:02}%C2%B0{self.parallels_minutes:02}'" \
               f"{self.parallels_seconds:04.1f}%22{self.side_SN}+" \
               f"{self.meridian_degrees:03}%C2%B0{self.meridian_minutes:02}'" \
               f"{self.meridian_seconds:04.1f}%22{self.side_EW}/"

        def __str__(self):
            return self.coordinate_link

        def get_coordinates(self):
            return self.coordinates

        def write_list_of_googlemap_link_in_file(self):
            with open("link_list.txt", "a") as file:
                file.write(self.coordinate_link)
                file.write("\n")

        def write_list_of_coordinates_in_file(self):
            with open("list_of_cord.txt", "a") as file:
                file.write(self.coordinates)
                file.write("\n")
