import { FILE_PATH } from "../../config.js";

export default async ({ params, request, response }) => {
  const decoder = new TextDecoder();
  const encoder = new TextEncoder();

  const draftValues = await request.body().value;

  try {
    const draftDino = {
      name: draftValues.name,
      color: draftValues.color,
      type: draftValues.type,
    };

    const raw = await Deno.readFile(FILE_PATH);
    let dinos = JSON.parse(decoder.decode(raw));

    dinos = dinos.map((dino) => {
      if (dino.id == params.id) {
        dino.name = draftDino.name;
        dino.color = draftDino.color;
        dino.type = draftDino.type;
      }

      return dino;
    });

    await Deno.writeFile(FILE_PATH, encoder.encode(JSON.stringify(dinos)));

    response.status = 200;
    response.body = { status: "success", dinos };
  } catch (error) {
    response.status = 500;
    response.body = { status: "error", error };
  }
};
