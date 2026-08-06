import fs from "node:fs/promises";
import path from "node:path";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const ROOT = "/Users/ahmadataka/Documents/Codex project/SMA Teladan/unique-value-teladan";
const FINAL = path.join(ROOT, "presentations", "materi-kelas-x-ai-gambar-dan-analisis-visual.pptx");
const QA_DIR = path.join(ROOT, "tmp_check_ai_visual_x_pptx");
const LOGO = "/Users/ahmadataka/Documents/Codex project/SMA Teladan/academic-track-teladan/assets/logo-sma-teladan-yogyakarta.png";

const W = 1280;
const H = 720;
const FRAME = { left: 76, top: 78, width: 1128, height: 548 };
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
    position: { left: 1098, top: 18, width: 86, height: 52 },
  });
}

function addFooter(slide, number) {
  slide.shapes.add({
    geometry: "rect",
    position: { left: 76, top: 674, width: 1128, height: 1.2 },
    fill: COLORS.line,
    line: { style: "solid", fill: "none", width: 0 },
  });
  addText(slide, "SMA Teladan Yogyakarta • Unique Value Kelas X", 78, 680, 420, 18, {
    size: 12,
    color: COLORS.muted,
  });
  addText(slide, String(number), 1136, 678, 60, 20, {
    size: 12,
    color: COLORS.muted,
    align: "right",
  });
}

function addHeaderBand(slide, title) {
  slide.shapes.add({
    geometry: "rect",
    position: { left: FRAME.left, top: FRAME.top, width: 944, height: 52 },
    fill: COLORS.blue,
    line: { style: "solid", fill: "none", width: 0 },
  });
  addText(slide, title, FRAME.left + 18, FRAME.top + 9, 850, 32, {
    size: 30,
    bold: true,
    color: COLORS.white,
  });
}

