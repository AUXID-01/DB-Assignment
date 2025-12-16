procedures.sql
-- 1️⃣ Function: Get survival rate for a given class
CREATE OR REPLACE FUNCTION get_survival_rate_by_class(p_class INT)
RETURNS TABLE (
  total INT,
  survived INT,
  survival_rate NUMERIC
)
AS $$
BEGIN
  RETURN QUERY
  SELECT
    COUNT(*)::INT,
    COUNT(*) FILTER (WHERE survived = true)::INT,
    ROUND(
      COUNT() FILTER (WHERE survived = true)::NUMERIC / COUNT() * 100,
      2
    )
  FROM passengers p
  JOIN passenger_classes pc ON p.class_id = pc.id
  WHERE pc.class_number = p_class;
END;
$$ LANGUAGE plpgsql;


-- 2️⃣ Function: Passengers above a given fare
CREATE OR REPLACE FUNCTION get_high_fare_passengers(min_fare NUMERIC)
RETURNS TABLE (
  passenger_ref INT,
  name TEXT,
  fare NUMERIC
)
AS $$
BEGIN
  RETURN QUERY
  SELECT passenger_ref, name, fare
  FROM passengers
  WHERE fare >= min_fare
  ORDER BY fare DESC;
END;
$$ LANGUAGE plpgsql;