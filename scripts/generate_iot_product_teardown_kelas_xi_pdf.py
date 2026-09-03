from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import ListFlowable, ListItem, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUTPUT_PATH = Path("/Users/ahmadataka/Documents/Codex project/SMA Teladan/unique-value-teladan/pdf/materi-kelas-xi-membedah-produk-iot.pdf")


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="TitleTeladan", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=21, leading=25, textColor=colors.HexColor("#16324F"), alignment=TA_CENTER, spaceAfter=8))
    styles.add(ParagraphStyle(name="SubtitleTeladan", parent=styles["Normal"], fontName="Helvetica", fontSize=11, leading=15, alignment=TA_CENTER, textColor=colors.HexColor("#355C7D"), spaceAfter=12))
    styles.add(ParagraphStyle(name="SectionTeladan", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=colors.white, backColor=colors.HexColor("#24577A"), borderPadding=(6, 8, 6), spaceBefore=10, spaceAfter=8))
    styles.add(ParagraphStyle(name="BodyTeladan", parent=styles["BodyText"], fontName="Helvetica", fontSize=10.8, leading=15.4, textColor=colors.HexColor("#1F2933"), alignment=TA_JUSTIFY, spaceAfter=6))
    styles.add(ParagraphStyle(name="CalloutTeladan", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=10.8, leading=15, textColor=colors.HexColor("#16324F"), backColor=colors.HexColor("#EAF3F8"), borderPadding=(7, 9, 7), spaceAfter=10))
    styles.add(ParagraphStyle(name="TableCellTeladan", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.9, leading=10.9, textColor=colors.HexColor("#1F2933")))
    styles.add(ParagraphStyle(name="TableHeadTeladan", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=9.1, leading=10.9, textColor=colors.white))
    styles.add(ParagraphStyle(name="SmallTeladan", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.8, leading=11.7, textColor=colors.HexColor("#425466"), spaceAfter=4))
    styles.add(ParagraphStyle(name="DiagramTeladan", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=8.6, leading=10.2, alignment=TA_CENTER, textColor=colors.HexColor("#16324F")))
    return styles


def bullets(items, style):
    return ListFlowable([ListItem(Paragraph(item, style), leftIndent=6) for item in items], bulletType="bullet", start="circle", leftIndent=16, bulletFontName="Helvetica", bulletFontSize=10, bulletOffsetY=2)


def table(rows, widths, styles):
    data = [[Paragraph(str(value), styles["TableHeadTeladan"] if r == 0 else styles["TableCellTeladan"]) for value in row] for r, row in enumerate(rows)]
    result = Table(data, colWidths=widths, repeatRows=1)
    result.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#24577A")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#B7C5D1")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F1F7FA")]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return result


def diagram(styles):
    items = [
        ("Input / Sensor", "membaca kondisi", "#DDEEF5"),
        ("Controller", "menjalankan aturan", "#E5F2E7"),
        ("Koneksi / Data", "mengirim informasi", "#FFF1D6"),
        ("Output / Actuator", "melakukan aksi", "#FDE6E1"),
        ("Manusia", "memantau dan memutuskan", "#EDE7F6"),
    ]
    cells = []
    for i, (title, body, _) in enumerate(items):
        cells.append(Paragraph(f"{title}<br/><font name='Helvetica'>{body}</font>", styles["DiagramTeladan"]))
        if i < len(items) - 1:
            cells.append(Paragraph("&rarr;", styles["DiagramTeladan"]))
    flow = Table([cells], colWidths=[2.65*cm, .35*cm, 2.65*cm, .35*cm, 2.65*cm, .35*cm, 2.65*cm, .35*cm, 2.65*cm])
    flow.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), colors.HexColor(items[0][2])), ("BACKGROUND", (2, 0), (2, 0), colors.HexColor(items[1][2])),
        ("BACKGROUND", (4, 0), (4, 0), colors.HexColor(items[2][2])), ("BACKGROUND", (6, 0), (6, 0), colors.HexColor(items[3][2])), ("BACKGROUND", (8, 0), (8, 0), colors.HexColor(items[4][2])),
        ("BOX", (0, 0), (0, 0), .6, colors.HexColor("#5593B8")), ("BOX", (2, 0), (2, 0), .6, colors.HexColor("#67A56B")),
        ("BOX", (4, 0), (4, 0), .6, colors.HexColor("#C8943E")), ("BOX", (6, 0), (6, 0), .6, colors.HexColor("#C87562")), ("BOX", (8, 0), (8, 0), .6, colors.HexColor("#8B70B2")),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3), ("TOPPADDING", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))
    return flow


