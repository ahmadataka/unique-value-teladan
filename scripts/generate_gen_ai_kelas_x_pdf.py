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
    Path("/Users/ahmadataka/Documents/SMA Teladan/output/pdf")
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
            fontSize=11,
            leading=16,
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
            fontSize=11,
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
            fontSize=9.3,
            leading=11.4,
            textColor=colors.HexColor("#1F2933"),
        )
    )
    styles.add(
        ParagraphStyle(
            name="TableHeadTeladan",
            parent=styles["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=9.6,
            leading=11.5,
            textColor=colors.white,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SmallTeladan",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=13,
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
            "Pengantar tentang AI generatif, contoh dekat dengan siswa, dan cara menggunakannya dengan bijak",
            styles["SubtitleTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Halo teman-teman. Setelah mengenal perubahan dunia pada Revolusi Industri 4.0, sekarang kita masuk ke salah satu teknologi yang sedang sangat sering dibicarakan: <i>Generative AI</i> atau Gen-AI. Teknologi ini bisa membantu manusia membuat teks, gambar, suara, bahkan ide. Karena itu, penting bagi kalian untuk mengenalnya dengan kepala yang terbuka dan sikap yang kritis.",
            styles["CalloutTeladan"],
        )
    )

    story.append(Paragraph("1. Tujuan Pembelajaran", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "Kalian memahami arti dasar <i>Generative AI</i> dengan bahasa sederhana.",
                "Kalian bisa membedakan AI biasa dan AI yang bersifat generatif.",
                "Kalian mengenali contoh penggunaan Gen-AI dalam belajar dan kehidupan sehari-hari.",
                "Kalian memahami manfaat, risiko, dan batasan Gen-AI.",
                "Kalian mulai membangun kebiasaan memakai teknologi secara jujur, cerdas, dan bertanggung jawab.",
            ],
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("2. Pembuka Kelas", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "Coba pikirkan: pernahkah kalian melihat AI yang bisa menjawab pertanyaan, menulis paragraf, membuat gambar dari perintah teks, atau merangkum catatan? Kalau iya, kalian sudah bersentuhan dengan Gen-AI. Teknologi ini terasa dekat karena hasilnya bisa langsung kita lihat dan pakai.",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "<b>Pancingan guru:</b> \"Kalau ada AI yang bisa membantu belajar, menurut kalian bantuan seperti apa yang paling berguna: menjelaskan materi, merangkum, membuat gambar, atau memberi ide?\"",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("3. Apa Itu Gen-AI?", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "<i>Generative AI</i> adalah jenis AI yang dapat menghasilkan konten baru berdasarkan pola dari data yang pernah dipelajarinya. Konten itu bisa berupa teks, gambar, suara, video, atau kode. Jadi, jika AI biasa sering dipakai untuk mengenali atau mengelompokkan, Gen-AI dipakai untuk <b>membuat</b> sesuatu yang baru.",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Contohnya, ketika kalian mengetik pertanyaan lalu AI menjawab dengan paragraf, atau ketika seseorang menulis perintah lalu AI membuat gambar sesuai deskripsi, itu adalah contoh kerja Gen-AI.",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Namun, penting diingat: Gen-AI tidak benar-benar \"mengerti\" seperti manusia. Ia bekerja dengan pola, prediksi, dan kemungkinan kata atau bentuk yang paling sesuai. Karena itu, hasilnya bisa membantu, tetapi tidak selalu benar.",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("4. Contoh Gen-AI yang Dekat dengan Siswa", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "AI yang membantu menjelaskan materi pelajaran dengan bahasa yang lebih sederhana.",
                "AI yang merangkum artikel atau catatan menjadi poin-poin penting.",
                "AI pembuat gambar dari deskripsi teks.",
                "AI yang membantu membuat ide judul, poster, atau presentasi.",
                "AI yang membantu menyusun contoh kode sederhana atau langkah pemecahan masalah.",
            ],
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "<b>Contoh dekat dengan kelas:</b> ketika kalian bingung dengan satu topik, Gen-AI bisa dipakai untuk meminta penjelasan ulang dengan gaya yang lebih mudah dipahami. Tetapi, kalian tetap perlu mengecek apakah penjelasan itu sesuai dengan materi dari guru dan buku pelajaran.",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("5. Manfaat dan Risiko Gen-AI", styles["SectionTeladan"]))
    benefit_risk_data = [
        ["Manfaat", "Risiko yang Perlu Diwaspadai"],
        ["Membantu mencari ide awal", "Jawaban bisa salah atau meyakinkan padahal keliru"],
        ["Membantu merangkum dan menjelaskan materi", "Siswa bisa menjadi terlalu bergantung"],
        ["Membantu membuat visual atau draft awal", "Ada risiko plagiarisme atau menyalin mentah-mentah"],
        ["Mempercepat pekerjaan tertentu", "Data pribadi atau tugas sensitif bisa tidak aman jika dibagikan sembarangan"],
    ]
    benefit_risk_table = Table(
        wrap_table(benefit_risk_data, styles["TableHeadTeladan"], styles["TableCellTeladan"]),
        colWidths=[8.1 * cm, 8.1 * cm],
    )
    benefit_risk_table.setStyle(
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
    story.append(benefit_risk_table)
    story.append(
        Paragraph(
            "Karena itu, Gen-AI paling baik dipakai sebagai <b>alat bantu berpikir</b>, bukan pengganti akal, kejujuran, atau usaha belajar kalian sendiri.",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("6. Cara Memakai Gen-AI dengan Bijak", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "Gunakan untuk membantu memahami, bukan untuk mencontek mentah-mentah.",
                "Selalu cek ulang fakta penting dari buku, guru, atau sumber tepercaya.",
                "Jangan masukkan data pribadi, kata sandi, atau informasi sensitif.",
                "Kalau memakai hasil AI untuk tugas, olah kembali dengan pemahaman dan bahasa kalian sendiri.",
                "Anggap AI sebagai alat diskusi awal, bukan sumber kebenaran terakhir.",
            ],
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Sikap yang paling penting adalah <b>jujur</b>. Teknologi boleh membantu, tetapi pemahaman tetap harus tumbuh dari kalian sendiri.",
            styles["CalloutTeladan"],
        )
    )

    story.append(PageBreak())

    story.append(Paragraph("7. Sumber Belajar Tambahan", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "Kalau kalian ingin membaca atau menonton penjelasan tambahan, berikut beberapa sumber yang mudah dibuka dan cocok untuk pengantar topik ini.",
            styles["BodyTeladan"],
        )
    )
    story.append(
        link_paragraph(
            "Google - Mempelajari AI generatif",
            "https://support.google.com/gemini/answer/13954172?hl=id",
            styles["BodyTeladan"],
        )
    )
    story.append(
        link_paragraph(
            "Microsoft AI - Apa itu AI generatif?",
            "https://www.microsoft.com/id-id/ai/ai-101/what-is-generative-ai",
            styles["BodyTeladan"],
        )
    )
    story.append(
        link_paragraph(
            "DW Indonesia - Apa Itu Generative AI?",
            "https://www.dw.com/id/apa-itu-generative-ai/video-66557921",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("8. Diskusi Singkat di Kelas", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "Apa bagian paling menarik dari Gen-AI menurut kalian?",
                "Kalau Gen-AI bisa membantu belajar, bantuan apa yang paling bermanfaat?",
                "Kapan penggunaan AI menjadi tidak jujur dalam tugas sekolah?",
                "Kalau jawaban AI terdengar meyakinkan, mengapa kita tetap perlu memeriksanya?",
            ],
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("9. Penugasan Kelompok", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "<b>Judul tugas:</b> Memakai Gen-AI untuk Belajar dengan Cerdas dan Bertanggung Jawab",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Bekerjalah dalam kelompok berisi 4-5 siswa. Pilih satu contoh penggunaan Gen-AI yang menurut kalian berguna untuk pelajar. Kalian boleh memilih AI untuk merangkum, menjelaskan materi, membuat gambar, mencari ide presentasi, atau contoh lain yang relevan.",
            styles["BodyTeladan"],
        )
    )
    story.append(
        bullet_list(
            [
                "Jelaskan alat atau penggunaan Gen-AI yang kalian pilih.",
                "Terangkan bagaimana alat itu bisa membantu pelajar.",
                "Sebutkan minimal 2 manfaat jika dipakai dengan benar.",
                "Sebutkan minimal 2 risiko jika dipakai tanpa bijak.",
                "Tuliskan aturan penggunaan yang jujur dan bertanggung jawab di sekolah.",
            ],
            styles["BodyTeladan"],
        )
    )

    task_data = [
        ["Format Jawaban Kelompok", ""],
        ["Contoh penggunaan Gen-AI", ""],
        ["Manfaat untuk pelajar", ""],
        ["Risiko yang perlu diwaspadai", ""],
        ["Aturan penggunaan yang bijak", ""],
        ["Kesimpulan kelompok", ""],
    ]
    task_table = Table(
        wrap_table(task_data, styles["TableHeadTeladan"], styles["TableCellTeladan"]),
        colWidths=[6.6 * cm, 9.6 * cm],
        rowHeights=[0.8 * cm] * len(task_data),
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
    story.append(Spacer(1, 0.25 * cm))
    story.append(
        Paragraph(
            "<b>Pengumpulan tugas:</b> kirim hasil kelompok ke <link href=\"mailto:ataka.ahmad@gmail.com\" color=\"blue\">ataka.ahmad@gmail.com</link>.<br/><b>Format subject email:</b> <b>SMA Teladan X - Tugas Gen-AI - [Nama Kelompok]</b><br/><b>Isi email singkat:</b> tulis nama anggota kelompok dan lampirkan 1 lembar jawaban ringkas atau 1 slide sederhana.",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("10. Penutup", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "Teman-teman, Gen-AI adalah teknologi yang kuat. Ia bisa membantu manusia belajar, berkarya, dan bekerja lebih cepat. Tetapi justru karena kuat, penggunaannya perlu sikap yang matang. Masa depan tidak hanya membutuhkan orang yang bisa memakai AI, tetapi juga orang yang tetap jujur, kritis, dan bertanggung jawab saat memakainya.",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Pertanyaan refleksi akhir: <b>kalau kalian diberi akses ke Gen-AI setiap hari untuk belajar, kebiasaan apa yang harus dijaga supaya AI membantu kalian bertumbuh, bukan membuat kalian malas berpikir?</b>",
            styles["CalloutTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Catatan: materi ini disusun sebagai lanjutan kelas X setelah pengantar Revolusi Industri 4.0.",
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
