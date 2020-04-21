### Build jar

./mvnw package

### Run jar

java -jar .\target\catalog-0.0.1-SNAPSHOT.jar

### Build container

docker build -t codelab/ecommerce-catalog .

### Run container

docker run -p 8081:8080 -t codelab/ecommerce-catalog