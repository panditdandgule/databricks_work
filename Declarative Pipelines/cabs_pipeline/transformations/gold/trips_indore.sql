CREATE OR REPLACE VIEW cabs.gold.fact_trips_indore
AS (
SELECT *
FROM cabs.gold.fact_trips
WHERE city_id = 'MP01'
);