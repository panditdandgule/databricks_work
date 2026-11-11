CREATE OR REPLACE VIEW cabs.gold.fact_trips_surat
AS (
SELECT *
FROM cabs.gold.fact_trips
WHERE city_id = 'GJ01'
);