from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import ListFlowable, ListItem, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


OUTPUT_PATH = Path("/Users/ahmadataka/Documents/Codex project/SMA Teladan/unique-value-teladan/pdf/materi-kelas-xi-skenario-uji-dan-validasi-iot.pdf")


def styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle(name="TitleT", parent=s["Title"], fontName="Helvetica-Bold", fontSize=21, leading=25, alignment=TA_CENTER, textColor=colors.HexColor("#16324F"), spaceAfter=8))
    s.add(ParagraphStyle(name="SubT", parent=s["Normal"], fontName="Helvetica", fontSize=11, leading=15, alignment=TA_CENTER, textColor=colors.HexColor("#355C7D"), spaceAfter=12))
    s.add(ParagraphStyle(name="SectionT", parent=s["Heading2"], fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=colors.white, backColor=colors.HexColor("#24577A"), borderPadding=(6, 8, 6), spaceBefore=10, spaceAfter=8))
    s.add(ParagraphStyle(name="BodyT", parent=s["BodyText"], fontName="Helvetica", fontSize=10.7, leading=15.2, textColor=colors.HexColor("#1F2933"), alignment=TA_JUSTIFY, spaceAfter=6))
    s.add(ParagraphStyle(name="CallT", parent=s["BodyText"], fontName="Helvetica-Bold", fontSize=10.6, leading=14.8, textColor=colors.HexColor("#16324F"), backColor=colors.HexColor("#EAF3F8"), borderPadding=(7, 9, 7), spaceAfter=10))
    s.add(ParagraphStyle(name="CellT", parent=s["BodyText"], fontName="Helvetica", fontSize=8.8, leading=10.7, textColor=colors.HexColor("#1F2933")))
    s.add(ParagraphStyle(name="HeadT", parent=s["BodyText"], fontName="Helvetica-Bold", fontSize=9, leading=10.7, textColor=colors.white))
    s.add(ParagraphStyle(name="DiagramT", parent=s["BodyText"], fontName="Helvetica-Bold", fontSize=8.6, leading=10.1, alignment=TA_CENTER, textColor=colors.HexColor("#16324F")))
    return s


def bullets(values, style):
    return ListFlowable([ListItem(Paragraph(value, style), leftIndent=6) for value in values], bulletType="bullet", start="circle", leftIndent=16, bulletFontName="Helvetica", bulletFontSize=10, bulletOffsetY=2)


def table(rows, widths, s):
    data = [[Paragraph(str(cell), s["HeadT"] if row == 0 else s["CellT"]) for cell in values] for row, values in enumerate(rows)]
    result = Table(data, colWidths=widths, repeatRows=1)
    result.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#24577A")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), .5, colors.HexColor("#B7C5D1")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F1F7FA")]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return result


def flow(s):
    items = [("Kondisi", "apa yang sedang terjadi", "#DDEEF5"), ("Input", "data apa yang terbaca", "#E5F2E7"), ("Aturan", "keputusan sistem", "#FFF1D6"), ("Output", "aksi atau notifikasi", "#FDE6E1"), ("Manusia", "cek dan tindak lanjut", "#EDE7F6")]
    cells = []
    for index, (title, detail, _) in enumerate(items):
        cells.append(Paragraph(f"{title}<br/><font name='Helvetica'>{detail}</font>", s["DiagramT"]))
        if index < len(items) - 1:
            cells.append(Paragraph("&rarr;", s["DiagramT"]))
    result = Table([cells], colWidths=[2.65*cm, .35*cm, 2.65*cm, .35*cm, 2.65*cm, .35*cm, 2.65*cm, .35*cm, 2.65*cm])
    cmds = [("ALIGN", (0, 0), (-1, -1), "CENTER"), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3), ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]
    for index, (_, _, color) in enumerate(items):
        column = index * 2
        cmds.extend([("BACKGROUND", (column, 0), (column, 0), colors.HexColor(color)), ("BOX", (column, 0), (column, 0), .6, colors.HexColor("#5593B8"))])
    result.setStyle(TableStyle(cmds))
    return result


def footer(canvas, doc):
    canvas.saveState(); canvas.setFont("Helvetica", 9); canvas.setFillColor(colors.HexColor("#5B6770")); canvas.drawRightString(A4[0] - 1.7*cm, 1.2*cm, f"Halaman {doc.page}"); canvas.restoreState()


