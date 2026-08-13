import fs from "node:fs/promises";
import path from "node:path";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const ROOT = "/Users/ahmadataka/Documents/Codex project/SMA Teladan/unique-value-teladan";
const FINAL = path.join(ROOT, "presentations", "materi-kelas-x-ar-vr-untuk-pendidikan.pptx");
const QA_DIR = path.join(ROOT, "tmp_check_ar_vr_x_pptx");
const LOGO = "/Users/ahmadataka/Documents/Codex project/SMA Teladan/academic-track-teladan/assets/logo-sma-teladan-yogyakarta.png";
const PRODUCT_IMAGE_DIR = path.join(ROOT, "assets", "product-images");

const W = 1280;
const H = 720;
const FRAME = { left: 76, top: 78, width: 1128, height: 548 };
const COLORS = {
  navy: "#16324F",
  blue: "#24577A",
  sky: "#EAF3F8",
  sky2: "#F5FAFD",
  ink: "#1F2933",
  muted: "#5B6770",
  line: "#C8D6E2",
  white: "#FFFFFF",
  soft: "#EEF5F8",
};

const logoBytes = await fs.readFile(LOGO);
const PRODUCT_IMAGES = {
  assemblr: {
    blob: await fs.readFile(path.join(PRODUCT_IMAGE_DIR, "assemblr-edu.png")),
    contentType: "image/png",
  },
  mergeCube: {
    blob: await fs.readFile(path.join(PRODUCT_IMAGE_DIR, "merge-cube.jpg")),
    contentType: "image/jpeg",
  },
  classvr: {
    blob: await fs.readFile(path.join(PRODUCT_IMAGE_DIR, "classvr.jpg")),
    contentType: "image/jpeg",
  },
  googleArts: {
    blob: await fs.readFile(path.join(PRODUCT_IMAGE_DIR, "google-arts-culture.jpg")),
    contentType: "image/jpeg",
  },
};

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
    addText(slide, item, left + 22, y, width - 22, fontSize * 2.2, {
      size: fontSize,
      color: COLORS.ink,
    });
    y += fontSize * 2.0 + gap;
  }
}

function addWrappedBulletText(slide, items, left, top, width, height, fontSize = 18) {
  const shape = slide.shapes.add({
    geometry: "textbox",
    position: { left, top, width, height },
    fill: "none",
    line: { style: "solid", fill: "none", width: 0 },
  });
  shape.text = items.map((item) => `• ${item}`).join("\n");
  shape.text.style = {
    fontFace: "Aptos",
    fontSize,
    color: COLORS.ink,
    alignment: "left",
  };
  return shape;
}

function addSourceNotes(slide, lines) {
  slide.speakerNotes.textFrame.setText(["[Sources]", ...lines]);
  slide.speakerNotes.setVisible(true);
}

function addCard(slide, left, top, width, height, title, body) {
  slide.shapes.add({
    geometry: "rect",
    position: { left, top, width, height },
    fill: COLORS.white,
    line: { style: "solid", fill: COLORS.line, width: 1 },
  });
  addText(slide, title, left + 18, top + 18, width - 36, 28, {
    size: 24,
    bold: true,
    color: COLORS.navy,
  });
  addText(slide, body, left + 18, top + 60, width - 36, height - 78, {
    size: 19,
    color: COLORS.ink,
  });
}

function addLinkBlock(slide, items, left, top, width, lineHeight = 24) {
  const shape = slide.shapes.add({
    geometry: "textbox",
    position: { left, top, width, height: Math.max(60, items.length * lineHeight + 12) },
    fill: "none",
    line: { style: "solid", fill: "none", width: 0 },
  });
  shape.text.set(
    items.map((item) => ({
      runs: [
        {
          run: `${item.label}: `,
          textStyle: { bold: true, color: COLORS.navy, fontSize: "15pt" },
        },
        {
          run: item.text,
          textStyle: { color: "#2563EB", underline: "sng", fontSize: "15pt" },
          link: { uri: item.url, isExternal: true },
        },
      ],
      spaceAfter: 3,
    })),
  );
  return shape;
}

