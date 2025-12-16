
CREATE TABLE IF NOT EXISTS passenger_classes (
    id SERIAL PRIMARY KEY,
    class_number INT UNIQUE NOT NULL CHECK (class_number BETWEEN 1 AND 3),
    description VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS embarkation_ports (
    id SERIAL PRIMARY KEY,
    code CHAR(1) UNIQUE NOT NULL,
    name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    passenger_ref INT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    sex VARCHAR(10) CHECK (sex IN ('male', 'female')),
    age NUMERIC(5,2),
    survived BOOLEAN NOT NULL,
    sib_sp INT DEFAULT 0 CHECK (sib_sp >= 0),
    parch INT DEFAULT 0 CHECK (parch >= 0),
    ticket VARCHAR(50),
    fare NUMERIC(10,2) CHECK (fare >= 0),
    cabin VARCHAR(50),
    class_id INT REFERENCES passenger_classes(id) ON DELETE SET NULL,
    embarkation_id INT REFERENCES embarkation_ports(id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_passengers_ref ON passengers(passenger_ref);
CREATE INDEX IF NOT EXISTS idx_passengers_survived ON passengers(survived);
CREATE INDEX IF NOT EXISTS idx_passengers_sex ON passengers(sex);
CREATE INDEX IF NOT EXISTS idx_passengers_class ON passengers(class_id);
CREATE INDEX IF NOT EXISTS idx_passengers_embarkation ON passengers(embarkation_id);
CREATE INDEX IF NOT EXISTS idx_passengers_age ON passengers(age);
CREATE INDEX IF NOT EXISTS idx_passengers_fare ON passengers(fare);