const cors = require("cors");
const express = require("express");
const axios = require("axios");
const app = express();

app.use(cors());

app.get("/rockets", (_request, response) => {
    return response.json([{
        name: "VLS-1",
        country: "Brazil",
        status: "RETIRED"
    }, {
        name: "VLM",
        country: "Brazil",
        status: "DEVELOPMENT"
    }, {
        name: "AUSROCK IV",
        countr: "Australia",
        status: "DEVELOPTMENT"

    }]);
});

app.get("/dragons", async (_request, response) => {
    const { data } = await axios('https://api.spacexdata.com/v4/dragons');
    return response.json(data);
});

app.listen("4567");