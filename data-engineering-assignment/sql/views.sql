-- 1️⃣ View: Survival statistics by class
CREATE OR REPLACE VIEW v_survival_by_class AS
SELECT
  pc.class_number,
  COUNT(*) AS total_passengers,
  COUNT(*) FILTER (WHERE p.survived = true) AS survived,
  ROUND(
    COUNT() FILTER (WHERE p.survived = true)::NUMERIC / COUNT() * 100,
    2
  ) AS survival_rate
FROM passengers p
JOIN passenger_classes pc ON p.class_id = pc.id
GROUP BY pc.class_number;


-- 2️⃣ View: Survival statistics by embarkation port
CREATE OR REPLACE VIEW v_survival_by_embarkation AS
SELECT
  ep.name AS embarkation_port,
  COUNT(*) AS total_passengers,
  COUNT(*) FILTER (WHERE p.survived = true) AS survived
FROM passengers p
JOIN embarkation_ports ep ON p.embarkation_id = ep.id
GROUP BY ep.name;