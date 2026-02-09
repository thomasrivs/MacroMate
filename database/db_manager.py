import duckdb
from pathlib import Path

DB_PATH = "nutrition_tracker.db"

def get_connection():
    return duckdb.connect(DB_PATH)

def init_database():
    conn = get_connection()

    schema_path = Path(__file__).parent / "schema.sql"
    with open(schema_path, 'r') as f:
        schema = f.read()

    conn.execute(schema)

    result = conn.execute("SELECT COUNT(*) FROM user_goals").fetchone()
    if result[0] == 0:
        conn.execute("""
            INSERT INTO user_goals (calories_target, protein_target, carbs_target, fat_target)
            VALUES (2790, 160, 380, 70)
            """)
    

    conn.close()
    
if __name__ == "__main__":
    init_database()
