CREATE OR REPLACE VIEW cabs.gold.fact_trips_coimbatore
AS (
SELECT *
FROM cabs.gold.fact_trips
WHERE city_id = 'TN01'
);