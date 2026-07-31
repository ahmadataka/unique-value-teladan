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
    / "materi-kelas-x-gen-ai-dan-penggunaan-bijak.pdf"
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
            leading=15.5,
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
    story.append(Paragraph("Materi Kelas X: Mengenal Gen-AI", styles["TitleTeladan"]))
    story.append(
        Paragraph(
            "Contoh tools, strategi prompting, use case akademik yang baik, contoh penggunaan buruk, dan etika pemakaiannya",
            styles["SubtitleTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Halo teman-teman. Di materi ini kita tidak hanya akan membahas apa itu <i>Generative AI</i>, tetapi juga bagaimana memakainya dengan cara yang benar. Kalian akan melihat contoh tool yang sedang populer, contoh penggunaan yang membantu belajar, contoh penggunaan yang buruk, dan sikap etis yang perlu dijaga saat memakai Gen-AI.",
            styles["CalloutTeladan"],
        )
    )

    story.append(Paragraph("1. Tujuan Pembelajaran", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "Kalian memahami arti dasar Gen-AI dengan bahasa sederhana.",
                "Kalian mengenali beberapa tool Gen-AI yang sering dipakai siswa dan guru.",
                "Kalian memahami contoh penggunaan Gen-AI yang baik untuk belajar.",
                "Kalian mengenali strategi <i>prompting</i> agar hasil AI lebih berguna.",
                "Kalian memahami contoh penggunaan yang buruk dan etika pemakaiannya.",
            ],
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("2. Apa Itu Gen-AI?", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "<i>Generative AI</i> adalah jenis AI yang dapat menghasilkan konten baru berdasarkan pola dari data yang pernah dipelajarinya. Konten itu bisa berupa teks, gambar, suara, video, atau kode. Jadi, jika AI biasa sering dipakai untuk mengenali atau mengelompokkan, Gen-AI dipakai untuk <b>membuat</b> sesuatu yang baru.",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Namun, Gen-AI tidak benar-benar berpikir seperti manusia. Ia bekerja dengan pola dan prediksi. Karena itu, hasilnya bisa cepat dan berguna, tetapi tetap bisa salah, bias, atau tidak sesuai konteks.",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("3. Contoh Tools Gen-AI", styles["SectionTeladan"]))
    tools_table = Table(
        wrap_table(
            [
                ["Tool", "Kegunaan Sederhana", "Link"],
                ["ChatGPT", "Membantu brainstorming, menjelaskan konsep, merangkum, dan menyusun draft.", "https://chatgpt.com/"],
                ["Gemini", "Membantu ide, ringkasan, tanya jawab, dan beberapa integrasi dengan layanan Google.", "https://gemini.google.com/app?hl=id"],
                ["Microsoft Copilot", "Membantu menulis, merangkum, dan bekerja dengan dokumen atau tugas berbasis Microsoft.", "https://copilot.microsoft.com/"],
            ],
            styles["TableHeadTeladan"],
            styles["TableCellTeladan"],
        ),
        colWidths=[3.0 * cm, 8.9 * cm, 4.0 * cm],
    )
    tools_table.setStyle(
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
    story.append(tools_table)
    story.append(
        Paragraph(
            "Kalian tidak harus memakai semua tool itu. Yang penting adalah memahami bahwa tiap tool punya kekuatan, keterbatasan, dan konteks penggunaan masing-masing.",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("4. Use Case Akademik yang Baik", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "<b>Meminta penjelasan ulang konsep.</b> Misalnya: \"Jelaskan Revolusi Industri 4.0 dengan bahasa siswa kelas X.\"",
                "<b>Menyusun ringkasan dari catatan sendiri.</b> Bukan menyalin penuh dari AI, tetapi memakai AI untuk merapikan poin yang sudah kalian buat.",
                "<b>Membuat pertanyaan latihan.</b> Misalnya AI diminta membuat 5 soal pilihan ganda dari topik yang sedang dipelajari.",
                "<b>Membantu membuat kerangka presentasi.</b> Misalnya outline 3 slide untuk topik tertentu.",
                "<b>Membantu memperbaiki tulisan.</b> Misalnya mengecek struktur, kejelasan, atau pilihan kata dalam esai yang kalian tulis sendiri.",
            ],
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Kunci dari semua contoh yang baik itu adalah: <b>AI membantu proses belajar</b>, bukan menggantikan proses berpikir kalian.",
            styles["CalloutTeladan"],
        )
    )

    story.append(Paragraph("5. Strategi Prompting yang Sederhana", styles["SectionTeladan"]))
    prompt_table = Table(
        wrap_table(
            [
                ["Langkah", "Pertanyaan yang Bisa Kalian Pakai"],
                ["1. Tentukan tujuan", "Saya ingin AI membantu untuk apa: menjelaskan, merangkum, memberi contoh, atau membuat latihan?"],
                ["2. Beri konteks", "Topiknya apa, level siswa berapa, dan gaya bahasa seperti apa yang saya butuhkan?"],
                ["3. Tentukan format hasil", "Apakah saya ingin poin-poin, tabel, contoh soal, atau paragraf singkat?"],
                ["4. Minta revisi", "Kalau jawabannya terlalu sulit, terlalu panjang, atau kurang jelas, minta AI memperbaikinya."],
            ],
            styles["TableHeadTeladan"],
            styles["TableCellTeladan"],
        ),
        colWidths=[3.2 * cm, 12.1 * cm],
    )
    prompt_table.setStyle(
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
    story.append(prompt_table)
    story.append(
        Paragraph(
            "<b>Contoh prompt yang lebih baik:</b> \"Jelaskan fotosintesis untuk siswa kelas X dalam 5 poin singkat, lalu buat 3 pertanyaan latihan beserta jawabannya.\"",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "<b>Contoh prompt yang kurang efektif:</b> \"Jelaskan fotosintesis.\" Prompt ini terlalu umum, jadi hasilnya bisa terlalu panjang atau tidak sesuai kebutuhan.",
            styles["BodyTeladan"],
        )
    )

    story.append(PageBreak())

    story.append(Paragraph("6. Contoh Penggunaan yang Buruk", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "Menyalin jawaban AI mentah-mentah lalu mengumpulkannya sebagai tugas pribadi.",
                "Meminta AI mengerjakan seluruh esai tanpa kalian pahami isinya.",
                "Memakai AI untuk mencontek saat kuis atau ujian.",
                "Memasukkan data pribadi, foto sensitif, atau dokumen penting tanpa izin.",
                "Menganggap jawaban AI pasti benar tanpa memeriksa ulang.",
            ],
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Kalau AI dipakai seperti itu, yang rusak bukan hanya kualitas belajar, tetapi juga kejujuran akademik dan tanggung jawab pribadi.",
            styles["CalloutTeladan"],
        )
    )

    story.append(Paragraph("7. Etika Penggunaan Gen-AI", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "<b>Jujur.</b> Jika AI membantu pekerjaan kalian, jangan berpura-pura semua itu murni hasil tanpa bantuan.",
                "<b>Verifikasi.</b> Cek kembali fakta penting dari guru, buku, atau sumber tepercaya.",
                "<b>Jaga privasi.</b> Jangan membagikan data pribadi, nilai, password, atau dokumen sensitif.",
                "<b>Gunakan untuk belajar.</b> Tujuannya adalah membantu kalian memahami, bukan mematikan usaha berpikir.",
                "<b>Hormati karya orang lain.</b> Jangan memakai AI untuk plagiarisme atau mengambil karya tanpa tanggung jawab.",
            ],
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("8. Sumber Belajar Tambahan", styles["SectionTeladan"]))
    story.append(
        link_paragraph(
            "OpenAI Help Center - What is ChatGPT?",
            "https://help.openai.com/en/articles/12677804-what-is-chatgpt-faq",
            styles["BodyTeladan"],
        )
    )
    story.append(
        link_paragraph(
            "Google Gemini Help - Learn about generative AI",
            "https://support.google.com/gemini/answer/13954172?hl=id",
            styles["BodyTeladan"],
        )
    )
    story.append(
        link_paragraph(
            "Microsoft AI - What is generative AI?",
            "https://www.microsoft.com/id-id/ai/ai-101/what-is-generative-ai",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("9. Penugasan Kelompok", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "<b>Judul tugas:</b> Menilai Penggunaan Gen-AI yang Cerdas dan Etis",
            styles["BodyTeladan"],
        )
    )
    story.append(
        bullet_list(
            [
                "Pilih satu tool Gen-AI, misalnya ChatGPT, Gemini, atau Copilot.",
                "Jelaskan fungsi sederhananya.",
                "Berikan 2 contoh penggunaan yang baik untuk pelajar.",
                "Berikan 2 contoh penggunaan yang buruk atau tidak etis.",
                "Tuliskan 3 aturan penggunaan Gen-AI yang menurut kelompok kalian penting di sekolah.",
                "Sertakan 2 contoh prompt: satu prompt yang baik dan satu prompt yang terlalu umum atau buruk.",
            ],
            styles["BodyTeladan"],
        )
    )
    task_data = [
        ["Format Jawaban Kelompok", ""],
        ["Nama tool", ""],
        ["Contoh penggunaan yang baik", ""],
        ["Contoh penggunaan yang buruk", ""],
        ["Contoh prompt yang baik", ""],
        ["Contoh prompt yang buruk", ""],
        ["Aturan etika kelompok", ""],
        ["Kesimpulan", ""],
    ]
    task_table = Table(
        wrap_table(task_data, styles["TableHeadTeladan"], styles["TableCellTeladan"]),
        colWidths=[6.4 * cm, 9.8 * cm],
        rowHeights=[0.72 * cm] * len(task_data),
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
            "<b>Pengumpulan tugas:</b> kirim hasil kelompok ke <link href=\"mailto:ataka.ahmad@gmail.com\" color=\"blue\">ataka.ahmad@gmail.com</link>.<br/><b>Format subject email:</b> <b>SMA Teladan X - Tugas Gen-AI - [Nama Kelompok]</b><br/><b>Isi email singkat:</b> tulis nama anggota kelompok dan lampirkan 1 lembar jawaban ringkas atau 1 slide sederhana.",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("10. Penutup", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "Teman-teman, Gen-AI adalah teknologi yang kuat. Ia bisa membantu belajar, menulis, merangkum, dan mencari ide. Tetapi justru karena kuat, penggunaannya harus disertai kejujuran, kebiasaan memeriksa ulang, dan tanggung jawab etis. Teknologi yang baik bukan yang membuat kalian berhenti berpikir, tetapi yang membantu kalian berpikir lebih baik.",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Pertanyaan refleksi akhir: <b>kalau kalian memakai Gen-AI untuk belajar setiap hari, aturan apa yang harus kalian pegang supaya AI membantu pertumbuhan kalian, bukan menggantikan usaha kalian?</b>",
            styles["CalloutTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Referensi ringkas materi ini diverifikasi pada Jumat, 31 Juli 2026 dari laman resmi OpenAI, Google, dan Microsoft.",
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
        title="Materi Kelas X Mengenal Gen-AI",
        author="OpenAI Codex",
    )
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    build_pdf()
