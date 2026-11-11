CREATE OR REPLACE VIEW cabs.gold.fact_trips_visakhapatnam
AS (
SELECT *
FROM cabs.gold.fact_trips
WHERE city_id = 'AP01'
);