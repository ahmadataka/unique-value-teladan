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
    Path("/Users/ahmadataka/Documents/Codex project/SMA Teladan/unique-value-teladan/pdf")
    / "materi-kelas-xi-smart-technology-dan-iot.pdf"
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
    story.append(Paragraph("Materi Kelas XI: Smart Technology dan IoT", styles["TitleTeladan"]))
    story.append(
        Paragraph(
            "Pengantar Internet of Things untuk ide penerapan di sekolah dan greenhouse",
            styles["SubtitleTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Halo teman-teman. Di sekitar kita, banyak teknologi yang terlihat sederhana tetapi sebenarnya bekerja secara cerdas: lampu otomatis, sensor suhu, notifikasi jarak jauh, sampai sistem penyiraman tanaman yang bisa dikendalikan dari ponsel. Pada sesi ini, kita akan mengenal konsep <b>Internet of Things (IoT)</b> dan membayangkan bagaimana teknologi itu bisa dipakai di sekolah maupun greenhouse.",
            styles["CalloutTeladan"],
        )
    )

    story.append(Paragraph("1. Tujuan Pembelajaran", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "Kalian memahami pengertian dasar IoT dengan bahasa yang sederhana.",
                "Kalian mengenali komponen utama dalam sistem IoT.",
                "Kalian memahami contoh penerapan smart technology di sekolah dan greenhouse.",
                "Kalian mampu merancang ide IoT sederhana yang relevan dengan lingkungan SMA Teladan.",
                "Kalian mengenali manfaat, risiko, dan etika penggunaan teknologi terhubung.",
            ],
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("2. Apa Itu IoT?", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "<b>Internet of Things</b> adalah konsep ketika benda fisik seperti sensor, lampu, pompa air, kipas, atau alat ukur dapat mengirim data dan menerima perintah melalui jaringan. Jadi, yang terhubung ke internet bukan hanya laptop atau ponsel, tetapi juga benda-benda yang membantu aktivitas sehari-hari.",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Kalimat kuncinya: <b>IoT membuat benda bisa merasakan kondisi, mengirim informasi, lalu membantu manusia mengambil tindakan lebih cepat.</b>",
            styles["CalloutTeladan"],
        )
    )

    story.append(Paragraph("3. Komponen Dasar IoT", styles["SectionTeladan"]))
    comp_table = Table(
        wrap_table(
            [
                ["Komponen", "Peran Sederhana", "Contoh"],
                ["Sensor", "Membaca kondisi lingkungan", "Sensor suhu, kelembapan tanah, cahaya, gerak"],
                ["Controller", "Mengolah data dan menjalankan logika", "Arduino, ESP32, microcontroller lain"],
                ["Koneksi", "Mengirim data atau menerima perintah", "Wi-Fi, Bluetooth, internet lokal"],
                ["Actuator", "Menjalankan aksi fisik", "Pompa air, relay lampu, kipas, buzzer"],
                ["Dashboard / Aplikasi", "Menampilkan data dan memberi kontrol", "Ponsel, web, panel monitoring"],
            ],
            styles["TableHeadTeladan"],
            styles["TableCellTeladan"],
        ),
        colWidths=[3.3 * cm, 6.0 * cm, 6.8 * cm],
    )
    comp_table.setStyle(
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
    story.append(comp_table)

    story.append(Paragraph("4. Bagaimana IoT Bekerja?", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "<b>Langkah 1:</b> sensor membaca kondisi, misalnya tanah kering atau suhu terlalu panas.",
                "<b>Langkah 2:</b> controller memproses data dan membandingkannya dengan aturan sistem.",
                "<b>Langkah 3:</b> sistem mengirim data ke aplikasi atau dashboard.",
                "<b>Langkah 4:</b> kalau perlu, actuator bekerja, misalnya menyalakan kipas atau pompa air.",
                "<b>Langkah 5:</b> manusia memantau dan memperbaiki sistem bila perlu.",
            ],
            styles["BodyTeladan"],
        )
    )
    story.append(Paragraph("5. Contoh Smart Technology di Sekolah", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "<b>Lampu otomatis.</b> Lampu koridor atau ruang tertentu menyala hanya saat dibutuhkan.",
                "<b>Monitoring suhu kelas.</b> Sekolah bisa memantau ruang yang terlalu panas dan mencari solusi ventilasi.",
                "<b>Sistem kehadiran atau akses ruangan.</b> Bisa dikaitkan dengan kartu atau sensor tertentu.",
                "<b>Pemantauan penggunaan listrik.</b> Sekolah dapat belajar menghemat energi melalui data nyata.",
                "<b>Notifikasi keamanan.</b> Sensor pintu atau gerak bisa mengirim peringatan ketika ada kondisi tidak biasa.",
            ],
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Poin pentingnya bukan sekadar alat terlihat canggih, tetapi apakah teknologi itu benar-benar membantu kenyamanan, keamanan, dan efisiensi sekolah.",
            styles["CalloutTeladan"],
        )
    )

    story.append(Paragraph("6. Contoh Smart Technology di Greenhouse atau Farming", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "<b>Sensor kelembapan tanah.</b> Memberi tahu kapan tanaman perlu disiram.",
                "<b>Monitoring suhu dan kelembapan udara.</b> Membantu menjaga lingkungan tumbuh yang stabil.",
                "<b>Penyiraman otomatis.</b> Pompa air bekerja saat kondisi tanah terlalu kering.",
                "<b>Pemantauan cahaya.</b> Berguna untuk melihat apakah tanaman mendapat intensitas cahaya yang cukup.",
                "<b>Dashboard pertumbuhan.</b> Data harian bisa dipakai sebagai bahan belajar, bukan hanya operasional.",
            ],
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("7. Ide Proyek IoT untuk SMA Teladan", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "Sistem monitoring suhu dan kelembapan greenhouse sekolah.",
                "Sistem penyiraman otomatis sederhana berbasis sensor kelembapan tanah.",
                "Lampu otomatis hemat energi untuk area tertentu di sekolah.",
                "Dashboard pemantauan lingkungan kelas atau taman sekolah.",
                "Alarm sederhana saat ada kondisi lingkungan yang melewati batas aman.",
            ],
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Kalau proyek IoT dibuat di sekolah, maka hasil terbaiknya bukan hanya alatnya hidup, tetapi datanya bisa dibaca, fungsinya jelas, dan manfaatnya terasa.",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("8. Risiko dan Etika Penggunaan IoT", styles["SectionTeladan"]))
    ethics_table = Table(
        wrap_table(
            [
                ["Prinsip", "Makna Sederhana"],
                ["Keamanan", "Perangkat yang terhubung harus dijaga agar tidak mudah diakses sembarang orang."],
                ["Privasi", "Kalau sistem menyentuh data orang, penggunaannya harus jelas dan bertanggung jawab."],
                ["Keandalan", "Sensor bisa salah baca, sehingga manusia tetap harus memeriksa hasil."],
                ["Tujuan yang jelas", "Teknologi dipakai untuk membantu, bukan sekadar terlihat modern."],
            ],
            styles["TableHeadTeladan"],
            styles["TableCellTeladan"],
        ),
        colWidths=[3.5 * cm, 11.7 * cm],
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

    story.append(Paragraph("9. Tugas Kelompok", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "<b>Judul tugas:</b> Merancang Ide IoT untuk Sekolah atau Greenhouse",
            styles["BodyTeladan"],
        )
    )
    story.append(
        bullet_list(
            [
                "Pilih satu konteks: <b>sekolah</b> atau <b>greenhouse/farming</b>.",
                "Tentukan masalah yang ingin dibantu oleh teknologi.",
                "Sebutkan sensor, controller, koneksi, dan actuator yang mungkin dipakai.",
                "Jelaskan alur kerjanya dari membaca data sampai tindakan yang dilakukan sistem.",
                "Tuliskan 2 manfaat dan 2 risiko dari ide tersebut.",
                "Sertakan sketsa sederhana atau diagram alur buatan kelompok.",
            ],
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "<b>Pengumpulan tugas:</b> kirim hasil kelompok ke <link href=\"mailto:ataka.ahmad@gmail.com\" color=\"blue\">ataka.ahmad@gmail.com</link>.<br/><b>Format subject email:</b> <b>SMA Teladan XI - Tugas IoT - [Nama Kelompok]</b>",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("10. Penutup", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "Teman-teman, IoT bukan hanya soal alat yang bisa tersambung ke internet. Yang jauh lebih penting adalah bagaimana teknologi itu membantu menyelesaikan masalah nyata. Kalau kalian bisa melihat kebutuhan di sekitar sekolah atau greenhouse, lalu menerjemahkannya menjadi sistem yang sederhana tetapi berguna, itu sudah menunjukkan cara berpikir teknologi yang kuat.",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Pertanyaan refleksi akhir: <b>kalau kalian diberi kesempatan membuat satu sistem IoT sederhana untuk SMA Teladan, masalah apa yang paling ingin kalian bantu selesaikan?</b>",
            styles["CalloutTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Materi ini disusun sebagai pengantar konsep smart technology dan IoT untuk konteks pembelajaran sekolah.",
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
        title="Materi Kelas XI Smart Technology dan IoT",
        author="OpenAI Codex",
    )
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    build_pdf()
