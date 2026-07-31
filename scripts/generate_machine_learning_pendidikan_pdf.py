from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


OUTPUT_PATH = (
    Path("/Users/ahmadataka/Documents/SMA Teladan/output/pdf")
    / "materi-kelas-xi-machine-learning-untuk-pendidikan-dan-sekolah-teladan.pdf"
)


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="MLTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=19,
            leading=22,
            textColor=colors.HexColor("#17324D"),
            alignment=TA_CENTER,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="MLSubtitle",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=10.2,
            leading=13.2,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#355C7D"),
            spaceAfter=12,
        )
    )
    styles.add(
        ParagraphStyle(
            name="MLSection",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=13.2,
            leading=16,
            textColor=colors.white,
            backColor=colors.HexColor("#24577A"),
            borderPadding=(6, 8, 6),
            spaceBefore=10,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="MLBody",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=10.3,
            leading=14.2,
            textColor=colors.HexColor("#1F2933"),
            alignment=TA_JUSTIFY,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="MLCallout",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=10.4,
            leading=13.8,
            textColor=colors.HexColor("#17324D"),
            backColor=colors.HexColor("#EAF3F8"),
            borderPadding=(7, 9, 7),
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="MLTableHead",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=9.0,
            leading=10.6,
            textColor=colors.white,
        )
    )
    styles.add(
        ParagraphStyle(
            name="MLTableCell",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.8,
            leading=10.5,
            textColor=colors.HexColor("#1F2933"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="MLSmall",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.8,
            leading=11.4,
            textColor=colors.HexColor("#425466"),
            spaceAfter=4,
        )
    )
    return styles


def bullet_list(items, style):
    return ListFlowable(
        [ListItem(Paragraph(item, style), leftIndent=6) for item in items],
        bulletType="bullet",
        start="circle",
        leftIndent=16,
        bulletFontName="Helvetica",
        bulletFontSize=10,
        bulletOffsetY=2,
    )


def link_paragraph(label, url, style):
    return Paragraph(f'<b>{label}</b><br/><link href="{url}" color="blue">{url}</link>', style)


def wrap_table(data, head_style, cell_style):
    wrapped = []
    for row_index, row in enumerate(data):
        new_row = []
        for cell in row:
            style = head_style if row_index == 0 else cell_style
            new_row.append(Paragraph(str(cell), style))
        wrapped.append(new_row)
    return wrapped


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

    story.append(Spacer(1, 0.6 * cm))
    story.append(
        Paragraph(
            "Materi Kelas XI: Machine Learning untuk Pendidikan",
            styles["MLTitle"],
        )
    )
    story.append(
        Paragraph(
            "Fokus pada mengenali teknologi yang berguna dan mengusulkan penerapannya di SMA Teladan Yogyakarta",
            styles["MLSubtitle"],
        )
    )
    story.append(
        Paragraph(
            "Halo teman-teman. Di materi ini kita tidak akan berlatih membuat model sendiri. Kita akan melihat bagaimana <i>machine learning</i> sudah dipakai dalam dunia pendidikan, lalu kalian akan menilai teknologi mana yang benar-benar bermanfaat dan layak diusulkan untuk lingkungan SMA Teladan Yogyakarta.",
            styles["MLCallout"],
        )
    )

    story.append(Paragraph("1. Tujuan Pembelajaran", styles["MLSection"]))
    story.append(
        bullet_list(
            [
                "Kalian memahami arti dasar <i>machine learning</i> dengan bahasa yang sederhana.",
                "Kalian mengenali contoh penggunaan <i>machine learning</i> di bidang pendidikan.",
                "Kalian bisa membedakan teknologi yang sekadar menarik dengan teknologi yang benar-benar berguna.",
                "Kalian berlatih mengamati kebutuhan sekolah sebelum mengusulkan solusi teknologi.",
                "Kalian menyusun usulan teknologi <i>machine learning</i> yang relevan untuk SMA Teladan Yogyakarta.",
            ],
            styles["MLBody"],
        )
    )

    story.append(Paragraph("2. Pembuka Kelas", styles["MLSection"]))
    story.append(
        Paragraph(
            "Coba bayangkan sekolah yang bisa membantu siswa belajar lebih tepat sasaran. Misalnya, sistem yang membantu guru melihat siswa mana yang perlu penguatan, aplikasi yang memberi rekomendasi latihan sesuai kemampuan, atau alat yang membantu merangkum materi panjang menjadi poin penting. Di situlah <i>machine learning</i> bisa berperan.",
            styles["MLBody"],
        )
    )
    story.append(
        Paragraph(
            "<b>Pertanyaan pembuka:</b> \"Kalau sekolah boleh memakai satu teknologi pintar untuk membantu belajar, kalian ingin teknologi itu membantu di bagian apa?\"",
            styles["MLBody"],
        )
    )

    story.append(Paragraph("3. Apa Itu Machine Learning?", styles["MLSection"]))
    story.append(
        Paragraph(
            "<i>Machine learning</i> adalah cara membuat komputer belajar dari data, lalu memakai pola yang ditemukan untuk memberi prediksi, rekomendasi, atau keputusan. Jadi komputer tidak hanya menjalankan aturan yang ditulis satu per satu, tetapi belajar dari contoh yang tersedia.",
            styles["MLBody"],
        )
    )
    story.append(
        Paragraph(
            "Di dunia pendidikan, data itu bisa berupa hasil latihan, jawaban kuis, kecepatan membaca, kebiasaan belajar, atau jenis materi yang paling sering dibuka siswa. Dari pola itu, sistem bisa membantu memberi masukan yang lebih tepat.",
            styles["MLBody"],
        )
    )

    story.append(Paragraph("4. Contoh Machine Learning di Bidang Pendidikan", styles["MLSection"]))
    story.append(
        bullet_list(
            [
                "Rekomendasi materi belajar berdasarkan kemampuan siswa.",
                "Sistem latihan adaptif yang menyesuaikan tingkat soal.",
                "Penerjemahan otomatis dan subtitle untuk membantu pemahaman.",
                "Pengecekan tulisan atau tata bahasa secara otomatis.",
                "Ringkasan materi panjang menjadi poin-poin penting.",
                "Pengenalan suara untuk mengubah ucapan menjadi teks.",
                "Pencarian cerdas untuk menemukan referensi yang relevan.",
            ],
            styles["MLBody"],
        )
    )

    story.append(Paragraph("5. Manfaat yang Perlu Kalian Nilai", styles["MLSection"]))
    evaluation_table_data = [
        ["Aspek", "Pertanyaan yang Perlu Dipikirkan"],
        ["Manfaat belajar", "Apakah teknologi ini benar-benar membantu siswa memahami materi?"],
        ["Kemudahan pakai", "Apakah siswa dan guru bisa memakainya tanpa pelatihan yang rumit?"],
        ["Akses", "Apakah bisa dipakai melalui handphone yang dimiliki siswa?"],
        ["Keamanan", "Apakah data pribadi siswa perlu dijaga dengan ketat?"],
        ["Keadilan", "Apakah hasilnya bisa bias atau merugikan sebagian siswa?"],
        ["Kesesuaian sekolah", "Apakah cocok dengan kebutuhan nyata di SMA Teladan Yogyakarta?"],
    ]
    evaluation_table = Table(
        wrap_table(evaluation_table_data, styles["MLTableHead"], styles["MLTableCell"]),
        colWidths=[4.4 * cm, 11.3 * cm],
    )
    evaluation_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#17324D")),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#A9BAC7")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F4F8FB")]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(evaluation_table)

    story.append(Paragraph("6. Contoh Teknologi yang Bisa Diamati", styles["MLSection"]))
    story.append(
        Paragraph(
            "Kalian tidak harus membuat aplikasinya. Tugas kalian adalah mengamati teknologi yang sudah ada, memahami manfaatnya, lalu menilai apakah cocok untuk dipakai di sekolah.",
            styles["MLBody"],
        )
    )
    story.append(
        bullet_list(
            [
                "Aplikasi belajar yang memberi soal adaptif.",
                "Alat ringkasan materi atau catatan otomatis.",
                "Penerjemah teks atau suara untuk membantu pemahaman.",
                "Pencarian visual atau pencarian cerdas untuk belajar.",
                "Aplikasi pendamping menulis atau pengecekan bahasa.",
                "Fitur <i>speech-to-text</i> untuk mencatat penjelasan guru.",
            ],
            styles["MLBody"],
        )
    )

    story.append(Paragraph("7. Video Pengantar Berbahasa Indonesia", styles["MLSection"]))
    story.append(
        Paragraph(
            "Agar pembahasan lebih mudah dibayangkan, kalian bisa menonton video pengantar berikut sebelum masuk ke tugas analisis.",
            styles["MLBody"],
        )
    )
    story.append(
        link_paragraph(
            "Bagaimana Machine Learning Bekerja",
            "https://www.youtube.com/watch?v=V31C2lveE9s",
            styles["MLBody"],
        )
    )
    story.append(
        link_paragraph(
            "Perbedaan AI dan Machine Learning",
            "https://www.youtube.com/watch?v=YpyEYWRIR7U",
            styles["MLBody"],
        )
    )
    story.append(
        Paragraph(
            "Setelah menonton, diskusikan bersama: \"Kalau teknologi belajar makin pintar, apa yang tetap harus dijaga oleh manusia, guru, dan siswa?\"",
            styles["MLCallout"],
        )
    )

    story.append(Paragraph("8. Cara Berpikir Sebelum Mengusulkan Teknologi", styles["MLSection"]))
    story.append(
        bullet_list(
            [
                "Mulailah dari masalah nyata, bukan dari nama aplikasi yang sedang populer.",
                "Pikirkan siapa yang akan terbantu: siswa, guru, wali kelas, atau sekolah.",
                "Nilai apakah manfaatnya lebih besar daripada risikonya.",
                "Pilih teknologi yang realistis dipakai, bukan hanya terdengar canggih.",
                "Ingat bahwa teknologi harus membantu proses belajar, bukan menggantikan guru.",
            ],
            styles["MLBody"],
        )
    )

    story.append(Paragraph("9. Alur Praktik Kelompok", styles["MLSection"]))
    practice_table_data = [
        ["Tahap", "Aktivitas"],
        ["1. Pilih masalah", "Tentukan satu masalah di lingkungan sekolah, misalnya kesulitan memahami materi, mencatat, mencari referensi, atau latihan mandiri."],
        ["2. Cari contoh teknologi", "Temukan satu atau dua teknologi berbasis machine learning yang berhubungan dengan masalah tersebut."],
        ["3. Amati fitur", "Catat fitur utama, siapa penggunanya, dan manfaat yang ditawarkan."],
        ["4. Nilai kecocokan", "Diskusikan apakah teknologi itu cocok untuk siswa dan guru di SMA Teladan Yogyakarta."],
        ["5. Buat usulan", "Susun satu rekomendasi teknologi beserta alasan, manfaat, dan catatan kehati-hatian."],
    ]
    practice_table = Table(
        wrap_table(practice_table_data, styles["MLTableHead"], styles["MLTableCell"]),
        colWidths=[3.4 * cm, 12.3 * cm],
    )
    practice_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#17324D")),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#A9BAC7")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F4F8FB")]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(practice_table)

    story.append(Paragraph("10. Ide Masalah yang Bisa Dipilih", styles["MLSection"]))
    story.append(
        bullet_list(
            [
                "Siswa kesulitan merangkum materi yang panjang.",
                "Siswa butuh latihan soal yang tingkatnya menyesuaikan kemampuan.",
                "Guru butuh alat bantu untuk melihat topik yang belum dipahami kelas.",
                "Siswa butuh bantuan memahami istilah asing atau materi berbahasa Inggris.",
                "Siswa butuh cara cepat mencari sumber belajar yang relevan.",
                "Siswa membutuhkan alat bantu mencatat dari penjelasan lisan.",
            ],
            styles["MLBody"],
        )
    )

    story.append(Paragraph("11. Tugas Kelompok", styles["MLSection"]))
    story.append(
        Paragraph(
            "<b>Judul:</b> Mengusulkan Teknologi Machine Learning yang Bermanfaat untuk SMA Teladan Yogyakarta",
            styles["MLBody"],
        )
    )
    story.append(
        bullet_list(
            [
                "Pilih satu masalah nyata di lingkungan belajar sekolah.",
                "Cari minimal satu teknologi atau aplikasi yang memakai machine learning dan relevan dengan masalah itu.",
                "Jelaskan bagaimana teknologi tersebut bekerja secara sederhana.",
                "Jelaskan siapa yang akan terbantu jika teknologi itu digunakan di sekolah.",
                "Jelaskan manfaat utamanya untuk proses belajar atau pengajaran.",
                "Jelaskan risiko atau keterbatasannya, misalnya ketergantungan, bias, atau privasi data.",
                "Buat usulan akhir: apakah teknologi ini layak dicoba di SMA Teladan Yogyakarta atau tidak.",
                "Sertakan screenshot hasil pencarian, tampilan fitur, atau contoh penggunaan yang kalian temukan.",
            ],
            styles["MLBody"],
        )
    )

    story.append(
        Paragraph(
            "<b>Format laporan singkat yang dikumpulkan:</b>",
            styles["MLBody"],
        )
    )
    story.append(
        bullet_list(
            [
                "Nama kelompok",
                "Masalah yang dipilih",
                "Nama teknologi atau aplikasi yang diamati",
                "Penjelasan singkat cara kerja teknologinya",
                "Manfaat untuk siswa atau guru",
                "Risiko atau keterbatasan",
                "Alasan mengapa cocok atau tidak cocok untuk SMA Teladan Yogyakarta",
                "Usulan akhir kelompok",
                "Screenshot pendukung",
            ],
            styles["MLBody"],
        )
    )
    story.append(
        Paragraph(
            "<b>Pengumpulan tugas:</b> kirim hasil kelompok ke <link href=\"mailto:ataka.ahmad@gmail.com\" color=\"blue\">ataka.ahmad@gmail.com</link>.<br/><b>Format subject email:</b> <b>SMA Teladan XI - Usulan Teknologi ML - [Nama Kelompok]</b><br/><b>Isi email singkat:</b> tulis nama anggota kelompok dan lampirkan hasil tugas beserta screenshot pendukung.",
            styles["MLBody"],
        )
    )

    story.append(Paragraph("12. Penutup", styles["MLSection"]))
    story.append(
        Paragraph(
            "Teman-teman, teknologi yang baik bukan teknologi yang paling rumit, tetapi teknologi yang paling membantu manusia menyelesaikan masalah nyata. Dalam dunia pendidikan, machine learning seharusnya membantu belajar menjadi lebih jelas, lebih terarah, dan lebih mudah diakses. Karena itu, sebelum memilih teknologi, kita perlu bertanya: siapa yang terbantu, bagaimana caranya, dan apa risikonya.",
            styles["MLBody"],
        )
    )
    story.append(
        Paragraph(
            "Pertanyaan refleksi akhir: <b>kalau SMA Teladan Yogyakarta hanya boleh mencoba satu teknologi machine learning untuk mendukung pembelajaran, teknologi apa yang paling layak dicoba lebih dulu, dan mengapa?</b>",
            styles["MLCallout"],
        )
    )
    story.append(
        Paragraph(
            "Referensi utama materi: video pengantar machine learning berbahasa Indonesia dan contoh-contoh penerapan machine learning dalam pembelajaran digital.",
            styles["MLSmall"],
        )
    )

    doc = SimpleDocTemplate(
        str(OUTPUT_PATH),
        pagesize=A4,
        leftMargin=1.5 * cm,
        rightMargin=1.5 * cm,
        topMargin=1.3 * cm,
        bottomMargin=1.5 * cm,
        title="Materi Kelas XI Machine Learning untuk Pendidikan",
        author="OpenAI Codex",
    )
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    build_pdf()
