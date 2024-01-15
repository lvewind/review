from pykml import parser


def read_coordinate_in_kml(kml_file_path: str):
    with open(kml_file_path, encoding="utf-8") as f:
        doc = parser.parse(f).getroot()
        try:
            coordinates_str = str(doc.Document.Placemark.LineString.coordinates).strip()
            coordinates_split = coordinates_str.split(" ")
            coordinates = []
            for coordinate in coordinates_split:
                coordinate_item = coordinate.split(",")
                coordinates.append([float(coordinate_item[0]), float(coordinate_item[1]), float(coordinate_item[2])])
            return coordinates
        except AttributeError as e:
            print(e)
            return
