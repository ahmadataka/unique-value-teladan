from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import ListFlowable, ListItem, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path("/Users/ahmadataka/Documents/Codex project/SMA Teladan/unique-value-teladan/pdf")


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


def p(text, style):
    return Paragraph(text, style)


def bullets(values, style):
    return ListFlowable([ListItem(p(value, style), leftIndent=6) for value in values], bulletType="bullet", start="circle", leftIndent=16, bulletFontName="Helvetica", bulletFontSize=10, bulletOffsetY=2)


def table(rows, widths, s):
    data = [[p(str(cell), s["HeadT"] if r == 0 else s["CellT"]) for cell in row] for r, row in enumerate(rows)]
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


def footer(canvas, doc):
    canvas.saveState(); canvas.setFont("Helvetica", 9); canvas.setFillColor(colors.HexColor("#5B6770")); canvas.drawRightString(A4[0] - 1.7 * cm, 1.2 * cm, f"Halaman {doc.page}"); canvas.restoreState()


def boxes(items, s):
    cells = []
    for index, (title, detail, color) in enumerate(items):
        cells.append(p(f"{title}<br/><font name='Helvetica'>{detail}</font>", s["DiagramT"]))
        if index < len(items) - 1:
            cells.append(p("&rarr;", s["DiagramT"]))
    widths = []
    for index in range(len(items)):
        widths.extend([3.05 * cm, .36 * cm] if index < len(items) - 1 else [3.05 * cm])
    result = Table([cells], colWidths=widths)
    commands = [("ALIGN", (0, 0), (-1, -1), "CENTER"), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3), ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]
    for index, (_, _, color) in enumerate(items):
        column = index * 2
        commands.extend([("BACKGROUND", (column, 0), (column, 0), colors.HexColor(color)), ("BOX", (column, 0), (column, 0), .6, colors.HexColor("#5593B8"))])
    result.setStyle(TableStyle(commands))
    return result


def build(filename, title, subtitle, body):
    ROOT.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(str(ROOT / filename), pagesize=A4, leftMargin=1.7*cm, rightMargin=1.7*cm, topMargin=1.5*cm, bottomMargin=1.7*cm, title=title, author="SMA Teladan")
    s = styles()
    story = [Spacer(1, .6*cm), p(title, s["TitleT"]), p(subtitle, s["SubT"])] + body(s)
    document.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"Created {ROOT / filename}")


