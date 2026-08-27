from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import ListFlowable, ListItem, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUTPUT_PATH = Path("/Users/ahmadataka/Documents/Codex project/SMA Teladan/unique-value-teladan/pdf/materi-kelas-x-society-5-dan-risiko-teknologi.pdf")


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="TitleTeladan", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=21, leading=25, textColor=colors.HexColor("#16324F"), alignment=TA_CENTER, spaceAfter=8))
    styles.add(ParagraphStyle(name="SubtitleTeladan", parent=styles["Normal"], fontName="Helvetica", fontSize=11, leading=15, alignment=TA_CENTER, textColor=colors.HexColor("#355C7D"), spaceAfter=12))
    styles.add(ParagraphStyle(name="SectionTeladan", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=colors.white, backColor=colors.HexColor("#24577A"), borderPadding=(6, 8, 6), spaceBefore=10, spaceAfter=8))
    styles.add(ParagraphStyle(name="BodyTeladan", parent=styles["BodyText"], fontName="Helvetica", fontSize=10.8, leading=15.4, textColor=colors.HexColor("#1F2933"), alignment=TA_JUSTIFY, spaceAfter=6))
    styles.add(ParagraphStyle(name="CalloutTeladan", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=10.8, leading=15, textColor=colors.HexColor("#16324F"), backColor=colors.HexColor("#EAF3F8"), borderPadding=(7, 9, 7), spaceAfter=10))
    styles.add(ParagraphStyle(name="TableCellTeladan", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.9, leading=10.9, textColor=colors.HexColor("#1F2933")))
    styles.add(ParagraphStyle(name="TableHeadTeladan", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=9.1, leading=10.9, textColor=colors.white))
    styles.add(ParagraphStyle(name="SmallTeladan", parent=styles["BodyText"], fontName="Helvetica", fontSize=8.9, leading=11.8, textColor=colors.HexColor("#425466"), spaceAfter=4))
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


def add_page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.HexColor("#5B6770"))
    canvas.drawRightString(A4[0] - 1.7 * cm, 1.2 * cm, f"Halaman {doc.page}")
    canvas.restoreState()


def link(label, url):
    return f'<link href="{url}" color="#1D5F85"><u>{label}</u></link>'


