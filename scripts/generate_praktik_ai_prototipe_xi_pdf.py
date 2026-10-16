"""Generate the Class XI practical guide using the existing Teladan PDF style."""
from html import escape
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
    Preformatted,
)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'pdf/materi-kelas-xi-praktik-ai-rangkaian-code-dan-prototipe.pdf'
EXAMPLES = ROOT / 'examples/prototipe-ai-kelas-xi'
WIDTH = A4[0] - 3.4 * cm
S = getSampleStyleSheet()
S.add(ParagraphStyle(name='TitleT', fontName='Helvetica-Bold', fontSize=21,
                     leading=25, alignment=TA_CENTER, textColor=colors.HexColor('#16324F'), spaceAfter=10))
S.add(ParagraphStyle(name='SubT', fontName='Helvetica', fontSize=11, leading=15,
                     alignment=TA_CENTER, textColor=colors.HexColor('#355C7D'), spaceAfter=12))
S.add(ParagraphStyle(name='SectionT', fontName='Helvetica-Bold', fontSize=14,
                     leading=18, textColor=colors.white, backColor=colors.HexColor('#24577A'),
                     borderPadding=(6, 8, 6), spaceBefore=11, spaceAfter=10, keepWithNext=True))
S.add(ParagraphStyle(name='BodyT', fontName='Helvetica', fontSize=10.4, leading=14.5,
                     textColor=colors.HexColor('#1F2933'), spaceAfter=7))
S.add(ParagraphStyle(name='CallT', parent=S['BodyT'], fontName='Helvetica-Bold',
                     textColor=colors.HexColor('#16324F'), backColor=colors.HexColor('#EAF3F8'),
                     borderPadding=(6, 8, 6), spaceBefore=5, spaceAfter=11))
S.add(ParagraphStyle(name='CellT', parent=S['BodyT'], fontSize=9.1, leading=12, spaceAfter=0))
S.add(ParagraphStyle(name='HeadT', parent=S['CellT'], fontName='Helvetica-Bold', textColor=colors.white))
S.add(ParagraphStyle(name='CodeT', fontName='Courier', fontSize=8.5, leading=10.8,
                     textColor=colors.HexColor('#16324F'), backColor=colors.HexColor('#F1F7FA'),
                     borderPadding=6, spaceBefore=4, spaceAfter=9))
S.add(ParagraphStyle(name='PromptT', parent=S['BodyT'], fontSize=9.7, leading=13.4,
                     backColor=colors.HexColor('#F1F7FA'), borderPadding=7, spaceBefore=5, spaceAfter=10))
story = []


def p(t, style='BodyT'):
    story.append(Paragraph(t, S[style]))


def section(t):
    p(t, 'SectionT')


def page(t):
    if story:
        story.append(PageBreak())
    section(t)


def steps(items):
    for i, t in enumerate(items, 1):
        p(f'<b>{i}.</b> {t}')


def prompt(t):
    p(escape(t).replace('\n', '<br/>'), 'PromptT')


def table(rows, widths):
    data = [[Paragraph(c, S['HeadT'] if i == 0 else S['CellT'])
             for c in row] for i, row in enumerate(rows)]
    t = Table(data, colWidths=[WIDTH * w for w in widths], repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#24577A')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F1F7FA')]),
        ('GRID', (0, 0), (-1, -1), .5, colors.HexColor('#B7C5D1')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6), ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6), ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.extend([t, Spacer(1, 7)])


def code(name, compact=False):
    style = S['CodeT']
    if compact:
        style = ParagraphStyle(name='Compact', parent=style, fontSize=8, leading=9.7)
    story.append(Preformatted((EXAMPLES / name).read_text().rstrip(), style))


def link(label, url):
    return f'<link href="{escape(url, quote=True)}" color="#1D5F85"><u>{label}</u></link>'


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Helvetica', 8.5)
    canvas.setFillColor(colors.HexColor('#5B6770'))
    canvas.drawString(1.7 * cm, 1.05 * cm, 'SMA Teladan Yogyakarta - Unique Value Kelas XI')
    canvas.drawRightString(A4[0] - 1.7 * cm, 1.05 * cm, f'Halaman {doc.page}')
    canvas.restoreState()


