from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import ListFlowable, ListItem, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUTPUT_PATH = Path("/Users/ahmadataka/Documents/Codex project/SMA Teladan/unique-value-teladan/pdf/materi-kelas-xi-komponen-smart-technology-dan-rab.pdf")


def build_styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle(name="TitleT", parent=s["Title"], fontName="Helvetica-Bold", fontSize=21, leading=25, alignment=TA_CENTER, textColor=colors.HexColor("#16324F"), spaceAfter=8))
    s.add(ParagraphStyle(name="SubT", parent=s["Normal"], fontName="Helvetica", fontSize=11, leading=15, alignment=TA_CENTER, textColor=colors.HexColor("#355C7D"), spaceAfter=12))
    s.add(ParagraphStyle(name="SectionT", parent=s["Heading2"], fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=colors.white, backColor=colors.HexColor("#24577A"), borderPadding=(6, 8, 6), spaceBefore=10, spaceAfter=8))
    s.add(ParagraphStyle(name="BodyT", parent=s["BodyText"], fontName="Helvetica", fontSize=10.7, leading=15.2, textColor=colors.HexColor("#1F2933"), alignment=TA_JUSTIFY, spaceAfter=6))
    s.add(ParagraphStyle(name="CallT", parent=s["BodyText"], fontName="Helvetica-Bold", fontSize=10.6, leading=14.8, textColor=colors.HexColor("#16324F"), backColor=colors.HexColor("#EAF3F8"), borderPadding=(7, 9, 7), spaceAfter=10))
    s.add(ParagraphStyle(name="CellT", parent=s["BodyText"], fontName="Helvetica", fontSize=8.7, leading=10.6, textColor=colors.HexColor("#1F2933")))
    s.add(ParagraphStyle(name="HeadT", parent=s["BodyText"], fontName="Helvetica-Bold", fontSize=8.9, leading=10.6, textColor=colors.white))
    s.add(ParagraphStyle(name="DiagramT", parent=s["BodyText"], fontName="Helvetica-Bold", fontSize=8.5, leading=10.0, alignment=TA_CENTER, textColor=colors.HexColor("#16324F")))
    return s


def bullets(values, style):
    return ListFlowable([ListItem(Paragraph(value, style), leftIndent=6) for value in values], bulletType="bullet", start="circle", leftIndent=16, bulletFontName="Helvetica", bulletFontSize=10, bulletOffsetY=2)


def table(rows, widths, s):
    data = [[Paragraph(str(cell), s["HeadT"] if index == 0 else s["CellT"]) for cell in row] for index, row in enumerate(rows)]
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


def system_diagram(s):
    items = [
        ("Sensor", "membaca kondisi", "#DDEEF5"),
        ("Microcontroller", "mengolah aturan", "#E5F2E7"),
        ("Driver / Relay", "menjembatani daya", "#FFF1D6"),
        ("Actuator", "melakukan aksi", "#FDE6E1"),
        ("Power", "menyuplai energi", "#EDE7F6"),
    ]
    cells = []
    for index, (title, detail, _) in enumerate(items):
        cells.append(Paragraph(f"{title}<br/><font name='Helvetica'>{detail}</font>", s["DiagramT"]))
        if index < len(items) - 1:
            cells.append(Paragraph("&rarr;", s["DiagramT"]))
    result = Table([cells], colWidths=[2.75*cm, .3*cm, 2.75*cm, .3*cm, 2.75*cm, .3*cm, 2.75*cm, .3*cm, 2.75*cm])
    result.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), colors.HexColor(items[0][2])), ("BACKGROUND", (2, 0), (2, 0), colors.HexColor(items[1][2])),
        ("BACKGROUND", (4, 0), (4, 0), colors.HexColor(items[2][2])), ("BACKGROUND", (6, 0), (6, 0), colors.HexColor(items[3][2])), ("BACKGROUND", (8, 0), (8, 0), colors.HexColor(items[4][2])),
        ("BOX", (0, 0), (0, 0), .6, colors.HexColor("#5593B8")), ("BOX", (2, 0), (2, 0), .6, colors.HexColor("#67A56B")),
        ("BOX", (4, 0), (4, 0), .6, colors.HexColor("#C8943E")), ("BOX", (6, 0), (6, 0), .6, colors.HexColor("#C87562")), ("BOX", (8, 0), (8, 0), .6, colors.HexColor("#8B70B2")),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3), ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))
    return result


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.HexColor("#5B6770"))
    canvas.drawRightString(A4[0] - 1.7 * cm, 1.2 * cm, f"Halaman {doc.page}")
    canvas.restoreState()