def kelas_x(s):
    return [
        p("Halo teman-teman. Kalian sudah mempelajari Society 5.0, Revolusi Industri 4.0, Gen-AI, analisis visual, AR/VR, algoritma, manfaat teknologi, dan risikonya. Sekarang kita akan memakai pengalaman itu untuk menyusun <b>proposal mini</b>. Kalian boleh meneliti suatu gejala atau merancang inovasi yang menyelesaikan masalah. Tujuannya bukan sekadar memakai teknologi, tetapi menghasilkan gagasan yang berbasis bukti, etis, dan layak dikembangkan.", s["CallT"]),
        p("1. Posisi Materi dan Tujuan", s["SectionT"]),
        p("Materi ini menjembatani kurikulum lama Kelas X semester 1 yang memuat Society 5.0, Informasi Digital, dan Analisis Data dengan draft kurikulum baru yang menempatkan Research sebelum Tech. Proposal dapat menjadi langkah awal menuju karya ilmiah, prototype, atau rencana usaha untuk persiapan umum <b>OPSI</b> dan <b>FIKSI</b>.", s["BodyT"]),
        table([
            ["Bekal sebelumnya", "Cara digunakan dalam proposal"],
            ["Society 5.0", "Memilih masalah manusia dan lingkungan yang benar-benar penting."],
            ["Informasi digital dan algoritma", "Mengkaji data, sumber informasi, perilaku digital, atau sistem rekomendasi."],
            ["Analisis data", "Mengumpulkan bukti awal, membandingkan kondisi, dan menyajikan temuan."],
            ["AI, AR/VR, dan teknologi lain", "Menjadi objek penelitian, alat bantu, atau bagian solusi jika memang diperlukan."],
            ["Etika teknologi", "Menjaga privasi, kejujuran, keadilan, keselamatan, dan kendali manusia."],
        ], [6.0*cm, 10.2*cm], s),
        p("2. Mulai dari Masalah dan Bukti", s["SectionT"]),
        p("Proposal yang kuat tidak dimulai dengan 'kami ingin memakai AI' atau 'kami ingin ikut lomba'. Mulailah dengan masalah yang dapat diamati. Cari bukti awal melalui pengamatan, wawancara singkat, data sederhana, atau sumber tepercaya. Setelah itu, tentukan apakah masalah tersebut lebih tepat <b>diteliti</b> atau <b>diselesaikan melalui inovasi</b>.", s["BodyT"]),
        table([
            ["Ide terlalu umum", "Masalah yang lebih tajam"],
            ["Meneliti media sosial.", "Apakah notifikasi dan autoplay memengaruhi durasi belajar mandiri siswa kelas X?"],
            ["Membuat AI untuk sekolah.", "Bagaimana alat cek sumber dapat membantu siswa membedakan informasi ilmiah dan ringkasan AI?"],
            ["Membuat sekolah ramah lingkungan.", "Bagaimana mengurangi kesalahan pemilahan sampah di area kantin sekolah?"],
        ], [8.1*cm, 8.1*cm], s),
        p("Rumus awal: <b>masalah + pihak yang terdampak + konteks + bukti awal + alasan penting.</b>", s["CallT"]),
        p("3. Pilih Jalur Proposal", s["SectionT"]),
        boxes([
            ("Masalah", "amati dan cari bukti", "#DDEEF5"),
            ("Pilih jalur", "penelitian atau inovasi", "#E5F2E7"),
            ("Rancang", "metode atau solusi", "#FFF1D6"),
            ("Uji", "temuan atau validasi", "#FDE6E1"),
        ], s),
        table([
            ["Jalur A: Penelitian / gaya OPSI", "Jalur B: Inovasi / gaya FIKSI"],
            ["Tujuan: menjawab pertanyaan melalui data dan metode yang jelas.", "Tujuan: menawarkan nilai atau solusi yang dapat digunakan dan divalidasi."],
            ["Cocok jika kalian ingin memahami hubungan, pola, perbedaan, sebab, atau pengalaman pengguna.", "Cocok jika kalian ingin membuat produk, layanan, sistem, kampanye, atau rencana usaha."],
            ["Output awal: rumusan masalah, dugaan/landasan, metode, data yang dibutuhkan, dan rencana analisis.", "Output awal: problem statement, pengguna, value proposition, cara kerja, prototype awal, dan rencana validasi."],
            ["Contoh: hubungan kebiasaan melihat rekomendasi video dengan keberagaman sumber belajar.", "Contoh: kartu cek sumber untuk membantu siswa mengevaluasi informasi digital sebelum digunakan dalam tugas."],
        ], [8.1*cm, 8.1*cm], s),
        p("Nama OPSI dan FIKSI digunakan sebagai arah pengembangan umum. Ketentuan, kategori, dan format resmi dapat berubah; jika proposal akan didaftarkan, selalu periksa pedoman tahun berjalan pada portal resmi.", s["CallT"]),
        p("4. Pertanyaan Kunci Tiap Jalur", s["SectionT"]),
        table([
            ["Penelitian", "Inovasi"],
            ["Apa pertanyaan penelitian yang ingin dijawab?", "Masalah siapa yang ingin diselesaikan?"],
            ["Data apa yang diperlukan dan bagaimana memperolehnya?", "Apa nilai tambah solusi dibanding cara yang sudah ada?"],
            ["Variabel, objek, atau fenomena apa yang diamati?", "Bagaimana produk atau layanan bekerja?"],
            ["Bagaimana data dianalisis agar kesimpulan tidak asal?", "Bagaimana membuat prototype minimum dan mengujinya?"],
            ["Apa keterbatasan, potensi bias, dan etika pengumpulan data?", "Apa risiko, biaya, akses, keselamatan, dan etika penggunaannya?"],
        ], [8.1*cm, 8.1*cm], s),
        p("5. Contoh Pengembangan Satu Masalah", s["SectionT"]),
        table([
            ["Titik awal", "Contoh pengembangan"],
            ["Masalah", "Siswa menerima banyak rekomendasi video, tetapi belum tentu memperoleh sumber belajar yang beragam dan tepercaya."],
            ["Jalur penelitian", "Mengkaji hubungan pola rekomendasi video dengan keberagaman sumber belajar yang digunakan siswa."],
            ["Data awal", "Diary penggunaan, daftar sumber yang muncul, survei singkat, dan wawancara tanpa mengambil data akun pribadi."],
            ["Jalur inovasi", "Membuat panduan atau alat sederhana yang membantu siswa membandingkan sumber, alasan rekomendasi, dan kredibilitas informasi."],
            ["Prototype awal", "Lembar cek digital atau kartu keputusan yang diuji kepada beberapa siswa."],
            ["Etika", "Meminta persetujuan, tidak membuka riwayat pribadi, menyamarkan identitas, dan tidak mengklaim hasil berlebihan."],
        ], [4.5*cm, 11.7*cm], s),
        p("6. Tugas Kelompok: Proposal Mini Riset atau Inovasi", s["SectionT"]),
        p("Pilih satu masalah nyata di sekolah, lingkungan belajar, atau masyarakat. Kembangkan tugas lama atau ide baru, tentukan jalur penelitian atau inovasi, lalu susun proposal yang menunjukkan perkembangan ide dan rencana kerja yang dapat dilakukan.", s["BodyT"]),
        table([
            ["Bagian wajib", "Isi minimum"],
            ["Judul, tim, dan jalur", "Judul sementara, anggota, serta pilihan Penelitian atau Inovasi."],
            ["Latar belakang", "Masalah spesifik, pihak yang terdampak, konteks, dan minimal satu bukti awal."],
            ["Tujuan", "Pertanyaan penelitian yang ingin dijawab atau perubahan yang ingin dihasilkan."],
            ["Landasan awal", "Minimal dua sumber tepercaya atau contoh karya/produk sejenis. Tuliskan tautan sumber."],
            ["Rencana utama", "Penelitian: objek, data, metode, dan analisis. Inovasi: pengguna, nilai tambah, cara kerja, dan prototype."],
            ["Etika dan risiko", "Minimal tiga pertimbangan, misalnya persetujuan, privasi, bias, keselamatan, akses, dan kejujuran penggunaan AI."],
            ["Rencana uji/validasi", "Cara memeriksa temuan atau memperoleh masukan pengguna terhadap solusi."],
            ["Jejak pengembangan", "Ide/tugas lama yang digunakan, perubahan yang dibuat, dan bantuan tool termasuk Gen-AI."],
        ], [4.5*cm, 11.7*cm], s),
        p("Bentuk hasil: 4-6 slide atau PDF 2-4 halaman. Jika memakai Gen-AI, tulis tool, tujuan penggunaan, bagian yang dibantu, dan bagian yang diperiksa sendiri.", s["CallT"]),
        p("7. Pengumpulan dan Referensi Ajang", s["SectionT"]),
        p("Kirim hasil kelompok ke <link href='mailto:ataka.ahmad@gmail.com' color='#1D5F85'><u>ataka.ahmad@gmail.com</u></link>.<br/><b>Subject email:</b> SMA Teladan X - Proposal Mini Riset/Inovasi - [Nama Kelompok]<br/>Sertakan nama anggota, pilihan jalur, dan file proposal.<br/><br/>Portal resmi: <link href='https://sma.pusatprestasinasional.kemdikbud.go.id/opsi/login' color='#1D5F85'><u>OPSI</u></link> | <link href='https://sma.pusatprestasinasional.kemdikbud.go.id/fiksi/login' color='#1D5F85'><u>FIKSI</u></link>.", s["CallT"]),
        p("8. Kriteria Penilaian", s["SectionT"]),
        table([
            ["Aspek", "Yang dicari"],
            ["Ketajaman masalah", "Spesifik, relevan, dan didukung bukti awal."],
            ["Kesesuaian jalur", "Pertanyaan, metode, atau solusi selaras dengan masalah yang dipilih."],
            ["Kualitas rencana", "Data/metode atau prototype/validasi dijelaskan secara masuk akal."],
            ["Sumber dan orisinalitas", "Menggunakan sumber tepercaya, mengakui bantuan, dan menunjukkan pengembangan ide sendiri."],
            ["Etika dan kelayakan", "Risiko, batas, privasi, keselamatan, waktu, dan sumber daya dipertimbangkan."],
            ["Komunikasi", "Proposal runtut, visual membantu, dan kelompok dapat menjelaskan alasan keputusan."],
        ], [4.5*cm, 11.7*cm], s),
        p("Penutup: karya yang kuat tidak harus langsung besar atau canggih. Mulailah dari masalah yang dekat, kumpulkan bukti dengan jujur, pilih cara kerja yang tepat, lalu perbaiki gagasan berdasarkan data dan masukan.", s["CallT"]),
    ]


