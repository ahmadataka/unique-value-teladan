import fs from "node:fs/promises";
import path from "node:path";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const ROOT = "/Users/ahmadataka/Documents/Codex project/SMA Teladan/unique-value-teladan";
const FINAL = path.join(ROOT, "presentations", "materi-kelas-x-gen-ai-dan-penggunaan-bijak.pptx");
const QA_DIR = path.join(ROOT, "tmp_check_gen_ai_x_pptx");
const LOGO = "/Users/ahmadataka/Documents/Codex project/SMA Teladan/academic-track-teladan/assets/logo-sma-teladan-yogyakarta.png";

const W = 1280;
const H = 720;
const FRAME = { left: 76, top: 70, width: 1128, height: 560 };
const COLORS = {
  navy: "#16324F",
  blue: "#24577A",
  sky: "#EAF3F8",
  sky2: "#F5FAFD",
  gold: "#D8A93A",
  ink: "#1F2933",
  muted: "#5B6770",
  line: "#C8D6E2",
  white: "#FFFFFF",
};

const logoBytes = await fs.readFile(LOGO);

function addText(slide, text, left, top, width, height, opts = {}) {
  const shape = slide.shapes.add({
    geometry: "textbox",
    position: { left, top, width, height },
    fill: "none",
    line: { style: "solid", fill: "none", width: 0 },
  });
  shape.text = text;
  shape.text.style = {
    fontFace: "Aptos",
    fontSize: opts.size ?? 20,
    bold: opts.bold ?? false,
    color: opts.color ?? COLORS.ink,
    alignment: opts.align ?? "left",
  };
  return shape;
}

function addLogo(slide) {
  slide.images.add({
    blob: logoBytes,
    contentType: "image/png",
    alt: "Logo SMA Teladan Yogyakarta",
    fit: "contain",
    position: { left: 1088, top: 28, width: 108, height: 64 },
  });
}

function addFooter(slide, number) {
  slide.shapes.add({
    geometry: "rect",
    position: { left: 76, top: 672, width: 1128, height: 1.2 },
    fill: COLORS.line,
    line: { style: "solid", fill: "none", width: 0 },
  });
  addText(slide, "SMA Teladan Yogyakarta • Unique Value Kelas X", 78, 680, 400, 18, {
    size: 12,
    color: COLORS.muted,
  });
  addText(slide, String(number), 1140, 678, 56, 20, {
    size: 12,
    color: COLORS.muted,
    align: "right",
  });
}

function addHeaderBand(slide, title) {
  slide.shapes.add({
    geometry: "rect",
    position: { left: FRAME.left, top: FRAME.top, width: 980, height: 56 },
    fill: COLORS.blue,
    line: { style: "solid", fill: "none", width: 0 },
  });
  addText(slide, title, FRAME.left + 18, FRAME.top + 10, 860, 34, {
    size: 32,
    bold: true,
    color: COLORS.white,
  });
}

