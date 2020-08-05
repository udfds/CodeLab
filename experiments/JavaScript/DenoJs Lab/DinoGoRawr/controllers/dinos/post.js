import { FILE_PATH } from "../../config.js";

export default async ({ request, response }) => {
  const decoder = new TextDecoder();
  const encoder = new TextEncoder();

  const draftValues = await request.body().value;

  try {
    const newDino = {
      id: dinos.length + 1,
      name: draftValues.name,
      color: draftValues.color,
      type: draftValues.type,
    };

    const raw = await Deno.readFile(FILE_PATH);
    const dinos = JSON.parse(decoder.decode(raw));
    dinos.push(newDino);

    await Deno.writeFile(FILE_PATH, encoder.encode(JSON.stringify(dinos)));

    response.status = 201;
    response.body = { status: "success", dinos };
  } catch (error) {
    response.status = 500;
    response.body = { status: "error", error };
  }
};