def kelas_xi(s):
    return [
        p("Halo teman-teman. Kalian sudah memiliki ide IoT, melakukan IoT Product Teardown, menyusun Innovation Pitch Canvas, dan membuat Component List serta RAB. Kini kita masuk ke <b>Pengembangan Prototype</b>: mengubah rencana menjadi versi minimum yang dapat diuji. Prototype tidak harus langsung berupa alat yang berfungsi penuh.", s["CallT"]),
        p("1. Posisi Kita dalam Kurikulum", s["SectionT"]),
        p("Sesi ini mengikuti <b>Minggu 14: Pengembangan Prototype</b>. Evidence yang dikumpulkan adalah Prototype dan catatan proses. Tujuannya bukan membuat alat paling mahal, tetapi membuktikan bahwa ide dapat diterjemahkan menjadi sistem yang jelas dan siap diuji.", s["BodyT"]),
        table([
            ["Yang sudah dimiliki kelompok", "Yang dilakukan sekarang"],
            ["Masalah, pengguna, dan ide inovasi", "Memilih satu fungsi inti yang paling penting untuk diuji lebih dahulu."],
            ["IoT Product Teardown", "Mengambil pelajaran dari produk nyata tanpa menyalin desain secara mentah."],
            ["Component List dan RAB", "Menentukan komponen minimum, kebutuhan daya, serta hal yang belum pasti."],
            ["Masukan dari kelas", "Memperbaiki desain berdasarkan risiko, kelayakan, dan kebutuhan pengguna."],
        ], [6.0*cm, 10.2*cm], s),
        p("2. Apa Itu Prototype?", s["SectionT"]),
        p("Prototype adalah versi awal untuk menjawab pertanyaan penting. Ia dapat berupa sketsa antarmuka, diagram sistem, maket dari kardus, simulasi alur, atau rangkaian sederhana. Prototype tidak perlu sempurna, tetapi harus cukup jelas untuk diuji dan diberi masukan.", s["BodyT"]),
        table([
            ["Bentuk prototype", "Kapan dipakai", "Contoh"],
            ["Paper / visual prototype", "Saat ingin menguji tampilan, alur pengguna, atau posisi alat.", "Sketsa dashboard greenhouse dan kartu notifikasi kondisi tanaman."],
            ["System prototype", "Saat ingin menunjukkan hubungan input, proses, output, dan manusia.", "Diagram sensor tanah -> ESP32 -> relay -> pompa -> siswa."],
            ["Logic simulation", "Saat alat belum ada, tetapi aturan sistem perlu diuji.", "Tabel: jika kelembapan di bawah ambang, sistem memberi notifikasi atau menyalakan pompa."],
            ["Hardware proof of concept", "Saat komponen dan pendampingan tersedia.", "Sensor mengirim pembacaan dan LED menyala sebagai pengganti pompa."],
        ], [4.0*cm, 5.8*cm, 6.4*cm], s),
        p("Prinsip MVP: <b>uji satu fungsi inti dahulu.</b> Smart Greenhouse tidak perlu langsung memiliki dashboard, notifikasi, kipas, pompa, dan banyak sensor. Mulailah dari pertanyaan: apakah sistem dapat mendeteksi kondisi tanah dan memberi tindakan yang aman?", s["CallT"]),
        PageBreak(),
        p("3. Dari Ide ke Prototype Plan", s["SectionT"]),
        boxes([
            ("Fungsi inti", "hal paling penting", "#DDEEF5"),
            ("Prototype", "versi minimum", "#E5F2E7"),
            ("Uji", "skenario dan data", "#FFF1D6"),
            ("Perbaiki", "catatan perubahan", "#FDE6E1"),
        ], s),
        p("4. Contoh: Prototype Smart Greenhouse", s["SectionT"]),
        table([
            ["Bagian", "Contoh keputusan prototype"],
            ["Fungsi inti", "Mendeteksi media tanam terlalu kering dan memberi tindakan yang tepat."],
            ["Versi minimum", "Sensor kelembapan + microcontroller + LED/buzzer sebagai simulasi notifikasi. Pompa boleh belum dipasang."],
            ["Aturan logika", "Jika nilai sensor di bawah ambang yang telah diuji, LED menyala dan siswa mengecek tanaman sebelum menyiram."],
            ["Cara uji", "Bandingkan pembacaan pada tanah basah, lembap, dan kering. Catat apakah notifikasi muncul sesuai kondisi."],
            ["Risiko", "Sensor salah baca, ambang tidak cocok, kabel longgar, atau siswa menganggap notifikasi sebagai keputusan otomatis."],
            ["Perbaikan berikutnya", "Ubah ambang, lindungi sensor, tambahkan kontrol manual, atau baru tambahkan pompa setelah logika bekerja."],
        ], [4.5*cm, 11.7*cm], s),
        p("5. Skenario Uji yang Baik", s["SectionT"]),
        p("Skenario uji bukan hanya 'alat menyala'. Skenario yang baik menentukan kondisi awal, tindakan yang dilakukan, hasil yang diharapkan, hasil yang terjadi, dan keputusan perbaikan.", s["BodyT"]),
        table([
            ["Kolom", "Contoh"],
            ["Tujuan uji", "Memeriksa apakah notifikasi tanah kering muncul pada kondisi yang tepat."],
            ["Kondisi awal", "Sensor berada pada media tanah yang basah, lembap, atau kering."],
            ["Tindakan", "Nyalakan sistem dan tunggu pembacaan sensor."],
            ["Hasil yang diharapkan", "LED/buzzer hanya menyala ketika nilai berada di bawah ambang yang ditetapkan."],
            ["Hasil nyata", "Tulis data/pengamatan yang benar-benar terjadi."],
            ["Keputusan", "Pertahankan, ubah ambang, perbaiki pemasangan, atau sederhanakan fungsi."],
        ], [4.5*cm, 11.7*cm], s),
        p("6. Tugas Kelompok: Prototype Plan dan Test Plan", s["SectionT"]),
        p("Kembangkan ide IoT kelompok menjadi rencana prototype yang realistis. Kalian boleh membuat paper prototype, diagram sistem, simulasi logika, atau proof of concept hardware sederhana. Tidak wajib membeli komponen atau membuat alat berfungsi penuh pada tahap ini.", s["BodyT"]),
        table([
            ["Bagian hasil", "Isi minimum"],
            ["Fungsi inti", "Satu fungsi paling penting yang ingin dibuktikan terlebih dahulu."],
            ["Bentuk prototype", "Pilih paper, visual, system diagram, logic simulation, atau hardware proof of concept; jelaskan alasan."],
            ["Sketsa sistem", "Input/sensor -> microcontroller/proses -> output -> manusia, termasuk kontrol manual bila ada."],
            ["Komponen minimum", "Komponen yang benar-benar dibutuhkan untuk prototype ini dan komponen yang ditunda."],
            ["Test plan", "Minimal tiga skenario uji lengkap dengan kondisi, hasil harapan, dan cara mencatat hasil."],
            ["Risiko dan keselamatan", "Minimal tiga risiko, termasuk daya/listrik, air/lingkungan, serta tindakan jika sistem salah."],
            ["Pembagian peran", "Siapa menyiapkan sketsa/komponen, mencatat hasil, dan menyampaikan refleksi."],
        ], [4.5*cm, 11.7*cm], s),
        p("Bentuk hasil: 3-5 slide atau satu PDF. Lampirkan foto sketsa/maket bila ada. Yang dinilai adalah kejelasan fungsi inti, mutu rencana uji, keamanan, dan kemampuan kelompok menjelaskan alasan desain.", s["CallT"]),
        p("7. Pengumpulan", s["SectionT"]),
        p("Kirim hasil kelompok ke <link href='mailto:ataka.ahmad@gmail.com' color='#1D5F85'><u>ataka.ahmad@gmail.com</u></link>.<br/><b>Subject email:</b> SMA Teladan XI - Prototype Plan dan Test Plan IoT - [Nama Kelompok]<br/>Sertakan nama anggota, file hasil, serta foto prototype/sketsa bila ada. Simpan sebagai evidence portofolio: <b>Unique Value - Tech - Minggu 14 - Prototype</b>.", s["CallT"]),
        p("Penutup: prototype adalah cara belajar dari kenyataan. Jika hasil uji menunjukkan ide perlu diubah, itu bukan kegagalan. Itu adalah bukti bahwa kelompok sedang merancang teknologi secara lebih matang.", s["CallT"]),
    ]


if __name__ == "__main__":
    build("materi-kelas-x-proposal-mini-riset-dan-inovasi.pdf", "Materi Kelas X: Proposal Mini Riset dan Inovasi", "Dari masalah nyata menuju gagasan untuk persiapan OPSI dan FIKSI", kelas_x)
    build("materi-kelas-xi-prototype-plan-dan-test-plan-iot.pdf", "Materi Kelas XI: Prototype Plan dan Test Plan IoT", "Mengubah ide dan RAB menjadi versi minimum yang siap diuji", kelas_xi)
