docker run --name postgres-dev \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=admin12345 \
  -e POSTGRES_DB=be_base_db \
  -p 5432:5432 \
  -d postgres:15