function addBulletList(slide, items, left, top, width, fontSize = 21, gap = 12) {
  let y = top;
  for (const item of items) {
    slide.shapes.add({
      geometry: "ellipse",
      position: { left, top: y + 7, width: 10, height: 10 },
      fill: COLORS.navy,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(slide, item, left + 22, y, width - 22, fontSize * 2.1, {
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

async function writeBlob(filePath, blob) {
  await fs.writeFile(filePath, new Uint8Array(await blob.arrayBuffer()));
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
      position: { left: 76, top: 114, width: 500, height: 408 },
      fill: COLORS.sky,
      line: { style: "solid", fill: "none", width: 0 },
    });
    slide.shapes.add({
      geometry: "rect",
      position: { left: 602, top: 114, width: 602, height: 408 },
      fill: COLORS.blue,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(slide, "Materi Kelas X", 118, 174, 320, 34, {
      size: 24,
      bold: true,
      color: COLORS.blue,
    });
    addText(slide, "AI untuk Gambar dan Analisis Visual", 112, 224, 420, 160, {
      size: 42,
      bold: true,
      color: COLORS.navy,
    });
    addText(
      slide,
      "Mengenal dua cara memakai AI pada gambar: membuat visual baru dan membaca informasi dari visual yang sudah ada.",
      114,
      390,
      412,
      100,
      { size: 20, color: COLORS.ink },
    );
    addText(
      slide,
      "Di sesi ini, kita belajar memakai AI visual untuk tugas akademik secara cerdas, etis, dan tetap kritis terhadap hasilnya.",
      640,
      170,
      500,
      132,
      { size: 22, color: COLORS.white },
    );
    addText(
      slide,
      "Fokus deck:\n• Image generation\n• Image analysis\n• Use case akademik\n• Prompting\n• Etika dan tugas",
      640,
      360,
      420,
      162,
      { size: 18, color: COLORS.white },
    );
    addFooter(slide, 1);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "AI Bisa Dipakai untuk Membuat dan Membaca Gambar");
    slide.shapes.add({
      geometry: "rect",
      position: { left: 92, top: 156, width: 500, height: 398 },
      fill: COLORS.sky2,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    slide.shapes.add({
      geometry: "rect",
      position: { left: 628, top: 156, width: 548, height: 398 },
      fill: COLORS.white,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    addText(slide, "1. Image Generation", 118, 186, 280, 64, {
      size: 24,
      bold: true,
      color: COLORS.navy,
    });
    addBulletList(
      slide,
      [
        "Kita memberi perintah teks, lalu AI membuat gambar baru.",
        "Cocok untuk poster, ilustrasi presentasi, komik konsep, atau visual ide proyek.",
        "Hasilnya harus tetap dicek: apakah sesuai fakta, konteks, dan etika?",
      ],
      118,
      260,
      430,
      19,
      8,
    );
    addText(slide, "2. Image Analysis", 654, 186, 260, 64, {
      size: 24,
      bold: true,
      color: COLORS.navy,
    });
    addBulletList(
      slide,
      [
        "Kita memberi gambar sebagai input, lalu AI membantu menjelaskan isinya.",
        "Cocok untuk membaca diagram, poster, foto eksperimen, atau infografik.",
        "AI membantu observasi, tetapi kesimpulan akhir tetap harus diperiksa manusia.",
      ],
      654,
      260,
      460,
      19,
      8,
    );
    addText(
      slide,
      "Kalimat kunci: AI visual bisa membantu melihat lebih cepat, tetapi memahami dengan benar tetap perlu nalar manusia.",
      104,
      584,
      1040,
      30,
      { size: 22, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 2);
    addSourceNotes(slide, [
      "OpenAI ChatGPT product: https://chatgpt.com/",
      "Google Gemini app: https://gemini.google.com/app",
      "Microsoft Copilot overview: https://www.microsoft.com/en-us/microsoft-copilot",
    ]);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Contoh Tools dan Use Case Akademik");
    const rows = [
      ["ChatGPT", "Bisa dipakai untuk meminta ide gambar, menganalisis poster, atau menjelaskan isi diagram/foto."],
      ["Gemini", "Bisa membantu memahami gambar, membuat deskripsi visual, dan memberi ide ilustrasi untuk presentasi."],
      ["DALL-E / image generator serupa", "Dipakai untuk membuat ilustrasi baru dari teks saat siswa butuh visual konsep atau poster edukatif."],
      ["Google Lens / fitur visual serupa", "Berguna untuk mengenali objek, teks, atau konteks visual sebagai bahan belajar awal."],
    ];
    let y = 154;
    for (const [title, body] of rows) {
      slide.shapes.add({
        geometry: "rect",
        position: { left: 96, top: y, width: 1080, height: 90 },
        fill: y === 154 ? COLORS.sky2 : COLORS.white,
        line: { style: "solid", fill: COLORS.line, width: 1 },
      });
      addText(slide, title, 120, y + 14, 280, 30, {
        size: 21,
        bold: true,
        color: COLORS.navy,
      });
      addText(slide, body, 374, y + 14, 756, 58, {
        size: 18,
        color: COLORS.ink,
      });
      y += 98;
    }
    addText(
      slide,
      "Intinya, pilih tool sesuai kebutuhan: ada yang lebih kuat untuk membuat visual baru, ada yang lebih membantu membaca visual yang sudah ada.",
      104,
      592,
      1040,
      32,
      { size: 18, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 3);
    addSourceNotes(slide, [
      "ChatGPT product: https://chatgpt.com/",
      "Gemini app: https://gemini.google.com/app",
      "OpenAI DALL-E overview: https://openai.com/dall-e/",
      "Google Lens overview: https://lens.google/",
    ]);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Use Case Akademik yang Perlu Diingat");
    slide.shapes.add({
      geometry: "rect",
      position: { left: 96, top: 160, width: 1080, height: 430 },
      fill: COLORS.sky2,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    addBulletList(
      slide,
      [
        "Membuat ilustrasi konsep, misalnya rantai makanan, kota masa depan, atau poster literasi digital.",
        "Membantu memahami diagram, grafik, atau peta konsep dengan bahasa yang lebih sederhana.",
        "Menyiapkan presentasi, sambil tetap memastikan siswa menjelaskan dengan pemahaman sendiri.",
        "Latihan observasi: membandingkan hasil analisis siswa dengan bantuan AI.",
        "Belajar deskripsi visual: mengubah gambar menjadi narasi atau sebaliknya.",
      ],
      122,
      194,
      1010,
      19,
      8,
    );
    addText(
      slide,
      "Prinsip utamanya: AI visual dipakai untuk membantu memahami dan mengomunikasikan ide, bukan menggantikan proses berpikir siswa.",
      120,
      612,
      1036,
      30,
      { size: 20, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 4);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Praktik Singkat Menggunakan GPT");
    slide.shapes.add({
      geometry: "rect",
      position: { left: 96, top: 156, width: 512, height: 420 },
      fill: COLORS.sky2,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    slide.shapes.add({
      geometry: "rect",
      position: { left: 640, top: 156, width: 536, height: 420 },
      fill: COLORS.white,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    addText(slide, "Langkah praktik", 120, 184, 240, 28, {
      size: 24,
      bold: true,
      color: COLORS.navy,
    });
    addBulletList(
      slide,
      [
        "Buka GPT lalu tentukan tujuan: membuat gambar atau menganalisis gambar.",
        "Tulis prompt yang jelas sesuai mata pelajaran dan kebutuhan tugas.",
        "Jika perlu analisis visual, unggah gambar yang ingin dibahas.",
        "Baca hasilnya dengan kritis, lalu perbaiki prompt jika masih terlalu umum.",
        "Simpan hasil penting dan catat bahwa AI dipakai sebagai bantuan belajar.",
      ],
      120,
      236,
      448,
      17,
      7,
    );
    addText(slide, "Contoh yang bisa langsung dicoba", 666, 184, 330, 28, {
      size: 24,
      bold: true,
      color: COLORS.navy,
    });
    addText(
      slide,
      "Generation:\n“Buat ide ilustrasi poster edukatif tentang pemanasan global untuk siswa kelas X, warna cerah, dan cocok untuk slide presentasi.”",
      666,
      232,
      466,
      108,
      { size: 17, color: COLORS.ink },
    );
    addText(
      slide,
      "Analysis:\n“Saya unggah poster ini. Tolong jelaskan pesan utamanya, warna dominan, dan 3 alasan kenapa poster ini efektif untuk pelajar.”",
      666,
      366,
      466,
      100,
      { size: 17, color: COLORS.ink },
    );
    addText(
      slide,
      "Kuncinya bukan sekali kirim prompt lalu selesai, tetapi berani merevisi sampai hasilnya benar-benar berguna.",
      108,
      600,
      1044,
      28,
      { size: 21, bold: true, color: COLORS.blue, align: "center" },
    );
    addFooter(slide, 5);
    addSourceNotes(slide, [
      "ChatGPT product: https://chatgpt.com/",
    ]);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Strategi Prompting untuk Image Generation");
    addText(slide, "Prompt gambar yang baik biasanya menjawab 4 hal:", 98, 156, 520, 34, {
      size: 28,
      bold: true,
      color: COLORS.navy,
    });
    addBulletList(
      slide,
      [
        "Objek utama: apa yang ingin ditampilkan?",
        "Konteks: dipakai untuk pelajaran apa dan suasananya bagaimana?",
        "Gaya visual: realistis, poster edukatif, ilustrasi sederhana, atau komik.",
        "Batasan: hindari hal sensitif, tetap sopan, dan sesuai tujuan akademik.",
      ],
      104,
      228,
      486,
      18,
      8,
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 644, top: 162, width: 532, height: 192 },
      fill: COLORS.sky,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(slide, "Prompt lebih baik", 668, 186, 220, 26, {
      size: 22,
      bold: true,
      color: COLORS.navy,
    });
    addText(
      slide,
      "“Buat ilustrasi poster edukatif tentang daur air untuk siswa kelas X, berwarna cerah, label jelas, dan mudah dipahami.”",
      668,
      228,
      458,
      92,
      { size: 18, color: COLORS.ink },
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 644, top: 386, width: 532, height: 154 },
      fill: COLORS.white,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    addText(slide, "Prompt terlalu umum", 668, 410, 240, 26, {
      size: 22,
      bold: true,
      color: COLORS.navy,
    });
    addText(slide, "“Buat gambar daur air.”", 668, 456, 300, 28, {
      size: 18,
      color: COLORS.ink,
    });
    addText(
      slide,
      "Semakin jelas tujuan dan konteksnya, semakin besar peluang hasil visualnya berguna untuk belajar.",
      106,
      584,
      1040,
      28,
      { size: 22, bold: true, color: COLORS.blue, align: "center" },
    );
    addFooter(slide, 6);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Strategi Prompting untuk Image Analysis");
    slide.shapes.add({
      geometry: "rect",
      position: { left: 96, top: 162, width: 510, height: 390 },
      fill: COLORS.sky2,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    slide.shapes.add({
      geometry: "rect",
      position: { left: 638, top: 162, width: 538, height: 430 },
      fill: COLORS.white,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    addText(slide, "Saat memberi gambar ke AI, mintalah hal yang spesifik:", 118, 188, 430, 54, {
      size: 24,
      bold: true,
      color: COLORS.navy,
    });
    addBulletList(
      slide,
      [
        "Jelaskan objek atau informasi penting yang terlihat.",
        "Sebutkan bagian yang belum jelas atau perlu diperiksa lebih lanjut.",
        "Hubungkan gambar dengan materi pelajaran yang sedang dibahas.",
        "Minta AI menjawab dalam format poin agar mudah dicek.",
      ],
      118,
      264,
      442,
      18,
      8,
    );
    addText(slide, "Contoh prompt analisis", 664, 188, 260, 28, {
      size: 24,
      bold: true,
      color: COLORS.navy,
    });
    addText(
      slide,
      "“Lihat poster ini. Jelaskan pesan utamanya, target audiensnya, warna yang paling dominan, lalu sebutkan 3 hal yang membuat poster ini efektif.”",
      664,
      242,
      462,
      120,
      { size: 18, color: COLORS.ink },
    );
    addText(slide, "Hal yang harus diingat", 664, 388, 260, 54, {
      size: 20,
      bold: true,
      color: COLORS.navy,
    });
    addBulletList(
      slide,
      [
        "AI bisa salah membaca detail kecil.",
        "Tulisan kecil atau simbol bisa salah dibaca.",
        "Gunakan AI sebagai pembantu observasi, bukan penentu akhir.",
      ],
      664,
      456,
      448,
      16,
      7,
    );
    addFooter(slide, 7);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Contoh Buruk dan Etika Penggunaan");
    slide.shapes.add({
      geometry: "rect",
      position: { left: 94, top: 160, width: 498, height: 350 },
      fill: COLORS.white,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    slide.shapes.add({
      geometry: "rect",
      position: { left: 628, top: 160, width: 548, height: 350 },
      fill: COLORS.sky2,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    addText(slide, "Penggunaan yang kurang tepat", 120, 186, 310, 28, {
      size: 24,
      bold: true,
      color: COLORS.navy,
    });
    addBulletList(
      slide,
      [
        "Memakai gambar AI lalu mengaku itu hasil karya sendiri sepenuhnya.",
        "Menghasilkan visual menyesatkan untuk tugas sekolah.",
        "Meminta AI menilai wajah atau identitas teman tanpa izin.",
        "Mengunggah foto pribadi atau sensitif ke tool tanpa pertimbangan.",
      ],
      120,
      242,
      426,
      18,
      8,
    );
    addText(slide, "Etika yang perlu dijaga", 654, 186, 300, 28, {
      size: 24,
      bold: true,
      color: COLORS.navy,
    });
    addBulletList(
      slide,
      [
        "Kejujuran: jelaskan jika tugas dibantu AI visual.",
        "Privasi: hormati wajah, foto, dan dokumen orang lain.",
        "Verifikasi: periksa hasil AI sebelum dibagikan.",
        "Tanggung jawab: gunakan untuk belajar, bukan memanipulasi fakta.",
      ],
      654,
      242,
      458,
      18,
      8,
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 94, top: 536, width: 1082, height: 80 },
      fill: COLORS.sky,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(
      slide,
      "Kemampuan teknis itu penting, tetapi kejujuran, izin, dan tanggung jawab tetap lebih penting.",
      116,
      560,
      1034,
      28,
      { size: 22, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 8);
    addSourceNotes(slide, [
      "Google Safety Center: https://safety.google/",
      "UNESCO guidance on generative AI in education: https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research",
    ]);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Tugas Kelompok");
    addText(
      slide,
      "Menganalisis dan Merancang Penggunaan AI Visual untuk Belajar",
      96,
      156,
      1080,
      42,
      { size: 30, bold: true, color: COLORS.navy },
    );
    addBulletList(
      slide,
      [
        "Pilih satu mata pelajaran yang menurut kelompok kalian cocok memakai AI visual.",
        "Jelaskan apakah AI akan dipakai untuk membuat gambar atau menganalisis gambar.",
        "Tulis 1 contoh prompt yang baik dan jelaskan kenapa prompt itu efektif.",
        "Berikan 2 manfaat akademik dan 2 risiko etika yang harus dijaga.",
        "Sertakan minimal 2 screenshot: proses memakai tool dan hasilnya.",
        "Tunjukkan singkat langkah praktik GPT yang kalian lakukan.",
      ],
      104,
      224,
      1036,
      19,
      7,
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 96, top: 506, width: 1080, height: 116 },
      fill: COLORS.sky2,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    addText(slide, "Pengumpulan tugas", 122, 528, 240, 24, {
      size: 20,
      bold: true,
      color: COLORS.blue,
    });
    addText(slide, "Kirim ke: ataka.ahmad@gmail.com", 122, 556, 430, 24, {
      size: 18,
      color: COLORS.ink,
    });
    addText(
      slide,
      "Subject: SMA Teladan X - Tugas AI Visual - [Nama Kelompok]",
      122,
      582,
      540,
      24,
      { size: 18, color: COLORS.ink },
    );
    addText(
      slide,
      "Output yang diharapkan: ringkasan 1 halaman atau 4-6 slide singkat.",
      724,
      542,
      388,
      24,
      { size: 18, color: COLORS.ink, align: "right" },
    );
    addFooter(slide, 9);
    addSourceNotes(slide, []);
  }

  for (const [index, slide] of presentation.slides.items.entries()) {
    const stem = `slide-${String(index + 1).padStart(2, "0")}`;
    const png = await presentation.export({ slide, format: "png", scale: 1 });
    await writeBlob(path.join(QA_DIR, `${stem}.png`), png);
  }

  const pptx = await PresentationFile.exportPptx(presentation);
  await pptx.save(FINAL);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
