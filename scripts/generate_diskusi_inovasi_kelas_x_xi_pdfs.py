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
    s.add(ParagraphStyle(name="CellT", parent=s["BodyText"], fontName="Helvetica", fontSize=8.8, leading=10.8, textColor=colors.HexColor("#1F2933")))
    s.add(ParagraphStyle(name="HeadT", parent=s["BodyText"], fontName="Helvetica-Bold", fontSize=9, leading=10.8, textColor=colors.white))
    s.add(ParagraphStyle(name="SmallT", parent=s["BodyText"], fontName="Helvetica", fontSize=8.7, leading=11.4, textColor=colors.HexColor("#425466"), spaceAfter=4))
    return s


def p(value, style):
    return Paragraph(value, style)


def bullets(values, style):
    return ListFlowable([ListItem(p(value, style), leftIndent=6) for value in values], bulletType="bullet", start="circle", leftIndent=16, bulletFontName="Helvetica", bulletFontSize=10, bulletOffsetY=2)


def table(rows, widths, s):
    data = [[p(str(cell), s["HeadT"] if i == 0 else s["CellT"]) for cell in row] for i, row in enumerate(rows)]
    result = Table(data, colWidths=widths, repeatRows=1)
    result.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#24577A")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#B7C5D1")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F1F7FA")]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return result


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.HexColor("#5B6770"))
    canvas.drawRightString(A4[0] - 1.7 * cm, 1.2 * cm, f"Halaman {doc.page}")
    canvas.restoreState()


def build(filename, title, subtitle, story):
    path = ROOT / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=1.7 * cm, rightMargin=1.7 * cm, topMargin=1.5 * cm, bottomMargin=1.7 * cm, title=title, author="SMA Teladan")
    s = styles()
    content = [Spacer(1, .6 * cm), p(title, s["TitleT"]), p(subtitle, s["SubT"])] + story(s)
    document.build(content, onFirstPage=footer, onLaterPages=footer)
    print(f"Created {path}")


