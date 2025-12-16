-- 1️⃣ Total passengers count
SELECT COUNT(*) AS total_passengers
FROM passengers;


-- 2️⃣ Survival rate (aggregation)
SELECT
  survived,
  COUNT(*) AS count
FROM passengers
GROUP BY survived;


-- 3️⃣ Average age of survivors vs non-survivors
SELECT
  survived,
  AVG(age) AS avg_age
FROM passengers
WHERE age IS NOT NULL
GROUP BY survived;


-- 4️⃣ Passengers per passenger class (JOIN)
SELECT
  pc.class_number,
  COUNT(p.id) AS passenger_count
FROM passengers p
JOIN passenger_classes pc ON p.class_id = pc.id
GROUP BY pc.class_number
ORDER BY pc.class_number;


-- 5️⃣ Survival rate per class (JOIN + aggregation)
SELECT
  pc.class_number,
  COUNT(*) FILTER (WHERE p.survived = true) AS survived_count,
  COUNT(*) AS total,
  ROUND(
    COUNT(*) FILTER (WHERE p.survived = true)::NUMERIC / COUNT(*) * 100,
    2
  ) AS survival_percentage
FROM passengers p
JOIN passenger_classes pc ON p.class_id = pc.id
GROUP BY pc.class_number
ORDER BY pc.class_number;


-- 6️⃣ Survival rate per embarkation port (JOIN)
SELECT
  ep.name AS embarkation_port,
  COUNT(*) FILTER (WHERE p.survived = true) AS survived,
  COUNT(*) AS total
FROM passengers p
JOIN embarkation_ports ep ON p.embarkation_id = ep.id
GROUP BY ep.name
ORDER BY total DESC;


-- 7️⃣ Detect duplicate passenger references (data quality)
SELECT
  passenger_ref,
  COUNT(*) AS occurrences
FROM passengers
GROUP BY passenger_ref
HAVING COUNT(*) > 1;


-- 8️⃣ Detect invalid ages (data validation)
SELECT *
FROM passengers
WHERE age < 0 OR age > 100;


-- 9️⃣ High-fare passengers who did NOT survive
SELECT
  passenger_ref,
  name,
  fare
FROM passengers
WHERE fare > 100 AND survived = false
ORDER BY fare DESC;


-- 🔟 Recently inserted passengers (App Script validation)
SELECT
  passenger_ref,
  name,
  created_at
FROM passengers
ORDER BY created_at DESC
LIMIT 10;