def build_pdf():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    s = styles()
    story = [Spacer(1, .6*cm), Paragraph("Materi Kelas XI: Skenario Uji dan Validasi IoT", s["TitleT"]), Paragraph("Menguji logika solusi sebelum alat dan komponen tersedia", s["SubT"])]
    story.append(Paragraph("Halo teman-teman. RAB kalian sudah selesai, tetapi alat belum tersedia. Itu bukan alasan untuk berhenti. Sebelum merakit, engineer justru perlu memastikan bahwa sistemnya masuk akal: kapan alat bekerja, data apa yang dibaca, apa tindakan sistem, dan apa yang harus dilakukan manusia jika terjadi kesalahan. Hari ini kita melakukan <b>simulasi uji tanpa alat</b>.", s["CallT"]))

    story.append(Paragraph("1. Tujuan Pembelajaran", s["SectionT"]))
    story.append(bullets([
        "Kalian dapat membedakan rencana uji logika dengan uji alat fisik.",
        "Kalian dapat menyusun skenario kondisi normal, kondisi batas, dan kondisi gagal untuk ide IoT.",
        "Kalian dapat memerankan alur data, keputusan sistem, output, dan tindakan manusia tanpa memakai komponen fisik.",
        "Kalian dapat menggunakan hasil simulasi untuk memperbaiki desain, RAB, atau aturan penggunaan sistem.",
    ], s["BodyT"]))

    story.append(Paragraph("2. Apa yang Diuji Jika Alat Belum Ada?", s["SectionT"]))
    story.append(Paragraph("Kita belum dapat membuktikan apakah sensor benar-benar akurat atau pompa benar-benar menyala. Namun, kita sudah dapat menguji <b>logika dan pengalaman penggunaan</b>: apakah aturan sistem jelas, apakah pengguna memahami notifikasi, apakah sistem punya batas aman, dan apa yang terjadi ketika data tidak masuk akal.", s["BodyT"]))
    story.append(table([
        ["Belum dapat diuji", "Sudah dapat divalidasi sekarang"],
        ["Nilai sensor aktual, ketahanan kabel, kecepatan pompa, atau konsumsi daya nyata.", "Apakah sensor yang dipilih relevan dengan masalah dan apakah alur data-keputusan-aksi masuk akal."],
        ["Kecocokan fisik komponen saat dirakit.", "Apakah kebutuhan komponen pada RAB sudah lengkap atau masih ada yang terlewat."],
        ["Keandalan alat setelah digunakan lama.", "Apa yang terjadi jika data hilang, salah, terlambat, atau pengguna tidak merespons notifikasi."],
        ["Efektivitas di lingkungan sebenarnya.", "Apakah solusi membantu pengguna dalam skenario yang realistis dan tidak menciptakan risiko baru."],
    ], [8.1*cm, 8.1*cm], s))
    story.append(Paragraph("Simulasi bukan pura-pura tanpa manfaat. Simulasi membantu kelompok menemukan asumsi yang keliru sebelum waktu dan biaya dipakai untuk merakit.", s["CallT"]))

    story.append(Paragraph("3. Format Skenario Uji", s["SectionT"]))
    story.append(flow(s))
    story.append(Spacer(1, 6))
    story.append(Paragraph("Setiap skenario harus menjawab: kondisi apa yang terjadi, data apa yang seharusnya diterima, keputusan apa yang diambil sistem, output apa yang muncul, dan apa tindakan manusia selanjutnya.", s["CallT"]))

    story.append(PageBreak())
    story.append(Paragraph("4. Contoh Simulasi: Smart Greenhouse", s["SectionT"]))
    story.append(table([
        ["Skenario", "Alur yang disimulasikan", "Keputusan desain"],
        ["Tanah terlalu kering", "Sensor membaca nilai di bawah ambang -> sistem memberi notifikasi -> siswa memeriksa tanaman -> penyiraman dilakukan sesuai aturan.", "Notifikasi tidak boleh langsung dianggap sebagai keputusan final tanpa pemeriksaan."],
        ["Tanah cukup lembap", "Sensor membaca nilai aman -> sistem tidak memberi notifikasi -> siswa melanjutkan pemantauan rutin.", "Sistem harus mencegah pompa menyala tanpa alasan."],
        ["Data sensor tidak masuk akal", "Sensor mengirim nilai berubah ekstrem -> sistem memberi tanda data perlu dicek -> siswa memeriksa sensor/kabel.", "Sistem perlu kondisi aman, bukan langsung menyiram berlebihan."],
        ["Air habis atau pompa bermasalah", "Sistem memberi notifikasi tetapi aksi fisik tidak dapat dilakukan -> siswa/guru melakukan langkah manual.", "RAB dan desain perlu mencantumkan kontrol manual serta prosedur perawatan."],
    ], [3.5*cm, 7.0*cm, 5.7*cm], s))
    story.append(Paragraph("Pada simulasi, anggota kelompok dapat memegang kartu peran: 'sensor', 'microcontroller', 'notifikasi', 'pompa', dan 'pengguna'. Bacakan kondisi awal, lalu jalankan alur sesuai aturan yang telah ditulis.", s["CallT"]))

    story.append(Paragraph("5. Empat Jenis Skenario yang Wajib Ada", s["SectionT"]))
    story.append(table([
        ["Jenis", "Pertanyaan panduan", "Contoh"],
        ["Normal", "Apa yang terjadi saat kondisi sesuai harapan?", "Tanah kering terbaca, notifikasi muncul, pengguna memeriksa."],
        ["Batas", "Apa yang terjadi saat data mendekati ambang keputusan?", "Nilai kelembapan sedikit di atas/bawah ambang; apakah aturan masih masuk akal?"],
        ["Gagal", "Apa yang terjadi saat data, koneksi, atau output tidak bekerja?", "Sensor putus, internet mati, atau pompa tidak dapat dijalankan."],
        ["Etika / pengguna", "Apa dampaknya jika pengguna salah memahami atau data digunakan berlebihan?", "Notifikasi membuat siswa panik atau data aktivitas pengguna dilihat pihak yang tidak perlu."],
    ], [3.3*cm, 6.0*cm, 6.9*cm], s))
    story.append(Paragraph("Jangan hanya membuat kondisi ideal. Teknologi yang bertanggung jawab juga harus memiliki respons saat sesuatu tidak berjalan sesuai rencana.", s["CallT"]))

    story.append(Paragraph("6. Tugas Kelompok: IoT Test Scenario and Validation Sheet", s["SectionT"]))
    story.append(Paragraph("Gunakan ide dan RAB kelompok kalian. Buat satu lembar skenario uji berbasis simulasi. Tidak perlu membeli, merakit, atau meminjam komponen. Kalian boleh memakai kartu, diagram, post-it, atau slide untuk menjalankan alur sistem bersama.", s["BodyT"]))
    story.append(table([
        ["Bagian hasil", "Isi minimum"],
        ["Ringkasan sistem", "Masalah, pengguna, fungsi utama, serta diagram input -> proses -> output -> manusia."],
        ["Aturan sistem", "Tulis aturan sederhana berbentuk 'jika ... maka ...' untuk fungsi inti."],
        ["Empat skenario", "Satu normal, satu batas, satu gagal, dan satu etika/pengguna."],
        ["Kartu peran atau visual", "Tunjukkan siapa/apa yang berperan sebagai sensor, sistem, output, dan pengguna."],
        ["Hasil simulasi", "Untuk tiap skenario, tulis hasil yang diharapkan, masalah yang ditemukan, dan perbaikan desain."],
        ["Dampak pada RAB", "Apakah ada komponen, biaya perlindungan, atau kebutuhan perawatan yang perlu ditambah/diubah?"],
        ["Refleksi", "Apa asumsi kelompok yang berubah setelah melakukan simulasi?"],
    ], [4.5*cm, 11.7*cm], s))
    story.append(Paragraph("Bentuk hasil: 3-5 slide atau satu PDF. Sertakan foto sketsa, kartu peran, atau diagram simulasi bila ada. Yang dinilai adalah kelogisan alur, keberanian menguji kondisi gagal, serta kualitas perbaikan desain.", s["CallT"]))

    story.append(Paragraph("7. Pengumpulan", s["SectionT"]))
    story.append(Paragraph("Kirim hasil kelompok ke <link href='mailto:ataka.ahmad@gmail.com' color='#1D5F85'><u>ataka.ahmad@gmail.com</u></link>.<br/><b>Subject email:</b> SMA Teladan XI - IoT Test Scenario dan Validation Sheet - [Nama Kelompok]<br/>Sertakan nama anggota, file hasil, serta foto simulasi/sketsa bila ada.", s["CallT"]))
    story.append(Paragraph("Penutup: sebelum alat dibuat, desain harus sudah mampu menjawab pertanyaan penting. Jika simulasi menunjukkan aturan belum aman atau alur belum jelas, kelompok telah menemukan hal berharga untuk diperbaiki sebelum biaya dan komponen digunakan.", s["CallT"]))

    doc = SimpleDocTemplate(str(OUTPUT_PATH), pagesize=A4, leftMargin=1.7*cm, rightMargin=1.7*cm, topMargin=1.5*cm, bottomMargin=1.7*cm, title="Materi Kelas XI Skenario Uji dan Validasi IoT", author="SMA Teladan")
    doc.build(story, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    build_pdf()
    print(f"Created {OUTPUT_PATH}")
