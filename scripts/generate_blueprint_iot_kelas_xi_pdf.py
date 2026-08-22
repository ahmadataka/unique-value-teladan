from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


OUTPUT_PATH = Path(
    "/Users/ahmadataka/Documents/Codex project/SMA Teladan/unique-value-teladan/"
    "pdf/materi-kelas-xi-blueprint-solusi-iot.pdf"
)


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="TitleTeladan", parent=styles["Title"], fontName="Helvetica-Bold",
        fontSize=21, leading=25, textColor=colors.HexColor("#16324F"),
        alignment=TA_CENTER, spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name="SubtitleTeladan", parent=styles["Normal"], fontName="Helvetica",
        fontSize=11, leading=15, alignment=TA_CENTER,
        textColor=colors.HexColor("#355C7D"), spaceAfter=12,
    ))
    styles.add(ParagraphStyle(
        name="SectionTeladan", parent=styles["Heading2"], fontName="Helvetica-Bold",
        fontSize=14, leading=18, textColor=colors.white,
        backColor=colors.HexColor("#24577A"), borderPadding=(6, 8, 6),
        spaceBefore=10, spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name="BodyTeladan", parent=styles["BodyText"], fontName="Helvetica",
        fontSize=10.8, leading=15.4, textColor=colors.HexColor("#1F2933"),
        alignment=TA_JUSTIFY, spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="CalloutTeladan", parent=styles["BodyText"], fontName="Helvetica-Bold",
        fontSize=10.8, leading=15, textColor=colors.HexColor("#16324F"),
        backColor=colors.HexColor("#EAF3F8"), borderPadding=(7, 9, 7), spaceAfter=10,
    ))
    styles.add(ParagraphStyle(
        name="TableCellTeladan", parent=styles["BodyText"], fontName="Helvetica",
        fontSize=8.6, leading=10.5, textColor=colors.HexColor("#1F2933"),
    ))
    styles.add(ParagraphStyle(
        name="TableHeadTeladan", parent=styles["BodyText"], fontName="Helvetica-Bold",
        fontSize=8.9, leading=10.7, textColor=colors.white,
    ))
    styles.add(ParagraphStyle(
        name="SmallTeladan", parent=styles["BodyText"], fontName="Helvetica",
        fontSize=8.8, leading=11.5, textColor=colors.HexColor("#425466"), spaceAfter=4,
    ))
    styles.add(ParagraphStyle(
        name="DiagramTeladan", parent=styles["BodyText"], fontName="Helvetica-Bold",
        fontSize=8.3, leading=10, textColor=colors.HexColor("#16324F"), alignment=TA_CENTER,
    ))
    return styles


def bullet_list(items, style):
    return ListFlowable(
        [ListItem(Paragraph(item, style), leftIndent=6) for item in items],
        bulletType="bullet", start="circle", leftIndent=16,
        bulletFontName="Helvetica", bulletFontSize=10, bulletOffsetY=2,
    )


def wrapped(data, head_style, cell_style):
    return [
        [Paragraph(str(cell), head_style if row_index == 0 else cell_style) for cell in row]
        for row_index, row in enumerate(data)
    ]


def standard_table(data, widths, styles, alternate=True):
    table = Table(wrapped(data, styles["TableHeadTeladan"], styles["TableCellTeladan"]), colWidths=widths)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#24577A")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.45, colors.HexColor("#B7C5D1")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ] + ([("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F4F8FB")])] if alternate else [])))
    return table


def system_diagram(styles):
    labels = [
        "Sensor<br/><font name='Helvetica'>membaca kondisi</font>",
        "Controller<br/><font name='Helvetica'>memutuskan aksi</font>",
        "Koneksi<br/><font name='Helvetica'>mengirim data</font>",
        "Dashboard<br/><font name='Helvetica'>memantau</font>",
        "Actuator<br/><font name='Helvetica'>melakukan aksi</font>",
    ]
    boxes = [Paragraph(label, styles["DiagramTeladan"]) for label in labels]
    arrows = [Paragraph("<b>&rarr;</b>", styles["DiagramTeladan"]) for _ in range(4)]
    row = [boxes[0], arrows[0], boxes[1], arrows[1], boxes[2], arrows[2], boxes[3], arrows[3], boxes[4]]
    diagram = Table([row], colWidths=[2.55 * cm, .42 * cm, 2.55 * cm, .42 * cm, 2.55 * cm, .42 * cm, 2.55 * cm, .42 * cm, 2.55 * cm])
    diagram.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), colors.HexColor("#DDEEF5")),
        ("BACKGROUND", (2, 0), (2, 0), colors.HexColor("#E5F2E7")),
        ("BACKGROUND", (4, 0), (4, 0), colors.HexColor("#FFF1D6")),
        ("BACKGROUND", (6, 0), (6, 0), colors.HexColor("#EDE7F6")),
        ("BACKGROUND", (8, 0), (8, 0), colors.HexColor("#FDE6E1")),
        ("BOX", (0, 0), (0, 0), .6, colors.HexColor("#5593B8")),
        ("BOX", (2, 0), (2, 0), .6, colors.HexColor("#67A56B")),
        ("BOX", (4, 0), (4, 0), .6, colors.HexColor("#C8943E")),
        ("BOX", (6, 0), (6, 0), .6, colors.HexColor("#8B70B2")),
        ("BOX", (8, 0), (8, 0), .6, colors.HexColor("#C87562")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3),
        ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return diagram


