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


OUTPUT_PATH = (
    Path("/Users/ahmadataka/Documents/Codex project/SMA Teladan/unique-value-teladan/pdf")
    / "materi-kelas-x-society-5-dan-design-challenge.pdf"
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
        backColor=colors.HexColor("#EAF3F8"), borderPadding=(7, 9, 7),
        spaceAfter=10,
    ))
    styles.add(ParagraphStyle(
        name="TableCellTeladan", parent=styles["BodyText"], fontName="Helvetica",
        fontSize=9.1, leading=11.3, textColor=colors.HexColor("#1F2933"),
    ))
    styles.add(ParagraphStyle(
        name="TableHeadTeladan", parent=styles["BodyText"], fontName="Helvetica-Bold",
        fontSize=9.3, leading=11.1, textColor=colors.white,
    ))
    styles.add(ParagraphStyle(
        name="SmallTeladan", parent=styles["BodyText"], fontName="Helvetica",
        fontSize=8.9, leading=12.0, textColor=colors.HexColor("#425466"),
        spaceAfter=4,
    ))
    return styles


def bullet_list(items, style):
    return ListFlowable(
        [ListItem(Paragraph(item, style), leftIndent=6) for item in items],
        bulletType="bullet", start="circle", leftIndent=16,
        bulletFontName="Helvetica", bulletFontSize=10, bulletOffsetY=2,
    )


def wrap_table(data, head_style, cell_style):
    return [
        [Paragraph(str(cell), head_style if row_index == 0 else cell_style) for cell in row]
        for row_index, row in enumerate(data)
    ]