function addProductVisualSlide(slide, config) {
  slide.background.fill = COLORS.white;
  addLogo(slide);
  addHeaderBand(slide, config.header);
  slide.shapes.add({
    geometry: "rect",
    position: { left: 96, top: 152, width: 420, height: 430 },
    fill: COLORS.sky,
    line: { style: "solid", fill: "none", width: 0 },
  });
  slide.images.add({
    blob: config.image.blob,
    contentType: config.image.contentType,
    alt: config.title,
    fit: config.imageFit ?? "contain",
    position: { left: 118, top: 178, width: 376, height: 270 },
  });
  addText(slide, "Tampilan produk", 226, 470, 160, 24, {
    size: 16,
    bold: true,
    color: COLORS.muted,
    align: "center",
  });
  addText(slide, config.title, 560, 176, 588, 40, {
    size: 30,
    bold: true,
    color: COLORS.navy,
  });
  addText(slide, config.summary, 560, 228, 588, 84, {
    size: 20,
    color: COLORS.ink,
  });
  addWrappedBulletText(slide, config.points, 568, 334, 552, 168, 18);
  addText(slide, "Link yang bisa dibuka:", 560, 520, 220, 22, {
    size: 18,
    bold: true,
    color: COLORS.navy,
  });
  addLinkBlock(slide, config.links, 560, 548, 540, 22);
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
    addText(slide, "AR dan VR\nuntuk Pendidikan", 112, 224, 420, 140, {
      size: 44,
      bold: true,
      color: COLORS.navy,
    });
    addText(
      slide,
      "Lanjutan dari AI visual menuju pengalaman belajar yang lebih imersif dan lebih interaktif.",
      114,
      388,
      412,
      86,
      { size: 20, color: COLORS.ink },
    );
    addText(
      slide,
      "Di sesi ini, kita tidak berhenti pada gambar. Kita melihat bagaimana visual bisa hadir di depan siswa dan membantu pemahaman materi secara lebih konkret.",
      640,
      170,
      500,
      146,
      { size: 22, color: COLORS.white },
    );
    addText(
      slide,
      "Fokus deck:\n• AR vs VR\n• Use case akademik\n• Produk nyata\n• Etika\n• Tugas lanjutan",
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
    addHeaderBand(slide, "Dari AI Visual ke Pengalaman Belajar yang Lebih Hidup");
    addText(
      slide,
      "Kalau kemarin kalian membuat dan membaca visual, sekarang pertanyaannya berubah:",
      96,
      156,
      1080,
      36,
      { size: 28, bold: true, color: COLORS.navy },
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 96, top: 222, width: 1080, height: 126 },
      fill: COLORS.sky,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(
      slide,
      "Bagaimana kalau visual itu tidak hanya dilihat, tetapi terasa hadir di depan kita?",
      140,
      256,
      992,
      56,
      { size: 30, bold: true, color: COLORS.navy, align: "center" },
    );
    addBulletList(
      slide,
      [
        "AR dan VR membantu konsep abstrak menjadi lebih dekat dan lebih konkret.",
        "Teknologi ini bisa dipakai untuk memahami materi, simulasi, dan presentasi ide proyek.",
        "Kuncinya tetap sama: bukan sekadar wow effect, tetapi nilai belajarnya.",
      ],
      104,
      396,
      1020,
      22,
      12,
    );
    addFooter(slide, 2);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "AR Menambah Dunia Nyata, VR Membuat Ruang Baru");
    addCard(
      slide,
      96,
      162,
      480,
      360,
      "AR",
      "Augmented Reality menambahkan objek atau informasi digital ke dunia nyata. Biasanya cukup memakai kamera ponsel atau tablet. Cocok untuk model 3D, poster interaktif, atau presentasi berbasis ruang sekitar.",
    );
    addCard(
      slide,
      608,
      162,
      568,
      360,
      "VR",
      "Virtual Reality membawa pengguna masuk ke lingkungan digital. Pengalaman ini cocok untuk tur virtual, simulasi laboratorium, atau eksplorasi tempat yang sulit dikunjungi langsung.",
    );
    addText(
      slide,
      "Kalimat kunci: AR menempel pada dunia nyata, VR mengajak kita masuk ke dunia virtual.",
      120,
      570,
      1030,
      28,
      { size: 22, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 3);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "AR dan VR Berguna Saat Materi Sulit Dibayangkan");
    addBulletList(
      slide,
      [
        "Biologi: model organ, sel, atau struktur tubuh menjadi lebih mudah diamati.",
        "Fisika dan astronomi: simulasi gerak benda, tata surya, atau medan ruang.",
        "Sejarah dan budaya: tur virtual museum, situs bersejarah, dan artefak.",
        "Geografi: bentuk permukaan bumi, gunung, kota, atau ruang greenhouse lebih mudah divisualkan.",
        "Presentasi proyek: siswa bisa menunjukkan rancangan ide secara lebih jelas kepada teman dan guru.",
      ],
      104,
      168,
      1030,
      22,
      12,
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 96, top: 548, width: 1080, height: 80 },
      fill: COLORS.soft,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(
      slide,
      "Teknologi ini paling kuat ketika membantu sesuatu yang abstrak menjadi terasa nyata.",
      120,
      574,
      1030,
      28,
      { size: 22, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 4);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    addProductVisualSlide(slide, {
      header: "Produk Nyata: Assemblr EDU",
      title: "Assemblr EDU",
      image: PRODUCT_IMAGES.assemblr,
      summary:
        "Platform 3D dan AR untuk pendidikan yang membantu guru dan siswa membuat materi lebih interaktif.",
      points: [
        "Visual ini penting agar siswa melihat bahwa AR pendidikan tidak selalu berupa headset; browser dan gadget biasa juga bisa dipakai.",
        "Cocok untuk presentasi proyek, visualisasi konsep abstrak, dan tugas berbasis model 3D.",
        "Relevan dengan konteks sekolah karena antarmukanya mirip platform belajar yang sudah akrab untuk siswa.",
      ],
      links: [
        { label: "Produk resmi", text: "Assemblr EDU", url: "https://about.edu.assemblrworld.com/id" },
        { label: "Video / demo", text: "Case study Assemblr EDU", url: "https://www.assemblrworld.com/es/case-study/assemblr-edu" },
      ],
    });
    addFooter(slide, 5);
    addSourceNotes(slide, [
      "Assemblr EDU: https://about.edu.assemblrworld.com/id",
      "Assemblr EDU case study: https://www.assemblrworld.com/id/case-study/assemblr-edu",
      "Image source: https://www.assemblrworld.com/id/blog/edu-kits-are-here-transforming-digital-teaching-aids",
    ]);
  }

  {
    const slide = presentation.slides.add();
    addProductVisualSlide(slide, {
      header: "Produk Nyata: Merge Cube",
      title: "Merge Cube",
      image: PRODUCT_IMAGES.mergeCube,
      summary:
        "Kubus fisik yang dipindai kamera untuk menampilkan objek digital 3D di tangan pengguna.",
      points: [
        "Visual produk ini penting karena siswa langsung paham bahwa AR bisa terasa seperti memegang objek belajar.",
        "Sangat cocok untuk sains: organ, fosil, molekul, atau tata surya terasa lebih nyata.",
        "Bisa jadi inspirasi bagi kelompok untuk membuat pengalaman AR yang sederhana tapi kuat secara edukatif.",
      ],
      links: [
        { label: "Produk resmi", text: "Merge EDU", url: "https://mergeedu.com" },
        { label: "Video / demo", text: "Getting started", url: "https://support.mergeedu.com/hc/en-us/articles/360061597232-Getting-Started-Welcome-to-Merge-EDU" },
      ],
    });
    addFooter(slide, 6);
    addSourceNotes(slide, [
      "Merge Cube info: https://support.mergeedu.com/hc/en-us/articles/360052933552-Get-a-Merge-Cube",
      "Merge Cube page: https://mergeedu.com/cube/it?lang=it",
      "Image source: https://www.ubuy.com.om/ar/product/2IEH9BU-merge-cube-hold-anything-science-and-stem-educational-tool-hands-on-digital-teaching-aids-science-simulations-and-stem-projects-home-school-remote-and",
    ]);
  }

  {
    const slide = presentation.slides.add();
    addProductVisualSlide(slide, {
      header: "Produk Nyata: ClassVR",
      title: "ClassVR",
      image: PRODUCT_IMAGES.classvr,
      summary:
        "Headset VR yang dirancang khusus untuk sekolah, lengkap dengan konten dan kontrol kelas.",
      points: [
        "Visual produk ini membantu siswa membayangkan bahwa VR sekolah berbeda dari VR gim biasa.",
        "Yang penting bukan hanya headsetnya, tetapi juga portal guru, konten, dan kontrol pemakaian di kelas.",
        "Cocok untuk virtual field trip, simulasi sains, dan pengalaman belajar terarah.",
      ],
      links: [
        { label: "Produk resmi", text: "ClassVR", url: "https://www.classvr.com/us/" },
        { label: "Cara kerja", text: "How ClassVR Works", url: "https://www.classvr.com/how-classvr-works/" },
      ],
    });
    addFooter(slide, 7);
    addSourceNotes(slide, [
      "ClassVR: https://www.classvr.com/us/",
      "ClassVR headset page: https://www.classvr.com/us/virtual-reality-headsets/",
      "Image source: https://www.cdw.com/product/avantis-classvr-add-on-headset-8-pack/7083391",
    ]);
  }

  {
    const slide = presentation.slides.add();
    addProductVisualSlide(slide, {
      header: "Produk Nyata: Google Arts & Culture",
      title: "Google Arts & Culture",
      image: PRODUCT_IMAGES.googleArts,
      summary:
        "Platform tur virtual, museum digital, dan pengalaman budaya 360 derajat yang bisa diakses dari perangkat biasa.",
      points: [
        "Visual ini penting agar siswa melihat bentuk nyata tur virtual, bukan hanya membayangkan dari kata-kata.",
        "Sangat kuat untuk sejarah, seni, budaya, dan literasi visual lintas mata pelajaran.",
        "Menunjukkan bahwa pengalaman imersif tidak selalu memerlukan headset; ponsel dan browser pun bisa cukup.",
      ],
      links: [
        { label: "Produk resmi", text: "Pocket Gallery", url: "https://artsandculture.google.com/project/pocket-gallery" },
        { label: "Video / demo", text: "Pocket Gallery demo", url: "https://artsandculture.google.com/project/pocket-gallery" },
      ],
    });
    addFooter(slide, 8);
    addSourceNotes(slide, [
      "Google Arts & Culture virtual tours: https://artsandculture.google.com/project/virtual-tours",
      "Google Arts & Culture story: https://artsandculture.google.com/story/LwVhZHf_Y7FfLg",
      "Image source: https://windowsight.com/art-is-going-digital-in-2020/",
    ]);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Teknologi Imersif Tetap Perlu Etika dan Tujuan yang Jelas");
    addBulletList(
      slide,
      [
        "Jangan terjebak pada efek keren jika nilai belajarnya tipis.",
        "Hormati privasi saat memakai kamera atau memindai ruang sekitar.",
        "Pastikan konten visual tetap akurat dan tidak menyesatkan.",
        "Perhatikan kenyamanan pengguna; tidak semua orang nyaman memakai sistem imersif lama-lama.",
        "Teknologi harus membantu berpikir, bukan membuat siswa pasif menerima pengalaman.",
      ],
      104,
      170,
      1020,
      22,
      12,
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 96, top: 542, width: 1080, height: 86 },
      fill: COLORS.sky,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(
      slide,
      "Pertanyaan kritis: apakah teknologi ini benar-benar membantu belajar, atau hanya terlihat canggih?",
      126,
      570,
      1020,
      28,
      { size: 22, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 9);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Tugas Kelompok");
    addText(
      slide,
      "Dari AI Visual ke AR/VR: merancang pembelajaran yang lebih interaktif",
      96,
      156,
      1080,
      40,
      { size: 28, bold: true, color: COLORS.navy, align: "center" },
    );
    addBulletList(
      slide,
      [
        "Pilih satu topik pelajaran yang cocok dibuat lebih imersif.",
        "Tentukan apakah ide kalian lebih cocok memakai AR atau VR.",
        "Sambungkan dengan tugas AI visual sebelumnya: boleh pakai mockup, gambar, atau ide visual lama.",
        "Jelaskan alur penggunaannya di kelas, manfaat akademik, risiko, dan aturan etikanya.",
        "Pilih satu produk nyata sebagai referensi dan jelaskan apa yang bisa ditiru.",
      ],
      104,
      228,
      1020,
      21,
      10,
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 96, top: 540, width: 1080, height: 90 },
      fill: COLORS.soft,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(
      slide,
      "Kirim ke ataka.ahmad@gmail.com\nSubject: SMA Teladan X - Tugas AR VR - [Nama Kelompok]",
      120,
      566,
      1030,
      42,
      { size: 20, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 10);
    addSourceNotes(slide, []);
  }

  for (const [index, slide] of presentation.slides.items.entries()) {
    const png = await presentation.export({ slide, format: "png", scale: 1 });
    await writeBlob(path.join(QA_DIR, `slide-${String(index + 1).padStart(2, "0")}.png`), png);
  }

  const pptx = await PresentationFile.exportPptx(presentation);
  await pptx.save(FINAL);
}

await main();