def kelas_x(s):
    return [
        p("Halo teman-teman. Kalian sudah memetakan manfaat dan risiko teknologi dalam Society 5.0. Sekarang kita melangkah satu tingkat lebih jauh: bukan hanya menemukan masalah, tetapi <b>mendesain penggunaan teknologi yang lebih aman, adil, dan tetap membantu manusia</b>. Teknologi bukan sekadar solusi atau masalah. Jawabannya bergantung pada tujuan, aturan, dan cara manusia memakainya.", s["CallT"]),
        p("1. Tujuan Pembelajaran", s["SectionT"]),
        bullets([
            "Kalian dapat menjelaskan mengapa satu teknologi dapat memberi manfaat sekaligus menciptakan masalah baru.",
            "Kalian dapat melihat dampak teknologi dari sudut pandang pengguna, teman, guru, sekolah, dan masyarakat.",
            "Kalian dapat mengubah satu risiko menjadi aturan penggunaan atau perbaikan desain yang realistis.",
            "Kalian dapat menyampaikan pendapat secara kritis tanpa langsung menyalahkan atau memuja teknologi.",
        ], s["BodyT"]),
        p("2. Teknologi: Solusi atau Masalah Baru?", s["SectionT"]),
        p("Pertanyaan ini tidak memiliki jawaban sesederhana 'baik' atau 'buruk'. Sebuah aplikasi belajar bisa membantu memahami materi, tetapi juga membuat siswa hanya menunggu jawaban instan. Kamera dapat membantu keamanan, tetapi dapat mengganggu privasi. Karena itu, dalam Society 5.0 kita perlu menilai <b>cara teknologi dipakai</b>, bukan hanya teknologinya.", s["BodyT"]),
        table([
            ["Teknologi", "Manfaat yang mungkin", "Masalah baru yang mungkin"],
            ["Gen-AI", "Menjelaskan konsep, memberi contoh, membantu refleksi.", "Jawaban disalin, informasi keliru dipercaya, kemampuan berpikir melemah."],
            ["Aplikasi absensi", "Administrasi lebih cepat dan data kehadiran rapi.", "Data pribadi berlebihan, kesalahan sistem, atau siswa merasa diawasi."],
            ["Media sosial", "Karya dan informasi lebih mudah dibagikan.", "Perundungan, hoaks, tekanan sosial, dan waktu layar berlebihan."],
            ["Sensor otomatis", "Lampu, pompa, atau kipas dapat bekerja lebih efisien.", "Sensor salah baca, alat tidak dirawat, atau manusia terlalu percaya sistem."],
        ], [3.4 * cm, 6.3 * cm, 6.5 * cm], s),
        p("Kalimat kunci: <b>teknologi yang bertanggung jawab harus bisa dijelaskan manfaatnya, risikonya, dan siapa yang tetap memegang kendali.</b>", s["CallT"]),
        PageBreak(),
        p("3. Kerangka Diskusi: 4R", s["SectionT"]),
        table([
            ["Tahap", "Pertanyaan yang dibahas"],
            ["Recognize", "Masalah nyata apa yang dibantu teknologi ini? Siapa penggunanya?"],
            ["Risk", "Apa risiko bagi privasi, keamanan, keadilan, kesehatan, atau kebiasaan pengguna?"],
            ["Redesign", "Fitur, aturan, atau kebiasaan apa yang dapat mengurangi risiko tersebut?"],
            ["Responsibility", "Siapa yang bertanggung jawab: pengguna, pembuat aplikasi, sekolah, atau semua pihak?"],
        ], [4.2 * cm, 12.0 * cm], s),
        p("4. Contoh: Gen-AI untuk Tugas Sekolah", s["SectionT"]),
        table([
            ["Bagian", "Contoh jawaban kritis"],
            ["Masalah yang dibantu", "Siswa membutuhkan contoh, umpan balik awal, atau penjelasan dengan bahasa yang lebih sederhana."],
            ["Risiko", "Siswa mengirim jawaban AI sebagai karya sendiri atau memakai informasi yang tidak diperiksa."],
            ["Redesign penggunaan", "AI dipakai untuk membuat pertanyaan latihan, memperbaiki struktur tulisan, atau membandingkan dua penjelasan; sumber asli tetap dibaca."],
            ["Aturan yang adil", "Siswa menjelaskan penggunaan AI dalam tugas; guru memberi alternatif jika siswa tidak memiliki akses akun atau perangkat."],
        ], [4.4 * cm, 11.8 * cm], s),
        p("Perbaikan tidak selalu berarti membuat aplikasi baru. Kadang solusi terbaik adalah batas penggunaan yang jelas, pilihan alternatif, atau pemeriksaan manusia sebelum keputusan dibuat.", s["CallT"]),
        p("5. Diskusi Kelompok: Risiko Menjadi Rancangan yang Lebih Baik", s["SectionT"]),
        p("Ambil satu teknologi dari Technology Risk Map kelompok kalian sebelumnya. Pilih <b>satu risiko paling penting</b>, lalu buat rancangan penggunaan yang lebih bertanggung jawab. Kalian tidak perlu membuat poster risiko baru; gunakan hasil lama sebagai bahan untuk memperbaiki solusi.", s["BodyT"]),
        table([
            ["Langkah", "Yang dikerjakan kelompok"],
            ["1. Pilih", "Pilih satu teknologi dan satu risiko yang paling relevan untuk siswa atau sekolah."],
            ["2. Buktikan", "Buat satu skenario singkat: apa yang dapat terjadi jika risiko itu dibiarkan?"],
            ["3. Rancang", "Buat minimal tiga perbaikan: aturan penggunaan, perubahan fitur, atau peran manusia."],
            ["4. Uji", "Tanyakan: apakah perbaikan ini realistis? Apakah masih adil bagi siswa yang akses teknologinya berbeda?"],
            ["5. Sampaikan", "Siapkan penjelasan singkat agar kelompok lain dapat memberi masukan."],
        ], [4.0 * cm, 12.2 * cm], s),
        PageBreak(),
        p("6. Tugas Kelompok: Responsible Technology Redesign", s["SectionT"]),
        p("Buat satu halaman poster/infografik digital atau 2 slide yang menunjukkan bagaimana kelompok kalian mengubah penggunaan teknologi menjadi lebih aman dan manusiawi.", s["BodyT"]),
        table([
            ["Komponen hasil", "Isi minimum"],
            ["Teknologi dan konteks", "Nama teknologi dan contoh pemakaian di sekolah, rumah, atau kehidupan siswa."],
            ["Masalah yang dipilih", "Satu risiko utama, lengkap dengan skenario singkat dampaknya."],
            ["Rancangan perbaikan", "Minimal tiga langkah: aturan, fitur, atau kontrol manusia."],
            ["Pihak yang bertanggung jawab", "Siapa yang perlu bertindak dan apa perannya."],
            ["Uji keadilan", "Bagaimana rancangan tetap dapat digunakan oleh siswa dengan akses perangkat/internet yang berbeda?"],
            ["Pesan utama", "Lengkapi: 'Teknologi ini membantu manusia jika ...'"],
        ], [4.3 * cm, 11.9 * cm], s),
        p("7. Pengumpulan", s["SectionT"]),
        p("Kirim hasil kelompok ke <link href='mailto:ataka.ahmad@gmail.com' color='#1D5F85'><u>ataka.ahmad@gmail.com</u></link>.<br/><b>Subject email:</b> SMA Teladan X - Tugas Responsible Technology Redesign - [Nama Kelompok]<br/>Sertakan nama anggota, teknologi yang dipilih, serta file poster/slide.", s["CallT"]),
        p("8. Penutup", s["SectionT"]),
        p("Society 5.0 tidak meminta kita menjauh dari teknologi. Society 5.0 meminta kita memastikan teknologi memperkuat kemampuan manusia, menghormati hak orang lain, dan tidak meninggalkan siapa pun.", s["CallT"]),
    ]