function addBulletList(slide, items, left, top, width, fontSize = 21, gap = 14) {
  let y = top;
  for (const item of items) {
    slide.shapes.add({
      geometry: "ellipse",
      position: { left, top: y + 8, width: 10, height: 10 },
      fill: COLORS.navy,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(slide, item, left + 22, y, width - 22, fontSize * 2.0, {
      size: fontSize,
      color: COLORS.ink,
    });
    y += fontSize * 2.0 + gap;
  }
}

function addSourceNotes(slide, lines) {
  slide.speakerNotes.textFrame.setText(["[Sources]", ...lines]);
  slide.speakerNotes.setVisible(true);
}

async function main() {
  await fs.mkdir(path.dirname(FINAL), { recursive: true });
  await fs.mkdir(QA_DIR, { recursive: true });

  const presentation = Presentation.create({
    slideSize: { width: W, height: H },
  });

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    slide.shapes.add({
      geometry: "rect",
      position: { left: 76, top: 114, width: 500, height: 410 },
      fill: COLORS.sky,
      line: { style: "solid", fill: "none", width: 0 },
    });
    slide.shapes.add({
      geometry: "rect",
      position: { left: 602, top: 114, width: 602, height: 410 },
      fill: COLORS.blue,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(slide, "Materi Kelas X", 118, 176, 360, 40, {
      size: 24,
      bold: true,
      color: COLORS.blue,
    });
    addText(slide, "Mengenal Gen-AI", 112, 230, 420, 120, {
      size: 48,
      bold: true,
      color: COLORS.navy,
    });
    addText(
      slide,
      "Contoh tools, use case akademik yang baik, strategi prompting, contoh penggunaan buruk, dan etika pemakaiannya.",
      114,
      374,
      410,
      106,
      { size: 21, color: COLORS.ink },
    );
    addText(
      slide,
      "Di materi ini, AI tidak dibahas sebagai sulap atau pengganti belajar. Fokusnya adalah bagaimana siswa memakai Gen-AI dengan cerdas, jujur, dan bertanggung jawab.",
      640,
      174,
      500,
      164,
      { size: 22, color: COLORS.white },
    );
    addText(
      slide,
      "Fokus deck:\n• Tool Gen-AI\n• Use case akademik\n• Prompting\n• Contoh buruk\n• Etika penggunaan",
      640,
      376,
      420,
      156,
      { size: 18, color: COLORS.white },
    );
    addFooter(slide, 1);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Apa Itu Gen-AI?");
    addText(
      slide,
      "Gen-AI adalah AI yang dapat menghasilkan konten baru seperti teks, gambar, suara, video, atau kode.",
      96,
      162,
      1080,
      70,
      { size: 28, bold: true, color: COLORS.navy },
    );
    addBulletList(
      slide,
      [
        "Ia bekerja dengan pola dan prediksi dari data yang pernah dipelajarinya.",
        "Karena itu, hasilnya bisa sangat membantu, tetapi tetap bisa salah atau bias.",
        "Gen-AI paling tepat dipakai sebagai alat bantu berpikir dan belajar.",
        "Gen-AI bukan pengganti guru, buku, atau usaha belajar siswa.",
      ],
      102,
      266,
      1020,
      22,
      10,
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 90, top: 548, width: 1088, height: 82 },
      fill: COLORS.sky,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(
      slide,
      "Kalimat kunci: AI bisa cepat, tetapi manusia tetap harus berpikir, memilih, dan memeriksa hasilnya.",
      108,
      574,
      1042,
      34,
      { size: 22, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 2);
    addSourceNotes(slide, [
      "OpenAI Help Center: https://help.openai.com/en/articles/12677804-what-is-chatgpt-faq",
      "Google Gemini Help: https://support.google.com/gemini/answer/13954172?hl=id",
      "Microsoft AI: https://www.microsoft.com/id-id/ai/ai-101/what-is-generative-ai",
    ]);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Contoh Tools Gen-AI");
    const cards = [
      ["ChatGPT", "Cocok untuk brainstorming, menjelaskan konsep, merangkum, dan menyusun draft awal."],
      ["Gemini", "Cocok untuk ide, tanya jawab, ringkasan, dan beberapa alur yang dekat dengan ekosistem Google."],
      ["Microsoft Copilot", "Cocok untuk membantu kerja berbasis dokumen, ringkasan, dan tugas yang dekat dengan layanan Microsoft."],
    ];
    let y = 170;
    for (const [title, body] of cards) {
      slide.shapes.add({
        geometry: "rect",
        position: { left: 96, top: y, width: 1080, height: 116 },
        fill: y === 170 ? COLORS.sky2 : COLORS.white,
        line: { style: "solid", fill: COLORS.line, width: 1 },
      });
      addText(slide, title, 122, y + 20, 220, 30, {
        size: 26,
        bold: true,
        color: COLORS.navy,
      });
      addText(slide, body, 320, y + 18, 820, 64, {
        size: 21,
        color: COLORS.ink,
      });
      y += 126;
    }
    addText(
      slide,
      "Prinsip penting: pilih tool berdasarkan kebutuhan tugas, bukan hanya karena sedang populer.",
      106,
      584,
      1048,
      30,
      { size: 22, bold: true, color: COLORS.blue, align: "center" },
    );
    addFooter(slide, 3);
    addSourceNotes(slide, [
      "ChatGPT product: https://chatgpt.com/",
      "Gemini app: https://gemini.google.com/app?hl=id",
      "Microsoft 365 Copilot overview: https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview",
    ]);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Use Case Akademik yang Baik");
    slide.shapes.add({
      geometry: "rect",
      position: { left: 92, top: 164, width: 520, height: 396 },
      fill: COLORS.sky2,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    slide.shapes.add({
      geometry: "rect",
      position: { left: 644, top: 164, width: 532, height: 396 },
      fill: COLORS.white,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    addText(slide, "Bantuan yang sehat", 118, 190, 260, 30, {
      size: 28,
      bold: true,
      color: COLORS.navy,
    });
    addBulletList(
      slide,
      [
        "Menjelaskan konsep dengan bahasa lebih sederhana.",
        "Merangkum catatan yang sudah dibuat siswa.",
        "Membuat soal latihan dan kunci jawaban.",
        "Membantu membuat kerangka presentasi.",
      ],
      118,
      240,
      440,
      20,
      8,
    );
    addText(slide, "Contoh konkret", 670, 190, 240, 30, {
      size: 28,
      bold: true,
      color: COLORS.navy,
    });
    addBulletList(
      slide,
      [
        "“Jelaskan fotosintesis untuk siswa kelas X dalam 5 poin.”",
        "“Buat 5 soal latihan dari materi Revolusi Industri 4.0.”",
        "“Rapikan outline presentasi saya jadi 3 slide utama.”",
        "“Tolong cek apakah paragraf saya sudah jelas dan runtut.”",
      ],
      670,
      240,
      448,
      20,
      8,
    );
    addText(
      slide,
      "Ukuran sederhananya: AI membantu proses belajar, bukan menggantikan proses berpikir.",
      106,
      594,
      1048,
      28,
      { size: 22, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 4);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Strategi Prompting");
    addText(slide, "Prompt yang baik biasanya punya 4 unsur:", 98, 160, 420, 34, {
      size: 28,
      bold: true,
      color: COLORS.navy,
    });
    addBulletList(
      slide,
      [
        "Tujuan: saya ingin AI membantu untuk apa?",
        "Konteks: topiknya apa, level siswa berapa?",
        "Format: saya ingin poin, tabel, atau contoh soal?",
        "Revisi: kalau hasil belum pas, minta diperbaiki lagi.",
      ],
      102,
      234,
      480,
      19,
      8,
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 644, top: 164, width: 532, height: 226 },
      fill: COLORS.sky,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(slide, "Prompt lebih baik", 670, 188, 220, 26, {
      size: 22,
      bold: true,
      color: COLORS.navy,
    });
    addText(
      slide,
      "“Jelaskan fotosintesis untuk siswa kelas X dalam 5 poin singkat, lalu buat 3 pertanyaan latihan beserta jawabannya.”",
      670,
      236,
      460,
      94,
      { size: 18, color: COLORS.ink },
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 644, top: 406, width: 532, height: 150 },
      fill: COLORS.white,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    addText(slide, "Prompt kurang efektif", 670, 430, 240, 26, {
      size: 22,
      bold: true,
      color: COLORS.navy,
    });
    addText(slide, "“Jelaskan fotosintesis.”", 670, 478, 300, 30, {
      size: 18,
      color: COLORS.ink,
    });
    addFooter(slide, 5);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Contoh Buruk dan Etika Penggunaan");
    slide.shapes.add({
      geometry: "rect",
      position: { left: 94, top: 164, width: 500, height: 344 },
      fill: COLORS.white,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    slide.shapes.add({
      geometry: "rect",
      position: { left: 626, top: 164, width: 550, height: 344 },
      fill: COLORS.sky2,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    addText(slide, "Penggunaan yang buruk", 120, 188, 280, 28, {
      size: 24,
      bold: true,
      color: COLORS.navy,
    });
    addBulletList(
      slide,
      [
        "Menyalin jawaban AI mentah-mentah.",
        "Memakai AI untuk mencontek ujian.",
        "Tidak memeriksa ulang fakta penting.",
        "Memasukkan data pribadi atau dokumen sensitif.",
      ],
      120,
      246,
      420,
      18,
      8,
    );
    addText(slide, "Etika yang harus dijaga", 652, 188, 300, 28, {
      size: 24,
      bold: true,
      color: COLORS.navy,
    });
    addBulletList(
      slide,
      [
        "Jujur tentang bantuan AI yang dipakai.",
        "Verifikasi informasi dengan sumber tepercaya.",
        "Gunakan AI untuk belajar, bukan menggantikan usaha.",
        "Hormati privasi dan karya orang lain.",
      ],
      652,
      246,
      456,
      18,
      8,
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 94, top: 534, width: 1082, height: 82 },
      fill: COLORS.sky,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(
      slide,
      "Gen-AI boleh membantu pekerjaan, tetapi karakter tetap dibentuk oleh kejujuran dan tanggung jawab manusia.",
      120,
      560,
      1028,
      28,
      { size: 22, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 6);
    addSourceNotes(slide, [
      "Google Gemini app notice: https://gemini.google.com/app?hl=id",
      "Google Gemini Help image generation policy: https://support.google.com/gemini/answer/14286560?p=b_gen_img",
    ]);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Tugas Kelompok");
    addText(
      slide,
      "Menilai Penggunaan Gen-AI yang Cerdas dan Etis",
      96,
      162,
      1080,
      42,
      { size: 30, bold: true, color: COLORS.navy },
    );
    addBulletList(
      slide,
      [
        "Pilih satu tool Gen-AI: ChatGPT, Gemini, atau Copilot.",
        "Jelaskan fungsi sederhananya.",
        "Berikan 2 contoh penggunaan yang baik untuk pelajar.",
        "Berikan 2 contoh penggunaan yang buruk atau tidak etis.",
        "Tulis 1 prompt yang baik dan 1 prompt yang terlalu umum atau buruk.",
        "Rumuskan 3 aturan etika penggunaan Gen-AI di sekolah.",
      ],
      104,
      230,
      1030,
      21,
      8,
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 96, top: 512, width: 1080, height: 112 },
      fill: COLORS.sky2,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    addText(slide, "Pengumpulan tugas", 122, 532, 260, 24, {
      size: 20,
      bold: true,
      color: COLORS.blue,
    });
    addText(slide, "Kirim ke: ataka.ahmad@gmail.com", 122, 560, 430, 24, {
      size: 18,
      bold: true,
      color: "#2563EB",
    });
    addText(slide, "Subject: SMA Teladan X - Tugas Gen-AI - [Nama Kelompok]", 122, 586, 790, 22, {
      size: 17,
      bold: true,
      color: COLORS.ink,
    });
    addFooter(slide, 7);
    addSourceNotes(slide, []);
  }

  for (const [index, slide] of presentation.slides.items.entries()) {
    const png = await presentation.export({ slide, format: "png", scale: 1 });
    await fs.writeFile(
      path.join(QA_DIR, `slide-${String(index + 1).padStart(2, "0")}.png`),
      new Uint8Array(await png.arrayBuffer()),
    );
  }

  const pptx = await PresentationFile.exportPptx(presentation);
  await pptx.save(FINAL);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
