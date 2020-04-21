package com.codelab.ecommerce.products.services;

import java.io.InputStream;
import org.apache.commons.io.IOUtils;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.springframework.stereotype.Service;

@Service
public class ProductsService {

    public JSONArray getProducts() {
        JSONObject json = getProductJson();

        return (JSONArray) json.get("products");
    }

    public JSONObject getProduct(String uuid) {
        JSONArray array = getProducts();
        JSONObject draft = null;
        JSONObject product = null;

        for (Object object : array) {
            if (object instanceof JSONObject) {
                draft = (JSONObject) object;

                String uuidDraft = (String) draft.get("uuid");
                if (uuid.equalsIgnoreCase(uuidDraft)) {
                    product = draft;
                    break;
                }
            }
        }

        return product;
    }

    private JSONObject getProductJson() {
        JSONObject json = null;
        try {
            InputStream inputStream = this.getClass().getClassLoader().getResourceAsStream("static/products.json");
            String dummy = new String(IOUtils.toByteArray(inputStream));

            JSONParser parser = new JSONParser();
            json = (JSONObject) parser.parse(dummy);

        } catch (Exception exception) {
            exception.printStackTrace();
        }

        return json;
    }
}