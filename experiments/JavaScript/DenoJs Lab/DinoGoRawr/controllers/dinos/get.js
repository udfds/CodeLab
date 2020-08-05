import { FILE_PATH } from "../../config.js";

export default async ({ response }) => {
  const decoder = new TextDecoder();

  try {
    const raw = await Deno.readFile(FILE_PATH);
    const dinos = JSON.parse(decoder.decode(raw));

    response.status = 200;
    response.body = { status: "success", dinos };
  } catch (error) {
    response.status = 500;
    response.body = { status: "error", error };
  }
};
