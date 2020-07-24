### Build jar

./mvnw package

### Run jar

java -Dserver.port=8083 -jar .\target\service-order-0.0.1-SNAPSHOT.jar

### Build container

docker build -t codelab/ecommerce-service-order .

### Run container

docker run -p 8083:8080 -t codelab/ecommerce-service-order