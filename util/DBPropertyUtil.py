import os
class DBPropertyUtil:
    @staticmethod
    def get_db_properties():
        properties = {}
        path = os.path.join(os.path.dirname(__file__), "db.properties")

        try:
            with open(path, "r") as file:
                for line in file:
                    if line.strip() and not line.startswith("#"):
                        key, value = line.strip().split("=")
                        properties[key.strip()] = value.strip()
            return properties
        except FileNotFoundError:
            print("Error: db.properties file not found at", path)
            return {}
        except Exception as e:
            print("Error reading db.properties:", e)
            return {}