def build_pdf():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    s = build_styles()
    story = [Spacer(1, .6 * cm), Paragraph("Materi Kelas XI: Komponen Smart Technology dan RAB", s["TitleT"]), Paragraph("Dari ide IoT menuju kebutuhan komponen dan estimasi biaya yang masuk akal", s["SubT"])]
    story.append(Paragraph("Halo teman-teman. Ide Smart School atau Smart Greenhouse kalian sekarang perlu diterjemahkan menjadi kebutuhan nyata. Pada sesi ini kalian akan belajar memilih komponen berdasarkan fungsinya, bukan sekadar karena namanya terlihat canggih. Setelah itu, kalian menyusun RAB atau Rencana Anggaran Biaya sederhana yang dapat diperiksa sumbernya.", s["CallT"]))

    story.append(Paragraph("1. Tujuan Pembelajaran", s["SectionT"]))
    story.append(bullets([
        "Kalian dapat menjelaskan peran sensor, aktuator, microcontroller, power supply, koneksi, dan komponen pendukung dalam sistem IoT.",
        "Kalian dapat memilih kandidat komponen yang sesuai dengan kebutuhan solusi, bukan berdasarkan merek semata.",
        "Kalian dapat mengenali risiko dasar seperti tegangan tidak cocok, arus tidak cukup, komponen tidak tahan lingkungan, dan biaya yang terlewat.",
        "Kalian dapat membuat RAB sederhana dengan jumlah, harga satuan, subtotal, sumber harga, dan catatan asumsi.",
    ], s["BodyT"]))

    story.append(Paragraph("2. Smart Technology Adalah Sistem", s["SectionT"]))
    story.append(Paragraph("Satu alat pintar biasanya tidak berdiri sendiri. Sensor membaca kondisi; microcontroller mengolah data dan aturan; driver atau relay membantu mengendalikan beban; actuator melakukan aksi; power supply memberi energi. Koneksi internet dan dashboard boleh ditambahkan bila benar-benar membantu pengguna.", s["BodyT"]))
    story.append(system_diagram(s))
    story.append(Spacer(1, 6))
    story.append(Paragraph("Contoh greenhouse: sensor kelembapan tanah membaca media tanam -> ESP32 memproses aturan -> relay menghubungkan daya ke pompa -> pompa mengalirkan air -> siswa mengecek kondisi tanaman dan sistem.", s["CallT"]))

    story.append(PageBreak())
    story.append(Paragraph("3. Komponen Utama dan Fungsinya", s["SectionT"]))
    story.append(table([
        ["Kelompok komponen", "Fungsi", "Contoh kata kunci pencarian"],
        ["Sensor", "Membaca kondisi fisik seperti suhu, kelembapan, cahaya, jarak, gerak, atau kualitas udara.", "DHT22, soil moisture capacitive, LDR, PIR motion sensor, ultrasonic."],
        ["Microcontroller", "Membaca sensor, menjalankan program, mengambil keputusan sederhana, dan dapat mengirim data.", "ESP32 DevKit, Arduino Uno, Arduino Nano."],
        ["Actuator", "Melakukan aksi fisik seperti menyalakan pompa, kipas, lampu, servo, atau buzzer.", "Mini water pump, DC fan, servo motor, LED, buzzer."],
        ["Driver / relay", "Membantu microcontroller mengendalikan perangkat yang membutuhkan daya lebih besar.", "1 channel relay 5V, motor driver, MOSFET module."],
        ["Power", "Menyediakan energi dengan tegangan dan arus yang sesuai untuk tiap bagian sistem.", "USB adapter 5V, battery holder, DC power supply, buck converter."],
        ["Pendukung", "Membuat rangkaian dapat dipasang, diuji, dan dirawat dengan aman.", "Breadboard, jumper wire, resistor, kabel, konektor, box enclosure."],
    ], [3.4*cm, 7.0*cm, 5.8*cm], s))
    story.append(Paragraph("Kata kunci pencarian membantu kalian menemukan kandidat produk. Jangan langsung membeli. Baca spesifikasi dan tanyakan apakah komponennya cocok dengan kebutuhan sistem.", s["CallT"]))

    story.append(PageBreak())
    story.append(Paragraph("4. Cara Memilih Komponen: Mulai dari Fungsi", s["SectionT"]))
    story.append(table([
        ["Pertanyaan sebelum memilih", "Contoh untuk greenhouse"],
        ["Kondisi apa yang harus dibaca?", "Kelembapan tanah, suhu udara, atau cahaya."],
        ["Aksi apa yang diperlukan?", "Menyalakan pompa, kipas, atau memberi notifikasi."],
        ["Apakah komponen perlu tahan air/panas/debu?", "Sensor di dekat tanah dan pompa perlu dilindungi dari air."],
        ["Tegangan dan arus berapa yang diperlukan?", "ESP32 umumnya memakai 3.3V/5V; pompa bisa memakai tegangan lain dan membutuhkan daya lebih besar."],
        ["Apakah microcontroller dapat mengendalikan actuator langsung?", "Biasanya tidak untuk pompa/motor; perlu relay, driver, atau MOSFET yang tepat."],
        ["Apa cara manual jika alat gagal?", "Siswa tetap dapat menyiram manual dan mematikan pompa melalui saklar/pencabutan daya."],
    ], [6.2*cm, 10.0*cm], s))

    story.append(Paragraph("5. Catatan Keselamatan Dasar", s["SectionT"]))
    story.append(bullets([
        "Jangan menghubungkan pompa, motor, atau perangkat berarus besar langsung ke pin microcontroller. Gunakan relay/driver yang sesuai dan minta pendampingan guru saat merakit.",
        "Tegangan harus cocok. Komponen 3.3V, 5V, 9V, dan 12V tidak boleh dianggap sama.",
        "Air dan listrik adalah kombinasi berisiko. Gunakan wadah, kabel, konektor, dan posisi pemasangan yang aman.",
        "Harga murah bukan satu-satunya pertimbangan. Pastikan spesifikasi, jumlah, kondisi produk, pengiriman, dan kemungkinan penggantian komponen sudah dipikirkan.",
        "RAB adalah estimasi. Harga berubah; selalu catat tanggal pencarian dan sumber harga.",
    ], s["BodyT"]))
    story.append(Paragraph("Jika kalian ragu mengenai rangkaian listrik atau spesifikasi komponen, tulis pertanyaannya. Lebih baik memeriksa sebelum membeli daripada membuat asumsi yang tidak aman.", s["CallT"]))

    story.append(Paragraph("6. Contoh Kandidat Komponen: Smart Greenhouse Dasar", s["SectionT"]))
    story.append(table([
        ["Kebutuhan", "Kandidat komponen", "Alasan kandidat"],
        ["Membaca tanah", "Capacitive soil moisture sensor", "Membaca kelembapan media tanam; pilih versi yang sesuai dengan kondisi penggunaan."],
        ["Mengolah aturan", "ESP32 DevKit", "Microcontroller dengan pin input/output dan koneksi Wi-Fi bila dashboard memang diperlukan."],
        ["Mengendalikan pompa", "Relay atau MOSFET module", "Membantu memisahkan kontrol microcontroller dari beban pompa."],
        ["Menyiram", "Mini water pump + selang", "Menyalurkan air; perlu disesuaikan dengan kebutuhan debit, tegangan, dan tinggi dorong."],
        ["Menyuplai daya", "Adaptor / power supply yang sesuai", "Harus mampu mencukupi kebutuhan seluruh komponen, terutama actuator."],
        ["Merakit dan melindungi", "Jumper, breadboard, konektor, box", "Sering terlupa dalam RAB padahal penting untuk uji coba, kerapian, dan keamanan."],
    ], [4.0*cm, 4.8*cm, 7.4*cm], s))

    story.append(PageBreak())
    story.append(Paragraph("7. Mengenal RAB", s["SectionT"]))
    story.append(Paragraph("RAB atau Rencana Anggaran Biaya adalah daftar biaya yang membuat rencana dapat diuji. RAB yang baik tidak hanya berisi total harga. Ia menunjukkan apa yang dibeli, berapa jumlahnya, dari mana angka harga berasal, dan asumsi apa yang dipakai.", s["BodyT"]))
    story.append(table([
        ["Kolom RAB", "Penjelasan"],
        ["No.", "Nomor urut komponen atau kebutuhan."],
        ["Komponen dan spesifikasi singkat", "Contoh: ESP32 DevKit, bukan hanya 'Arduino'."],
        ["Fungsi", "Alasan komponen ini dibutuhkan oleh sistem."],
        ["Jumlah", "Jumlah satuan yang benar-benar diperlukan, termasuk jika butuh cadangan."],
        ["Harga satuan", "Harga pada saat pencarian, termasuk catatan apakah pengiriman belum masuk."],
        ["Subtotal", "Jumlah x harga satuan."],
        ["Sumber dan tanggal", "Tautan toko/situs atau screenshot, serta tanggal saat harga dicari."],
        ["Catatan", "Kecocokan tegangan, stok, opsi pengganti, atau asumsi lain."],
    ], [4.8*cm, 11.4*cm], s))
    story.append(Paragraph("Jangan membuat angka harga. Gunakan sumber yang dapat dicek. Bila ada dua pilihan, boleh tulis keduanya dan jelaskan alasan memilih satu kandidat.", s["CallT"]))

    story.append(Paragraph("8. Contoh Format RAB", s["SectionT"]))
    story.append(table([
        ["No.", "Komponen", "Fungsi", "Jml", "Harga satuan", "Subtotal", "Sumber / tgl"],
        ["1", "ESP32 DevKit", "Mengolah sensor dan aturan", "1", "Isi setelah riset", "Jumlah x harga", "Tautan/screenshot, tgl"],
        ["2", "Sensor kelembapan tanah", "Membaca kondisi media tanam", "1", "Isi setelah riset", "Jumlah x harga", "Tautan/screenshot, tgl"],
        ["3", "Relay/driver", "Mengendalikan pompa dengan aman", "1", "Isi setelah riset", "Jumlah x harga", "Tautan/screenshot, tgl"],
        ["4", "Pompa dan selang", "Mengalirkan air", "1", "Isi setelah riset", "Jumlah x harga", "Tautan/screenshot, tgl"],
        ["5", "Power dan pendukung", "Daya, kabel, konektor, box", "Sesuai", "Isi setelah riset", "Jumlah x harga", "Tautan/screenshot, tgl"],
        ["", "TOTAL ESTIMASI", "", "", "", "Jumlah seluruh subtotal", ""],
    ], [.8*cm, 2.8*cm, 3.3*cm, 1.0*cm, 2.4*cm, 2.3*cm, 3.5*cm], s))

    story.append(Paragraph("9. Tugas Kelompok: Component List dan RAB", s["SectionT"]))
    story.append(Paragraph("Gunakan ide IoT kelompok kalian dari IoT Innovation Pitch Canvas. Buat daftar kandidat komponen dan RAB sederhana. Belum perlu membeli atau merakit apa pun. Tujuan tugas ini adalah memeriksa apakah ide kalian masuk akal dari sisi kebutuhan alat dan perkiraan biaya.", s["BodyT"]))
    story.append(table([
        ["Bagian hasil", "Isi minimum"],
        ["Ringkasan ide", "Masalah, pengguna, dan aksi utama sistem dalam 2-3 kalimat."],
        ["Diagram sistem", "Sensor/input -> microcontroller -> relay/driver bila perlu -> actuator/output -> manusia."],
        ["Daftar komponen", "Minimal satu kandidat untuk sensor, microcontroller, power, serta komponen actuator/pendukung yang relevan."],
        ["RAB", "Tabel lengkap berisi jumlah, harga satuan, subtotal, sumber, tanggal pencarian, dan total estimasi."],
        ["Pemeriksaan kecocokan", "Tulis minimal tiga catatan: tegangan/daya, perlindungan lingkungan, keselamatan, atau alternatif komponen."],
        ["Refleksi", "Komponen apa yang paling mahal/berisiko dan bagaimana kelompok dapat menyederhanakan ide bila anggaran terbatas?"],
    ], [4.5*cm, 11.7*cm], s))
    story.append(Paragraph("Bentuk hasil: 2-4 slide atau satu dokumen PDF. Lampirkan screenshot atau tautan sumber harga. Harga dapat berubah, jadi yang dinilai adalah ketelitian pencarian dan alasan pemilihan, bukan total biaya paling murah.", s["CallT"]))

    story.append(Paragraph("10. Pengumpulan", s["SectionT"]))
    story.append(Paragraph("Kirim hasil kelompok ke <link href='mailto:ataka.ahmad@gmail.com' color='#1D5F85'><u>ataka.ahmad@gmail.com</u></link>.<br/><b>Subject email:</b> SMA Teladan XI - Tugas Component List dan RAB - [Nama Kelompok]<br/>Sertakan nama anggota, file hasil, dan sumber harga yang digunakan.", s["CallT"]))
    story.append(Paragraph("Penutup: RAB yang baik menunjukkan bahwa kelompok tidak hanya punya ide menarik, tetapi juga memahami apa yang diperlukan agar ide itu dapat diuji dengan aman dan realistis.", s["CallT"]))

    doc = SimpleDocTemplate(str(OUTPUT_PATH), pagesize=A4, leftMargin=1.7*cm, rightMargin=1.7*cm, topMargin=1.5*cm, bottomMargin=1.7*cm, title="Materi Kelas XI Komponen Smart Technology dan RAB", author="SMA Teladan")
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    build_pdf()
    print(f"Created {OUTPUT_PATH}")
