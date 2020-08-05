import { Router } from "https://deno.land/x/oak/mod.ts";
import allDinos from "./controllers/dinos/get.js";
import createDino from "./controllers/dinos/post.js";
import deleteDino from "./controllers/dinos/delete.js";
import updateDino from "./controllers/dinos/put.js";

const router = new Router();

router.get("/", ({ response }) => {
  response.body = "Dino API";
});

router.get("/dinos", allDinos);
router.post("/dinos", createDino);
router.delete("/dinos/:id", deleteDino);
router.put("/dinos/:id", updateDino);

export default router;
