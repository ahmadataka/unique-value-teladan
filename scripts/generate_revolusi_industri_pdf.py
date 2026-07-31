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
    / "materi-pengantar-revolusi-industri-4-kelas-x.pdf"
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
        [
            ListItem(Paragraph(item, style), leftIndent=6)
            for item in items
        ],
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
            text = str(cell)
            style = head_style if row_index == 0 else cell_style
            wrapped_row.append(Paragraph(text, style))
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
    story.append(Paragraph("Materi Kelas X: Pengantar Revolusi Industri 4.0", styles["TitleTeladan"]))
    story.append(
        Paragraph(
            "Sesi sekitar 60 menit - dirancang dengan bahasa yang menyapa siswa dan mudah dipakai langsung di kelas",
            styles["SubtitleTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Halo teman-teman. Hari ini kita akan membahas bagaimana dunia berubah dari kerja manual menjadi dunia yang serba digital. Kalian akan melihat bahwa Revolusi Industri 4.0 bukan sesuatu yang jauh dari kehidupan kalian, karena sebenarnya kalian sudah hidup di dalamnya setiap hari.",
            styles["CalloutTeladan"],
        )
    )

    story.append(Paragraph("1. Tujuan Pembelajaran", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "Kalian memahami arti revolusi industri dengan bahasa sederhana.",
                "Kalian mengenali perbedaan Revolusi Industri 1.0, 2.0, 3.0, dan 4.0.",
                "Kalian dapat memberi contoh teknologi Revolusi Industri 4.0 dalam kehidupan sehari-hari.",
                "Kalian mulai berpikir kritis tentang manfaat dan risiko perkembangan teknologi.",
            ],
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("2. Pembuka Kelas", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "Sebelum mulai, coba pikirkan: sejak bangun pagi sampai masuk kelas, teknologi apa saja yang sudah kalian pakai? Mungkin alarm di ponsel, chat, maps, video pendek, pembayaran digital, atau bahkan AI. Dari pertanyaan sederhana ini kita bisa melihat bahwa teknologi sudah menempel pada hidup kita.",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "<b>Pancingan guru:</b> \"Kalau internet mati sehari penuh, kegiatan kalian apa saja yang langsung terganggu?\"",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("3. Materi Inti", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "Revolusi industri adalah perubahan besar dalam cara manusia bekerja, memproduksi barang, dan menjalani hidup. Perubahan ini tidak terjadi sekali, tetapi bertahap. Setiap tahap ditandai oleh teknologi baru yang membuat hidup manusia berubah dengan cepat.",
            styles["BodyTeladan"],
        )
    )

    story.append(
        bullet_list(
            [
                "<b>Revolusi Industri 1.0 - mesin uap.</b> Pada tahap ini, pekerjaan manual mulai dibantu mesin. Contohnya kereta uap dan mesin tenun.",
                "<b>Revolusi Industri 2.0 - listrik.</b> Produksi menjadi lebih cepat, lebih besar, dan lebih massal. Contohnya pabrik modern, lampu listrik, dan produksi mobil.",
                "<b>Revolusi Industri 3.0 - komputer dan otomatisasi.</b> Mesin mulai dikendalikan sistem digital. Contohnya ATM, komputer kasir, dan robot pabrik.",
                "<b>Revolusi Industri 4.0 - internet, data, dan AI.</b> Mesin, manusia, dan data saling terhubung. Contohnya e-commerce, ojek online, perangkat pintar, dan AI.",
            ],
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Jadi, kalau kalian bertanya \"Apa yang khas dari Revolusi Industri 4.0?\", jawabannya adalah <b>keterhubungan</b>. Bukan hanya mesin yang canggih, tetapi mesin, manusia, internet, dan data saling terkoneksi.",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "<b>Contoh dekat dengan kalian:</b> saat kalian memesan makanan lewat aplikasi, sistem membaca lokasi, menghubungkan pembeli, penjual, dan pengantar, lalu memproses pembayaran digital. Itu contoh nyata dunia 4.0.",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("4. Teknologi Kunci Revolusi Industri 4.0", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "<b>Internet of Things (IoT)</b> - benda bisa saling mengirim data, misalnya smartwatch atau sensor suhu.",
                "<b>Artificial Intelligence (AI)</b> - komputer bisa membantu menganalisis, memberi saran, atau menghasilkan jawaban.",
                "<b>Big Data</b> - data dalam jumlah sangat besar dipakai untuk membaca pola dan mengambil keputusan.",
                "<b>Cloud Computing</b> - penyimpanan dan pemrosesan data dilakukan lewat internet.",
                "<b>Automation and Robotics</b> - pekerjaan tertentu dapat dibantu atau digantikan mesin otomatis.",
            ],
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("5. Dampak Positif dan Tantangan", styles["SectionTeladan"]))
    impact_data = [
        ["Dampak Positif", "Tantangan yang Perlu Diwaspadai"],
        [
            "Pekerjaan lebih cepat dan efisien",
            "Ketergantungan pada gawai dan internet",
        ],
        [
            "Akses informasi dan belajar jadi lebih mudah",
            "Hoaks, misinformasi, dan bias algoritma",
        ],
        [
            "Komunikasi dan kolaborasi lintas tempat",
            "Privasi data dan keamanan digital",
        ],
        [
            "Muncul pekerjaan dan peluang baru",
            "Beberapa pekerjaan lama berkurang",
        ],
    ]
    impact_table = Table(
        wrap_table(impact_data, styles["TableHeadTeladan"], styles["TableCellTeladan"]),
        colWidths=[8.1 * cm, 8.1 * cm],
    )
    impact_table.setStyle(
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
    story.append(impact_table)
    story.append(
        Paragraph(
            "Artinya, kita tidak cukup hanya menjadi pengguna teknologi. Kalian juga perlu menjadi pengguna yang <b>cerdas, kritis, dan bertanggung jawab</b>.",
            styles["BodyTeladan"],
        )
    )

    story.append(PageBreak())

    story.append(Paragraph("6. Rekomendasi Video Pengantar", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "Supaya pembuka materi terasa lebih hidup, kalian bisa menonton salah satu video berikut sebagai pemantik. Saat menonton, coba tangkap ide besarnya, lalu pikirkan contohnya dalam kehidupan kalian sendiri.",
            styles["BodyTeladan"],
        )
    )
    story.append(link_paragraph("CNBC Indonesia - Apa Itu Revolusi Industri 4.0?", "https://www.youtube.com/watch?v=XENMOfD-mLs", styles["BodyTeladan"]))
    story.append(link_paragraph("OVIS UI - Revolusi Industri 4.0 #1: Definisi, Ciri, dan Perjalanannya", "https://www.youtube.com/watch?v=bpH4eezD1Vg", styles["BodyTeladan"]))
    story.append(link_paragraph("OVIS UI - Revolusi Industri 4.0 #2: Perubahan yang Terjadi", "https://www.youtube.com/watch?v=PTe1EWq3b6U", styles["BodyTeladan"]))
    story.append(
        Paragraph(
            "Saat menonton, coba jawab dalam hati: <b>teknologi apa yang paling terasa dekat dengan kehidupan saya, dan mengapa teknologi itu penting?</b>",
            styles["CalloutTeladan"],
        )
    )

    story.append(Paragraph("7. Diskusi Singkat Setelah Video", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "Apa perbedaan hidup manusia sebelum dan sesudah teknologi digital berkembang cepat?",
                "Teknologi apa yang paling membantu kalian belajar?",
                "Apakah semua perkembangan teknologi selalu baik? Mengapa?",
                "Kalau AI makin canggih, keterampilan manusia apa yang tetap penting?",
            ],
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("8. Penugasan Kelompok", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "<b>Judul tugas:</b> Teknologi Revolusi Industri 4.0 di Sekitar Kita",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Sekarang giliran kalian. Bekerjalah dalam kelompok berisi 4-5 siswa. Pilih satu teknologi yang sering kalian lihat atau pakai dalam kehidupan sehari-hari. Kalian boleh memilih ojek online, e-wallet, AI chatbot, smartwatch, e-commerce, Google Maps, smart home, atau contoh lain yang relevan.",
            styles["BodyTeladan"],
        )
    )
    story.append(
        bullet_list(
            [
                "Jelaskan teknologi yang kalian pilih dan untuk apa teknologi itu dipakai.",
                "Terangkan mengapa teknologi itu termasuk bagian dari Revolusi Industri 4.0.",
                "Sebutkan minimal 2 manfaat teknologi itu bagi pelajar atau masyarakat.",
                "Sebutkan minimal 2 risiko jika teknologi itu dipakai tanpa bijak.",
                "Berikan 1 saran penggunaan yang cerdas dan bertanggung jawab.",
            ],
            styles["BodyTeladan"],
        )
    )

    task_data = [
        ["Format Jawaban Kelompok", ""],
        ["Nama teknologi", ""],
        ["Cara kerja sederhananya", ""],
        ["Mengapa termasuk Revolusi Industri 4.0", ""],
        ["Manfaat", ""],
        ["Risiko", ""],
        ["Saran penggunaan bijak", ""],
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
            "<b>Pengumpulan tugas:</b> kirim hasil kelompok ke <link href=\"mailto:ataka.ahmad@gmail.com\" color=\"blue\">ataka.ahmad@gmail.com</link>.<br/><b>Format subject email:</b> <b>SMA Teladan X - Tugas Revolusi Industri 4.0 - [Nama Kelompok]</b><br/><b>Isi email singkat:</b> tulis nama anggota kelompok dan lampirkan 1 lembar jawaban ringkas atau 1 slide sederhana.",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("9. Penutup", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "Teman-teman, Revolusi Industri 4.0 bukan hanya tentang mesin canggih. Intinya adalah bagaimana teknologi, data, dan manusia saling terhubung. Karena itu, masa depan tidak hanya membutuhkan orang yang bisa memakai teknologi, tetapi juga orang yang bisa berpikir, bekerja sama, dan mengambil keputusan dengan bijak. Kalian tidak harus menjadi ahli teknologi hari ini, tetapi kalian perlu mulai memahami dunia yang sedang kalian masuki.",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Pertanyaan refleksi akhir: <b>dari semua teknologi yang kalian kenal, mana yang paling membantu hidup manusia, dan mana yang paling perlu diawasi penggunaannya?</b>",
            styles["CalloutTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Catatan: materi ini disusun untuk sesi pengantar sekitar 1 jam bagi siswa kelas X.",
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
        title="Materi Pengantar Revolusi Industri 4.0 Kelas X",
        author="OpenAI Codex",
    )
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    build_pdf()
