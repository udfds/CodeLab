### Build jar

./mvnw package

### Run jar

java -jar .\target\api-0.0.1-SNAPSHOT.jar

### Build container

docker build -t codelab/service-orders-api .

### Run container

docker run -p 8081:8080 -t codelab/service-orders-api