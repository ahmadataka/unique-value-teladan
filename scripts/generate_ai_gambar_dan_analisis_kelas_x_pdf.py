from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
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
    / "materi-kelas-x-ai-gambar-dan-analisis-visual.pdf"
)


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="TitleTeladan",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=21,
            leading=25,
            textColor=colors.HexColor("#16324F"),
            alignment=TA_CENTER,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SubtitleTeladan",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=11,
            leading=15,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#355C7D"),
            spaceAfter=12,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionTeladan",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            textColor=colors.white,
            backColor=colors.HexColor("#24577A"),
            borderPadding=(6, 8, 6),
            spaceBefore=10,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyTeladan",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=10.8,
            leading=15.4,
            textColor=colors.HexColor("#1F2933"),
            alignment=TA_JUSTIFY,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CalloutTeladan",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=10.8,
            leading=15,
            textColor=colors.HexColor("#16324F"),
            backColor=colors.HexColor("#EAF3F8"),
            borderPadding=(7, 9, 7),
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="TableCellTeladan",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.0,
            leading=11.0,
            textColor=colors.HexColor("#1F2933"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="TableHeadTeladan",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=9.3,
            leading=11.0,
            textColor=colors.white,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SmallTeladan",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.1,
            leading=12.2,
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
        wrapped_row = []
        for cell in row:
            style = head_style if row_index == 0 else cell_style
            wrapped_row.append(Paragraph(str(cell), style))
        wrapped.append(wrapped_row)
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
    story.append(Paragraph("Materi Kelas X: AI Gambar dan Analisis Visual", styles["TitleTeladan"]))
    story.append(
        Paragraph(
            "Pendalaman Gen-AI melalui pembuatan gambar, pembacaan gambar, use case akademik, dan etika visual",
            styles["SubtitleTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Halo teman-teman. Kalau pertemuan sebelumnya kita mengenal Gen-AI secara umum, pada sesi ini kita akan masuk ke cabang yang lebih spesifik: AI untuk membuat gambar dan AI untuk membaca gambar. Kalian akan melihat bahwa visual AI bisa sangat membantu belajar, tetapi juga punya risiko besar kalau dipakai tanpa tanggung jawab.",
            styles["CalloutTeladan"],
        )
    )

    story.append(Paragraph("1. Tujuan Pembelajaran", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "Kalian memahami perbedaan image generation dan image analysis.",
                "Kalian mengenali contoh tool AI yang bekerja dengan gambar.",
                "Kalian memahami penggunaan AI gambar yang bermanfaat untuk belajar.",
                "Kalian mengenali risiko manipulasi visual dan etika penggunaannya.",
                "Kalian mampu menyusun tugas kecil berbasis prompt atau analisis gambar secara bertanggung jawab.",
            ],
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("2. Dua Arah Penggunaan AI pada Gambar", styles["SectionTeladan"]))
    compare_table = Table(
        wrap_table(
            [
                ["Jenis", "Apa yang Dilakukan", "Contoh Sederhana"],
                ["Image Generation", "AI membuat gambar baru dari perintah teks atau contoh referensi.", "Membuat ilustrasi poster, gambar konsep, atau visual ide presentasi."],
                ["Image Analysis", "AI membaca, mendeskripsikan, atau mengenali isi gambar yang diberikan pengguna.", "Menjelaskan isi diagram, membaca objek di foto, atau membantu memahami gambar pembelajaran."],
            ],
            styles["TableHeadTeladan"],
            styles["TableCellTeladan"],
        ),
        colWidths=[3.1 * cm, 6.2 * cm, 6.8 * cm],
    )
    compare_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#24577A")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#B7C5D1")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#F9FBFC"), colors.HexColor("#EEF5F8")]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(compare_table)
    story.append(
        Paragraph(
            "Intinya, image generation membuat visual baru, sedangkan image analysis mencoba memahami visual yang sudah ada.",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("3. Contoh Tools yang Relevan", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "<b>ChatGPT</b> dapat dipakai untuk membantu menulis prompt gambar atau menganalisis gambar yang diunggah.",
                "<b>Gemini</b> dapat membantu menjelaskan isi gambar, memberi deskripsi visual, atau mendiskusikan makna gambar.",
                "<b>Image generators</b> seperti DALL-E dan tool sejenis dipakai untuk membuat ilustrasi baru dari teks.",
                "<b>Google Lens</b> lebih dekat ke analysis: mengenali objek, teks, atau informasi dari gambar dunia nyata.",
            ],
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("4. Use Case Akademik yang Baik", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "<b>Membuat ilustrasi konsep.</b> Misalnya visual rantai makanan, kota masa depan, atau poster literasi digital.",
                "<b>Membantu memahami diagram.</b> Siswa bisa meminta AI menjelaskan isi grafik, peta konsep, atau bagan sederhana.",
                "<b>Menyiapkan presentasi.</b> AI membantu membuat visual pendukung untuk slide, lalu siswa tetap menjelaskan dengan pemahamannya sendiri.",
                "<b>Latihan observasi.</b> Guru memberi satu gambar, lalu siswa membandingkan analisis mereka dengan analisis AI.",
                "<b>Belajar deskripsi visual.</b> Siswa belajar mengubah gambar menjadi narasi atau sebaliknya, sehingga melatih imajinasi dan komunikasi.",
            ],
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Di dunia akademik, AI visual paling sehat dipakai sebagai <b>alat bantu memahami dan mengomunikasikan ide</b>, bukan alat untuk memalsukan bukti atau mengganti kerja intelektual siswa.",
            styles["CalloutTeladan"],
        )
    )

    story.append(Paragraph("5. Praktik Singkat Menggunakan GPT", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "<b>Langkah 1: buka GPT dan tentukan tujuan.</b> Misalnya kalian ingin membuat ilustrasi untuk presentasi atau ingin menganalisis poster.",
                "<b>Langkah 2: tulis perintah yang jelas.</b> Sebutkan topik, level siswa, dan hasil yang kalian butuhkan.",
                "<b>Langkah 3: kalau perlu, unggah gambar.</b> Ini dipakai saat kalian ingin GPT membantu membaca atau menjelaskan gambar tertentu.",
                "<b>Langkah 4: baca hasilnya dengan kritis.</b> Jangan langsung percaya; cek apakah isinya sesuai konteks pelajaran.",
                "<b>Langkah 5: revisi prompt.</b> Kalau hasil terlalu umum, tambahkan detail, format jawaban, atau fokus analisis.",
                "<b>Langkah 6: simpan hasil penting dan catat bahwa AI dipakai sebagai bantuan.</b>",
            ],
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "<b>Contoh praktik generation:</b> “Buat ide ilustrasi poster edukatif tentang pemanasan global untuk siswa kelas X, warna cerah, dan mudah dipakai di slide.”",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "<b>Contoh praktik analysis:</b> “Saya unggah poster ini. Tolong jelaskan pesan utamanya, warna dominan, dan 3 alasan kenapa poster ini efektif untuk pelajar.”",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("6. Strategi Prompt untuk Image Generation", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "Tentukan <b>subjek</b> yang jelas: apa yang ingin dibuat?",
                "Tambahkan <b>konteks</b>: untuk poster kelas, ilustrasi presentasi, atau tugas seni?",
                "Jelaskan <b>gaya visual</b>: realistis, kartun, infografis, sketsa, atau flat illustration.",
                "Tentukan <b>detail penting</b>: warna dominan, suasana, jumlah objek, dan elemen yang harus muncul.",
                "Kalau hasil belum pas, lakukan <b>iterasi</b>: ubah prompt sedikit demi sedikit, jangan asal ulang total.",
            ],
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "<b>Contoh prompt yang baik:</b> “Buat ilustrasi flat style untuk siswa SMA tentang rantai makanan di ekosistem sawah, warna cerah, ada padi, belalang, katak, ular, dan elang, cocok untuk slide presentasi pendidikan.”",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "<b>Contoh prompt yang lemah:</b> “Buat gambar rantai makanan.” Prompt ini terlalu umum, sehingga hasilnya bisa tidak sesuai kebutuhan tugas.",
            styles["BodyTeladan"],
        )
    )

    story.append(PageBreak())

    story.append(Paragraph("7. Strategi Prompt untuk Image Analysis", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "Beritahu AI <b>apa yang ingin dianalisis</b>: objek, suasana, diagram, teks, atau makna umum.",
                "Kalau gambar dipakai untuk tugas sekolah, minta AI menjawab dengan <b>bahasa level siswa</b>.",
                "Mintalah format yang jelas: deskripsi singkat, poin-poin, atau penjelasan langkah demi langkah.",
                "Kalau gambar memuat data atau diagram, tetap cek ulang ke sumber asli, karena AI bisa salah membaca detail.",
            ],
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "<b>Contoh prompt analysis yang baik:</b> “Jelaskan isi diagram ini dalam 5 poin singkat untuk siswa kelas X, lalu sebutkan bagian mana yang paling penting untuk dipahami.”",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("8. Contoh Penggunaan yang Buruk", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "Membuat gambar palsu seolah-olah itu foto asli atau bukti kejadian nyata.",
                "Mengubah gambar orang lain tanpa izin lalu menyebarkannya.",
                "Memakai AI visual untuk tugas seni tanpa mengakui bantuan AI sama sekali.",
                "Mengunggah foto pribadi, wajah teman, atau dokumen sensitif tanpa persetujuan.",
                "Mengandalkan analisis AI sepenuhnya padahal gambar perlu dibaca dengan konteks manusia.",
            ],
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("9. Etika Visual dan Literasi Digital", styles["SectionTeladan"]))
    ethics_table = Table(
        wrap_table(
            [
                ["Prinsip", "Makna Sederhana"],
                ["Kejujuran", "Kalau visual dibuat atau dibantu AI, jangan menyamar seolah itu hasil murni manual atau foto nyata."],
                ["Privasi", "Jangan unggah wajah, dokumen, atau data sensitif tanpa izin."],
                ["Verifikasi", "Kalau visual dipakai sebagai informasi, cek apakah isinya akurat dan tidak menyesatkan."],
                ["Tanggung jawab", "Gunakan AI untuk mendukung belajar, bukan untuk memanipulasi, memfitnah, atau menipu."],
            ],
            styles["TableHeadTeladan"],
            styles["TableCellTeladan"],
        ),
        colWidths=[3.4 * cm, 11.8 * cm],
    )
    ethics_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#24577A")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#B7C5D1")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#F9FBFC"), colors.HexColor("#EEF5F8")]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(ethics_table)

    story.append(Paragraph("10. Tugas Kelompok", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "<b>Judul tugas:</b> AI Visual untuk Belajar secara Cerdas dan Etis",
            styles["BodyTeladan"],
        )
    )
    story.append(
        bullet_list(
            [
                "Pilih salah satu fokus: <b>image generation</b> atau <b>image analysis</b>.",
                "Kalau memilih image generation, buat 2 contoh prompt: satu yang baik dan satu yang terlalu umum.",
                "Kalau memilih image analysis, siapkan 1 gambar/diagram lalu tulis prompt analisis yang baik.",
                "Sertakan screenshot singkat langkah praktik menggunakan GPT.",
                "Jelaskan 2 manfaat AI visual untuk siswa.",
                "Jelaskan 2 risiko atau penyalahgunaan AI visual.",
                "Tulis 3 aturan etika yang menurut kelompok kalian paling penting.",
            ],
            styles["BodyTeladan"],
        )
    )
    task_table = Table(
        wrap_table(
            [
                ["Format Jawaban Kelompok", ""],
                ["Fokus yang dipilih", ""],
                ["Contoh prompt utama", ""],
                ["Manfaat akademik", ""],
                ["Risiko/penyalahgunaan", ""],
                ["Aturan etika kelompok", ""],
                ["Kesimpulan", ""],
            ],
            styles["TableHeadTeladan"],
            styles["TableCellTeladan"],
        ),
        colWidths=[6.0 * cm, 10.2 * cm],
        rowHeights=[0.76 * cm] * 7,
    )
    task_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#24577A")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#A9BAC7")),
                ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7FAFC")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(task_table)
    story.append(
        Paragraph(
            "<b>Pengumpulan tugas:</b> kirim hasil kelompok ke <link href=\"mailto:ataka.ahmad@gmail.com\" color=\"blue\">ataka.ahmad@gmail.com</link>.<br/><b>Format subject email:</b> <b>SMA Teladan X - Tugas AI Visual - [Nama Kelompok]</b><br/><b>Isi email singkat:</b> tulis nama anggota kelompok, lampirkan 1 lembar jawaban ringkas atau 1 slide sederhana, dan sertakan screenshot praktik GPT.",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("11. Penutup", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "Teman-teman, AI visual itu menarik karena hasilnya langsung terlihat. Tetapi justru karena visual sangat mudah memengaruhi orang, pemakaiannya harus lebih hati-hati. Kalian boleh memakai AI untuk membantu belajar dan berkarya, tetapi jangan sampai visual yang dibuat atau dianalisis AI dipakai untuk menipu, memalsukan, atau menggantikan tanggung jawab berpikir kalian sendiri.",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Pertanyaan refleksi akhir: <b>kalau gambar bisa dibuat atau dianalisis AI dengan sangat cepat, keterampilan manusia apa yang justru menjadi semakin penting?</b>",
            styles["CalloutTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Referensi ringkas materi ini disusun dari dokumentasi produk AI umum dan prinsip literasi digital visual untuk konteks pendidikan.",
            styles["SmallTeladan"],
        )
    )

    doc = SimpleDocTemplate(
        str(OUTPUT_PATH),
        pagesize=A4,
        leftMargin=1.7 * cm,
        rightMargin=1.7 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.7 * cm,
        title="Materi Kelas X AI Gambar dan Analisis Visual",
        author="OpenAI Codex",
    )
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    build_pdf()
