CREATE OR REPLACE VIEW cabs.gold.fact_trips_lucknow
AS (
SELECT *
FROM cabs.gold.fact_trips
WHERE city_id = 'UP01'
);