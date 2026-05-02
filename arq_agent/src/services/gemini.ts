import { GoogleGenerativeAI } from "@google/generative-ai";

const API_KEY = import.meta.env.VITE_GEMINI_API_KEY || "";
const genAI = new GoogleGenerativeAI(API_KEY);

export interface Detail {
  id: string;
  text: string;
  referenceImage?: string;
}

// Detects the real mimeType from a Base64 data URL
function getMimeType(base64: string): string {
  const match = base64.match(/^data:([a-zA-Z0-9]+\/[a-zA-Z0-9-.+]+);base64,/);
  return match ? match[1] : "image/jpeg";
}

// Retry with exponential backoff for quota/rate limit errors (429)
async function withRetry<T>(fn: () => Promise<T>, retries = 3, delayMs = 5000): Promise<T> {
  try {
    return await fn();
  } catch (err: any) {
    const is429 = err?.message?.includes('429') || err?.status === 429;
    if (is429 && retries > 0) {
      console.warn(`Rate limit hit. Tentando novamente em ${delayMs / 1000}s... (${retries} tentativas restantes)`);
      await new Promise(resolve => setTimeout(resolve, delayMs));
      return withRetry(fn, retries - 1, delayMs * 2);
    }
    throw err;
  }
}

// ───────────────────────────────────────────────
// AGENTE 1: Análise do SketchUp
// ───────────────────────────────────────────────
export async function analyzeSketch(base64Image: string) {
  const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash" });
  const mimeType = getMimeType(base64Image);

  const prompt = `
    Você é um especialista em arquitetura e design de interiores.
    Analise esta imagem de um projeto 3D do SketchUp com extremo rigor e detalhamento.

    Identifique e liste TODOS os elementos visíveis (materiais, móveis, iluminação, cores).
    Retorne SOMENTE um JSON válido com a estrutura:
    {"elements": ["elemento 1 detalhado", "elemento 2 detalhado"]}
  `;

  const result = await withRetry(() => model.generateContent([
    prompt,
    {
      inlineData: {
        data: base64Image.split(",")[1],
        mimeType: mimeType as any,
      },
    },
  ]));

  const response = await result.response;
  const text = response.text();
  const jsonMatch = text.match(/\{[\s\S]*\}/);
  if (jsonMatch) return JSON.parse(jsonMatch[0]);

  throw new Error("Falha ao analisar a imagem.");
}

// ───────────────────────────────────────────────
// AGENTE 2: Gerador de Especificação JSON
// ───────────────────────────────────────────────
export async function generateRenderSpec(
  details: Detail[],
  context: { style: string; lighting: string; theme: string }
): Promise<{ prompt: string; specJson: string }> {
  const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash" });

  const detailDescriptions = details.map((d, i) => {
    let desc = `${i + 1}. ${d.text}`;
    if (d.referenceImage) desc += ` (Ver imagem de referência anexada)`;
    return desc;
  }).join("\n");

  const prompt = `
    Você é um especialista em renderização arquitetônica fotorrealista.
    Gere uma especificação técnica (JSON) para renderizar a imagem considerando:
    
    ESTILO: ${context.style}
    LUZ: ${context.lighting}
    TEMA: ${context.theme}

    ELEMENTOS E REFERÊNCIAS:
    ${detailDescriptions}

    A especificação deve garantir fidelidade absoluta ao modelo 3D e usar as referências visuais anexadas para texturas e estilos de materiais.
    Retorne JSON: {"prompt_renderizacao": "...", "spec_json": {...}}
  `;

  const content: any[] = [prompt];
  details.forEach(d => {
    if (d.referenceImage) {
      content.push({ text: `Referência para: ${d.text.substring(0, 30)}...` });
      content.push({
        inlineData: {
          data: d.referenceImage.split(",")[1],
          mimeType: getMimeType(d.referenceImage)
        }
      });
    }
  });

  const result = await withRetry(() => model.generateContent(content));
  const text = result.response.text();
  const jsonMatch = text.match(/\{[\s\S]*\}/);

  if (jsonMatch) {
    const parsed = JSON.parse(jsonMatch[0]);
    return {
      prompt: parsed.prompt_renderizacao,
      specJson: JSON.stringify(parsed.spec_json, null, 2),
    };
  }

  throw new Error("Falha ao gerar especificação.");
}

