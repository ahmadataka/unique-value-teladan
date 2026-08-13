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
    / "materi-kelas-xi-smart-home-di-sekolah.pdf"
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
    story.append(Paragraph("Materi Kelas XI: Smart Home di Sekolah", styles["TitleTeladan"]))
    story.append(
        Paragraph(
            "Lanjutan dari materi IoT menuju sistem pintar yang lebih terintegrasi untuk sekolah dan greenhouse",
            styles["SubtitleTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Halo teman-teman. Pada pertemuan sebelumnya kalian sudah merancang ide IoT untuk sekolah atau greenhouse. Di materi kali ini, kita mulai dari ide kalian dulu, lalu kita lihat bagaimana ide-ide itu bisa berkembang menjadi <b>smart home</b> atau <b>smart school system</b> yang lebih utuh, lebih jelas manfaatnya, dan lebih siap dipresentasikan.",
            styles["CalloutTeladan"],
        )
    )

    story.append(Paragraph("1. Tujuan Pembelajaran", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "Kalian memahami hubungan antara IoT dan konsep smart home atau smart school.",
                "Kalian melihat contoh sistem pintar yang relevan untuk ruang kelas, keamanan, energi, dan greenhouse.",
                "Kalian mengenali produk atau inovasi nyata yang dapat menjadi referensi ide.",
                "Kalian memahami risiko dan etika penggunaan sistem otomatis di lingkungan sekolah.",
                "Kalian mampu menyempurnakan ide kelompok menjadi konsep smart school atau smart greenhouse yang lebih matang.",
            ],
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("2. Awal Sesi: Presentasi Singkat Ide Kelompok", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "Setiap kelompok mempresentasikan ide IoT sebelumnya secara singkat.",
                "Fokus presentasi: masalah yang ingin dibantu, sensor atau alat yang dipakai, manfaat utama, dan tantangan yang mungkin muncul.",
                "Setelah semua kelompok berbagi, kelas mencari pola umum: efisiensi energi, keamanan, kenyamanan, monitoring, dan keberlanjutan.",
            ],
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Bagian ini penting karena materi baru tidak dimulai dari nol. Kalian sudah punya benih idenya. Sekarang tugas kita adalah membuat ide itu menjadi sistem yang lebih terintegrasi dan lebih realistis.",
            styles["CalloutTeladan"],
        )
    )

    story.append(Paragraph("3. Dari IoT ke Smart Home atau Smart School", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "IoT biasanya berbicara tentang alat yang bisa membaca data, mengirim data, lalu membantu tindakan. Sementara itu, smart home atau smart school berbicara tentang <b>sistem</b>. Jadi bukan hanya satu sensor atau satu alat, tetapi gabungan beberapa komponen yang saling bekerja sama untuk membuat ruang menjadi lebih aman, lebih hemat, atau lebih nyaman.",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Kalimat kuncinya: <b>IoT adalah bahan penyusun, sedangkan smart system adalah hasil integrasinya.</b>",
            styles["CalloutTeladan"],
        )
    )

    story.append(Paragraph("4. Apa Itu Smart Home dan Smart School?", styles["SectionTeladan"]))
    compare_table = Table(
        wrap_table(
            [
                ["Konsep", "Makna Sederhana", "Contoh"],
                ["Smart Home", "Rumah yang memakai sensor, data, dan otomatisasi untuk membantu kenyamanan, keamanan, dan efisiensi.", "Lampu otomatis, termostat pintar, notifikasi pintu terbuka."],
                ["Smart School", "Lingkungan sekolah yang memakai sistem serupa untuk membantu belajar, operasional, dan pengelolaan fasilitas.", "Monitoring suhu kelas, akses ruang, penyiraman greenhouse otomatis."],
            ],
            styles["TableHeadTeladan"],
            styles["TableCellTeladan"],
        ),
        colWidths=[3.0 * cm, 7.2 * cm, 6.0 * cm],
    )
    compare_table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#24577A")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#B7C5D1")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#F9FBFC"), colors.HexColor("#EEF5F8")]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    story.append(compare_table)

    story.append(Paragraph("5. Komponen Utama Sistem Smart School", styles["SectionTeladan"]))
    comp_table = Table(
        wrap_table(
            [
                ["Komponen", "Peran", "Contoh di Sekolah"],
                ["Sensor", "Membaca kondisi lingkungan", "Suhu kelas, kelembapan tanah, gerak, pintu terbuka"],
                ["Controller", "Mengolah data dan menentukan aksi", "ESP32, Arduino, controller lain"],
                ["Koneksi", "Menghubungkan alat dan dashboard", "Wi-Fi, jaringan lokal"],
                ["Actuator", "Melakukan tindakan fisik", "Lampu, kipas, pompa air, buzzer"],
                ["Dashboard / Aplikasi", "Memantau data dan memberi perintah", "Panel monitoring, aplikasi ponsel, tampilan web"],
            ],
            styles["TableHeadTeladan"],
            styles["TableCellTeladan"],
        ),
        colWidths=[3.2 * cm, 5.8 * cm, 7.2 * cm],
    )
    comp_table.setStyle(
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
    story.append(comp_table)

    story.append(PageBreak())

    story.append(Paragraph("6. Use Case di Sekolah dan Greenhouse", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "<b>Ruang kelas:</b> lampu dan kipas otomatis untuk efisiensi energi dan kenyamanan belajar.",
                "<b>Keamanan ruang:</b> sensor pintu, gerak, atau notifikasi saat ada akses di luar jam tertentu.",
                "<b>Greenhouse sekolah:</b> monitoring suhu, kelembapan, dan penyiraman berbasis sensor tanah.",
                "<b>Pemantauan fasilitas:</b> data air, listrik, atau suhu ruangan dapat dicatat untuk evaluasi jangka panjang.",
                "<b>Presentasi ide siswa:</b> dashboard sederhana bisa membantu kelompok menjelaskan bagaimana sistem mereka bekerja.",
            ],
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("7. Produk dan Inovasi Nyata", styles["SectionTeladan"]))
    product_rows = [
        [
            "Google Nest Learning Thermostat",
            "Mengatur suhu secara lebih cerdas dan membantu efisiensi energi. Cocok untuk menjelaskan logika kontrol suhu otomatis.",
            '<link href="https://store.google.com/us/product/nest_learning_thermostat_4th_gen?hl=en-US" color="blue">Google Store</link>',
        ],
        [
            "Aqara Motion and Door Sensors",
            "Contoh sensor pintar untuk gerak, pintu, atau kondisi ruang. Relevan untuk keamanan dan otomasi sederhana.",
            '<link href="https://us.aqara.com/collections/smart-home-sensor" color="blue">Aqara Sensors</link>',
        ],
        [
            "Rachio Smart Sprinkler Controller",
            "Contoh sistem penyiraman pintar yang cocok dipakai sebagai referensi untuk greenhouse atau taman sekolah.",
            '<link href="https://rachio.com/products" color="blue">Rachio Products</link>',
        ],
        [
            "Arduino Greenhouse Kit / Explore IoT Kit",
            "Contoh kit pendidikan yang langsung menghubungkan sensor, data, dan aktuator untuk konteks pertanian pintar.",
            '<link href="https://www.arduino.cc/education/greenhouse/" color="blue">Arduino Greenhouse</link>',
        ],
    ]
    prod_table = Table(
        wrap_table(
            [["Produk", "Relevansi untuk Ideation", "Link"]] + product_rows,
            styles["TableHeadTeladan"],
            styles["TableCellTeladan"],
        ),
        colWidths=[4.2 * cm, 8.6 * cm, 3.0 * cm],
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
            "Yang perlu kalian lihat dari produk-produk itu bukan hanya nama mereknya, tetapi logika sistemnya: masalah apa yang dibantu, data apa yang dibaca, aksi apa yang dilakukan, dan apa manfaat nyatanya bagi pengguna.",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("8. Risiko dan Etika", styles["SectionTeladan"]))
    story.append(
        bullet_list(
            [
                "Jangan mengumpulkan data berlebihan jika tidak benar-benar dibutuhkan.",
                "Hindari sistem yang bisa merekam atau memantau orang tanpa persetujuan yang jelas.",
                "Perhatikan keamanan data dan akses perangkat, terutama jika sistem bisa membuka pintu atau mengaktifkan alat.",
                "Pikirkan juga skenario gagal: bagaimana jika sensor salah membaca atau koneksi terputus?",
                "Teknologi harus membantu manusia mengambil keputusan, bukan membuat pengguna berhenti berpikir.",
            ],
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("9. Tugas Kelompok Lanjutan", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "<b>Judul tugas:</b> Menyempurnakan Ide Menjadi Konsep Smart School atau Smart Greenhouse",
            styles["BodyTeladan"],
        )
    )
    story.append(
        bullet_list(
            [
                "Ambil kembali ide IoT kelompok kalian dari pertemuan sebelumnya.",
                "Pilih satu arah: <b>smart school</b> atau <b>smart greenhouse</b>.",
                "Perjelas masalah utama yang ingin diselesaikan.",
                "Tuliskan sensor, controller, koneksi, dashboard, dan actuator yang akan dipakai.",
                "Jelaskan alur kerja sistem dari membaca data sampai tindakan yang dilakukan.",
                "Pilih satu produk nyata sebagai referensi, lalu jelaskan apa yang bisa ditiru dan apa yang harus disesuaikan.",
                "Tuliskan 2 manfaat, 2 risiko, dan 3 prinsip etika penggunaan sistem tersebut.",
            ],
            styles["BodyTeladan"],
        )
    )
    task_table = Table(
        wrap_table(
            [
                ["Format Jawaban Kelompok", ""],
                ["Nama proyek", ""],
                ["Masalah yang dibantu", ""],
                ["Komponen sistem", ""],
                ["Alur kerja", ""],
                ["Produk referensi", ""],
                ["Manfaat", ""],
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
            "<b>Pengumpulan tugas:</b> kirim hasil kelompok ke <link href=\"mailto:ataka.ahmad@gmail.com\" color=\"blue\">ataka.ahmad@gmail.com</link>.<br/><b>Format subject email:</b> <b>SMA Teladan XI - Tugas Smart Home - [Nama Kelompok]</b><br/><b>Isi email singkat:</b> tulis nama anggota kelompok, lampirkan 1 lembar jawaban ringkas atau 1 slide sederhana, dan jika ada sketsa sistem atau diagram blok, sertakan juga.",
            styles["BodyTeladan"],
        )
    )

    story.append(Paragraph("10. Penutup", styles["SectionTeladan"]))
    story.append(
        Paragraph(
            "Teman-teman, smart technology yang baik bukan hanya yang bisa bekerja otomatis, tetapi yang benar-benar membantu kebutuhan nyata. Kalau kalian bisa melihat masalah di sekitar sekolah, menerjemahkannya menjadi sistem yang sederhana namun masuk akal, lalu memikirkan etikanya juga, itu sudah menunjukkan cara berpikir teknologi yang matang.",
            styles["BodyTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Pertanyaan refleksi akhir: <b>kalau satu sistem pintar sederhana benar-benar bisa dibangun di SMA Teladan, masalah apa yang paling layak dibantu lebih dulu?</b>",
            styles["CalloutTeladan"],
        )
    )
    story.append(
        Paragraph(
            "Sumber produk yang dibahas: Google Nest, Aqara, Rachio, dan Arduino Education.",
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
        title="Materi Kelas XI Smart Home di Sekolah",
        author="OpenAI Codex",
    )
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    build_pdf()