def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.HexColor("#5B6770"))
    canvas.drawRightString(A4[0] - 1.7 * cm, 1.2 * cm, f"Halaman {doc.page}")
    canvas.restoreState()


def build_pdf():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    styles = build_styles()
    story = []

    story.append(Spacer(1, .6 * cm))
    story.append(Paragraph("Materi Kelas XI: Dari Ide ke Blueprint", styles["TitleTeladan"]))
    story.append(Paragraph("Merancang Solusi IoT untuk SMA Teladan", styles["SubtitleTeladan"]))
    story.append(Paragraph(
        "Halo teman-teman. Kalian sudah punya ide IoT untuk sekolah atau greenhouse. Sekarang kita naik satu langkah: ide itu akan diubah menjadi <b>blueprint</b>, yaitu rancangan yang menjelaskan masalah, cara kerja sistem, komponen, biaya, dan risiko. Kalian belum perlu merakit alat hari ini. Kalian akan berpikir seperti tim produk dan engineer yang menyiapkan rancangan sebelum prototipe dibuat.",
        styles["CalloutTeladan"],
    ))

    story.append(Paragraph("1. Tujuan Pembelajaran", styles["SectionTeladan"]))
    story.append(bullet_list([
        "Kalian dapat merangkum kembali ide IoT kelompok dengan lebih fokus.",
        "Kalian dapat memilih masalah nyata, pengguna, dan ukuran keberhasilan solusi.",
        "Kalian dapat membuat diagram sistem yang masuk akal dari sensor sampai aksi.",
        "Kalian dapat membandingkan kandidat komponen dan menyusun estimasi biaya awal.",
        "Kalian dapat mempertimbangkan keselamatan, privasi, dan etika sebelum sebuah solusi dibangun.",
    ], styles["BodyTeladan"]))

    story.append(Paragraph("2. Mengingat Kembali Ide IoT Kalian", styles["SectionTeladan"]))
    story.append(Paragraph(
        "Pada pertemuan sebelumnya, kelompok kalian sudah memikirkan ide <b>Smart School</b> atau <b>Smart Greenhouse</b>. Ide yang baik belum tentu langsung siap dibuat. Agar siap, kita perlu menjawab: masalah siapa yang dibantu, data apa yang dibaca, keputusan apa yang dibuat, dan apa bukti bahwa solusi itu benar-benar berguna.",
        styles["BodyTeladan"],
    ))
    story.append(Paragraph(
        "Tantangan hari ini: jangan mulai dari alat yang keren. Mulailah dari masalah yang cukup penting untuk diselesaikan.",
        styles["CalloutTeladan"],
    ))

    story.append(Paragraph("3. Menentukan Masalah dan Pihak yang Terlibat", styles["SectionTeladan"]))
    story.append(standard_table([
        ["Pertanyaan", "Contoh Smart Greenhouse", "Contoh Smart School"],
        ["Masalah apa?", "Tanaman bisa terlambat disiram ketika tanah mulai terlalu kering.", "Lampu atau kipas ruang kelas tetap menyala ketika ruangan kosong."],
        ["Siapa terdampak?", "Tim greenhouse, guru, dan tanaman.", "Siswa, guru, petugas sarana, dan sekolah."],
        ["Bukti sederhana?", "Catatan kondisi tanah atau hasil observasi beberapa hari.", "Observasi jadwal pemakaian ruang dan lampu/kipas yang menyala."],
        ["Batas solusi?", "Bukan pengganti perawatan manusia.", "Tidak boleh merekam identitas atau wajah siswa tanpa alasan jelas."],
    ], [3.2 * cm, 6.9 * cm, 6.9 * cm], styles))
    story.append(Spacer(1, 5))
    story.append(bullet_list([
        "Tulis masalah dalam satu kalimat yang spesifik, misalnya: 'Tim greenhouse kesulitan mengetahui kapan media tanam terlalu kering saat tidak berada di lokasi.'",
        "Sebutkan paling sedikit dua pihak yang akan memakai atau terdampak oleh sistem.",
        "Hindari masalah yang terlalu besar seperti 'membuat sekolah menjadi canggih'. Persempit menjadi sesuatu yang bisa diuji.",
    ], styles["BodyTeladan"]))

    story.append(PageBreak())
    story.append(Paragraph("4. Solusi dan Ukuran Keberhasilan", styles["SectionTeladan"]))
    story.append(Paragraph(
        "Solusi bukan sekadar nama alat. Solusi harus menjelaskan <b>apa yang terjadi ketika sistem membaca kondisi tertentu</b>. Setelah itu, tentukan ukuran keberhasilan yang dapat diamati. Ukuran ini belum harus sempurna, tetapi harus bisa dibuktikan ketika prototipe dibuat nanti.",
        styles["BodyTeladan"],
    ))
    story.append(standard_table([
        ["Bagian", "Contoh yang masih umum", "Contoh yang lebih siap diuji"],
        ["Solusi", "Membuat greenhouse pintar.", "Sensor tanah mengirim pembacaan; sistem memberi notifikasi ketika nilai melewati batas kering."],
        ["Aksi", "Membantu menyiram tanaman.", "Pompa menyala maksimal 20 detik setelah kelembapan berada di bawah ambang yang sudah diuji."],
        ["Metrik", "Tanaman lebih sehat.", "Data tercatat dan notifikasi terkirim; penyiraman tidak dilakukan saat tanah masih cukup lembap."],
    ], [3.0 * cm, 5.8 * cm, 8.2 * cm], styles))
    story.append(Spacer(1, 5))
    story.append(Paragraph(
        "Contoh metrik yang bisa dipakai: jumlah pembacaan sensor yang berhasil dicatat, waktu respons notifikasi, berkurangnya lampu yang menyala saat ruangan kosong, atau jumlah penyiraman yang dilakukan sesuai ambang. Metrik harus membantu kita belajar, bukan sekadar membuat angka terlihat bagus.",
        styles["CalloutTeladan"],
    ))

    story.append(Paragraph("5. Blueprint Sistem: Dari Input ke Aksi", styles["SectionTeladan"]))
    story.append(Paragraph(
        "Blueprint sistem menunjukkan aliran kerja. Sistem yang baik tidak perlu rumit, tetapi setiap bagian perlu punya alasan. Sensor membaca kondisi, controller menjalankan aturan, koneksi mengirim data bila diperlukan, dashboard membantu manusia memantau, dan actuator menjalankan tindakan fisik.",
        styles["BodyTeladan"],
    ))
    story.append(system_diagram(styles))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "Contoh: sensor kelembapan tanah membaca kondisi media tanam &rarr; ESP32 membandingkan nilai dengan ambang &rarr; data dikirim lewat Wi-Fi &rarr; dashboard menampilkan status &rarr; relay menyalakan pompa. Manusia tetap dapat mengecek data dan menghentikan aksi jika ada keadaan tidak wajar.",
        styles["SmallTeladan"],
    ))

    story.append(Paragraph("6. Memilih Komponen dengan Alasan", styles["SectionTeladan"]))
    story.append(bullet_list([
        "<b>Controller:</b> pilih yang punya kemampuan cukup untuk proyek. ESP32 cocok untuk banyak ide pemula karena menyediakan Wi-Fi dan Bluetooth. Arduino dapat dipilih bila fokusnya rangkaian lokal yang sederhana.",
        "<b>Sensor:</b> pilih berdasarkan kondisi yang ingin diketahui, bukan berdasarkan popularitas. Suhu/kelembapan udara, kelembapan tanah, cahaya, gerak, atau bukaan pintu adalah contoh input.",
        "<b>Actuator:</b> pilih aksi yang aman dan proporsional, misalnya LED indikator, buzzer, kipas kecil, atau pompa DC kecil. Jangan merencanakan sambungan listrik PLN tanpa pendampingan teknis guru.",
        "<b>Konektivitas dan dashboard:</b> Wi-Fi sekolah, jaringan lokal, atau pencatatan lokal bisa dipilih sesuai kebutuhan. Dashboard hanya perlu menampilkan data yang benar-benar berguna bagi pengguna.",
    ], styles["BodyTeladan"]))

    story.append(PageBreak())
    story.append(Paragraph("7. Contoh Kandidat Komponen dan Estimasi Awal", styles["SectionTeladan"]))
    story.append(Paragraph(
        "Tabel ini adalah contoh paket awal untuk sebuah greenhouse sederhana. Harga adalah <b>ilustrasi hasil penelusuran pada Agustus 2026</b>, bukan daftar belanja wajib. Harga, stok, ongkir, dan versi produk dapat berubah. Kelompok kalian wajib membuka tautan sumber dan mengganti dengan harga yang kalian temukan sendiri saat menyusun laporan.",
        styles["CalloutTeladan"],
    ))
    story.append(standard_table([
        ["Komponen", "Fungsi", "Estimasi", "Sumber contoh"],
        ["ESP32 DevKit V1", "Controller dengan Wi-Fi/Bluetooth untuk membaca sensor dan mengirim data.", "Rp210.000", "<link href='https://shopee.co.id/ESP32-DEVKIT-V1-ESP-WROOM-32-i.75743391.1454970710' color='#1C5D86'><u>Shopee: ESP32 DevKit V1</u></link>"],
        ["DHT22", "Membaca suhu dan kelembapan udara.", "Rp25.000", "<link href='https://www.blibli.com/jual/dht-22' color='#1C5D86'><u>Blibli: DHT22</u></link>"],
        ["Sensor tanah kapasitif", "Membaca kelembapan media tanam; tipe kapasitif dipilih karena tidak memakai elektroda terbuka.", "Rp10.800", "<link href='https://www.easyware.co.id/product/capacitive-soil-moisture-sensor-v2-0-anti-karat-sensor-kelembapan-tanah-esp32/' color='#1C5D86'><u>EasyWare: sensor tanah</u></link>"],
        ["Relay 1 channel", "Saklar elektronik antara controller dan beban DC kecil.", "Rp25.000", "<link href='https://online-journals.org/index.php/i-jim/article/download/41145/14005/135835' color='#1C5D86'><u>Contoh BOM proyek IoT</u></link>"],
        ["Pompa mini DC 5V", "Menyalurkan air untuk demonstrasi penyiraman skala kecil.", "Cek harga terbaru", "<link href='https://shopee.co.id/MINI-WATER-PUMP-DC-5V-MINI-SUBMERSIBLE-5VOLT-5VDC-POMPA-AIR-MINI-5V-DC-i.119918417.24055637833' color='#1C5D86'><u>Shopee: pompa mini</u></link>"],
        ["Kabel, breadboard, catu daya", "Menyambungkan dan memberi daya pada rangkaian prototipe.", "Isi setelah riset", "Cari dari penjual tepercaya; cek tegangan dan kecocokan konektor."],
    ], [3.1 * cm, 5.5 * cm, 2.1 * cm, 5.7 * cm], styles))
    story.append(Spacer(1, 6))
    story.append(Paragraph(
        "Catatan desain: satu komponen murah tetapi tidak kompatibel dapat membuat biaya proyek membengkak. Periksa tegangan kerja, jenis sinyal, kebutuhan daya, dan apakah alat tersebut aman dipakai pada konteks sekolah sebelum memilihnya.",
        styles["SmallTeladan"],
    ))

    story.append(Paragraph("8. Produk Nyata sebagai Referensi, Bukan untuk Ditiru Mentah-Mentah", styles["SectionTeladan"]))
    story.append(standard_table([
        ["Referensi", "Hal yang Bisa Dipelajari", "Tautan"],
        ["Arduino Automated Greenhouse", "Contoh proyek sekolah yang memantau kondisi, mengatur pencahayaan/suhu/kelembapan, dan memantau dari ponsel.", "<link href='https://cloud.arduino.cc/building-automated-greenhouse' color='#1C5D86'><u>Arduino case study</u></link>"],
        ["Arduino Cloud", "Dashboard untuk melihat data dan mengontrol perangkat; contoh penggunaan smart garden juga tersedia.", "<link href='https://cloud.arduino.cc/how-it-works/' color='#1C5D86'><u>Arduino Cloud</u></link>"],
        ["ESP32", "Controller yang mendukung Wi-Fi dan Bluetooth, relevan untuk perangkat IoT sederhana.", "<link href='https://www.espressif.com/en/products/socs/esp32/documentation' color='#1C5D86'><u>Dokumentasi Espressif</u></link>"],
    ], [4.1 * cm, 8.0 * cm, 4.3 * cm], styles))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "Saat melihat produk nyata, jangan hanya bertanya 'fiturnya apa?'. Tanyakan juga: masalah siapa yang diselesaikan, data apa yang diambil, siapa yang punya akses, serta fitur mana yang tidak cocok untuk sekolah kita.",
        styles["CalloutTeladan"],
    ))

    story.append(PageBreak())
    story.append(Paragraph("9. Keselamatan, Privasi, dan Etika", styles["SectionTeladan"]))
    story.append(bullet_list([
        "<b>Keselamatan listrik:</b> prototipe awal sebaiknya memakai tegangan rendah. Rangkaian yang terhubung listrik PLN hanya boleh dirancang atau diuji dengan pendampingan guru/teknisi yang kompeten.",
        "<b>Keamanan fisik:</b> kabel, pompa, dan kotak perangkat tidak boleh mengganggu jalur siswa atau terkena air tanpa perlindungan yang sesuai.",
        "<b>Privasi:</b> pilih data minimum yang diperlukan. Sensor suhu atau gerak mungkin cukup; kamera atau data identitas tidak otomatis dibutuhkan untuk setiap masalah.",
        "<b>Transparansi:</b> pengguna perlu tahu apa yang diukur, untuk tujuan apa, dan siapa yang dapat melihat datanya.",
        "<b>Kendali manusia:</b> otomatisasi harus memiliki batas dan cara dihentikan. Sistem dapat keliru membaca sensor atau gagal terhubung.",
        "<b>Keadilan dan keberlanjutan:</b> pikirkan siapa yang akan merawat alat, biaya penggantian komponen, serta limbah elektronik setelah proyek selesai.",
    ], styles["BodyTeladan"]))
    story.append(Paragraph(
        "Prinsip sederhana: teknologi yang baik bukan hanya berfungsi, tetapi juga aman, bisa dijelaskan, dan menghormati orang yang berada di sekitarnya.",
        styles["CalloutTeladan"],
    ))

    story.append(Paragraph("10. Penugasan Kelompok: IoT Solution Design Report", styles["SectionTeladan"]))
    story.append(Paragraph(
        "Buat sebuah laporan rancangan solusi IoT untuk SMA Teladan. Laporan dapat dibuat sebagai 2-3 halaman atau 5-7 slide. Pilih satu konteks: Smart School atau Smart Greenhouse. Gunakan bahasa kalian sendiri dan tunjukkan alasan di balik setiap pilihan.",
        styles["BodyTeladan"],
    ))
    story.append(bullet_list([
        "<b>Masalah dan stakeholder:</b> masalah spesifik, bukti/observasi singkat, serta pihak yang terdampak.",
        "<b>Solusi dan metrik keberhasilan:</b> apa yang sistem lakukan dan bagaimana kalian tahu solusi tersebut membantu.",
        "<b>Desain sistem:</b> diagram sensor &rarr; controller &rarr; koneksi/dashboard &rarr; actuator/pengguna, dengan penjelasan singkat.",
        "<b>Tabel komponen dan harga:</b> minimal empat komponen, jumlah, harga satuan, subtotal, tautan sumber, serta total anggaran awal.",
        "<b>Produk referensi:</b> minimal dua produk/proyek nyata dan satu hal yang kalian adaptasi dari masing-masing referensi.",
        "<b>Risiko dan etika:</b> minimal tiga risiko, termasuk keselamatan atau privasi, serta cara menguranginya.",
        "<b>Rencana implementasi:</b> langkah pertama yang akan diuji saat alat tersedia, pembagian peran, dan indikator keberhasilan awal.",
    ], styles["BodyTeladan"]))
    story.append(KeepTogether([
        Paragraph("Pengumpulan", styles["SectionTeladan"]),
        Paragraph(
            "Kirim hasil kelompok ke <b>ataka.ahmad@gmail.com</b> dengan subjek: <b>SMA Teladan XI - Tugas Blueprint IoT - [Nama Kelompok]</b>. Pastikan tautan sumber harga dapat dibuka dan semua anggota kelompok tercantum dalam laporan. Ingat: solusi yang baik tidak harus paling rumit, tetapi harus membantu, aman, dan dapat dirawat.",
            styles["CalloutTeladan"],
        ),
    ]))

    doc = SimpleDocTemplate(
        str(OUTPUT_PATH), pagesize=A4, rightMargin=1.7 * cm, leftMargin=1.7 * cm,
        topMargin=1.55 * cm, bottomMargin=1.65 * cm,
        title="Materi Kelas XI - Dari Ide ke Blueprint Solusi IoT",
        author="SMA Teladan",
    )
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    build_pdf()
