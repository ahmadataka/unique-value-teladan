from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import ListFlowable, ListItem, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUTPUT_PATH = Path("/Users/ahmadataka/Documents/Codex project/SMA Teladan/unique-value-teladan/pdf/materi-kelas-x-data-algoritma-dan-rekomendasi-digital.pdf")


def make_styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle(name="TitleT", parent=s["Title"], fontName="Helvetica-Bold", fontSize=21, leading=25, alignment=TA_CENTER, textColor=colors.HexColor("#16324F"), spaceAfter=8))
    s.add(ParagraphStyle(name="SubT", parent=s["Normal"], fontName="Helvetica", fontSize=11, leading=15, alignment=TA_CENTER, textColor=colors.HexColor("#355C7D"), spaceAfter=12))
    s.add(ParagraphStyle(name="SectionT", parent=s["Heading2"], fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=colors.white, backColor=colors.HexColor("#24577A"), borderPadding=(6, 8, 6), spaceBefore=10, spaceAfter=8))
    s.add(ParagraphStyle(name="BodyT", parent=s["BodyText"], fontName="Helvetica", fontSize=10.7, leading=15.2, textColor=colors.HexColor("#1F2933"), alignment=TA_JUSTIFY, spaceAfter=6))
    s.add(ParagraphStyle(name="CallT", parent=s["BodyText"], fontName="Helvetica-Bold", fontSize=10.6, leading=14.8, textColor=colors.HexColor("#16324F"), backColor=colors.HexColor("#EAF3F8"), borderPadding=(7, 9, 7), spaceAfter=10))
    s.add(ParagraphStyle(name="CellT", parent=s["BodyText"], fontName="Helvetica", fontSize=8.8, leading=10.7, textColor=colors.HexColor("#1F2933")))
    s.add(ParagraphStyle(name="HeadT", parent=s["BodyText"], fontName="Helvetica-Bold", fontSize=9, leading=10.7, textColor=colors.white))
    s.add(ParagraphStyle(name="DiagramT", parent=s["BodyText"], fontName="Helvetica-Bold", fontSize=8.7, leading=10.2, alignment=TA_CENTER, textColor=colors.HexColor("#16324F")))
    return s


def bullets(values, style):
    return ListFlowable([ListItem(Paragraph(value, style), leftIndent=6) for value in values], bulletType="bullet", start="circle", leftIndent=16, bulletFontName="Helvetica", bulletFontSize=10, bulletOffsetY=2)


def table(rows, widths, s):
    data = [[Paragraph(str(value), s["HeadT"] if index == 0 else s["CellT"]) for value in row] for index, row in enumerate(rows)]
    result = Table(data, colWidths=widths, repeatRows=1)
    result.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#24577A")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), .5, colors.HexColor("#B7C5D1")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F1F7FA")]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return result


def diagram(s):
    items = [("Jejak data", "klik, pencarian, tontonan", "#DDEEF5"), ("Algoritma", "mencari pola", "#E5F2E7"), ("Rekomendasi", "konten atau produk", "#FFF1D6"), ("Pilihan kita", "tetap bisa mengatur", "#FDE6E1")]
    cells = []
    for index, (title, detail, _) in enumerate(items):
        cells.append(Paragraph(f"{title}<br/><font name='Helvetica'>{detail}</font>", s["DiagramT"]))
        if index < len(items) - 1:
            cells.append(Paragraph("&rarr;", s["DiagramT"]))
    result = Table([cells], colWidths=[3.35*cm, .42*cm, 3.35*cm, .42*cm, 3.35*cm, .42*cm, 3.35*cm])
    commands = [("ALIGN", (0, 0), (-1, -1), "CENTER"), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3), ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]
    for index, (_, _, color) in enumerate(items):
        column = index * 2
        commands.extend([("BACKGROUND", (column, 0), (column, 0), colors.HexColor(color)), ("BOX", (column, 0), (column, 0), .6, colors.HexColor("#5593B8"))])
    result.setStyle(TableStyle(commands))
    return result


def footer(canvas, doc):
    canvas.saveState(); canvas.setFont("Helvetica", 9); canvas.setFillColor(colors.HexColor("#5B6770")); canvas.drawRightString(A4[0] - 1.7*cm, 1.2*cm, f"Halaman {doc.page}"); canvas.restoreState()


