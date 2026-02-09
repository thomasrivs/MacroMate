CREATE TABLE IF NOT EXISTS foods (
    id INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL,
    calories DECIMAL(6,2),
    protein DECIMAL(5,2),
    carbs DECIMAL(5,2),
    fat DECIMAL(5,2),
    serving_size DECIMAL(6,2),
    serving_unit VARCHAR(20),
    source VARCHAR(50),  -- 'openfoodfacts', 'custom', 'favorite'
    barcode VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS daily_logs (
    id INTEGER PRIMARY KEY,
    log_date DATE NOT NULL,
    meal_type VARCHAR(20),  -- 'breakfast', 'lunch', 'dinner', 'snack'
    food_id INTEGER,
    quantity DECIMAL(6,2),
    logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (food_id) REFERENCES foods(id)
);

CREATE TABLE IF NOT EXISTS user_goals (
    calories_target INTEGER,
    protein_target INTEGER,
    carbs_target INTEGER,
    fat_target INTEGER,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);