story.append(Spacer(1, .35 * cm))
p('Praktik AI untuk Rangkaian, Code, dan Prototipe', 'TitleT')
p('Kelas XI - Melanjutkan daftar komponen dan RAB menjadi percobaan pertama', 'SubT')
p('Halo teman-teman. Kalian sudah menyusun ide, memilih komponen, dan membuat RAB. '
  'Hari ini kalian akan menggunakan AI untuk membantu menerjemahkan rencana tersebut menjadi '
  'rangkaian, program, atau prototipe dasar yang dapat dicoba. Pilih satu fungsi inti agar '
  'kelompok kalian punya hasil yang dapat ditunjukkan dan diperbaiki.', 'CallT')
section('1. Target sesi ini')
table([
    ['Jalur kelompok', 'Target minimum yang dapat ditunjukkan'],
    ['Arduino / ESP32', 'Input berubah, program membaca nilai, lalu LED atau Serial Monitor memberi respons.'],
    ['Line follower', 'Dua input sensor menghasilkan keputusan maju, kiri, kanan, atau berhenti. Motor menyusul setelah pemeriksaan.'],
    ['Software deteksi kantuk', 'Kamera lokal terbuka, wajah/mata terdeteksi, dan status berubah. Kesalahan deteksi dicatat.'],
], [.29, .71])
section('2. Persiapan kelompok')
steps([
    'Buka ide, diagram, daftar komponen, dan RAB terakhir. Tentukan bagian yang ingin kalian buktikan dahulu.',
    'Catat model lengkap board, sensor, driver, sumber daya, atau perangkat kamera. Sertakan foto label/pin bila tersedia.',
    'Gunakan laptop bersama untuk simulasi atau menjalankan kode. AI dapat dibuka lewat HP, tetapi unggah program dan Python lebih mudah lewat laptop.',
    'Bagi peran: operator, pemeriksa rangkaian/kode, pencatat uji, dan penjelas hasil. Satu orang boleh memegang dua peran.',
])
p('Alat belum tersedia? Tetap mulai. Gunakan Wokwi untuk Arduino/ESP32, tombol sebagai pengganti sensor, '
  'Serial Monitor sebagai pengganti motor, atau webcam sebagai pengganti CCTV.', 'CallT')

page('3. Cara bekerja dengan AI')
p('Gunakan ChatGPT, Gemini, atau asisten lain yang dapat kalian akses. Berikan spesifikasi yang benar. '
  'Minta bantuan satu tahap, jalankan hasilnya, lalu bawa kembali bukti percobaan ke AI.')
section('Prompt awal: ubah RAB menjadi rencana prototipe')
prompt('Kami siswa kelas XI SMA Teladan. Ide kami: [masalah dan solusi].\n'
       'Fungsi yang ingin kami buktikan hari ini: [satu fungsi].\n'
       'Komponen/perangkat dari RAB: [model lengkap, jumlah, tegangan, driver, power].\n'
       'Yang tersedia sekarang: [alat, laptop, simulator, kamera].\n'
       'Bantu kami bertahap. Jika spesifikasi belum jelas, tanyakan dahulu.\n'
       'Keluarkan: (1) alur input-proses-output, (2) asumsi dan hal yang perlu dicek, '
       '(3) tabel sambungan pin atau arsitektur software, (4) kode minimum dan dependensi, '
       '(5) langkah menjalankan, (6) tiga skenario uji.\n'
       'Untuk hardware, cek tegangan logika, ground, driver, dan daya. '
       'Gunakan LED/Serial dahulu untuk beban motor atau pompa. Jangan mengarang spesifikasi.')
section('Sesudah AI menjawab')
steps([
    'Minta AI menjelaskan fungsi setiap bagian. Kalian harus bisa menerangkan input, keputusan, dan outputnya.',
    'Cocokkan pin, tegangan, dan library dengan dokumentasi produsen. Nama board yang mirip belum tentu memiliki pin yang sama.',
    'Simpan kode versi pertama. Jalankan, lalu catat input, hasil harapan, hasil nyata, dan pesan error.',
    'Ubah satu hal setiap percobaan. Simpan versi perbaikan beserta alasan perubahannya.',
])
section('Prompt ketika terjadi error')
prompt('Target program: [...]. Board/OS dan versi library: [...].\n'
       'Kode yang digunakan: [tempel kode].\nPesan error lengkap atau output: [tempel teks].\n'
       'Hasil yang kami harapkan: [...]. Hasil nyata: [...].\n'
       'Jelaskan dugaan penyebab, cara memeriksa, lalu perubahan terkecil. '
       'Jangan mengganti semua kode tanpa alasan. Jelaskan baris yang berubah.')
p('Sebelum mengirim screenshot, tutupi password Wi-Fi, token API, alamat kamera, dan identitas pribadi.', 'CallT')

