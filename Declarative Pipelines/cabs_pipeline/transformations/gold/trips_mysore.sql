CREATE OR REPLACE VIEW cabs.gold.fact_trips_mysore
AS (
SELECT *
FROM cabs.gold.fact_trips
WHERE city_id = 'KA01'
);