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
    / "materi-kelas-xi-pengantar-machine-learning-dan-teachable-machine.pdf"
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
    story.append(Paragraph("Materi Kelas XI: Pengantar Machine Learning", styles["MLTitle"]))
    story.append(
        Paragraph(
            "Dilengkapi pengantar Teachable Machine dan alur praktik sederhana untuk kelas",
            styles["MLSubtitle"],
        )
    )
    story.append(
        Paragraph(
            "Halo teman-teman. Di sesi ini kita akan berkenalan dengan <i>machine learning</i>, yaitu cara komputer belajar dari data. Kita tidak akan mulai dari rumus yang rumit. Kita akan mulai dari contoh yang dekat dengan kehidupan kalian, lalu masuk ke Teachable Machine supaya kalian bisa melihat sendiri bahwa model sederhana pun bisa dilatih.",
            styles["MLCallout"],
        )
    )

    story.append(Paragraph("1. Tujuan Pembelajaran", styles["MLSection"]))
    story.append(
        bullet_list(
            [
                "Kalian memahami arti dasar <i>machine learning</i> dengan bahasa sederhana.",
                "Kalian bisa membedakan AI, <i>machine learning</i>, dan model yang belajar dari contoh data.",
                "Kalian mengenali alur dasar: data - pelatihan - pengujian - prediksi.",
                "Kalian memahami apa itu Teachable Machine dan kapan alat itu berguna.",
                "Kalian siap melakukan praktik sederhana klasifikasi gambar menggunakan webcam atau file gambar.",
            ],
            styles["MLBody"],
        )
    )

    story.append(Paragraph("2. Pembuka Kelas", styles["MLSection"]))
    story.append(
        Paragraph(
            "Pernahkah kalian bertanya, mengapa YouTube bisa memberi rekomendasi video yang terasa cocok? Mengapa galeri ponsel bisa mengenali wajah? Mengapa e-commerce bisa menebak produk yang mungkin kalian sukai? Banyak sistem seperti itu memakai <i>machine learning</i>.",
            styles["MLBody"],
        )
    )
    story.append(
        Paragraph(
            "<b>Pancingan guru:</b> \"Menurut kalian, bagaimana cara komputer membedakan foto kucing dan foto anjing jika tidak diberi aturan satu per satu oleh manusia?\"",
            styles["MLBody"],
        )
    )

    story.append(Paragraph("3. Apa Itu Machine Learning?", styles["MLSection"]))
    story.append(
        Paragraph(
            "<i>Machine learning</i> adalah cabang AI yang memungkinkan komputer belajar dari contoh data, lalu membuat prediksi atau keputusan tanpa harus dituliskan semua aturannya secara manual. Jadi, daripada kita menulis aturan \"jika begini maka begitu\" untuk semua kemungkinan, kita memberi contoh, lalu komputer mencari pola dari contoh itu.",
            styles["MLBody"],
        )
    )
    story.append(
        Paragraph(
            "Bayangkan kalian ingin mengajari komputer membedakan botol dan gelas. Kalian tidak harus menjelaskan semua detail bentuknya dengan kalimat. Kalian cukup memberi banyak contoh foto botol dan gelas. Dari situlah komputer belajar pola yang sering muncul.",
            styles["MLBody"],
        )
    )

    story.append(Paragraph("4. Bedanya AI dan Machine Learning", styles["MLSection"]))
    ai_table_data = [
        ["Istilah", "Makna Sederhana"],
        ["Artificial Intelligence (AI)", "Bidang besar yang membuat mesin melakukan tugas yang tampak cerdas."],
        ["Machine Learning", "Bagian dari AI yang membuat mesin belajar dari data dan contoh."],
        ["Deep Learning", "Bagian lebih khusus dari machine learning yang memakai jaringan saraf berlapis."],
    ]
    ai_table = Table(
        wrap_table(ai_table_data, styles["MLTableHead"], styles["MLTableCell"]),
        colWidths=[4.2 * cm, 11.5 * cm],
    )
    ai_table.setStyle(
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
    story.append(ai_table)

    story.append(Paragraph("5. Cara Kerja Machine Learning", styles["MLSection"]))
    story.append(
        bullet_list(
            [
                "<b>1. Kumpulkan data.</b> Misalnya foto botol, gelas, atau ekspresi wajah.",
                "<b>2. Beri label.</b> Data dikelompokkan ke kelas tertentu, misalnya \"Botol\" dan \"Gelas\".",
                "<b>3. Latih model.</b> Komputer mencari pola dari data yang sudah diberi label.",
                "<b>4. Uji model.</b> Model dicoba dengan data baru yang belum pernah dilihat saat pelatihan.",
                "<b>5. Pakai model.</b> Jika hasilnya cukup baik, model dipakai untuk mengenali data baru.",
            ],
            styles["MLBody"],
        )
    )
    story.append(
        Paragraph(
            "Bagian pentingnya adalah <b>kualitas data</b>. Kalau datanya sedikit, tidak jelas, atau terlalu mirip antar-kelas, model akan mudah salah. Jadi dalam machine learning, data yang baik sering lebih penting daripada penjelasan yang panjang.",
            styles["MLBody"],
        )
    )

    story.append(Paragraph("6. Contoh yang Dekat dengan Siswa", styles["MLSection"]))
    story.append(
        bullet_list(
            [
                "Filter wajah di kamera ponsel.",
                "Pengenalan wajah untuk membuka perangkat.",
                "Rekomendasi video, lagu, atau produk.",
                "Deteksi spam pada email atau pesan.",
                "Pengenalan suara pada asisten digital.",
            ],
            styles["MLBody"],
        )
    )

    story.append(Paragraph("7. Video Pengantar Berbahasa Indonesia", styles["MLSection"]))
    story.append(
        Paragraph(
            "Supaya pengantar materi terasa lebih hidup, kalian bisa menonton 1 atau 2 video berikut. Keduanya berbahasa Indonesia dan cocok untuk membuka diskusi sebelum praktik.",
            styles["MLBody"],
        )
    )
    story.append(link_paragraph("Bagaimana Machine Learning Bekerja", "https://www.youtube.com/watch?v=V31C2lveE9s", styles["MLBody"]))
    story.append(link_paragraph("Perbedaan AI dan Machine Learning", "https://www.youtube.com/watch?v=YpyEYWRIR7U", styles["MLBody"]))
    story.append(
        Paragraph(
            "Setelah menonton, minta siswa menjawab: \"Apa perbedaan AI dan machine learning?\" dan \"Mengapa data penting dalam machine learning?\"",
            styles["MLCallout"],
        )
    )
    story.append(
        Paragraph(
            "Kalau kalian ingin langsung melihat contoh praktik Teachable Machine, buka juga tutorial berikut. Video ini tidak harus berbahasa Indonesia, tetapi alurnya jelas dan cocok untuk melihat langkah praktik dari awal sampai uji model.",
            styles["MLBody"],
        )
    )
    story.append(
        link_paragraph(
            "Tutorial Teachable Machine: Image Classification",
            "https://thecodingtrain.com/tracks/teachable-machine/",
            styles["MLBody"],
        )
    )

    story.append(Paragraph("8. Apa Itu Teachable Machine?", styles["MLSection"]))
    story.append(
        Paragraph(
            "Teachable Machine adalah alat berbasis web dari Google yang memudahkan siapa pun melatih model machine learning tanpa menulis kode. Berdasarkan penjelasan resmi Google, alurnya sangat sederhana: <b>kumpulkan contoh, latih model, lalu uji hasilnya</b>. Alat ini dapat dipakai untuk klasifikasi gambar, suara, dan pose tubuh.",
            styles["MLBody"],
        )
    )
    story.append(
        Paragraph(
            "Situs resmi: <link href=\"https://teachablemachine.withgoogle.com/\" color=\"blue\">https://teachablemachine.withgoogle.com/</link>",
            styles["MLBody"],
        )
    )
    story.append(
        Paragraph(
            "Dalam konteks kelas XI, Teachable Machine sangat cocok karena siswa bisa langsung melihat konsep machine learning secara nyata. Mereka tidak hanya mendengar teori, tetapi juga mengalami proses memberi contoh data, melatih model, lalu melihat hasil prediksi.",
            styles["MLBody"],
        )
    )

    story.append(Paragraph("9. Kelebihan Teachable Machine untuk Pembelajaran", styles["MLSection"]))
    story.append(
        bullet_list(
            [
                "Tidak perlu coding untuk praktik awal.",
                "Cepat dipakai di kelas melalui browser.",
                "Mudah dipahami karena berbasis contoh langsung.",
                "Bisa digunakan untuk gambar, suara, atau pose.",
                "Cocok untuk diskusi tentang akurasi, bias, dan kualitas data.",
            ],
            styles["MLBody"],
        )
    )

    story.append(Paragraph("10. Hal yang Perlu Ditekankan ke Siswa", styles["MLSection"]))
    story.append(
        bullet_list(
            [
                "Model tidak benar-benar \"mengerti\" seperti manusia. Model hanya mencari pola dari data.",
                "Jika data latih buruk, hasil prediksi juga akan buruk.",
                "Akurasi tinggi saat latihan belum tentu berarti model selalu bagus di dunia nyata.",
                "Machine learning tetap perlu dicek manusia; hasil model tidak boleh diterima mentah-mentah.",
            ],
            styles["MLBody"],
        )
    )

    story.append(Paragraph("11. Alur Praktik Kelas dengan Teachable Machine", styles["MLSection"]))
    practice_table_data = [
        ["Tahap", "Aktivitas"],
        ["1. Tentukan kelas", "Misalnya dua kelas: \"Buku\" dan \"Botol\" atau \"Tangan Terbuka\" dan \"Tangan Mengepal\"."],
        ["2. Kumpulkan contoh", "Ambil contoh gambar dengan webcam atau unggah file gambar. Usahakan jumlah tiap kelas seimbang."],
        ["3. Latih model", "Klik tombol train dan tunggu model belajar dari contoh yang diberikan."],
        ["4. Uji model", "Coba tunjukkan objek baru ke kamera dan lihat prediksinya."],
        ["5. Evaluasi", "Diskusikan kapan model benar, kapan model salah, dan apa penyebabnya."],
    ]
    practice_table = Table(
        wrap_table(practice_table_data, styles["MLTableHead"], styles["MLTableCell"]),
        colWidths=[3.2 * cm, 12.5 * cm],
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

    story.append(Paragraph("12. Ide Tugas Kelompok", styles["MLSection"]))
    story.append(
        Paragraph(
            "<b>Judul:</b> Menguji Seberapa Baik Model Belajar dari Data",
            styles["MLBody"],
        )
    )
    story.append(
        bullet_list(
            [
                "Buat model dengan 2 kelas sederhana.",
                "Latih model menggunakan contoh yang cukup banyak dan bervariasi.",
                "Uji model dengan contoh baru.",
                "Ambil screenshot saat proses pengumpulan data untuk tiap kelas.",
                "Ambil screenshot setelah model selesai dilatih.",
                "Ambil screenshot saat model sedang diuji dan menampilkan hasil prediksi.",
                "Catat minimal 3 situasi saat model benar dan 3 situasi saat model salah.",
                "Jelaskan dugaan penyebab kesalahan: cahaya, sudut kamera, jumlah data, atau kemiripan objek.",
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
                "Kelas yang dipilih",
                "Jumlah dan jenis data yang dikumpulkan",
                "Screenshot pengumpulan data",
                "Screenshot hasil training model",
                "Screenshot hasil pengujian atau prediksi",
                "Contoh hasil prediksi yang benar",
                "Contoh hasil prediksi yang salah",
                "Analisis penyebab kesalahan",
                "Saran perbaikan model",
            ],
            styles["MLBody"],
        )
    )
    story.append(
        Paragraph(
            "<b>Pengumpulan tugas:</b> kirim hasil kelompok ke <link href=\"mailto:ataka.ahmad@gmail.com\" color=\"blue\">ataka.ahmad@gmail.com</link>.<br/><b>Format subject email:</b> <b>SMA Teladan XI - Tugas Machine Learning - [Nama Kelompok]</b><br/><b>Isi email singkat:</b> tulis nama anggota kelompok dan lampirkan hasil tugas beserta screenshot praktik kalian.",
            styles["MLBody"],
        )
    )

    story.append(Paragraph("13. Penutup", styles["MLSection"]))
    story.append(
        Paragraph(
            "Teman-teman, machine learning bukan sulap. Komputer tidak tiba-tiba pintar sendiri. Komputer belajar dari data yang kita berikan. Karena itu, saat kalian memakai alat seperti Teachable Machine, kalian sedang melihat proses yang sangat penting dalam AI modern: bagaimana data membentuk hasil model. Semakin baik datanya, semakin baik peluang model untuk bekerja dengan benar.",
            styles["MLBody"],
        )
    )
    story.append(
        Paragraph(
            "Pertanyaan refleksi akhir: <b>kalau model salah mengenali objek, apakah itu berarti teknologinya jelek, atau justru datanya yang perlu diperbaiki?</b>",
            styles["MLCallout"],
        )
    )
    story.append(
        Paragraph(
            "Referensi utama materi: video penjelasan berbahasa Indonesia dari LMS SPADA Indonesia; situs resmi Teachable Machine dari Google; dan dokumentasi resmi Google tentang alur Gather - Train - Export.",
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
        title="Materi Kelas XI Pengantar Machine Learning",
        author="OpenAI Codex",
    )
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    build_pdf()