page('4. Jalur A: Arduino / ESP32')
p('Mulai dari input analog dan LED. Pada contoh ini potensiometer mewakili nilai sensor; '
  'hasilnya belum menjadi ukuran kelembapan atau jarak. Gunakan Arduino Uno di Wokwi atau alat nyata dengan pendampingan.')
table([
    ['Sambungan contoh Arduino Uno', 'Keterangan'],
    ['Potensiometer VCC ke 5V; GND ke GND; SIG ke A0', 'Untuk potensiometer 3 kaki nyata: kaki tengah ke A0, dua ujung ke 5V dan GND.'],
    ['D8 ke resistor 330 ohm ke anoda LED; katoda ke GND', 'Resistor membatasi arus. LED menjadi pengganti output pompa/motor pada tahap awal.'],
], [.56, .44])
p('<b>Langkah:</b> buka '+link('Wokwi','https://wokwi.com/')+', buat proyek Arduino Uno, '
  'tambahkan potentiometer, LED, dan resistor; sambungkan sesuai tabel. Tempel kode berikut, jalankan simulasi, '
  'lalu putar potensiometer sambil membaca Serial Monitor pada 115200 baud.')
code('sensor_led_uno.ino')
p('<b>Hasil harapan:</b> nilai di bawah 400 menyalakan LED, di atas 600 mematikannya. '
  'Di antara dua ambang, status sebelumnya tetap. Ini mengurangi output bolak-balik di dekat satu ambang.')
p('<b>Untuk ESP32:</b> minta AI menyesuaikan model board, pin ADC, pin LED, dan rentang nilai. '
  'Pada ESP32 klasik, GPIO34 dapat dipakai sebagai input ADC dan GPIO23 untuk LED; contoh pin ini '
  'tidak berlaku otomatis untuk ESP32-C3/S3. Gunakan logika 3,3V, verifikasi pinout, dan jangan masukkan sinyal 5V ke GPIO.', 'CallT')

page('5. Jalur B: robot line follower')
p('Pisahkan pengujian sensor, keputusan arah, dan driver motor. Contoh ini memakai dua tombol pada Uno '
  'untuk mewakili dua sensor digital. Tiap tombol menghubungkan D2 atau D3 ke GND ketika ditekan. '
  'INPUT_PULLUP membuat tombol yang ditekan terbaca LOW.')
table([
    ['Kiri', 'Kanan', 'Keputusan contoh'],
    ['1', '1', 'MAJU: kedua sensor berada di atas garis hitam yang cukup lebar.'],
    ['1', '0', 'KIRI: arahkan robot ke sisi kiri.'],
    ['0', '1', 'KANAN: arahkan robot ke sisi kanan.'],
    ['0', '0', 'STOP: garis hilang pada contoh ini.'],
], [.12, .12, .76])
p('Angka 1 berarti <b>garis terdeteksi</b>, bukan selalu tegangan HIGH. Aturan ini hanya contoh untuk '
  'susunan sensor dan lebar garis tersebut. Periksa pembacaan hitam/putih pada robot kalian; '
  'garis sempit atau susunan sensor lain dapat memerlukan aturan berbeda.')
code('line_follower_logika_uno.ino')
prompt('Logika sensor kami sudah sesuai hasil uji [lampirkan tabel]. Board: [...], driver motor: [...], '
       'pin IN/EN/STBY: [...], motor dan sumber daya: [...]. Bantu petakan MAJU/KIRI/KANAN/STOP '
       'ke fungsi motor sesuai datasheet driver. Jelaskan arah putaran, PWM, ground, dan kondisi stop. '
       'Mulai dengan roda terangkat dan kecepatan rendah. Jangan menghubungkan motor langsung ke GPIO.')
p('Sebelum motor bergerak, periksa driver, sumber daya, dan wiring bersama guru. '
  'Jika alat belum ada, hasil Serial empat keadaan sudah menjadi prototipe logika yang sah.', 'CallT')

page('6. Jalur C: software kamera untuk ide deteksi kantuk')
p('Mulai dari webcam laptop atau rekaman yang dibuat khusus dengan izin partisipan. '
  'Jalankan Python secara lokal. Sambungan CCTV/RTSP ditambahkan setelah alur dasar berjalan dan ada izin pemilik kamera.')
