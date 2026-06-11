CREATE TABLE IF NOT EXISTS interview.source.fileLookup
(
    file string,
    type string
);

INSERT INTO interview.source.fileLookup
VALUES ('productsOrders', '.csv'),
('orders_day1', '.csv')