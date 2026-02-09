from database.db_manager import get_connection

class Food:
    def __init__(self, name, calories, protein, carbs, fat, serving_size=100, serving_unit="g", source="custom"):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.serving_size = serving_size
        self.serving_unit = serving_unit
        self.source = source
    
    def save(self):
        conn = get_connection()
        conn.execute("""
            INSERT INTO foods (name, calories, protein, carbs, fat, 
                             serving_size, serving_unit, source)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, [self.name, self.calories, self.protein, self.carbs, 
              self.fat, self.serving_size, self.serving_unit, self.source]
              )
        conn.close()

    @staticmethod
    def search(query):
        conn = get_connection()
        results = conn.execute("""
            SELECT * FROM foods 
            WHERE WHERE LOWER(name) LIKE LOWER(?) = {}
        """, [f"%{query}%"]).fetchdf()

        conn.close()
        return results

    @staticmethod
    def get_all():
        """Récupère tous les aliments"""
        conn = get_connection()
        results = conn.execute("SELECT * FROM foods ORDER BY name").fetchdf()
        conn.close()
        return results 