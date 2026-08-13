import fs from "node:fs/promises";
import path from "node:path";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const ROOT = "/Users/ahmadataka/Documents/Codex project/SMA Teladan/unique-value-teladan";
const FINAL = path.join(ROOT, "presentations", "materi-kelas-xi-smart-home-di-sekolah.pptx");
const QA_DIR = path.join(ROOT, "tmp_check_smart_home_xi_pptx");
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
  nest: {
    blob: await fs.readFile(path.join(PRODUCT_IMAGE_DIR, "nest-thermostat.jpg")),
    contentType: "image/jpeg",
  },
  aqara: {
    blob: await fs.readFile(path.join(PRODUCT_IMAGE_DIR, "aqara-p1.png")),
    contentType: "image/png",
  },
  rachio: {
    blob: await fs.readFile(path.join(PRODUCT_IMAGE_DIR, "rachio.png")),
    contentType: "image/png",
  },
  greenhouse: {
    blob: await fs.readFile(path.join(PRODUCT_IMAGE_DIR, "arduino-greenhouse.jpg")),
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
  addText(slide, "SMA Teladan Yogyakarta • Unique Value Kelas XI", 78, 680, 420, 18, {
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
  addText(slide, title, left + 18, top + 18, width - 36, 34, {
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
    addText(slide, "Materi Kelas XI", 118, 174, 320, 34, {
      size: 24,
      bold: true,
      color: COLORS.blue,
    });
    addText(slide, "Smart Home\n di Sekolah", 112, 224, 420, 140, {
      size: 44,
      bold: true,
      color: COLORS.navy,
    });
    addText(
      slide,
      "Lanjutan dari ide IoT menuju sistem pintar yang lebih utuh untuk sekolah dan greenhouse.",
      114,
      388,
      412,
      88,
      { size: 20, color: COLORS.ink },
    );
    addText(
      slide,
      "Di sesi ini, ide kelompok kalian jadi titik awal. Lalu kita pelajari bagaimana sensor, kontrol, dan aksi otomatis bisa digabung menjadi sistem yang benar-benar berguna.",
      640,
      170,
      500,
      148,
      { size: 22, color: COLORS.white },
    );
    addText(
      slide,
      "Fokus deck:\n• Presentasi ide awal\n• Smart school system\n• Produk nyata\n• Etika\n• Tugas lanjutan",
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
    addHeaderBand(slide, "Kita Mulai dari Ide Kalian Dulu");
    addBulletList(
      slide,
      [
        "Setiap kelompok mempresentasikan ide IoT dari tugas sebelumnya secara singkat.",
        "Fokus presentasi: masalah yang ingin dibantu, sensor atau alat yang dipakai, manfaat, dan tantangan.",
        "Setelah itu, kelas mencari pola bersama: efisiensi energi, keamanan, kenyamanan, monitoring, dan keberlanjutan.",
      ],
      104,
      172,
      1020,
      22,
      12,
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 96, top: 500, width: 1080, height: 118 },
      fill: COLORS.sky,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(
      slide,
      "Tujuan pembuka ini sederhana: kita tidak mulai dari teori kosong. Kalian sudah punya ide, sekarang kita bikin ide itu lebih matang.",
      124,
      534,
      1024,
      52,
      { size: 24, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 2);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "IoT Adalah Bahan, Smart School Adalah Sistem");
    addCard(
      slide,
      96,
      162,
      480,
      354,
      "IoT",
      "Sensor, alat, dan perangkat yang bisa membaca kondisi, mengirim data, lalu membantu aksi. Satu sensor saja belum otomatis menjadi smart system.",
    );
    addCard(
      slide,
      608,
      162,
      568,
      354,
      "Smart School",
      "Gabungan banyak komponen yang bekerja sama: sensor, controller, dashboard, dan actuator. Fokusnya bukan alat tunggal, tetapi manfaat sistem bagi sekolah.",
    );
    addText(
      slide,
      "Sekolah bisa dipandang sebagai rumah besar: ada ruang kelas, taman, greenhouse, listrik, air, dan keamanan yang semuanya bisa dikelola lebih cerdas.",
      100,
      560,
      1060,
      56,
      { size: 22, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 3);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Komponen Inti Smart School");
    const rows = [
      ["Sensor", "Membaca suhu, cahaya, gerak, pintu, kelembapan tanah, atau kondisi ruang."],
      ["Controller", "Mengolah data dan memutuskan aturan aksi sistem."],
      ["Koneksi", "Menghubungkan alat ke dashboard atau aplikasi pemantau."],
      ["Actuator", "Menyalakan lampu, kipas, pompa, buzzer, atau perangkat lain."],
      ["Dashboard", "Menampilkan data supaya manusia bisa memantau dan mengevaluasi."],
    ];
    let y = 154;
    for (const [title, body] of rows) {
      slide.shapes.add({
        geometry: "rect",
        position: { left: 96, top: y, width: 1080, height: 82 },
        fill: y === 154 ? COLORS.sky2 : COLORS.white,
        line: { style: "solid", fill: COLORS.line, width: 1 },
      });
      addText(slide, title, 120, y + 14, 220, 28, {
        size: 22,
        bold: true,
        color: COLORS.navy,
      });
      addText(slide, body, 332, y + 14, 788, 50, {
        size: 18,
        color: COLORS.ink,
      });
      y += 88;
    }
    addFooter(slide, 4);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Diagram Sederhana: Bagaimana Smart School Bekerja");
    const boxes = [
      { x: 96, title: "Sensor", body: "Suhu, cahaya,\ngerak, pintu,\nkelembapan tanah" },
      { x: 326, title: "Controller", body: "ESP32 / Arduino\nmembaca aturan\ndan logika" },
      { x: 556, title: "Dashboard", body: "Data tampil di\nponsel atau web\nuntuk dipantau" },
      { x: 786, title: "Actuator", body: "Lampu, kipas,\npompa, buzzer\nmenjalankan aksi" },
      { x: 1016, title: "Pengguna", body: "Guru / siswa\nmemeriksa data\ndan mengevaluasi" },
    ];
    for (const box of boxes) {
      slide.shapes.add({
        geometry: "roundRect",
        position: { left: box.x, top: 248, width: 170, height: 160 },
        fill: box.title === "Dashboard" ? COLORS.sky : COLORS.white,
        line: { style: "solid", fill: COLORS.line, width: 1.2 },
        borderRadius: "rounded-xl",
      });
      addText(slide, box.title, box.x + 16, 270, 138, 28, {
        size: 22,
        bold: true,
        color: COLORS.navy,
        align: "center",
      });
      addText(slide, box.body, box.x + 16, 318, 138, 72, {
        size: 18,
        color: COLORS.ink,
        align: "center",
      });
    }
    const arrows = [273, 503, 733, 963];
    for (const x of arrows) {
      slide.shapes.add({
        geometry: "rightArrow",
        position: { left: x, top: 300, width: 34, height: 42 },
        fill: COLORS.blue,
        line: { style: "solid", fill: "none", width: 0 },
      });
    }
    slide.shapes.add({
      geometry: "rect",
      position: { left: 96, top: 486, width: 1090, height: 92 },
      fill: COLORS.soft,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(
      slide,
      "Contoh alur: sensor suhu ruang membaca kondisi kelas -> controller memutuskan kipas perlu aktif -> dashboard menampilkan perubahan -> guru bisa memantau apakah sistemnya benar-benar membantu.",
      128,
      514,
      1028,
      44,
      { size: 21, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 5);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Use Case yang Masuk Akal untuk Sekolah dan Greenhouse");
    addBulletList(
      slide,
      [
        "Lampu atau kipas otomatis untuk efisiensi energi di ruang kelas.",
        "Monitoring suhu dan kondisi udara agar ruang belajar lebih nyaman.",
        "Sensor pintu atau gerak untuk keamanan ruangan tertentu.",
        "Penyiraman greenhouse otomatis berbasis kelembapan tanah.",
        "Dashboard sederhana untuk membaca data dan mengevaluasi kebiasaan penggunaan energi atau air.",
      ],
      104,
      168,
      1020,
      22,
      12,
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 96, top: 550, width: 1080, height: 78 },
      fill: COLORS.soft,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(
      slide,
      "Pertanyaan penting: masalah nyata apa yang paling layak dibantu lebih dulu di lingkungan sekolah?",
      126,
      574,
      1020,
      28,
      { size: 22, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 6);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    addProductVisualSlide(slide, {
      header: "Produk Nyata: Google Nest Learning Thermostat",
      title: "Google Nest Learning Thermostat",
      image: PRODUCT_IMAGES.nest,
      summary:
        "Termostat pintar yang mempelajari preferensi suhu dan membantu penghematan energi.",
      points: [
        "Visual produk ini penting agar siswa membayangkan bentuk nyata alat kontrol suhu yang sering hanya dibahas sebagai konsep.",
        "Mudah dipakai untuk menjelaskan sensor suhu, keputusan otomatis, dan kenyamanan ruang belajar.",
        "Bisa jadi inspirasi ide smart classroom, walau versi sekolah tentu perlu disesuaikan dengan fasilitas yang ada.",
      ],
      links: [
        { label: "Produk resmi", text: "Nest Thermostat", url: "https://store.google.com/us/product/nest_learning_thermostat_4th_gen?hl=en-US" },
        { label: "Video / demo", text: "Demo di halaman produk", url: "https://store.google.com/us/product/nest_learning_thermostat_4th_gen?hl=en-US&pli=1" },
      ],
    });
    addFooter(slide, 7);
    addSourceNotes(slide, [
      "Nest product: https://store.google.com/us/product/nest_learning_thermostat_4th_gen?hl=en-US",
      "Nest guide: https://support.google.com/googlehome/answer/9248184?hl=en",
      "Image source: https://termofol.co.uk/product/google-nest-smart-learning-thermostat-stainless-t200377-2nd-gen/",
    ]);
  }

  {
    const slide = presentation.slides.add();
    addProductVisualSlide(slide, {
      header: "Produk Nyata: Aqara Sensors",
      title: "Aqara Motion Sensor",
      image: PRODUCT_IMAGES.aqara,
      summary:
        "Contoh sensor gerak yang menunjukkan bagaimana perangkat kecil bisa menjadi input penting bagi sistem pintar.",
      points: [
        "Visual ini membantu siswa melihat bahwa sensor adalah benda fisik yang konkret, bukan sekadar istilah di diagram.",
        "Mudah dikaitkan dengan ide keamanan ruang, lampu otomatis, atau notifikasi akses.",
        "Sekaligus membuka diskusi penting tentang privasi, batas pemantauan, dan kebutuhan nyata.",
      ],
      links: [
        { label: "Produk resmi", text: "Motion Sensor P1", url: "https://us.aqara.com/products/motion-sensor-p1" },
        { label: "Video / demo", text: "Installation video", url: "https://www.aqara.com/en/product/motion-sensor-p1/installation-video/" },
      ],
    });
    addFooter(slide, 8);
    addSourceNotes(slide, [
      "Aqara Motion Sensor P1: https://us.aqara.com/products/motion-sensor-p1",
      "Aqara sensors: https://us.aqara.com/collections/smart-home-sensor",
      "Image source: https://www.ecowizard.co.uk/smart-security/aqara-motion-sensor-p1/",
    ]);
  }

  {
    const slide = presentation.slides.add();
    addProductVisualSlide(slide, {
      header: "Produk Nyata: Rachio Smart Sprinkler",
      title: "Rachio Smart Sprinkler",
      image: PRODUCT_IMAGES.rachio,
      summary:
        "Contoh sistem penyiraman pintar yang menggabungkan controller dan aplikasi untuk pengelolaan air.",
      points: [
        "Visual ini membantu siswa melihat hubungan antara hardware dan aplikasi pemantau di ponsel.",
        "Sangat cocok untuk ide greenhouse, taman sekolah, atau area tanam berbasis data.",
        "Mudah dipakai untuk diskusi tentang efisiensi air dan keberlanjutan.",
      ],
      links: [
        { label: "Produk resmi", text: "Rachio 3", url: "https://rachio.com/products/rachio-3" },
        { label: "Video / demo", text: "Rachio demo page", url: "https://go.rachio.com/srp/" },
      ],
    });
    addFooter(slide, 9);
    addSourceNotes(slide, [
      "Rachio products: https://rachio.com/products",
      "Rachio quick start: https://support.rachio.com/en_us/rachio-smart-sprinkler-controller-quick-start-guide-rkmbECixZe",
      "Image source: https://rachio.com/",
    ]);
  }

  {
    const slide = presentation.slides.add();
    addProductVisualSlide(slide, {
      header: "Produk Nyata: Arduino Greenhouse Kit",
      title: "Arduino Greenhouse Kit",
      image: PRODUCT_IMAGES.greenhouse,
      summary:
        "Kit edukasi greenhouse yang memperlihatkan sensor, pompa, kontrol, dan lingkungan tanam dalam satu sistem.",
      points: [
        "Visual ini penting karena siswa bisa langsung melihat bahwa smart greenhouse bukan ide abstrak, tetapi sistem yang bisa dirakit.",
        "Mudah dipakai untuk menjelaskan hubungan sensor, dashboard, relay, pompa, dan tanaman.",
        "Sangat cocok untuk proyek sustainability sekolah dan ideation berbasis data nyata.",
      ],
      links: [
        { label: "Produk resmi", text: "Arduino Greenhouse Kit", url: "https://www.arduino.cc/education/greenhouse/" },
        { label: "Demo / project", text: "Greenhouse Project", url: "https://www.arduino.cc/education/greenhouse-project" },
      ],
    });
    addFooter(slide, 10);
    addSourceNotes(slide, [
      "Arduino Greenhouse Kit: https://www.arduino.cc/education/greenhouse/",
      "Arduino Greenhouse Project: https://www.arduino.cc/education/greenhouse-project",
      "Image source: https://technologieservices.fr/ts_fr/277630.html",
    ]);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Sistem Pintar Tetap Perlu Etika dan Batas yang Jelas");
    addBulletList(
      slide,
      [
        "Jangan mengumpulkan data yang tidak perlu.",
        "Pikirkan privasi jika sistem menyentuh area pemantauan orang atau ruang pribadi.",
        "Perhatikan keamanan akses jika alat bisa menyalakan perangkat, membuka ruang, atau mengirim notifikasi.",
        "Rancang juga skenario gagal: apa yang terjadi jika sensor salah membaca atau koneksi putus?",
        "Teknologi harus membantu keputusan manusia, bukan membuat pengguna pasif.",
      ],
      104,
      170,
      1020,
      22,
      12,
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 96, top: 544, width: 1080, height: 84 },
      fill: COLORS.sky,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(
      slide,
      "Pertanyaan kunci: sistem pintar yang baik itu aman, berguna, masuk akal, dan bisa dipertanggungjawabkan.",
      120,
      570,
      1030,
      28,
      { size: 22, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 11);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Tugas Kelompok");
    addText(
      slide,
      "Menyempurnakan ide menjadi konsep Smart School atau Smart Greenhouse",
      96,
      156,
      1080,
      40,
      { size: 28, bold: true, color: COLORS.navy, align: "center" },
    );
    addBulletList(
      slide,
      [
        "Ambil kembali ide IoT kelompok dari pertemuan sebelumnya.",
        "Pilih arah proyek: smart school atau smart greenhouse.",
        "Perjelas masalah, komponen sistem, alur kerja, manfaat, dan risiko.",
        "Pilih satu produk nyata sebagai referensi dan jelaskan apa yang bisa ditiru.",
        "Sertakan tiga prinsip etika yang harus dijaga jika sistem ini benar-benar dipakai.",
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
      "Kirim ke ataka.ahmad@gmail.com\nSubject: SMA Teladan XI - Tugas Smart Home - [Nama Kelompok]",
      120,
      566,
      1030,
      42,
      { size: 20, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 12);
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