section('Target prototipe pertama')
table([
    ['Tahap', 'Yang kalian buktikan'],
    ['Input', 'Kamera memberi frame dan program berhenti dengan jelas jika frame gagal.'],
    ['Deteksi', 'Model bawaan OpenCV mencari wajah dan mata. Program contoh hanya menilai satu wajah.'],
    ['Status', 'Dua mata terdeteksi, mata kurang terdeteksi, atau kondisi tidak dapat dinilai.'],
    ['Waktu', 'Mata kurang terdeteksi selama 2 detik memunculkan permintaan pemeriksaan visibilitas. Ini ambang latihan.'],
], [.2, .8])
p('Mata tidak terdeteksi dapat terjadi karena gelap, kacamata, sudut kepala, atau kegagalan model. '
  '<b>Program awal ini belum mendeteksi kantuk secara andal.</b> Ia membantu kalian menguji kamera, '
  'model deteksi, timer, dan tampilan status sebelum mengembangkan indikator yang lebih baik.', 'CallT')
section('Persiapan dan menjalankan')
steps([
    'Pastikan Python 3 dan aplikasi terminal tersedia. Buat folder proyek, lalu lingkungan virtual dengan <font name="Courier">python -m venv .venv</font>. '
    'Aktifkan dengan <font name="Courier">.venv\\Scripts\\activate</font> (Windows) atau <font name="Courier">source .venv/bin/activate</font> (macOS/Linux). '
    'Jika perintah python tidak tersedia, coba python3.',
    'Pasang paket pada lingkungan tersebut: <font name="Courier">python -m pip install opencv-python</font>. '
    'Gunakan paket biasa, bukan headless, karena program menampilkan jendela.',
    'Salin kode halaman berikut ke <font name="Courier">kamera_indikator.py</font>. '
    'Jalankan <font name="Courier">python kamera_indikator.py</font>. Izinkan akses kamera dan tutup aplikasi kamera lain.',
    'Tekan q pada jendela kamera untuk keluar. Jika kamera tidak terbuka, cek izin dan coba indeks 1 pada VideoCapture hanya jika ada kamera lain.',
])
section('Prompt pengembangan setelah baseline berjalan')
prompt('Baseline OpenCV kami menampilkan status visibilitas mata. Jangan menyimpulkan kantuk hanya '
       'karena detector gagal. Bantu rancang tahap lanjut dengan landmark mata dan durasi penutupan, '
       'kalibrasi tiap orang, status tidak dapat dinilai, serta uji salah alarm. '
       'Jelaskan dependensi, model yang perlu diunduh, dan batasnya sebelum memberi kode tambahan.')

page('7. Kode awal kamera lokal')
p('Kode ini memakai model Haar cascade bawaan OpenCV. Ia tidak menyimpan foto/video dan tidak '
  'mengirim frame ke internet. Saat tidak ada atau ada beberapa wajah, timer direset dan status tidak dapat dinilai.')
code('kamera_indikator.py', compact=True)
p('Kedipan singkat, kepala menoleh, dan pencahayaan berbeda perlu dicoba. '
  'Keberhasilan kode berjalan belum membuktikan ketepatan deteksi kantuk.', 'CallT')

page('8. Uji prototipe dan perbaiki bersama AI')
table([
    ['Jalur', 'Skenario uji minimum', 'Hasil yang dicatat'],
    ['Sensor dan LED', 'Input rendah, tinggi, lalu di antara ambang. Ulangi saat nilai mendekati ambang.', 'Nilai input, status LED, dan apakah status berubah sesuai aturan.'],
    ['Line follower', 'Empat kombinasi input. Jika motor terpasang: arah tiap roda dan kondisi garis hilang.', 'Pembacaan asli sensor, keputusan arah, hasil motor, dan koreksi mapping.'],
    ['Kamera', 'Mata terbuka; kedip; mata ditutup singkat; kepala menoleh; tidak ada wajah; dua wajah.', 'Status, durasi, salah alarm, kondisi gagal deteksi, dan perbedaan pencahayaan.'],
], [.21, .43, .36])
section('Format catatan uji')
table([
    ['Kondisi/input', 'Hasil harapan', 'Hasil nyata', 'Keputusan'],
    ['Contoh: nilai ADC 300', 'LED aktif', 'Isi dari percobaan kalian', 'Pertahankan / perbaiki dan jelaskan'],
    ['Contoh: wajah keluar frame', 'Tidak dapat dinilai; timer reset', 'Isi dari percobaan kalian', 'Periksa alur kondisi jika berbeda'],
], [.24, .27, .25, .24])
section('Ketika hasil belum sesuai')
steps([
    'Periksa catu daya, board/port, ground, pin, baud rate, dan polaritas LED sebelum mengubah seluruh kode.',
    'Jika library gagal dipasang atau kamera tidak muncul, kirim pesan error lengkap ke AI beserta OS dan versi Python/IDE.',
    'Minta AI membuat tabel penyebab, cara cek, dan perbaikan terkecil. Ulangi satu skenario setelah perubahan.',
    'Catat bagian yang belum dapat diuji. Jangan mengubah hasil yang gagal menjadi klaim berhasil.',
])
p('Pada prototipe fisik, matikan daya sebelum mengubah kabel. Gunakan USB atau sumber DC tegangan rendah '
  'yang sesuai spesifikasi. Hindari listrik PLN pada praktik ini. Pompa, kipas, dan motor memerlukan '
  'driver serta suplai yang sesuai; simulasi belum membuktikan keamanan listrik rangkaian nyata.', 'CallT')
