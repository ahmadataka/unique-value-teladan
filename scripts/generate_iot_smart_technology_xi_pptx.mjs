import fs from "node:fs/promises";
import path from "node:path";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const ROOT = "/Users/ahmadataka/Documents/Codex project/SMA Teladan/unique-value-teladan";
const FINAL = path.join(ROOT, "presentations", "materi-kelas-xi-smart-technology-dan-iot.pptx");
const QA_DIR = path.join(ROOT, "tmp_check_iot_xi_pptx");
const LOGO = "/Users/ahmadataka/Documents/Codex project/SMA Teladan/academic-track-teladan/assets/logo-sma-teladan-yogyakarta.png";

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
    addText(slide, "Materi Kelas XI", 118, 174, 320, 34, {
      size: 24,
      bold: true,
      color: COLORS.blue,
    });
    addText(slide, "Smart Technology\ndan IoT", 112, 224, 420, 140, {
      size: 44,
      bold: true,
      color: COLORS.navy,
    });
    addText(
      slide,
      "Pengantar Internet of Things untuk ide penerapan di sekolah dan greenhouse.",
      114,
      388,
      412,
      86,
      { size: 20, color: COLORS.ink },
    );
    addText(
      slide,
      "Di sesi ini, kita belajar melihat bagaimana sensor, data, dan alat otomatis bisa dipakai untuk membantu lingkungan sekolah maupun farming secara nyata.",
      640,
      170,
      500,
      138,
      { size: 22, color: COLORS.white },
    );
    addText(
      slide,
      "Fokus deck:\n• Konsep IoT\n• Komponen sistem\n• Use case sekolah\n• Use case greenhouse\n• Etika dan tugas",
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
    addHeaderBand(slide, "Apa Itu IoT?");
    addText(
      slide,
      "Internet of Things adalah konsep ketika benda fisik bisa membaca kondisi, mengirim data, dan menerima perintah melalui jaringan.",
      96,
      160,
      1080,
      68,
      { size: 28, bold: true, color: COLORS.navy },
    );
    addBulletList(
      slide,
      [
        "Yang terhubung bukan hanya laptop dan ponsel, tetapi juga sensor, pompa, lampu, kipas, dan alat lain.",
        "IoT membuat alat bisa membantu manusia mengambil keputusan lebih cepat.",
        "Tujuan terbaik IoT bukan sekadar terlihat canggih, tetapi benar-benar menyelesaikan masalah nyata.",
      ],
      102,
      266,
      1020,
      22,
      10,
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 92, top: 546, width: 1084, height: 78 },
      fill: COLORS.sky,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(
      slide,
      "Kalimat kunci: IoT membuat benda bisa merasakan kondisi, mengirim informasi, lalu membantu manusia bertindak.",
      116,
      570,
      1034,
      30,
      { size: 22, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 2);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Komponen Dasar Sistem IoT");
    const rows = [
      ["Sensor", "Membaca kondisi lingkungan seperti suhu, cahaya, kelembapan, atau gerak."],
      ["Controller", "Mengolah data dan menjalankan aturan yang dibuat pengguna."],
      ["Koneksi", "Mengirim data dan menerima perintah, misalnya lewat Wi-Fi."],
      ["Actuator", "Menjalankan aksi fisik seperti menyalakan pompa, kipas, atau lampu."],
      ["Dashboard", "Menampilkan data agar manusia bisa memantau dan mengambil keputusan."],
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
    addFooter(slide, 3);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Bagaimana IoT Bekerja?");
    slide.shapes.add({
      geometry: "rect",
      position: { left: 96, top: 162, width: 1080, height: 398 },
      fill: COLORS.sky2,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    addBulletList(
      slide,
      [
        "Sensor membaca kondisi, misalnya tanah kering atau suhu terlalu panas.",
        "Controller memproses data dan membandingkannya dengan aturan yang sudah dibuat.",
        "Sistem mengirim data ke aplikasi atau dashboard.",
        "Actuator bekerja jika perlu, misalnya menyalakan pompa atau kipas.",
        "Manusia tetap memantau hasilnya dan memperbaiki sistem bila perlu.",
      ],
      124,
      196,
      1010,
      22,
      10,
    );
    addText(
      slide,
      "Urutan sederhananya: baca kondisi -> olah data -> kirim informasi -> jalankan aksi -> cek ulang.",
      110,
      600,
      1040,
      28,
      { size: 21, bold: true, color: COLORS.blue, align: "center" },
    );
    addFooter(slide, 4);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Contoh Smart Technology di Sekolah");
    addBulletList(
      slide,
      [
        "Lampu otomatis untuk area tertentu agar hemat energi.",
        "Monitoring suhu ruang kelas untuk kenyamanan belajar.",
        "Pemantauan penggunaan listrik sebagai bahan evaluasi efisiensi.",
        "Sensor keamanan sederhana pada pintu atau area tertentu.",
        "Dashboard lingkungan sekolah agar data bisa dipakai untuk belajar juga.",
      ],
      112,
      174,
      980,
      21,
      10,
    );
    slide.shapes.add({
      geometry: "rect",
      position: { left: 96, top: 520, width: 1080, height: 98 },
      fill: COLORS.sky,
      line: { style: "solid", fill: "none", width: 0 },
    });
    addText(
      slide,
      "Pertanyaan pentingnya: apakah teknologi ini membantu kenyamanan, keamanan, atau efisiensi sekolah secara nyata?",
      122,
      552,
      1030,
      30,
      { size: 21, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 5);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Contoh Smart Technology di Greenhouse");
    slide.shapes.add({
      geometry: "rect",
      position: { left: 96, top: 162, width: 510, height: 392 },
      fill: COLORS.sky2,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    slide.shapes.add({
      geometry: "rect",
      position: { left: 638, top: 162, width: 538, height: 392 },
      fill: COLORS.white,
      line: { style: "solid", fill: COLORS.line, width: 1 },
    });
    addText(slide, "Contoh fungsi", 120, 190, 220, 28, {
      size: 24,
      bold: true,
      color: COLORS.navy,
    });
    addBulletList(
      slide,
      [
        "Sensor kelembapan tanah untuk membaca kebutuhan air.",
        "Monitoring suhu dan kelembapan udara.",
        "Penyiraman otomatis saat tanah terlalu kering.",
        "Pemantauan cahaya untuk kondisi tumbuh tanaman.",
      ],
      120,
      246,
      430,
      18,
      8,
    );
    addText(slide, "Nilai belajarnya", 664, 190, 220, 28, {
      size: 24,
      bold: true,
      color: COLORS.navy,
    });
    addBulletList(
      slide,
      [
        "Siswa belajar bahwa data lingkungan bisa dipakai untuk keputusan nyata.",
        "Proyek bisa menggabungkan teknologi, sains, dan observasi lapangan.",
        "Hasilnya dapat dipakai sebagai sistem sederhana sekaligus bahan presentasi.",
      ],
      664,
      246,
      448,
      18,
      8,
    );
    addFooter(slide, 6);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Risiko dan Etika IoT");
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
    addText(slide, "Risiko yang perlu diingat", 120, 186, 320, 28, {
      size: 24,
      bold: true,
      color: COLORS.navy,
    });
    addBulletList(
      slide,
      [
        "Sensor bisa salah membaca kondisi.",
        "Koneksi bisa terputus atau tidak stabil.",
        "Perangkat bisa rusak jika lingkungan tidak cocok.",
        "Sistem yang tidak aman bisa diakses pihak yang salah.",
      ],
      120,
      242,
      426,
      18,
      8,
    );
    addText(slide, "Etika penggunaan", 654, 186, 300, 28, {
      size: 24,
      bold: true,
      color: COLORS.navy,
    });
    addBulletList(
      slide,
      [
        "Gunakan teknologi untuk tujuan yang jelas dan bermanfaat.",
        "Jaga keamanan perangkat dan data yang terhubung.",
        "Kalau menyentuh data orang, gunakan dengan tanggung jawab.",
        "Tetap verifikasi hasil sistem dengan pengamatan manusia.",
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
      "IoT yang baik bukan hanya berjalan otomatis, tetapi juga aman, masuk akal, dan berguna.",
      116,
      560,
      1034,
      28,
      { size: 22, bold: true, color: COLORS.navy, align: "center" },
    );
    addFooter(slide, 7);
    addSourceNotes(slide, []);
  }

  {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.white;
    addLogo(slide);
    addHeaderBand(slide, "Tugas Kelompok");
    addText(
      slide,
      "Merancang Ide IoT untuk Sekolah atau Greenhouse",
      96,
      156,
      1080,
      42,
      { size: 30, bold: true, color: COLORS.navy },
    );
    addBulletList(
      slide,
      [
        "Pilih satu konteks: sekolah atau greenhouse/farming.",
        "Tentukan masalah yang ingin dibantu oleh teknologi.",
        "Sebutkan sensor, controller, koneksi, dan actuator yang mungkin dipakai.",
        "Jelaskan alur kerja sistem dari membaca data sampai tindakan.",
        "Tuliskan 2 manfaat dan 2 risiko dari ide tersebut.",
        "Sertakan sketsa atau diagram alur sederhana dari kelompok.",
      ],
      104,
      224,
      1036,
      20,
      8,
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
      "Subject: SMA Teladan XI - Tugas IoT - [Nama Kelompok]",
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
    addFooter(slide, 8);
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
