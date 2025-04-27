INSERT INTO tourism_city (name) VALUES
('Delhi'),
('Mumbai'),
('Bangalore'),
('Chennai'),
('Kolkata'),
('Hyderabad'),
('Pune'),
('Jaipur'),
('Ahmedabad'),
('Kanpur');


-- Insert bookings (example, replace user_id with actual user id)
INSERT INTO tourism_booking (user_id, venue_id, hotel_id, start_date, end_date) VALUES
(1, (SELECT id FROM tourism_venue WHERE name='Convention Center'), (SELECT id FROM tourism_hotel WHERE name='Hotel Taj'), '2025-05-01', '2025-05-05');