p('Pada proyek kamera, gunakan relawan yang setuju, tutupi identitas pada screenshot, dan hindari unggahan '
  'rekaman CCTV sekolah ke layanan AI publik. Prototipe ini untuk belajar, bukan alat penilaian atau penghukuman siswa.')

page('9. Tugas kelompok dan dokumentasi')
p('Lanjutkan ide serta RAB kalian. Pilih satu jalur yang paling sesuai dan tunjukkan versi minimum '
  'yang benar-benar kalian coba pada sesi ini. Kalian boleh mengumpulkan hasil simulasi, '
  'pengujian logika, atau software lokal jika alat belum tersedia.')
table([
    ['Bagian hasil', 'Yang perlu kalian lampirkan'],
    ['Ide dan ruang lingkup', 'Masalah, fungsi inti sesi ini, serta hubungan dengan RAB terakhir.'],
    ['Rangkaian / arsitektur', 'Hardware: diagram dan tabel pin/daya. Software: alur kamera, deteksi, aturan, dan output.'],
    ['Kode', 'File .ino atau .py yang dipakai, dependensi, dan langkah menjalankan. Jelaskan tiga bagian penting kode.'],
    ['Bukti praktik', 'Minimal dua screenshot berbeda: susunan/wiring atau kode; serta hasil simulasi/Serial/tampilan kamera. Samarkan identitas dan rahasia.'],
    ['Catatan uji', 'Minimal tiga skenario dengan hasil nyata. Line follower juga mencakup empat kombinasi input.'],
    ['Jejak bantuan AI', 'Prompt utama, satu saran AI yang diperiksa/dikoreksi, serta perubahan kode yang dibuat kelompok.'],
    ['Rencana berikutnya', 'Kendala, perbaikan, pembagian peran, dan revisi komponen/RAB jika diperlukan.'],
], [.25, .75])
p('Kumpulkan satu PDF ringkas beserta file kode atau tautan proyek simulasi yang dapat dibuka. '
  'Penilaian berfokus pada kesesuaian dengan ide, pemahaman kode/rangkaian, bukti uji, '
  'perbaikan, dan kejujuran. Prototipe yang belum sempurna tetap bernilai jika hasilnya terdokumentasi.', 'CallT')
p('Kirim ke '+link('ataka.ahmad@gmail.com','mailto:ataka.ahmad@gmail.com')+'.<br/>'
  '<b>Subject:</b> SMA Teladan XI - Prototipe Dasar Berbantuan AI - [Nama Kelompok]<br/>'
  'Sertakan semua nama anggota dan jelaskan apakah hasil memakai simulasi atau alat nyata.')
section('Referensi teknis yang dapat kalian cek')
p(link('Wokwi: simulator dan dukungan perangkat','https://docs.wokwi.com/getting-started/supported-hardware')+'<br/>'
  +link('Arduino: membaca input analog','https://docs.arduino.cc/built-in-examples/basics/AnalogReadSerial/')+'<br/>'
  +link('Espressif: panduan desain hardware','https://docs.espressif.com/projects/esp-faq/en/latest/hardware-related/hardware-design.html')+'<br/>'
  +link('OpenCV: kamera dan video','https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html')+'<br/>'
  +link('OpenCV: deteksi wajah dan mata dengan cascade','https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html'))

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, leftMargin=1.7 * cm,
                        rightMargin=1.7 * cm, topMargin=1.45 * cm,
                        bottomMargin=1.65 * cm,
                        title='Praktik AI untuk Rangkaian, Code, dan Prototipe - Kelas XI',
                        author='SMA Teladan Yogyakarta')
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUTPUT)