def build_pdf():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    s = make_styles()
    story = [Spacer(1, .6*cm), Paragraph("Materi Kelas X: Data, Algoritma, dan Rekomendasi Digital", s["TitleT"]), Paragraph("Memahami mengapa konten digital yang muncul pada setiap orang bisa berbeda", s["SubT"])]
    story.append(Paragraph("Halo teman-teman. Pernahkah kalian mencari satu video, lalu setelah itu beranda dipenuhi video serupa? Atau dua orang mencari topik yang sama tetapi hasilnya berbeda? Hal ini berkaitan dengan data dan algoritma. Pada sesi ini kita tidak perlu membuat aplikasi. Kita belajar menjadi pengguna teknologi yang lebih sadar, kritis, dan mampu mengambil keputusan sendiri.", s["CallT"]))

    story.append(Paragraph("1. Tujuan Pembelajaran", s["SectionT"]))
    story.append(bullets([
        "Kalian dapat menjelaskan secara sederhana hubungan antara data, algoritma, dan rekomendasi digital.",
        "Kalian dapat mengenali jejak data yang mungkin muncul saat menggunakan platform digital.",
        "Kalian dapat memahami manfaat rekomendasi sekaligus risiko seperti filter bubble, bias, dan penggunaan berlebihan.",
        "Kalian dapat memilih kebiasaan digital yang membuat kalian tetap memegang kendali.",
    ], s["BodyT"]))

    story.append(Paragraph("2. Apa yang Dimaksud Algoritma?", s["SectionT"]))
    story.append(Paragraph("Algoritma adalah serangkaian langkah atau aturan untuk mengolah informasi dan menghasilkan keputusan atau saran. Algoritma ada di banyak tempat: urutan video di beranda, hasil pencarian, rekomendasi lagu, pilihan filter foto, sampai rute perjalanan. Algoritma tidak mengenal kalian seperti teman mengenal teman. Ia membaca pola dari data yang tersedia.", s["BodyT"]))
    story.append(diagram(s))
    story.append(Spacer(1, 6))
    story.append(Paragraph("Contoh: kalian menonton beberapa video tentang sepak bola. Platform dapat menggunakan riwayat tontonan, durasi menonton, klik, dan interaksi untuk memperkirakan video lain yang mungkin kalian pilih. Perkiraan itu tidak selalu benar dan tidak selalu mewakili semua minat kalian.", s["CallT"]))

    story.append(PageBreak())
    story.append(Paragraph("3. Jejak Data di Kehidupan Sehari-hari", s["SectionT"]))
    story.append(table([
        ["Aktivitas", "Data atau sinyal yang mungkin terbaca", "Mengapa perlu sadar?"],
        ["Mencari informasi", "Kata kunci, bahasa, waktu pencarian, perangkat, lokasi kasar.", "Hasil pencarian dapat dipengaruhi konteks dan riwayat."],
        ["Menonton video", "Video yang dipilih, durasi tonton, suka, komentar, skip.", "Beranda dapat menjadi semakin sempit pada jenis konten tertentu."],
        ["Berbelanja online", "Produk dilihat, keranjang, klik iklan, rentang harga.", "Iklan dan rekomendasi dapat mengikuti minat atau kebiasaan belanja."],
        ["Menggunakan aplikasi", "Izin kamera, mikrofon, kontak, lokasi, notifikasi.", "Tidak semua izin selalu diperlukan untuk fungsi utama aplikasi."],
    ], [3.6*cm, 6.3*cm, 6.3*cm], s))
    story.append(Paragraph("Data bukan selalu hal buruk. Data dapat membantu layanan menjadi lebih relevan. Yang penting adalah memahami data apa yang dibutuhkan, siapa yang mengelolanya, dan bagaimana kita dapat membatasi atau mengatur penggunaannya.", s["CallT"]))

    story.append(Paragraph("4. Manfaat dan Risiko Rekomendasi Digital", s["SectionT"]))
    story.append(table([
        ["Manfaat", "Risiko yang perlu diwaspadai", "Tindakan pengguna"],
        ["Membantu menemukan materi belajar atau video yang relevan.", "Konten yang sering muncul dianggap otomatis paling benar.", "Cek sumber, bandingkan dengan sumber lain, dan cari kata kunci berbeda."],
        ["Mempercepat pencarian musik, buku, atau produk yang disukai.", "Pilihan menjadi terlalu sempit karena hanya melihat yang mirip dengan kebiasaan lama.", "Sengaja cari topik atau perspektif berbeda."],
        ["Memberi iklan yang mungkin sesuai kebutuhan.", "Tergoda membeli karena iklan muncul berulang-ulang.", "Tunda keputusan, bandingkan harga, dan tanyakan apakah benar-benar perlu."],
        ["Membuat aplikasi lebih mudah dipakai.", "Waktu layar meningkat karena konten terus direkomendasikan.", "Atur notifikasi, gunakan batas waktu, dan berhenti dengan sadar."],
    ], [4.2*cm, 6.0*cm, 6.0*cm], s))

    story.append(Paragraph("5. Filter Bubble dan Bias", s["SectionT"]))
    story.append(Paragraph("<b>Filter bubble</b> adalah keadaan ketika kita terlalu sering menerima informasi yang mirip dengan minat atau pendapat kita sendiri. Sementara itu, <b>bias</b> dapat muncul ketika data yang dipakai tidak mewakili semua orang atau aturan sistem lebih menguntungkan sebagian kelompok. Keduanya dapat membuat kita merasa bahwa apa yang sering muncul di layar adalah seluruh kenyataan.", s["BodyT"]))
    story.append(table([
        ["Situasi", "Pertanyaan kritis"],
        ["Video tentang satu topik terus muncul", "Apa ada penjelasan atau sudut pandang lain yang belum saya lihat?"],
        ["Hasil pencarian pertama terlihat meyakinkan", "Siapa sumbernya? Apakah ada sumber tepercaya lain yang mendukung atau membantah?"],
        ["Rekomendasi produk terlihat sangat cocok", "Apakah saya benar-benar membutuhkan ini, atau hanya sering melihat iklannya?"],
        ["Satu kelompok tidak muncul dalam contoh data", "Siapa yang mungkin belum terwakili dan apa dampaknya?"],
    ], [7.0*cm, 9.2*cm], s))
    story.append(Paragraph("Prinsip penting: algoritma dapat memberi saran, tetapi manusia tetap perlu menilai. Jangan menyerahkan rasa ingin tahu dan keputusan sepenuhnya kepada beranda.", s["CallT"]))

    story.append(Paragraph("6. Tugas Kelompok: Algorithm Diary dan Control Plan", s["SectionT"]))
    story.append(Paragraph("Selama satu hari, amati satu platform digital yang biasa digunakan kelompok, misalnya YouTube, TikTok, Instagram, Spotify, marketplace, atau mesin pencari. Tidak perlu membagikan akun, password, riwayat pribadi, atau screenshot data sensitif. Cukup amati pola secara umum dan diskusikan bersama.", s["BodyT"]))
    story.append(table([
        ["Bagian hasil", "Isi minimum"],
        ["Platform dan fungsi", "Nama platform serta alasan kalian memilihnya."],
        ["Pola yang terlihat", "Minimal tiga contoh rekomendasi/hasil yang muncul dan kemungkinan alasan kemunculannya."],
        ["Data atau sinyal", "Data apa yang mungkin digunakan? Bedakan fakta yang terlihat dengan dugaan kelompok."],
        ["Manfaat", "Dua hal yang benar-benar terbantu oleh rekomendasi tersebut."],
        ["Risiko", "Minimal tiga risiko, misalnya filter bubble, informasi keliru, iklan berlebihan, privasi, atau waktu layar."],
        ["Control plan", "Minimal tiga tindakan praktis agar pengguna tetap memegang kendali."],
        ["Refleksi", "Lengkapi: 'Saya akan menggunakan rekomendasi digital dengan lebih ... karena ...'"],
    ], [4.4*cm, 11.8*cm], s))
    story.append(Paragraph("Bentuk hasil: satu poster/infografik atau 2-3 slide. Jangan menyertakan identitas akun, chat pribadi, alamat, nomor telepon, atau data teman tanpa izin.", s["CallT"]))

    story.append(Paragraph("7. Pengumpulan", s["SectionT"]))
    story.append(Paragraph("Kirim hasil kelompok ke <link href='mailto:ataka.ahmad@gmail.com' color='#1D5F85'><u>ataka.ahmad@gmail.com</u></link>.<br/><b>Subject email:</b> SMA Teladan X - Tugas Algorithm Diary - [Nama Kelompok]<br/>Sertakan nama anggota, platform yang diamati, dan file poster/slide.", s["CallT"]))
    story.append(Paragraph("Penutup: memahami algoritma bukan berarti takut memakai teknologi. Dengan memahami pola dan batasnya, kalian dapat memanfaatkan rekomendasi digital tanpa kehilangan pilihan dan pemikiran sendiri.", s["CallT"]))
    doc = SimpleDocTemplate(str(OUTPUT_PATH), pagesize=A4, leftMargin=1.7*cm, rightMargin=1.7*cm, topMargin=1.5*cm, bottomMargin=1.7*cm, title="Materi Kelas X Data, Algoritma, dan Rekomendasi Digital", author="SMA Teladan")
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    build_pdf()
    print(f"Created {OUTPUT_PATH}")