// ───────────────────────────────────────────────
// AGENTE 3: Renderizador (Nano Banana)
// ───────────────────────────────────────────────
export async function renderImage(
  renderPrompt: string,
  sketchBase64: string,
  context: { style: string; lighting: string; theme: string; details: Detail[] }
): Promise<string> {
  const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash-image" });
  const content: any[] = [
    `Transform this SketchUp model into a realistic render. 
     FIDELITY: Absolute to architecture geometry and spatial layout.
     STYLE PRESETS: ${context.style} | LIGHT: ${context.lighting}
     TECHNICAL RENDER PROMPT: ${renderPrompt}`,
    {
      inlineData: {
        data: sketchBase64.split(",")[1],
        mimeType: getMimeType(sketchBase64)
      }
    }
  ];

  const result = await withRetry(() => model.generateContent(content));
  const response = await result.response;

  for (const part of response.candidates?.[0]?.content?.parts ?? []) {
    if (part.inlineData?.mimeType?.startsWith("image/")) {
      return `data:${part.inlineData.mimeType};base64,${part.inlineData.data}`;
    }
  }

  throw new Error("A API não retornou uma imagem.");
}

// ───────────────────────────────────────────────
// AGENTE 4: Análise de Fidelidade
// ───────────────────────────────────────────────
export async function analyzeFidelity(
  originalBase64: string,
  renderedBase64: string,
  details: Detail[]
): Promise<{ score: number; issues: string[]; suggestions: string[] }> {
  const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash" });

  const prompt = `
    Compare o modelo 3D original com a renderização gerada.
    Avalie a fidelidade baseada nestes elementos:
    ${details.map(d => `- ${d.text}`).join("\n")}

    Retorne JSON: {"score": 0-100, "issues": [], "suggestions": []}
  `;

  const result = await withRetry(() => model.generateContent([
    { text: "3D Original:" },
    { inlineData: { data: originalBase64.split(",")[1], mimeType: getMimeType(originalBase64) } },
    { text: "Render Gerado:" },
    { inlineData: { data: renderedBase64.split(",")[1], mimeType: getMimeType(renderedBase64) } },
    { text: prompt }
  ]));

  const text = result.response.text();
  const jsonMatch = text.match(/\{[\s\S]*\}/);
  if (jsonMatch) return JSON.parse(jsonMatch[0]);

  return { score: 0, issues: ["Erro na análise"], suggestions: [] };
}

// ───────────────────────────────────────────────
// AGENTE 5: Refinamento
// ───────────────────────────────────────────────
export async function refineRender(
  annotatedBase64: string,
  originalBase64: string,
  feedback: string,
  details: Detail[],
  context: { style: string; lighting: string; theme: string }
): Promise<string> {
  const model = genAI.getGenerativeModel({ model: "gemini-2.5-flash-image" });

  const content: any[] = [
    `Refine this architectural render. 
     FEEDBACK: ${feedback}. 
     STYLE: ${context.style} | LIGHT: ${context.lighting}
     Ensure these elements are respected: ${details.map(d => d.text).join(", ")}`,
    {
      inlineData: {
        data: originalBase64.split(",")[1],
        mimeType: getMimeType(originalBase64)
      }
    },
    {
      inlineData: {
        data: annotatedBase64.split(",")[1],
        mimeType: getMimeType(annotatedBase64)
      }
    }
  ];

  const result = await withRetry(() => model.generateContent(content));
  const response = await result.response;

  for (const part of response.candidates?.[0]?.content?.parts ?? []) {
    if (part.inlineData?.mimeType?.startsWith("image/")) {
      return `data:${part.inlineData.mimeType};base64,${part.inlineData.data}`;
    }
  }

  throw new Error("Falha no refinamento.");
}
