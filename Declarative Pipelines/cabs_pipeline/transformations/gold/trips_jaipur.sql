CREATE OR REPLACE VIEW cabs.gold.fact_trips_jaipur
AS (
SELECT *
FROM cabs.gold.fact_trips
WHERE city_id = 'RJ01'
);