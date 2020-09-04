CREATE DATABASE drones;

CREATE ROLE application_backend WITH LOGIN PASSWORD 'application_pass123*';
GRANT ALL PRIVILEGES ON DATABASE drones TO application_backend;
ALTER USER application_backend CREATEDB;

