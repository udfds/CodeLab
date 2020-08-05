import { Application } from "https://deno.land/x/oak/mod.ts";
import { PORT } from "./config.js";
import router from "./router.js";

const app = new Application();

app.use(router.routes());
app.use(router.allowedMethods());

console.log("Application running on port:" + PORT);

await app.listen({ port: PORT });