def kelas_xi(s):
    return [
        p("Halo teman-teman. Kalian sudah membedah produk IoT dan melihat bahwa sistem pintar bukan hanya soal sensor atau Wi-Fi. Sekarang gunakan temuan tersebut untuk mematangkan ide inovasi kalian. Pada sesi ini, kelompok akan mengubah ide yang masih umum menjadi gagasan yang menjawab masalah nyata, masuk akal dibuat, dan siap menerima kritik.", s["CallT"]),
        p("1. Tujuan Pembelajaran", s["SectionT"]),
        bullets([
            "Kalian dapat memilih masalah yang cukup spesifik untuk diselesaikan dengan IoT.",
            "Kalian dapat menghubungkan ide dengan pengguna, sensor/data, output, dan peran manusia.",
            "Kalian dapat membedakan ide yang menarik dari ide yang benar-benar berguna dan layak dicoba.",
            "Kalian dapat memberi serta menerima umpan balik untuk memperkuat rancangan inovasi.",
        ], s["BodyT"]),
        p("2. Ide Inovasi yang Kuat Dimulai dari Masalah", s["SectionT"]),
        p("Jangan mulai dari kalimat 'kita ingin memakai sensor'. Mulailah dari masalah yang dapat dilihat dan dirasakan pengguna. Sensor dan aplikasi adalah alat, bukan tujuan. Ide yang baik menjelaskan siapa yang terbantu, kapan masalah terjadi, dan bagaimana perubahan dapat diukur.", s["BodyT"]),
        table([
            ["Terlalu umum", "Lebih tajam"],
            ["Membuat smart greenhouse.", "Membantu penjaga greenhouse mengetahui media tanam terlalu kering sebelum tanaman layu."],
            ["Membuat sekolah pintar.", "Mengurangi lampu ruang yang menyala saat ruangan benar-benar kosong tanpa mengganggu kegiatan belajar."],
            ["Membuat alat absensi IoT.", "Membantu guru melihat kehadiran kegiatan ekstrakurikuler tanpa mengumpulkan data yang tidak diperlukan."],
        ], [8.1 * cm, 8.1 * cm], s),
        p("Rumus sederhana: <b>Pengguna + masalah spesifik + kondisi pemicu + hasil yang diharapkan.</b>", s["CallT"]),
        p("3. Contoh Produk dan Inovasi Nyata", s["SectionT"]),
        table([
            ["Contoh", "Masalah yang dibantu", "Pelajaran untuk kelompok"],
            ["Smart irrigation", "Tanaman tidak disiram tepat saat media tanam kering.", "Tidak semua tanaman membutuhkan ambang kelembapan yang sama; manusia tetap perlu memeriksa."],
            ["Smart lighting", "Energi terbuang saat lampu menyala di ruangan kosong.", "Sensor gerak saja mungkin cukup; kamera tidak selalu diperlukan."],
            ["Air-quality monitor", "Pengguna tidak sadar ventilasi ruangan kurang baik.", "Data harus diterjemahkan menjadi tindakan, misalnya membuka jendela atau menyalakan ventilasi."],
            ["Smart bin", "Tempat sampah penuh terlambat diketahui.", "Biaya, daya, dan perawatan sensor harus sebanding dengan manfaatnya."],
        ], [4.3 * cm, 6.1 * cm, 5.8 * cm], s),
        p("4. Canvas Ide Inovasi IoT", s["SectionT"]),
        table([
            ["Bagian", "Pertanyaan panduan"],
            ["Pengguna", "Siapa yang mengalami masalah ini secara langsung?"],
            ["Masalah", "Apa yang sering terjadi dan mengapa masalah tersebut penting?"],
            ["Bukti sederhana", "Apa yang kalian lihat, alami, atau dengar yang menunjukkan masalah ini memang ada?"],
            ["Sistem IoT", "Data apa yang diperlukan? Sensor apa yang mungkin digunakan? Output atau aksi apa yang membantu?"],
            ["Peran manusia", "Siapa yang memeriksa hasil, merawat alat, dan memutuskan tindakan akhir?"],
            ["Batas dan risiko", "Apa yang dapat gagal? Data apa yang tidak boleh dikumpulkan? Apa alternatif manualnya?"],
            ["Ukuran keberhasilan", "Tanda sederhana apa yang menunjukkan ide ini benar-benar membantu?"],
        ], [4.2 * cm, 12.0 * cm], s),
        p("5. Contoh Menguatkan Ide: Greenhouse Teladan", s["SectionT"]),
        table([
            ["Bagian", "Contoh ide yang dapat diuji"],
            ["Pengguna", "Siswa piket, guru pendamping, atau penjaga greenhouse."],
            ["Masalah", "Kondisi media tanam baru diketahui setelah tanaman mulai layu atau jadwal penyiraman tidak sesuai kondisi."],
            ["Sistem", "Sensor kelembapan tanah mengirim pembacaan ke controller; indikator/dashboard memberi peringatan; pompa hanya aktif jika ada pemeriksaan atau aturan yang aman."],
            ["Peran manusia", "Memeriksa air, kondisi daun, jadwal pemeliharaan, serta memutuskan jika data sensor tidak masuk akal."],
            ["Risiko", "Sensor rusak, pompa macet, listrik padam, ambang terlalu rendah/tinggi, atau sistem menyiram terlalu banyak."],
            ["Keberhasilan", "Tanaman lebih terpantau dan jadwal perawatan lebih tepat, bukan sekadar alat berhasil tersambung ke internet."],
        ], [4.3 * cm, 11.9 * cm], s),
        p("Ingat: ide yang matang tidak menjanjikan bahwa teknologi akan menyelesaikan semua masalah. Ide yang matang menjelaskan batasnya dan siapa yang akan menjalankannya.", s["CallT"]),
        p("6. Lokakarya Kelas: Innovation Pitch and Feedback", s["SectionT"]),
        p("Setiap kelompok menyiapkan pitch singkat untuk satu ide IoT. Kelompok lain bertindak sebagai calon pengguna, teknisi, penjaga anggaran, dan penjaga etika. Tujuannya bukan mencari ide paling rumit, tetapi menemukan ide yang paling relevan dan dapat dipertanggungjawabkan.", s["BodyT"]),
        table([
            ["Bagian pitch", "Yang disampaikan"],
            ["Masalah", "Siapa yang mengalami masalah dan dalam situasi apa?"],
            ["Gagasan sistem", "Input/sensor -> controller/data -> output/aksi -> manusia."],
            ["Manfaat", "Perubahan konkret apa yang diharapkan?"],
            ["Batas", "Satu risiko atau kelemahan yang sudah kalian sadari."],
            ["Permintaan masukan", "Satu pertanyaan spesifik yang ingin kalian dapatkan dari kelas."],
        ], [4.2 * cm, 12.0 * cm], s),
        p("Pertanyaan umpan balik yang berguna: 'Masalahnya cukup nyata?', 'Apakah sensor benar-benar dibutuhkan?', 'Siapa yang merawatnya?', 'Apa yang terjadi jika sistem gagal?', dan 'Apakah ada cara yang lebih sederhana?'.", s["CallT"]),
        p("7. Tugas Kelompok: IoT Innovation Pitch Canvas", s["SectionT"]),
        p("Lengkapi satu <b>IoT Innovation Pitch Canvas</b> sebagai hasil pengembangan ide kelompok. Ini bukan blueprint teknis lengkap dan belum perlu membuat prototipe. Fokusnya adalah membuktikan bahwa ide kalian layak dilanjutkan ke tahap desain sistem.", s["BodyT"]),
        table([
            ["Komponen hasil", "Isi minimum"],
            ["Judul dan pengguna", "Nama ide serta pihak yang paling terbantu."],
            ["Masalah dan bukti", "Masalah spesifik dan satu bukti/pengamatan sederhana."],
            ["Sketsa sistem", "Diagram input/sensor -> proses/data -> output -> manusia."],
            ["Manfaat dan ukuran sukses", "Dua manfaat serta indikator sederhana untuk menilai keberhasilan."],
            ["Komponen kandidat", "Minimal tiga komponen atau layanan yang mungkin diperlukan, tanpa wajib menentukan merek."],
            ["Risiko dan penjagaan", "Minimal tiga risiko dan cara mengurangi masing-masing risiko."],
            ["Masukan kelas", "Tiga masukan yang diterima dan satu perubahan ide setelah diskusi."],
        ], [4.5 * cm, 11.7 * cm], s),
        p("Bentuk hasil: satu poster/infografik digital atau 2-3 slide. Sertakan nama semua anggota. Kelompok boleh memakai hasil IoT Product Teardown sebagai referensi, tetapi jangan menyalin desain produk lain tanpa menjelaskan penyesuaiannya.", s["CallT"]),
        p("8. Pengumpulan", s["SectionT"]),
        p("Kirim hasil kelompok ke <link href='mailto:ataka.ahmad@gmail.com' color='#1D5F85'><u>ataka.ahmad@gmail.com</u></link>.<br/><b>Subject email:</b> SMA Teladan XI - Tugas IoT Innovation Pitch Canvas - [Nama Kelompok]<br/>Sertakan nama anggota, file poster/slide, dan satu kalimat tentang perubahan ide setelah mendapat masukan kelas.", s["CallT"]),
        p("9. Penutup", s["SectionT"]),
        p("Inovasi yang baik bukan yang paling banyak komponennya. Inovasi yang baik memahami masalah manusia, menggunakan teknologi secukupnya, dan siap diperbaiki setelah mendengar pengguna.", s["CallT"]),
    ]


if __name__ == "__main__":
    build("materi-kelas-x-teknologi-solusi-atau-masalah-baru.pdf", "Materi Kelas X: Teknologi, Solusi atau Masalah Baru?", "Memperdalam Society 5.0 melalui diskusi kritis dan desain penggunaan yang bertanggung jawab", kelas_x)
    build("materi-kelas-xi-diskusi-ide-inovasi-iot.pdf", "Materi Kelas XI: Diskusi Ide Inovasi IoT", "Mematangkan gagasan Smart School atau Smart Greenhouse melalui pitch dan umpan balik", kelas_xi)