def styled_table(data, widths, styles):
    table = Table(
        wrap_table(data, styles["TableHeadTeladan"], styles["TableCellTeladan"]),
        colWidths=widths,
        repeatRows=1,
    )
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#24577A")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#B7C5D1")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F1F7FA")]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return table


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
    styles = build_styles()
    story = []

    story.append(Spacer(1, 0.6 * cm))
    story.append(Paragraph("Materi Kelas X: Society 5.0 dan Design Challenge", styles["TitleTeladan"]))
    story.append(Paragraph(
        "Merancang sekolah yang lebih manusiawi dengan teknologi yang benar-benar berguna",
        styles["SubtitleTeladan"],
    ))
    story.append(Paragraph(
        "Halo teman-teman. Kalian sudah mengenal Gen-AI, membuat dan membaca visual dengan AI, lalu melihat AR/VR untuk belajar. Sekarang kita naik satu tingkat: bukan hanya bertanya <i>teknologinya keren atau tidak</i>, tetapi <b>masalah manusia apa yang dapat dibantu teknologi?</b> Di sesi ini kalian akan menjadi tim perancang solusi untuk sekolah.",
        styles["CalloutTeladan"],
    ))

    story.append(Paragraph("1. Tujuan Pembelajaran", styles["SectionTeladan"]))
    story.append(bullet_list([
        "Kalian memahami Society 5.0 sebagai gagasan masyarakat yang berpusat pada manusia.",
        "Kalian membedakan fokus Industry 4.0 dan Society 5.0 secara sederhana.",
        "Kalian mengenali inovasi nyata yang memakai teknologi untuk memperluas akses dan membantu belajar.",
        "Kalian mencoba proses desain yang dimulai dari kebutuhan pengguna, bukan dari alat yang sedang tren.",
        "Kalian mampu menyusun ide solusi untuk satu masalah nyata di lingkungan sekolah.",
    ], styles["BodyTeladan"]))

    story.append(Paragraph("2. Jembatan dari Materi Sebelumnya", styles["SectionTeladan"]))
    story.append(Paragraph(
        "Gen-AI dapat membantu mencari gagasan, merangkum, atau membuat visual. AI gambar dapat membantu membaca informasi visual. AR/VR dapat membuat pembelajaran terasa lebih dekat dan interaktif. Semua itu adalah <b>alat</b>. Namun alat yang baik baru bermakna jika dipakai untuk membuat hidup, belajar, dan bekerja menjadi lebih aman, adil, mudah diakses, dan bermakna.",
        styles["BodyTeladan"],
    ))
    story.append(Paragraph(
        "Pertanyaan utama hari ini: <b>Jika teknologi tersedia, bagaimana kita memastikan teknologi itu tetap berpihak pada manusia?</b>",
        styles["CalloutTeladan"],
    ))

    story.append(Paragraph("3. Apa Itu Society 5.0?", styles["SectionTeladan"]))
    story.append(Paragraph(
        "Society 5.0 adalah visi masyarakat masa depan yang menggabungkan dunia fisik dan dunia digital untuk menyelesaikan persoalan sosial, sambil tetap menempatkan manusia sebagai pusatnya. Gagasan ini diperkenalkan oleh Cabinet Office Jepang. Artinya, sensor, data, internet, AI, dan robot bukan tujuan akhir. Teknologi dipakai untuk membantu manusia hidup lebih baik.",
        styles["BodyTeladan"],
    ))
    story.append(styled_table([
        ["Tahap masyarakat", "Gambaran singkat"],
        ["Society 1.0", "Masyarakat berburu dan meramu."],
        ["Society 2.0", "Masyarakat pertanian."],
        ["Society 3.0", "Masyarakat industri."],
        ["Society 4.0", "Masyarakat informasi: komputer dan internet mempercepat pertukaran data."],
        ["Society 5.0", "Masyarakat berpusat pada manusia: data dan teknologi dipakai untuk menjawab kebutuhan nyata, dengan perhatian pada kesejahteraan, keselamatan, dan keadilan."],
    ], [4.0 * cm, 12.2 * cm], styles))

    story.append(Paragraph("4. Industry 4.0 dan Society 5.0: Bukan Musuh, tetapi Berbeda Fokus", styles["SectionTeladan"]))
    story.append(styled_table([
        ["Pertanyaan", "Industry 4.0", "Society 5.0"],
        ["Fokus utama", "Otomatisasi, konektivitas, efisiensi proses.", "Kebutuhan manusia dan penyelesaian masalah sosial."],
        ["Pertanyaan yang sering muncul", "Bagaimana pekerjaan menjadi lebih cepat dan akurat?", "Siapa yang terbantu, siapa yang mungkin tertinggal, dan apa dampaknya?"],
        ["Contoh di sekolah", "Absensi digital yang mengurangi pekerjaan administrasi.", "Sistem belajar yang juga mempertimbangkan akses siswa, privasi data, dan dukungan bagi yang kesulitan."],
        ["Ukuran keberhasilan", "Proses lebih efisien.", "Kehidupan dan pengalaman pengguna benar-benar membaik secara adil."],
    ], [3.3 * cm, 6.45 * cm, 6.45 * cm], styles))

    story.append(Paragraph("5. Contoh Inovasi Nyata: Teknologi yang Membantu Manusia", styles["SectionTeladan"]))
    story.append(Paragraph(
        "Lihat contoh berikut sebagai bahan berpikir, bukan untuk ditiru mentah-mentah. Perhatikan selalu: masalah apa yang dibantu, siapa penggunanya, dan batasannya.",
        styles["BodyTeladan"],
    ))
    story.append(styled_table([
        ["Produk/inovasi", "Masalah manusia yang dibantu", "Pelajaran untuk tim kalian"],
        [link("Seeing AI", "https://www.microsoft.com/en-us/ai/seeing-ai"), "Membantu orang dengan gangguan penglihatan mengenali teks, benda, dan lingkungan melalui kamera serta audio.", "Desain yang baik memperluas akses. Tanyakan: apakah solusi kita juga ramah bagi pengguna dengan kebutuhan berbeda?"],
        [link("Khanmigo", "https://www.khanacademy.org/khan-labs"), "Mendukung belajar dengan tutor berbasis AI dan alat bantu guru.", "Teknologi belajar seharusnya mengajak siswa berpikir, bukan menggantikan proses belajarnya."],
        [link("Google Maps: aksesibilitas", "https://support.google.com/maps/answer/11118109"), "Membantu pengguna menemukan informasi tempat dan rute yang lebih mudah diakses.", "Informasi yang sederhana dapat sangat berarti bagi orang yang mobilitasnya berbeda."],
        [link("Be My Eyes", "https://www.bemyeyes.com/"), "Menghubungkan pengguna tunanetra dengan relawan atau bantuan visual berbasis teknologi.", "Solusi dapat menggabungkan teknologi dan kepedulian manusia, bukan memilih salah satunya."],
    ], [4.1 * cm, 6.15 * cm, 5.95 * cm], styles))

    story.append(Paragraph("6. Cara Berpikir Desain yang Berpusat pada Manusia", styles["SectionTeladan"]))
    story.append(Paragraph(
        "Kita akan memakai versi sederhana dari proses <i>Double Diamond</i> dari Design Council. Kuncinya: jangan terburu-buru menentukan aplikasi atau alat. Pahami dulu orang dan masalahnya.",
        styles["BodyTeladan"],
    ))
    story.append(styled_table([
        ["Langkah", "Apa yang kalian lakukan", "Contoh di sekolah"],
        ["1. Temukan", "Amati, tanya, dan kumpulkan beberapa kemungkinan masalah.", "Siswa sering terlambat menemukan ruang kelas pengganti."],
        ["2. Tentukan", "Pilih satu masalah yang paling nyata, penting, dan mungkin dibantu.", "Masalah fokus: informasi perubahan ruang belum mudah terlihat."],
        ["3. Kembangkan", "Buat beberapa ide solusi, lalu bandingkan manfaat dan risikonya.", "Papan informasi digital, QR di titik sekolah, atau notifikasi terarah."],
        ["4. Sampaikan", "Pilih solusi terbaik, buat sketsa/diagram, dan uji lewat umpan balik sederhana.", "Minta teman mencoba membaca sketsa informasi dan memberi masukan."],
    ], [3.0 * cm, 6.0 * cm, 7.2 * cm], styles))
    story.append(Paragraph(
        "Ingat: <b>teknologi bukan jawaban pertama.</b> Jawaban pertama adalah pemahaman terhadap kebutuhan orang yang akan memakai solusi tersebut.",
        styles["CalloutTeladan"],
    ))

    story.append(Paragraph("7. Etika: Empat Pertanyaan Wajib Sebelum Membuat Solusi", styles["SectionTeladan"]))
    story.append(bullet_list([
        "<b>Manfaat:</b> apakah solusi ini benar-benar membantu, atau hanya terlihat canggih?",
        "<b>Privasi:</b> data apa yang dikumpulkan? Apakah data siswa, foto, lokasi, atau kebiasaan benar-benar diperlukan?",
        "<b>Inklusi:</b> apakah solusi masih dapat dipakai oleh siswa dengan perangkat, kemampuan, atau akses internet yang berbeda?",
        "<b>Tanggung jawab:</b> jika alat salah memberi informasi atau merugikan seseorang, siapa yang memeriksa dan memperbaikinya?",
    ], styles["BodyTeladan"]))
    story.append(Paragraph(
        "Untuk teknologi yang menyentuh anak dan pendidikan, UNICEF menekankan keselamatan, perlindungan data dan privasi, keadilan, transparansi, serta kepentingan terbaik anak. Karena itu, solusi yang baik tidak harus mengumpulkan data sebanyak-banyaknya.",
        styles["CalloutTeladan"],
    ))

    story.append(Paragraph("8. Design Challenge Kelompok: Sekolah yang Lebih Manusiawi", styles["SectionTeladan"]))
    story.append(Paragraph(
        "Bayangkan kalian adalah tim inovasi SMA Teladan. Pilih satu masalah nyata yang dirasakan siswa, guru, staf, atau pengunjung sekolah. Rancang solusi yang memakai teknologi secara secukupnya dan tetap berpihak pada manusia.",
        styles["BodyTeladan"],
    ))
    story.append(Paragraph("Pilihan area masalah (atau pilih masalah nyata lain yang kalian amati):", styles["CalloutTeladan"]))
    story.append(bullet_list([
        "Akses informasi sekolah: jadwal, perubahan ruangan, kegiatan, atau pengumuman.",
        "Kenyamanan dan keselamatan: antrean, titik rawan, pencahayaan, air minum, atau navigasi tamu.",
        "Belajar yang inklusif: materi lebih mudah dipahami, akses bagi siswa berkebutuhan berbeda, atau dukungan belajar teman sebaya.",
        "Lingkungan sekolah: sampah, energi, kebersihan, tanaman, atau penggunaan air.",
        "Kebersamaan dan kesejahteraan: siswa baru, komunikasi antarwarga sekolah, atau ruang istirahat yang lebih nyaman.",
    ], styles["BodyTeladan"]))

    story.append(Paragraph("9. Aturan Main Ide Kalian", styles["SectionTeladan"]))
    story.append(bullet_list([
        "Mulailah dari satu pengguna dan satu masalah yang spesifik. Hindari masalah yang terlalu besar seperti 'membuat sekolah lebih modern'.",
        "Boleh memakai AI, aplikasi, QR code, sensor, AR/VR, data sederhana, atau bahkan solusi non-digital jika itu lebih tepat.",
        "Jelaskan mengapa teknologi diperlukan. Jika papan informasi biasa sudah cukup, itu juga jawaban yang sah.",
        "Jangan menggunakan nama, foto, nomor telepon, atau data pribadi siswa tanpa izin.",
        "Solusi tidak perlu benar-benar dibuat hari ini. Yang dinilai adalah alasan, kepedulian pada pengguna, dan rancangan yang masuk akal.",
    ], styles["BodyTeladan"]))

    story.append(KeepTogether([
        Paragraph("10. Format Laporan Kelompok", styles["SectionTeladan"]),
        Paragraph(
            "Buat laporan ringkas 2-3 halaman atau 5-7 slide. Gunakan bahasa kalian sendiri dan sertakan sumber bila mengambil data, gambar, atau ide dari internet.",
            styles["BodyTeladan"],
        ),
    ]))
    story.append(styled_table([
        ["Bagian", "Isi minimum"],
        ["1. Judul dan anggota", "Nama ide dan nama seluruh anggota kelompok."],
        ["2. Masalah dan pengguna", "Siapa yang mengalami masalah? Kapan/di mana masalah terjadi? Bukti sederhana: hasil pengamatan, kutipan wawancara singkat, atau contoh situasi."],
        ["3. Solusi", "Jelaskan ide kalian dalam 1 paragraf. Teknologi apa yang dipakai dan mengapa?"],
        ["4. Sketsa atau alur", "Buat gambar/diagram sederhana: pengguna -> langkah penggunaan -> hasil yang diterima pengguna."],
        ["5. Manfaat dan batasan", "Dua manfaat nyata, satu kemungkinan keterbatasan, dan cara menguranginya."],
        ["6. Etika", "Jawab: bagaimana kalian menjaga privasi, keadilan akses, dan peran manusia?"],
        ["7. Referensi", "Tulis tautan sumber produk/inovasi yang menginspirasi ide kalian."],
    ], [4.0 * cm, 12.2 * cm], styles))

    story.append(Paragraph("11. Pengumpulan", styles["SectionTeladan"]))
    story.append(KeepTogether([
        Paragraph(
            "Kirim laporan kelompok ke <b>ataka.ahmad@gmail.com</b> dengan subjek email:",
            styles["BodyTeladan"],
        ),
        Paragraph(
            "<b>SMA Teladan X - Tugas Society 5.0 - [Nama Kelompok]</b>",
            styles["CalloutTeladan"],
        ),
        Paragraph(
            "Pastikan nama file jelas, misalnya: <i>Society5_Kelompok_Inovator.pdf</i>. Sebelum mengirim, cek kembali: apakah ide kalian membantu manusia, bukan sekadar memakai teknologi?",
            styles["BodyTeladan"],
        ),
    ]))

    story.append(Paragraph("12. Sumber Belajar dan Inspirasi", styles["SectionTeladan"]))
    sources = [
        f"{link('Cabinet Office, Government of Japan - Society 5.0', 'https://www8.cao.go.jp/cstp/english/society5_0/index.html')}<br/>Definisi Society 5.0 sebagai masyarakat berpusat pada manusia yang memadukan ruang siber dan fisik untuk menjawab persoalan sosial.",
        f"{link('Design Council - Framework for Innovation', 'https://www.designcouncil.org.uk/resources/framework-for-innovation/')}<br/>Rujukan proses Double Diamond untuk memahami masalah dan mengembangkan solusi.",
        f"{link('UNICEF - EdTech for Good Framework 2.0', 'https://www.unicef.org/digitaleducation/edtech-for-good')}<br/>Kerangka untuk menilai teknologi pendidikan agar aman, adil, sesuai konteks, dan bermanfaat.",
        f"{link('UNICEF - Guidance on AI and Children', 'https://www.unicef.org/innocenti/reports/policy-guidance-ai-children')}<br/>Prinsip keselamatan, privasi, keadilan, transparansi, dan kesejahteraan anak dalam penggunaan AI.",
        f"{link('Microsoft - Seeing AI', 'https://www.microsoft.com/en-us/ai/seeing-ai')}<br/>Contoh inovasi aksesibilitas berbasis kamera dan audio.",
        f"{link('Khan Academy - Khanmigo', 'https://www.khanacademy.org/khan-labs')}<br/>Contoh asisten belajar berbasis AI dan diskusi tentang penggunaan AI yang mendukung proses belajar.",
    ]
    story.append(bullet_list(sources, styles["SmallTeladan"]))
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph(
        "Penutup: Society 5.0 bukan tentang sekolah yang dipenuhi layar atau robot. Society 5.0 adalah tentang sekolah yang lebih peka terhadap kebutuhan warganya, lalu memakai teknologi dengan bijak untuk membantu.",
        styles["CalloutTeladan"],
    ))

    doc = SimpleDocTemplate(
        str(OUTPUT_PATH), pagesize=A4,
        rightMargin=1.7 * cm, leftMargin=1.7 * cm,
        topMargin=1.5 * cm, bottomMargin=1.8 * cm,
        title="Materi Kelas X: Society 5.0 dan Design Challenge",
        author="SMA Teladan",
    )
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    build_pdf()
    print(f"Created {OUTPUT_PATH}")