def build_pdf():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    s = build_styles()
    story = []

    story += [Spacer(1, .6 * cm), Paragraph("Materi Kelas X: Society 5.0 dan Risiko Teknologi", s["TitleTeladan"]), Paragraph("Teknologi dapat membantu manusia, tetapi juga dapat memunculkan masalah baru", s["SubtitleTeladan"])]
    story.append(Paragraph(
        "Halo teman-teman. Pekan lalu kalian sudah merancang solusi teknologi untuk sekolah. Hari ini kita melihat sisi yang sering terlupa: setiap teknologi bisa membawa manfaat, tetapi juga berpotensi menimbulkan masalah baru. Society 5.0 meminta kita tidak hanya kagum pada teknologi, melainkan bertanya apakah teknologi itu tetap aman, adil, dan bermanfaat bagi manusia.",
        s["CalloutTeladan"],
    ))

    story.append(Paragraph("1. Tujuan Pembelajaran", s["SectionTeladan"]))
    story.append(bullets([
        "Kalian memahami hubungan Society 5.0 dengan penggunaan teknologi yang berpusat pada manusia.",
        "Kalian dapat membedakan manfaat teknologi dengan risiko atau dampak yang mungkin muncul.",
        "Kalian mengenali risiko seperti privasi, ketergantungan, hoaks, bias, keamanan, dan kesenjangan akses.",
        "Kalian mampu menyusun peta risiko sederhana serta aturan penggunaan teknologi yang bertanggung jawab.",
    ], s["BodyTeladan"]))

    story.append(Paragraph("2. Society 5.0 Bukan Berarti Teknologi Sebanyak-Banyaknya", s["SectionTeladan"]))
    story.append(Paragraph(
        "Dalam Society 5.0, teknologi seperti AI, internet, sensor, aplikasi, dan data dipakai untuk membantu manusia menyelesaikan persoalan nyata. Karena manusia adalah pusatnya, sebuah teknologi tidak cukup dinilai dari kecepatannya. Kita juga perlu menilai apakah semua orang dapat mengaksesnya, apakah datanya aman, dan apakah keputusan akhirnya masih bisa dikendalikan manusia.",
        s["BodyTeladan"],
    ))
    story.append(table([
        ["Pertanyaan Society 5.0", "Mengapa penting?"],
        ["Siapa yang terbantu?", "Teknologi yang baik harus menjawab kebutuhan pengguna, bukan hanya mengikuti tren."],
        ["Siapa yang mungkin dirugikan atau tertinggal?", "Satu teknologi dapat bekerja baik untuk sebagian orang, tetapi menyulitkan orang lain."],
        ["Data apa yang dikumpulkan?", "Data pribadi, foto, lokasi, atau kebiasaan tidak boleh dikumpulkan tanpa alasan yang jelas."],
        ["Apa yang terjadi jika sistem salah?", "Manusia perlu tetap bisa memeriksa, menghentikan, dan memperbaiki keputusan teknologi."],
    ], [6.1 * cm, 10.1 * cm], s))
    story.append(Paragraph("Kalimat kuncinya: <b>teknologi yang baik bukan hanya bisa bekerja, tetapi juga bisa dipertanggungjawabkan.</b>", s["CalloutTeladan"]))

    story.append(PageBreak())
    story.append(Paragraph("3. Manfaat yang Sama Dapat Memiliki Risiko", s["SectionTeladan"]))
    story.append(table([
        ["Teknologi", "Manfaat", "Masalah baru yang mungkin muncul"],
        ["Gen-AI untuk belajar", "Membantu menjelaskan konsep, memberi contoh, atau latihan soal.", "Siswa menyalin jawaban, informasi keliru dipercaya, atau proses berpikir digantikan."],
        ["Media sosial", "Memudahkan komunikasi dan berbagi karya.", "Perundungan, tekanan sosial, hoaks, serta penggunaan berlebihan."],
        ["Kamera / absensi digital", "Membantu keamanan dan administrasi.", "Privasi terganggu bila data atau rekaman tidak dikelola dengan jelas."],
        ["Sistem rekomendasi", "Memudahkan menemukan konten atau produk yang relevan.", "Membatasi sudut pandang, memperkuat bias, atau membuat pengguna terus terpaku pada layar."],
        ["Otomasi", "Menghemat waktu untuk tugas berulang.", "Kesalahan sistem dapat berdampak besar jika manusia tidak memeriksa hasilnya."],
    ], [3.5 * cm, 5.2 * cm, 7.5 * cm], s))

    story.append(Paragraph("4. Enam Jenis Risiko yang Perlu Kita Kenali", s["SectionTeladan"]))
    story.append(table([
        ["Risiko", "Contoh dekat dengan siswa", "Pertanyaan kritis"],
        ["Privasi", "Foto teman atau tugas pribadi diunggah ke tool tanpa izin.", "Apakah data ini benar-benar perlu dibagikan?"],
        ["Informasi keliru", "Jawaban AI atau video viral dipercaya tanpa cek sumber.", "Dari mana informasi ini berasal dan bisa dicek ke mana?"],
        ["Bias dan ketidakadilan", "Sistem tidak memahami bahasa, kondisi, atau kebutuhan sebagian pengguna.", "Apakah hasilnya adil bagi orang yang berbeda?"],
        ["Ketergantungan", "Tugas selalu diserahkan ke AI tanpa proses berpikir sendiri.", "Apakah teknologi membantu belajar atau menggantikannya?"],
        ["Keamanan", "Password dibagikan atau tautan palsu diklik.", "Apa yang bisa terjadi jika akun atau perangkat disalahgunakan?"],
        ["Kesenjangan akses", "Tugas digital menganggap semua siswa punya perangkat dan internet yang sama.", "Apakah ada cara lain agar semua orang tetap bisa ikut?"],
    ], [3.4 * cm, 6.4 * cm, 6.4 * cm], s))
    story.append(Paragraph("Tidak semua risiko berarti teknologi harus dilarang. Risiko perlu dipahami agar kita bisa menetapkan batas, kebiasaan aman, dan cara menggunakan teknologi dengan lebih baik.", s["CalloutTeladan"]))

    story.append(Paragraph("5. Cara Membaca Kasus: Manfaat - Risiko - Penjagaan", s["SectionTeladan"]))
    story.append(Paragraph("Gunakan tiga langkah ini saat membaca teknologi apa pun.", s["BodyTeladan"]))
    story.append(table([
        ["Langkah", "Yang dicari", "Contoh: AI untuk merangkum materi"],
        ["1. Manfaat", "Apa yang terbantu?", "Membantu siswa memahami gambaran awal teks panjang."],
        ["2. Risiko", "Masalah apa yang mungkin muncul?", "Ringkasan dapat salah atau terlalu sederhana; siswa berhenti membaca sumber asli."],
        ["3. Penjagaan", "Aturan apa yang membuat penggunaan lebih aman?", "Bandingkan dengan sumber asli, tulis sumber, dan gunakan hasil AI sebagai bahan diskusi, bukan jawaban akhir."],
    ], [3.0 * cm, 5.6 * cm, 7.6 * cm], s))

    story.append(Paragraph("6. Contoh Kasus Sekolah", s["SectionTeladan"]))
    story.append(Paragraph(
        "Bayangkan sekolah ingin memasang sistem kamera pintar untuk mengetahui apakah ruang kelas kosong sehingga lampu dan kipas bisa dimatikan. Ide ini dapat menghemat energi. Tetapi sistem tersebut juga bisa merekam orang, salah membaca kondisi, atau membuat siswa merasa diawasi terus-menerus.",
        s["BodyTeladan"],
    ))
    story.append(bullets([
        "Manfaat: penggunaan listrik dapat lebih hemat dan fasilitas lebih terpantau.",
        "Risiko: privasi, kesalahan sensor, akses rekaman yang tidak jelas, serta rasa tidak nyaman.",
        "Penjagaan: gunakan sensor gerak tanpa identitas bila cukup, jelaskan tujuan sistem, batasi siapa yang mengakses data, dan sediakan kontrol manual.",
    ], s["BodyTeladan"]))
    story.append(Paragraph("Perhatikan bahwa solusi yang lebih sederhana kadang lebih etis. Untuk mengatur lampu, sensor gerak mungkin lebih cukup daripada kamera.", s["CalloutTeladan"]))

    story.append(Paragraph("7. Tugas Kelompok: Technology Risk Map", s["SectionTeladan"]))
    story.append(Paragraph(
        "Pilih satu teknologi yang dekat dengan kehidupan siswa, sekolah, atau rumah. Kalian tidak membuat proposal solusi baru. Kali ini tugas kalian adalah membaca teknologi tersebut secara kritis: apa manfaatnya, masalah baru apa yang mungkin muncul, dan bagaimana kita dapat menggunakannya dengan lebih bertanggung jawab.",
        s["BodyTeladan"],
    ))
    story.append(Paragraph("Pilih salah satu contoh, atau teknologi lain yang disepakati kelompok:", s["CalloutTeladan"]))
    story.append(bullets([
        "ChatGPT, Gemini, atau tool Gen-AI lain untuk belajar.",
        "Media sosial, rekomendasi konten, atau fitur video pendek.",
        "Kamera keamanan, absensi digital, atau aplikasi pelacak lokasi.",
        "Game online, aplikasi belajar, atau sistem notifikasi sekolah.",
        "Teknologi smart home, sensor, atau perangkat otomatis di rumah/sekolah.",
    ], s["BodyTeladan"]))

    story.append(Paragraph("8. Isi Technology Risk Map", s["SectionTeladan"]))
    story.append(table([
        ["Bagian", "Isi minimum"],
        ["Teknologi dan konteks", "Nama teknologi serta situasi ketika siswa/kelompok memakainya."],
        ["Manfaat utama", "Minimal dua manfaat yang spesifik, bukan hanya 'memudahkan'."],
        ["Peta risiko", "Minimal tiga risiko dari kategori: privasi, informasi keliru, bias, ketergantungan, keamanan, atau kesenjangan akses."],
        ["Siapa terdampak", "Sebutkan pihak yang mungkin memperoleh manfaat maupun terkena dampak negatif."],
        ["Contoh situasi", "Satu contoh nyata atau skenario yang mungkin terjadi di sekolah/rumah."],
        ["Aturan penggunaan", "Minimal tiga aturan atau langkah penjagaan yang realistis."],
        ["Refleksi Society 5.0", "Lengkapi kalimat: 'Teknologi ini selaras dengan Society 5.0 jika ...'"],
    ], [4.2 * cm, 12.0 * cm], s))
    story.append(Paragraph(
        "Bentuk hasil: satu poster/infografik digital atau 2-3 slide. Gunakan visual sederhana seperti panah, ikon, atau tabel. Tidak perlu memakai AI untuk membuat visual. Jika memakai AI, tulis tool dan prompt secara jujur.",
        s["CalloutTeladan"],
    ))
    story.append(Paragraph("9. Pengumpulan", s["SectionTeladan"]))
    story.append(Paragraph(
        "Kirim hasil kelompok ke <link href='mailto:ataka.ahmad@gmail.com' color='#1D5F85'><u>ataka.ahmad@gmail.com</u></link>.<br/><b>Subject email:</b> SMA Teladan X - Tugas Technology Risk Map - [Nama Kelompok]<br/>Sertakan nama anggota, teknologi yang dipilih, dan file poster/slide. Pastikan semua anggota memahami isi hasil sebelum dikirim.",
        s["CalloutTeladan"],
    ))

    story.append(Paragraph("10. Referensi Belajar", s["SectionTeladan"]))
    story.append(bullets([
        f"{link('UNESCO - Guidance for Generative AI in Education and Research', 'https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research')}<br/>Menekankan pendekatan human-centered, perlindungan data, dan penggunaan Gen-AI yang aman serta bermakna di pendidikan.",
        f"{link('UNICEF - Guidance on AI and Children', 'https://www.unicef.org/innocenti/reports/policy-guidance-ai-children')}<br/>Membahas keselamatan, privasi, keadilan, transparansi, inklusi, dan kesejahteraan anak dalam penggunaan AI.",
        f"{link('UNESCO - AI and Education: Protecting the Rights of Learners', 'https://www.unesco.org/en/articles/ai-and-education-protecting-rights-learners')}<br/>Menjelaskan peluang sekaligus risiko kesenjangan akses, privasi, keselamatan, etika, dan keadilan dalam teknologi pendidikan.",
        f"{link('Cabinet Office, Government of Japan - Society 5.0', 'https://www8.cao.go.jp/cstp/english/society5_0/index.html')}<br/>Rujukan utama konsep masyarakat berpusat pada manusia yang memadukan dunia fisik dan digital.",
    ], s["SmallTeladan"]))
    story.append(Paragraph("Penutup: berpikir kritis terhadap teknologi bukan berarti anti-teknologi. Justru dengan memahami manfaat dan risikonya, kita dapat memakai teknologi dengan lebih cerdas, aman, dan manusiawi.", s["CalloutTeladan"]))

    doc = SimpleDocTemplate(str(OUTPUT_PATH), pagesize=A4, leftMargin=1.7 * cm, rightMargin=1.7 * cm, topMargin=1.5 * cm, bottomMargin=1.7 * cm, title="Materi Kelas X Society 5.0 dan Risiko Teknologi", author="SMA Teladan")
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    build_pdf()
    print(f"Created {OUTPUT_PATH}")
