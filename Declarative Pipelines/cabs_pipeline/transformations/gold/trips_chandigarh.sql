CREATE OR REPLACE VIEW cabs.gold.fact_trips_chandigarh
AS (
SELECT *
FROM cabs.gold.fact_trips
WHERE city_id = 'CH01'
);




