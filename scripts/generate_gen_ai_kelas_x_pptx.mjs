import fs from "node:fs/promises";
import path from "node:path";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const ROOT = "/Users/ahmadataka/Documents/Codex project/sma-teladan-unique-value";
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
    position: { left: FRAME.left, top: FRAME.top, width: 1128, height: 56 },
    fill: COLORS.blue,
    line: { style: "solid", fill: "none", width: 0 },
  });
  addText(slide, title, FRAME.left + 18, FRAME.top + 10, 760, 34, {
    size: 32,
    bold: true,
    color: COLORS.white,
  });
}

function addBulletList(slide, items, left, top, width, fontSize = 21, gap = 16) {
  let y = top;
  for (const item of items) {
    slide.shapes.add({
      geometry: "ellipse",
      position: { left, top: y + 9, width: 10, height: 10 },
      fill: COLORS.navy,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(slide, item, left + 22, y, width - 22, fontSize * 1.9, {
      size: fontSize,
      color: COLORS.ink,
    });
    y += fontSize * 1.9 + gap;
  }
}

function addSourceNotes(slide, lines) {
  slide.speakerNotes.textFrame.setText([
    "[Sources]",
    ...lines,
  ]);
  slide.speakerNotes.setVisible(true);
}

async function main() {
  await fs.mkdir(path.dirname(FINAL), { recursive: true });
  await fs.mkdir(QA_DIR, { recursive: true });

  const presentation = Presentation.create({
    slideSize: { width: W, height: H },
  });
  presentation.theme.colorScheme = {
    name: "Teladan Gen AI",
    themeColors: {
      accent1: COLORS.blue,
      accent2: COLORS.gold,
      accent3: "#5F87A2",
      accent4: "#A6C4D8",
      accent5: "#345D7A",
      accent6: "#6F8CA0",
      bg1: COLORS.white,
      bg2: COLORS.sky2,
      tx1: COLORS.ink,
      tx2: COLORS.muted,
      dk1: "#000000",
      dk2: COLORS.navy,
      lt1: COLORS.white,
      lt2: "#E5EEF5",
      hlink: "#2563EB",
      folHlink: "#7C3AED",
    },
  };

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    slide.shapes.add({
      geometry: "rect",
      position: { left: 76, top: 114, width: 490, height: 404 },
      fill: COLORS.sky,
      line: { style: "solid", fill: "none", width: 0 },
    });
    slide.shapes.add({
      geometry: "rect",
      position: { left: 596, top: 114, width: 608, height: 404 },
      fill: COLORS.blue,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(slide, "Materi Kelas X", 116, 174, 360, 54, {
      size: 24,
      bold: true,
      color: COLORS.blue,
    });
    addText(slide, "Mengenal Gen-AI", 112, 230, 400, 120, {
      size: 50,
      bold: true,
      color: COLORS.navy,
    });
    addText(
      slide,
      "Pengantar tentang AI generatif, contoh dekat dengan siswa, dan cara menggunakannya dengan bijak.",
      114,
      372,
      390,
      104,
      { size: 22, color: COLORS.ink },
    );
    addText(
      slide,
      "Setelah Revolusi Industri 4.0, kita masuk ke teknologi yang sedang sangat dekat dengan kehidupan belajar siswa: AI yang bisa membantu membuat teks, gambar, ide, dan penjelasan.",
      636,
      192,
      520,
      176,
      { size: 24, color: COLORS.white },
    );
    addText(
      slide,
      "Fokus deck ini:\n• Apa itu Gen-AI\n• Contoh dekat dengan siswa\n• Manfaat dan risiko\n• Penggunaan yang jujur dan bertanggung jawab",
      636,
      394,
      500,
      128,
      { size: 20, color: COLORS.white },
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
      "Gen-AI adalah jenis AI yang dapat menghasilkan konten baru berdasarkan pola dari data yang pernah dipelajarinya.",
      96,
      162,
      1080,
      72,
      { size: 28, bold: true, color: COLORS.navy },
    );
    addBulletList(
      slide,
      [
        "Konten itu bisa berupa teks, gambar, suara, video, atau kode.",
        "Kalau AI biasa sering dipakai untuk mengenali atau mengelompokkan, Gen-AI dipakai untuk membuat sesuatu yang baru.",
        "Gen-AI membantu manusia, tetapi tidak benar-benar berpikir seperti manusia.",
        "Karena bekerja dengan pola dan prediksi, hasilnya bisa berguna tetapi tidak selalu benar.",
      ],
      102,
      270,
      1020,
      22,
      10,
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 90, top: 560, width: 1088, height: 72 },
      fill: COLORS.sky,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(
      slide,
      "Gagasan penting: Gen-AI paling tepat dilihat sebagai alat bantu berpikir dan berkarya, bukan sumber kebenaran terakhir.",
      110,
      582,
      1040,
      36,
      { size: 22, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 2);
    addSourceNotes(slide, [
      "Google Gemini Help Center (id): https://support.google.com/gemini/answer/13954172?hl=id",
      "Microsoft AI: https://www.microsoft.com/id-id/ai/ai-101/what-is-generative-ai",
    ]);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Contoh Gen-AI yang Dekat dengan Siswa");
    slide.shapes.add({
      geometry: "rect",
      position: { left: 90, top: 156, width: 520, height: 430 },
      fill: COLORS.sky2,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    slide.shapes.add({
      geometry: "rect",
      position: { left: 648, top: 156, width: 530, height: 430 },
      fill: COLORS.white,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    addText(slide, "Untuk belajar", 114, 186, 220, 30, {
      size: 28,
      bold: true,
      color: COLORS.navy,
    });
    addBulletList(
      slide,
      [
        "Menjelaskan materi dengan bahasa yang lebih sederhana.",
        "Merangkum artikel atau catatan menjadi poin-poin penting.",
        "Membantu mencari ide presentasi atau poster.",
        "Membantu memahami contoh kode atau langkah pemecahan masalah.",
      ],
      114,
      242,
      450,
      20,
      8,
    );
    addText(slide, "Untuk kreativitas", 672, 186, 220, 30, {
      size: 28,
      bold: true,
      color: COLORS.navy,
    });
    addBulletList(
      slide,
      [
        "Membuat gambar dari deskripsi teks.",
        "Menyusun draft awal tulisan atau caption.",
        "Membantu membuat variasi ide konten.",
        "Memberi contoh struktur narasi atau alur presentasi.",
      ],
      672,
      242,
      450,
      20,
      8,
    );
    addText(
      slide,
      "Yang harus dijaga: hasil AI tetap perlu dicek, dipahami, dan diolah ulang dengan bahasa serta pemikiran kalian sendiri.",
      106,
      614,
      1048,
      34,
      { size: 22, bold: true, color: COLORS.blue, align: "center" },
    );
    addFooter(slide, 3);
    addSourceNotes(slide, [
      "Google Gemini Help Center (id): https://support.google.com/gemini/answer/13954172?hl=id",
    ]);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Manfaat dan Risiko Gen-AI");
    slide.shapes.add({
      geometry: "rect",
      position: { left: 96, top: 164, width: 500, height: 56 },
      fill: COLORS.blue,
      line: { style: "solid", fill: "none", width: 0 },
    });
    slide.shapes.add({
      geometry: "rect",
      position: { left: 620, top: 164, width: 556, height: 56 },
      fill: COLORS.blue,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(slide, "Manfaat", 116, 176, 240, 30, {
      size: 24,
      bold: true,
      color: COLORS.white,
    });
    addText(slide, "Risiko yang Perlu Diwaspadai", 640, 176, 430, 30, {
      size: 24,
      bold: true,
      color: COLORS.white,
    });
    slide.shapes.add({
      geometry: "rect",
      position: { left: 96, top: 220, width: 500, height: 304 },
      fill: COLORS.sky2,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    slide.shapes.add({
      geometry: "rect",
      position: { left: 620, top: 220, width: 556, height: 304 },
      fill: COLORS.white,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    addBulletList(
      slide,
      [
        "Membantu mencari ide awal.",
        "Membantu merangkum dan menjelaskan materi.",
        "Membantu membuat draft awal.",
        "Mempercepat pekerjaan tertentu.",
      ],
      122,
      244,
      432,
      20,
      8,
    );
    addBulletList(
      slide,
      [
        "Jawaban bisa salah tetapi terdengar meyakinkan.",
        "Siswa bisa terlalu bergantung dan malas berpikir.",
        "Ada risiko plagiarisme jika menyalin mentah-mentah.",
        "Data pribadi bisa tidak aman jika dibagikan sembarangan.",
      ],
      646,
      244,
      486,
      20,
      8,
    );
    addText(
      slide,
      "Kesimpulan slide ini: Gen-AI berguna jika dipakai untuk membantu belajar, tetapi berbahaya jika dipakai tanpa kejujuran dan pemeriksaan ulang.",
      110,
      546,
      1048,
      60,
      { size: 22, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 4);
    addSourceNotes(slide, [
      "Microsoft AI: https://www.microsoft.com/id-id/ai/ai-101/what-is-generative-ai",
      "Google Gemini Help Center (id): https://support.google.com/gemini/answer/13954172?hl=id",
    ]);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Cara Memakai Gen-AI dengan Bijak");
    addBulletList(
      slide,
      [
        "Gunakan untuk membantu memahami, bukan untuk mencontek mentah-mentah.",
        "Selalu cek ulang fakta penting dari buku, guru, atau sumber tepercaya.",
        "Jangan masukkan data pribadi, kata sandi, atau informasi sensitif.",
        "Kalau memakai hasil AI untuk tugas, olah kembali dengan pemahaman dan bahasa kalian sendiri.",
        "Anggap AI sebagai alat diskusi awal, bukan pengganti nalar dan kejujuran.",
      ],
      106,
      170,
      1020,
      23,
      12,
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 132, top: 536, width: 1010, height: 84 },
      fill: COLORS.sky,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(
      slide,
      "Sikap yang paling penting adalah jujur. Teknologi boleh membantu, tetapi pemahaman tetap harus tumbuh dari kalian sendiri.",
      164,
      560,
      950,
      34,
      { size: 24, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 5);
    addSourceNotes(slide, [
      "Google Gemini Help Center (id): https://support.google.com/gemini/answer/13954172?hl=id",
    ]);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Tugas Kelompok");
    addText(
      slide,
      "Memakai Gen-AI untuk Belajar dengan Cerdas dan Bertanggung Jawab",
      96,
      162,
      1080,
      48,
      { size: 28, bold: true, color: COLORS.navy },
    );
    addBulletList(
      slide,
      [
        "Pilih satu contoh penggunaan Gen-AI yang menurut kalian berguna untuk pelajar.",
        "Jelaskan bagaimana alat itu bisa membantu belajar.",
        "Sebutkan minimal 2 manfaat jika dipakai dengan benar.",
        "Sebutkan minimal 2 risiko jika dipakai tanpa bijak.",
        "Tuliskan aturan penggunaan yang jujur dan bertanggung jawab di sekolah.",
      ],
      104,
      242,
      1030,
      22,
      10,
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 96, top: 494, width: 1080, height: 126 },
      fill: COLORS.sky2,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    addText(slide, "Pengumpulan tugas", 122, 520, 260, 28, {
      size: 20,
      bold: true,
      color: COLORS.blue,
    });
    addText(slide, "Kirim ke: ataka.ahmad@gmail.com", 122, 550, 420, 24, {
      size: 19,
      color: "#2563EB",
      bold: true,
    });
    addText(slide, "Subject: SMA Teladan X - Tugas Gen-AI - [Nama Kelompok]", 122, 578, 780, 24, {
      size: 18,
      bold: true,
      color: COLORS.ink,
    });
    addText(slide, "Lampirkan 1 lembar jawaban ringkas atau 1 slide sederhana.", 122, 602, 760, 22, {
      size: 18,
      color: COLORS.ink,
    });
    addFooter(slide, 6);
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
