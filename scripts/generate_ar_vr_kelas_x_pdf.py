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
    / "materi-kelas-x-ar-vr-untuk-pendidikan.pdf"
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
            fontSize=9.1,
            leading=11.2,
            textColor=colors.HexColor("#1F2933"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="TableHeadTeladan",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=9.4,
            leading=11.1,
            textColor=colors.white,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SmallTeladan",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.2,
            leading=12.4,
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
    story.append(Paragraph("Materi Kelas X: AR/VR untuk Pendidikan", styles["TitleTeladan"]))
    story.append(
        Paragraph(
            "Lanjutan dari AI visual menuju pengalaman belajar yang lebih imersif, interaktif, dan tetap etis",
            styles["SubtitleTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Halo teman-teman. Kalau pada pertemuan sebelumnya kalian belajar memakai AI untuk membuat dan membaca gambar, sekarang kita melangkah lebih jauh: bagaimana kalau visual itu tidak hanya dilihat, tetapi terasa hadir di depan kita? Di sesi ini, kita akan mengenal <b>Augmented Reality (AR)</b> dan <b>Virtual Reality (VR)</b> sebagai teknologi yang bisa membantu belajar dengan cara yang lebih konkret dan menarik.",
            styles["CalloutTeladan"],
        )
    )

    story.append(Paragraph("1. Tujuan Pembelajaran", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "Kalian memahami perbedaan dasar antara AR dan VR dengan bahasa sederhana.",
                "Kalian melihat bagaimana AR/VR dapat dipakai untuk membantu pelajaran di sekolah.",
                "Kalian mengenali contoh produk atau inovasi nyata yang memakai AR/VR.",
                "Kalian memahami manfaat, keterbatasan, dan etika penggunaan teknologi imersif.",
                "Kalian mampu merancang ide pembelajaran berbasis AR/VR sebagai lanjutan dari tugas AI visual sebelumnya.",
            ],
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("2. Jembatan dari Materi Sebelumnya", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "Kemarin kalian berlatih memakai AI visual untuk membuat gambar atau membaca isi visual. Itu sudah bagus sebagai langkah awal. Tetapi dalam pembelajaran, kadang kita tidak cukup hanya melihat gambar datar. Ada materi yang lebih mudah dipahami ketika siswa bisa melihat objek 3D, menaruh model digital di meja, atau masuk ke simulasi lingkungan tertentu. Di situlah AR dan VR menjadi menarik.",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Kalimat kuncinya: <b>dari visual statis menuju pengalaman visual yang lebih hidup dan interaktif.</b>",
            styles["CalloutTeladan"],
        )
    )

    story.append(Paragraph("3. Apa Itu AR dan VR?", styles["SectionTeladan"]))
    compare_table = Table(
        wrap_table(
            [
                ["Teknologi", "Makna Sederhana", "Contoh Pengalaman"],
                ["AR", "Dunia nyata tetap terlihat, lalu diberi tambahan objek atau informasi digital.", "Melihat model organ 3D muncul lewat kamera ponsel di atas meja."],
                ["VR", "Pengguna masuk ke lingkungan digital buatan komputer dan fokus pada ruang virtual itu.", "Tur virtual museum, simulasi laboratorium, atau eksplorasi ruang angkasa."],
            ],
            styles["TableHeadTeladan"],
            styles["TableCellTeladan"],
        ),
        colWidths=[2.2 * cm, 6.0 * cm, 8.0 * cm],
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

    story.append(Paragraph("4. Mengapa AR/VR Menarik untuk Belajar?", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "Membantu konsep abstrak menjadi lebih konkret, misalnya struktur sel, molekul, atau tata surya.",
                "Memberi pengalaman simulasi yang aman ketika praktik langsung sulit, mahal, atau berisiko.",
                "Meningkatkan rasa ingin tahu karena siswa merasa lebih dekat dengan materi.",
                "Membantu presentasi ide proyek agar orang lain lebih mudah membayangkan hasilnya.",
                "Mendorong diskusi kelompok karena siswa tidak hanya membaca, tetapi juga mengamati dan menafsirkan pengalaman visual.",
            ],
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("5. Contoh Penggunaan Akademik", styles["SectionTeladan"]))
    use_table = Table(
        wrap_table(
            [
                ["Mata Pelajaran", "Ide Penggunaan"],
                ["Biologi", "Melihat model organ, sistem tubuh, atau bagian sel dalam bentuk 3D."],
                ["Fisika", "Simulasi tata surya, medan gaya, atau gerak benda dalam ruang virtual."],
                ["Sejarah", "Tur virtual ke museum, situs budaya, atau rekonstruksi ruang bersejarah."],
                ["Geografi", "Melihat bentuk permukaan bumi, gunung api, atau tata ruang kota secara visual."],
                ["Presentasi Proyek", "Menampilkan rancangan produk, poster interaktif, atau model ruang dalam format AR."],
            ],
            styles["TableHeadTeladan"],
            styles["TableCellTeladan"],
        ),
        colWidths=[4.0 * cm, 12.2 * cm],
    )
    use_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#24577A")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#B7C5D1")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F4F8FB")]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    story.append(use_table)

    story.append(PageBreak())

    story.append(Paragraph("6. Produk dan Inovasi Nyata", styles["SectionTeladan"]))
    product_rows = [
        [
            "Assemblr EDU",
            "Platform 3D/AR yang membantu guru dan siswa membuat atau memakai materi pembelajaran interaktif. Relevan karena dekat dengan konteks pendidikan Indonesia dan bisa diakses lewat gadget sehari-hari.",
            '<link href="https://about.edu.assemblrworld.com/id" color="blue">https://about.edu.assemblrworld.com/id</link>',
        ],
        [
            "Merge Cube",
            "Alat berbentuk kubus yang memungkinkan siswa melihat dan memanipulasi objek digital 3D melalui perangkat. Sangat cocok untuk sains dan STEM.",
            '<link href="https://support.mergeedu.com/hc/en-us/articles/360052933552-Get-a-Merge-Cube" color="blue">https://support.mergeedu.com/hc/en-us/articles/360052933552-Get-a-Merge-Cube</link>',
        ],
        [
            "ClassVR",
            "Solusi VR untuk sekolah yang menyediakan headset, konten pembelajaran, dan kontrol kelas. Menunjukkan bahwa VR bisa dirancang khusus untuk pendidikan, bukan hanya untuk gim.",
            '<link href="https://www.classvr.com/us/" color="blue">https://www.classvr.com/us/</link>',
        ],
        [
            "Google Arts & Culture",
            "Platform yang menyediakan tur virtual museum, situs budaya, dan pengalaman 360 derajat. Cocok untuk sejarah, seni, dan budaya.",
            '<link href="https://artsandculture.google.com/project/virtual-tours" color="blue">https://artsandculture.google.com/project/virtual-tours</link>',
        ],
    ]
    prod_table = Table(
        wrap_table(
            [["Produk", "Apa yang Bisa Dipelajari", "Link"]] + product_rows,
            styles["TableHeadTeladan"],
            styles["TableCellTeladan"],
        ),
        colWidths=[3.2 * cm, 8.4 * cm, 4.6 * cm],
    )
    prod_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#24577A")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#B7C5D1")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#F9FBFC"), colors.HexColor("#EEF5F8")]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ]
        )
    )
    story.append(prod_table)
    story.append(
        Paragraph(
            "Dari contoh-contoh itu, kita bisa belajar bahwa teknologi imersif tidak harus selalu mahal atau sangat rumit. Yang penting adalah apakah pengalaman itu benar-benar membantu siswa memahami materi.",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("7. Manfaat dan Batasannya", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "<b>Manfaat:</b> lebih menarik, lebih konkret, dan bisa membantu visualisasi konsep yang sulit dibayangkan.",
                "<b>Batasan:</b> butuh perangkat, koneksi, dan kadang tidak semua sekolah punya fasilitas lengkap.",
                "<b>Risiko:</b> siswa bisa terlalu fokus pada efek wow dan lupa pada tujuan belajarnya.",
                "<b>Catatan penting:</b> teknologi yang tampak keren belum tentu otomatis efektif untuk pembelajaran.",
            ],
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("8. Etika Penggunaan AR/VR", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "Jangan memakai visual manipulatif untuk menipu atau membuat informasi palsu terlihat meyakinkan.",
                "Hormati privasi saat memakai kamera, terutama pada aktivitas AR yang memindai ruang sekitar.",
                "Pastikan konten yang dipakai tetap akurat dan relevan dengan pelajaran.",
                "Perhatikan kesehatan dan kenyamanan pengguna, misalnya jika ada yang mudah pusing atau lelah mata.",
                "Gunakan teknologi untuk membantu berpikir, bukan menggantikan usaha memahami materi.",
            ],
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("9. Pertanyaan Kritis untuk Siswa", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "Saat melihat teknologi AR/VR, jangan langsung bertanya “keren atau tidak?”. Coba ubah pertanyaannya menjadi: <b>apakah teknologi ini membantu belajar lebih jelas, lebih aman, atau lebih aktif?</b> Kalau jawabannya tidak, mungkin teknologinya belum dipakai pada tempat yang tepat.",
            styles["CalloutTeladan"],
        )
    )

    story.append(Paragraph("10. Tugas Kelompok", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "<b>Judul tugas:</b> Dari AI Visual ke AR/VR: Merancang Pembelajaran yang Lebih Interaktif",
            styles["BodyTeladan"],
        )
    )
    story.append(
        bullet_list(
            [
                "Pilih satu topik pelajaran yang menurut kelompok kalian cocok dibuat lebih imersif.",
                "Tentukan apakah ide kalian lebih cocok memakai <b>AR</b> atau <b>VR</b>.",
                "Sambungkan dengan tugas sebelumnya: boleh gunakan gambar, mockup, atau ide visual yang sudah pernah kalian buat.",
                "Jelaskan bagaimana siswa akan memakai teknologi itu saat belajar.",
                "Tuliskan 2 manfaat akademik, 2 risiko, dan 3 aturan etika yang perlu dijaga.",
                "Pilih satu produk nyata sebagai referensi, lalu jelaskan apa yang bisa ditiru dan apa yang perlu disesuaikan untuk konteks sekolah.",
            ],
            styles["BodyTeladan"],
        )
    )
    task_table = Table(
        wrap_table(
            [
                ["Format Jawaban Kelompok", ""],
                ["Topik pelajaran", ""],
                ["AR atau VR", ""],
                ["Alur penggunaan di kelas", ""],
                ["Produk referensi", ""],
                ["Manfaat akademik", ""],
                ["Risiko dan etika", ""],
                ["Kesimpulan", ""],
            ],
            styles["TableHeadTeladan"],
            styles["TableCellTeladan"],
        ),
        colWidths=[6.0 * cm, 10.2 * cm],
    )
    task_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#24577A")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#A9BAC7")),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTNAME", (0, 1), (0, -1), "Helvetica-Bold"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7FAFC")]),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    story.append(task_table)
    story.append(
        Paragraph(
            "<b>Pengumpulan tugas:</b> kirim hasil kelompok ke <link href=\"mailto:ataka.ahmad@gmail.com\" color=\"blue\">ataka.ahmad@gmail.com</link>.<br/><b>Format subject email:</b> <b>SMA Teladan X - Tugas AR VR - [Nama Kelompok]</b><br/><b>Isi email singkat:</b> tulis nama anggota kelompok dan lampirkan 1 lembar jawaban ringkas atau 1 slide sederhana. Jika ada mockup visual, lampirkan juga.",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("11. Penutup", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "Teman-teman, AR dan VR bukan hanya teknologi yang terlihat modern. Nilai utamanya ada pada kemampuannya membantu kita memahami sesuatu yang tadinya jauh, abstrak, atau sulit dibayangkan. Kalau kalian bisa memakai teknologi ini dengan kritis, kreatif, dan bertanggung jawab, maka teknologi benar-benar menjadi alat belajar yang kuat.",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Pertanyaan refleksi akhir: <b>kalau satu materi pelajaran di sekolah kalian bisa dibuat lebih hidup lewat AR atau VR, materi apa yang paling layak dipilih dan mengapa?</b>",
            styles["CalloutTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Sumber produk yang dibahas: Assemblr EDU, Merge EDU, ClassVR, dan Google Arts & Culture.",
            styles["SmallTeladan"],
        )
    )

    doc = SimpleDocTemplate(
        str(OUTPUT_PATH),
        pagesize=A4,
        leftMargin=1.7 * cm,
        rightMargin=1.7 * cm,
        topMargin=1.4 * cm,
        bottomMargin=1.6 * cm,
        title="Materi Kelas X AR VR untuk Pendidikan",
        author="OpenAI Codex",
    )
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    build_pdf()
