CREATE OR REPLACE VIEW cabs.gold.fact_trips_kochi
AS (
SELECT *
FROM cabs.gold.fact_trips
WHERE city_id = 'KL01'
);