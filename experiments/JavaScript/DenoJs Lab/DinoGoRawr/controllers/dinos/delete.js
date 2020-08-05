import { FILE_PATH } from "../../config.js";

export default async ({ params, request, response }) => {
  const decoder = new TextDecoder();
  const encoder = new TextEncoder();

  try {
    const raw = await Deno.readFile(FILE_PATH);
    let dinos = JSON.parse(decoder.decode(raw));

    dinos = dinos.filter((dino) => dino.id != params.id);

    await Deno.writeFile(FILE_PATH, encoder.encode(JSON.stringify(dinos)));

    response.status = 201;
    response.body = { status: "success", dinos };
  } catch (error) {
    response.status = 500;
    response.body = { status: "error", error };
  }
};
