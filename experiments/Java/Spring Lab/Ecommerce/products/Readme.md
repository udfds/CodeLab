### Build jar

./mvnw package

### Run jar

java -Dserver.port=8081 -jar .\target\products-0.0.1-SNAPSHOT.jar

### Build container

docker build -t codelab/ecommerce-products .

### Run container

docker run -p 8081:8080 -t codelab/ecommerce-products