def add_page_number(canvas, doc):
    canvas.saveState(); canvas.setFont("Helvetica", 9); canvas.setFillColor(colors.HexColor("#5B6770")); canvas.drawRightString(A4[0] - 1.7 * cm, 1.2 * cm, f"Halaman {doc.page}"); canvas.restoreState()


def link(label, url):
    return f'<link href="{url}" color="#1D5F85"><u>{label}</u></link>'


def build_pdf():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    s = build_styles(); story = []
    story += [Spacer(1, .6 * cm), Paragraph("Materi Kelas XI: Membedah Produk IoT", s["TitleTeladan"]), Paragraph("Belajar dari sistem pintar nyata sebelum membuat prototipe sendiri", s["SubtitleTeladan"])]
    story.append(Paragraph(
        "Halo teman-teman. Kalian sudah memiliki ide Smart School atau Smart Greenhouse. Pada sesi ini kalian tidak perlu merakit alat dan tidak perlu menulis blueprint baru. Kalian akan menjadi <b>technology detective</b>: membedah produk IoT nyata untuk melihat bagaimana sistemnya bekerja, data apa yang dipakai, serta apa yang bisa dan tidak bisa kita tiru untuk SMA Teladan.",
        s["CalloutTeladan"],
    ))

    story.append(Paragraph("1. Tujuan Pembelajaran", s["SectionTeladan"]))
    story.append(bullets([
        "Kalian dapat mengenali komponen penting dalam sebuah produk IoT nyata.",
        "Kalian dapat menjelaskan alur sensor, controller, koneksi, data, output, dan peran manusia.",
        "Kalian dapat membedakan fitur yang benar-benar berguna dari fitur yang hanya terlihat canggih.",
        "Kalian dapat mengidentifikasi risiko kegagalan, privasi, keamanan, dan kebutuhan perawatan sebuah sistem pintar.",
    ], s["BodyTeladan"]))

    story.append(Paragraph("2. Cara Membaca Produk IoT", s["SectionTeladan"]))
    story.append(Paragraph(
        "Produk IoT bukan sekadar alat yang terhubung ke Wi-Fi. Ia adalah sistem: ada kondisi yang dibaca, aturan yang diproses, data yang mungkin dikirim, aksi fisik yang dilakukan, dan manusia yang tetap perlu memantau hasilnya.",
        s["BodyTeladan"],
    ))
    story.append(diagram(s))
    story.append(Spacer(1, 6))
    story.append(Paragraph("Contoh sederhana: sensor tanah membaca kondisi media tanam -> controller membandingkan nilai dengan ambang -> data muncul di dashboard -> relay menyalakan pompa -> siswa/guru mengecek apakah tanaman benar-benar terbantu.", s["CalloutTeladan"]))

    story.append(Paragraph("3. Lima Pertanyaan Technology Detective", s["SectionTeladan"]))
    story.append(table([
        ["Pertanyaan", "Yang perlu kalian cari"],
        ["Masalah apa yang dibantu?", "Bukan nama fiturnya, tetapi masalah pengguna yang ingin diselesaikan."],
        ["Apa input dan outputnya?", "Sensor/data apa yang dibaca? Aksi apa yang dilakukan sistem?"],
        ["Bagaimana data bergerak?", "Apakah data disimpan lokal, dikirim ke aplikasi/cloud, atau dilihat melalui dashboard?"],
        ["Apa yang dapat gagal?", "Sensor salah baca, koneksi putus, daya habis, komponen macet, atau pengguna salah memahami data."],
        ["Apa batas etikanya?", "Data siapa yang dikumpulkan, siapa yang dapat mengakses, dan apakah ada alternatif yang lebih minim data?"],
    ], [6.0 * cm, 10.2 * cm], s))

    story.append(PageBreak())
    story.append(Paragraph("4. Empat Produk Nyata yang Dapat Dibedah", s["SectionTeladan"]))
    story.append(table([
        ["Produk", "Apa yang bisa dipelajari", "Tautan resmi"],
        ["Arduino Greenhouse Kit", "Greenhouse pendidikan dengan sensor cahaya, kelembapan, suhu, CO2, serta aktuator seperti kipas dan pompa. Data dapat dipantau melalui dashboard.", link("Arduino Greenhouse Kit", "https://www.arduino.cc/education/greenhouse/")],
        ["Aqara Motion Sensor P1", "Sensor gerak dengan pengaturan sensitivitas dan timeout. Cocok untuk memahami input sensor, false alarm, dan batas penggunaan sensor di ruang manusia.", link("Aqara Motion Sensor P1", "https://www.aqara.com/en/product/motion-sensor-p1")],
        ["Google Nest Learning Thermostat", "Menggabungkan sensor suhu, jadwal, aplikasi, serta pengendalian kenyamanan dan energi. Cocok untuk membahas otomatisasi dan data kebiasaan pengguna.", link("Google Nest", "https://store.google.com/us/product/nest_learning_thermostat_4th_gen?hl=en-US")],
        ["Arduino Greenhouse Project", "Contoh proyek yang memakai sensor dan relay untuk mengaktifkan humidifier atau pompa, serta memperlihatkan hubungan hardware dan kebutuhan tanaman.", link("Arduino Greenhouse Project", "https://www.arduino.cc/education/greenhouse-project/")],
    ], [4.1 * cm, 8.3 * cm, 3.8 * cm], s))
    story.append(Paragraph("Catatan: produk nyata adalah bahan belajar, bukan template yang harus ditiru. Kondisi sekolah, biaya, keamanan, dan kebutuhan pengguna di SMA Teladan bisa berbeda.", s["CalloutTeladan"]))

    story.append(Paragraph("5. Contoh Bedah: Smart Greenhouse", s["SectionTeladan"]))
    story.append(table([
        ["Bagian", "Contoh pembacaan sistem"],
        ["Masalah", "Tanaman tidak selalu dipantau pada saat media tanam mulai kering atau suhu terlalu tinggi."],
        ["Input", "Sensor kelembapan tanah, suhu, kelembapan udara, cahaya, atau CO2."],
        ["Controller dan aturan", "Board membaca data lalu membandingkan dengan batas yang telah diuji."],
        ["Output", "Pompa, kipas, lampu, atau notifikasi dapat diaktifkan jika kondisi tertentu terpenuhi."],
        ["Peran manusia", "Memeriksa tanaman, mengatur ambang, mengisi air, merawat alat, serta memutuskan tindakan saat sistem tidak wajar."],
        ["Risiko", "Sensor dapat salah baca, air habis, pompa macet, koneksi putus, atau sistem menyiram terlalu sering."],
    ], [5.1 * cm, 11.1 * cm], s))
    story.append(Paragraph("Prinsip penting: data dari sensor adalah petunjuk, bukan pengganti pengamatan manusia. Tanaman dan lingkungan nyata lebih rumit daripada satu angka pada dashboard.", s["CalloutTeladan"]))

    story.append(Paragraph("6. Checklist Saat Membaca Produk", s["SectionTeladan"]))
    story.append(bullets([
        "Cari foto atau screenshot resmi produk agar kelompok memahami bentuk perangkatnya.",
        "Tandai bagian yang menjadi input, controller, koneksi, dashboard, output, dan pengguna.",
        "Bedakan fakta dari asumsi. Jika informasi tidak ada di sumber, tulis sebagai pertanyaan, bukan seolah-olah fakta.",
        "Tanyakan apakah fitur itu cocok untuk sekolah atau greenhouse Teladan, atau justru terlalu mahal/rumit/tidak perlu.",
        "Sebutkan minimal satu situasi ketika sistem tidak boleh bekerja otomatis tanpa pemeriksaan manusia.",
    ], s["BodyTeladan"]))

    story.append(PageBreak())
    story.append(Paragraph("7. Tugas Kelompok: IoT Product Teardown", s["SectionTeladan"]))
    story.append(Paragraph(
        "Pilih satu produk IoT nyata dari daftar di atas atau produk lain yang mendapat persetujuan kelompok. Buat <b>IoT Product Teardown Card</b>: satu poster/infografik digital atau 2-3 slide yang membedah cara kerja produk tersebut. Tugas ini bukan membuat ide proyek baru; fokusnya adalah belajar membaca sistem secara teknis dan kritis.",
        s["BodyTeladan"],
    ))
    story.append(Paragraph("8. Isi IoT Product Teardown Card", s["SectionTeladan"]))
    story.append(table([
        ["Bagian", "Isi minimum"],
        ["Produk dan masalah", "Nama produk, screenshot/foto resmi, serta masalah pengguna yang dibantu."],
        ["Diagram sistem", "Sensor/input -> controller -> koneksi/data -> output/actuator -> manusia."],
        ["Komponen/fungsi", "Minimal tiga komponen atau fungsi yang dapat kalian identifikasi."],
        ["Data dan dashboard", "Data apa yang mungkin dibaca atau ditampilkan? Siapa yang idealnya boleh melihatnya?"],
        ["Manfaat dan batas", "Dua manfaat; satu fitur yang mungkin tidak perlu atau tidak cocok untuk SMA Teladan."],
        ["Risiko dan kegagalan", "Minimal tiga risiko: teknis, keamanan, biaya/perawatan, atau privasi."],
        ["Pelajaran untuk Teladan", "Satu hal yang layak diadaptasi dan satu hal yang harus diubah sebelum dipakai di sekolah/greenhouse."],
    ], [4.4 * cm, 11.8 * cm], s))
    story.append(Paragraph("Gunakan tautan sumber dalam kartu kalian. Jika memakai gambar produk, tulis sumbernya. Jangan memakai foto teman atau data sekolah tanpa izin.", s["CalloutTeladan"]))

    story.append(Paragraph("9. Pengumpulan", s["SectionTeladan"]))
    story.append(Paragraph(
        "Kirim hasil kelompok ke <link href='mailto:ataka.ahmad@gmail.com' color='#1D5F85'><u>ataka.ahmad@gmail.com</u></link>.<br/><b>Subject email:</b> SMA Teladan XI - Tugas IoT Product Teardown - [Nama Kelompok]<br/>Sertakan nama anggota, produk yang dipilih, dan poster/slide hasil bedah sistem.",
        s["CalloutTeladan"],
    ))

    story.append(Paragraph("10. Referensi Belajar", s["SectionTeladan"]))
    story.append(bullets([
        f"{link('Arduino Greenhouse Kit', 'https://www.arduino.cc/education/greenhouse/')}<br/>Contoh kit pendidikan yang menggabungkan sensor, dashboard, dan aktuator untuk greenhouse.",
        f"{link('Arduino Greenhouse Project', 'https://www.arduino.cc/education/greenhouse-project/')}<br/>Contoh proyek greenhouse dengan sensor, relay, humidifier, dan pompa.",
        f"{link('Aqara Motion Sensor P1', 'https://www.aqara.com/en/product/motion-sensor-p1')}<br/>Contoh sensor gerak yang dapat dipakai untuk mengamati input, sensitivitas, dan false alarm.",
        f"{link('Google Nest Learning Thermostat', 'https://store.google.com/us/product/nest_learning_thermostat_4th_gen?hl=en-US')}<br/>Contoh sistem pengelolaan suhu dan energi berbasis sensor, aplikasi, dan otomasi.",
    ], s["SmallTeladan"]))
    story.append(Paragraph("Penutup: engineer yang baik tidak hanya dapat merakit alat. Mereka juga mampu membaca sistem yang sudah ada, melihat batasnya, lalu memilih teknologi yang paling masuk akal untuk manusia dan lingkungannya.", s["CalloutTeladan"]))

    doc = SimpleDocTemplate(str(OUTPUT_PATH), pagesize=A4, leftMargin=1.7*cm, rightMargin=1.7*cm, topMargin=1.5*cm, bottomMargin=1.7*cm, title="Materi Kelas XI Membedah Produk IoT", author="SMA Teladan")
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    build_pdf()
    print(f"Created {OUTPUT_PATH}")
