import fs from 'node:fs/promises';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import { Presentation, PresentationFile } from '@oai/artifact-tool';

const ROOT = '/Users/ahmadataka/Documents/Codex project/SMA Teladan/unique-value-teladan';
const SKILL = '/Users/ahmadataka/.codex/plugins/cache/openai-primary-runtime/presentations/26.1013.11914/skills/presentations';
const BUILD = path.join(ROOT, 'tmp/opsi-fiksi-x');
const FINAL = path.join(ROOT, 'presentations/materi-kelas-x-opsi-fiksi-dan-pematangan-proposal.pptx');
const PYTHON = '/Users/ahmadataka/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3';
process.env.RUNTIME_NODE_MODULES ??= '/Users/ahmadataka/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
const C = { navy:'#16324F', blue:'#24577A', sky:'#EAF3F8', ink:'#1F2933', muted:'#5B6770', line:'#C8D6E2', white:'#FFFFFF' };
const OPSI = 'https://repositori.kemendikdasmen.go.id/36363/';
const FIKSI = 'https://pusatprestasinasional.kemendikdasmen.go.id/event/riset-dan-inovasi/sma/festival-inovasi-dan-kewirausahaan-siswa-nasional-2026-2026-sma';
const D = '/Users/ahmadataka/Downloads/';
const sources = {
  outline:D+'Outline_Pematangan_Ide_OPSI_dan_FIKSI_2026.docx',
  opsi:D+'Panduan Menulis Proposal OPSI.pdf',
  fiksi:D+'Slide Sosialisasi FIKSI SMA_MA_SMK_MAK_Sederajat 2026.pdf',
  shi:D+'Contoh Ringkasan Eksekutif FIKSI_SHI Team_2025.pdf',
  previous:path.join(ROOT,'pdf/materi-kelas-x-proposal-mini-riset-dan-inovasi.pdf'),
};
const logo = await fs.readFile('/Users/ahmadataka/Documents/Codex project/SMA Teladan/academic-track-teladan/assets/logo-sma-teladan-yogyakarta.png');
const deck = Presentation.create({slideSize:{width:1280,height:720}});
const links=[];

function text(s,t,x,y,w,h,size=25,bold=false,color=C.ink,name) {
  const a=s.shapes.add({name,geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
  a.text=t;
  a.text.style={fontFace:'Aptos',fontSize:size,bold,color,alignment:'left'};
  return a;
}
function rect(s,x,y,w,h,fill) {
  s.shapes.add({geometry:'rect',position:{left:x,top:y,width:w,height:h},fill,line:{fill:'none',width:0}});
}
function base(title,refs=[]) {
  const s=deck.slides.add(); s.background.fill=C.white;
  s.images.add({blob:logo,contentType:'image/png',alt:'Logo SMA Teladan Yogyakarta',fit:'contain',position:{left:1098,top:18,width:86,height:52}});
  rect(s,76,78,1128,58,C.blue);
  text(s,title,94,88,1078,42,30,true,C.white);
  rect(s,76,674,1128,1.2,C.line);
  text(s,'SMA Teladan Yogyakarta · Unique Value Kelas X',78,680,740,22,12,false,C.muted);
  text(s,String(deck.slides.items.length),1155,680,40,22,12,false,C.muted);
  s.speakerNotes.textFrame.setText(['Sumber:',...refs]);
  return s;
}
function lines(s,items,x=96,y=184,w=1080,size=26,gap=91) {
  items.forEach((item,i)=>text(s,item,x,y+i*gap,w,gap-13,size));
}
function note(s,t) {
  rect(s,96,579,1080,66,C.sky);
  text(s,t,112,591,1048,48,21,true,C.navy);
}
function pair(s,left,right) {
  text(s,left[0],96,175,500,44,29,true,C.navy);
  text(s,right[0],682,175,500,44,29,true,C.navy);
  lines(s,left.slice(1),96,241,490,24,87);
  lines(s,right.slice(1),682,241,490,24,87);
}
function link(s,label,url,x,y,w=1060) {
  const name='LINK_'+links.length;
  text(s,label,x,y,w,40,22,true,C.blue,name);
  links.push({slide:deck.slides.items.length,name,url});
}

{
  const s=base('OPSI dan FIKSI',[sources.previous,sources.outline,OPSI,FIKSI]);
  text(s,'Proposal kalian\nsiap dikembangkan',96,204,1080,146,52,true,C.navy);
  text(s,'Penelitian yang menjawab pertanyaan\nInovasi yang memberi manfaat dan memiliki peluang usaha',98,395,1070,100,29);
  note(s,'Hari ini kita mempertajam ide dari tugas Proposal Mini Riset dan Inovasi.');
}
{
  const s=base('Proposal terakhir sebagai titik awal',[sources.previous]);
  lines(s,[
    'Buka kembali judul, masalah, bukti awal, dan pilihan jalur kelompok kalian.',
    'Bagian mana yang masih berupa dugaan? Tandai klaim yang perlu bukti.',
    'Apa masukan yang sudah diterima? Catat perubahan yang akan dibuat.',
    'Kalian akan menyusun proposal versi 2 dari ide yang sama.'
  ]);
  note(s,'Perubahan arah boleh dilakukan jika kalian menjelaskan bukti atau alasannya.');
}
{
  const s=base('Penelitian dan kewirausahaan',[OPSI,FIKSI,sources.fiksi]);
  pair(s,['OPSI','Olimpiade Penelitian Siswa Indonesia','Pertanyaan utama: apa yang ingin kita ketahui atau buktikan?','Bukti: data, metode, analisis, dan keterbatasan.'],
    ['FIKSI','Festival Inovasi dan Kewirausahaan Siswa','Pertanyaan utama: siapa membutuhkan solusi ini dan bagaimana usahanya berjalan?','Bukti: kebutuhan pelanggan, prototype, biaya, dan model usaha.']);
  note(s,'Alat teknologi bisa menjadi penelitian OPSI maupun produk FIKSI. Fokus buktinya berbeda.');
}
{
  const s=base('OPSI: ide yang dapat diteliti',[OPSI,sources.outline]);
  lines(s,['Kalian dapat mengkaji fenomena alam, perilaku sosial, atau sistem teknologi.',
    'Pertanyaan harus cukup spesifik untuk dijawab dengan data.',
    'Metode menjelaskan siapa atau apa yang diamati, caranya, dan analisisnya.',
    'Hasil penelitian boleh berbeda dari dugaan awal. Laporkan dengan jujur.']);
  note(s,'Untuk penelitian rekayasa, keberhasilan alat perlu ukuran dan pembanding yang jelas.');
}
{
  const s=base('Contoh OPSI: rekomendasi video',[sources.previous,sources.outline]);
  text(s,'Hubungan rekomendasi video dengan\nkeberagaman sumber belajar siswa',96,176,1070,93,34,true,C.navy);
  lines(s,['Pertanyaan: apakah penggunaan rekomendasi berkaitan dengan jumlah jenis sumber belajar?',
    'Data: diary sukarela, kategori sumber, dan wawancara tanpa membuka akun pribadi.',
    'Analisis: bandingkan pola dan jelaskan faktor lain yang mungkin berpengaruh.'],96,303,1070,25,84);
  note(s,'Contoh ide kelas. Hubungan antarvariabel belum membuktikan sebab dan akibat.');
}
{
  const s=base('Metode yang cukup jelas untuk dilakukan',[sources.opsi,sources.outline]);
  lines(s,['Objek atau partisipan: siapa atau apa yang akan kalian amati?',
    'Instrumen: tabel observasi, kuesioner, wawancara, atau alat ukur.',
    'Prosedur: langkah kerja, kondisi pembanding, dan cara mencatat data.',
    'Analisis: cara menjawab pertanyaan menggunakan data yang terkumpul.']);
  note(s,'Tuliskan keterbatasan. Jangan memakai kata “pengaruh” jika desain hanya mengamati hubungan.');
}
{
  const s=base('FIKSI: inovasi yang memiliki peluang usaha',[sources.fiksi,FIKSI]);
  lines(s,['Solusi dapat berupa produk atau jasa dengan calon pelanggan yang jelas.',
    'Nilai tambah menjelaskan alasan pelanggan memilih solusi kalian.',
    'Validasi pasar membantu memeriksa kebutuhan dan minat calon pengguna.',
    'Model usaha menjelaskan biaya, harga, pendapatan, dan cara menjangkau pelanggan.']);
  note(s,'Untuk ide awal, jalur latihan yang paling dekat adalah perencanaan usaha.');
}
{
  const s=base('Gambaran luaran FIKSI',[sources.fiksi+' halaman 6',FIKSI]);
  s.images.add({blob:await fs.readFile(path.join(ROOT,'assets/opsi-fiksi/fiksi-luaran.png')),contentType:'image/png',alt:'Materi resmi FIKSI 2026 tentang perencanaan dan pengembangan usaha',fit:'contain',position:{left:96,top:162,width:1080,height:375}});
  note(s,'Sosialisasi 2026: prototype dan rencana bisnis menjadi bagian pengembangan gagasan usaha.');
}
{
  const s=base('Contoh FIKSI: SHI Apps',[sources.shi+' halaman 1–7']);
  text(s,'Layanan belajar riset\nuntuk pelajar',96,190,575,95,34,true,C.navy);
  lines(s,['Sumber contoh: ringkasan eksekutif SHI Team 2025.',
    'Masalah pengguna: kebutuhan pelatihan dan pendampingan karya ilmiah.',
    'Solusi: kelas serta layanan pendampingan melalui platform digital.'],96,313,575,24,82);
  s.images.add({blob:await fs.readFile(path.join(ROOT,'assets/opsi-fiksi/shi-contoh.png')),contentType:'image/png',alt:'Program layanan SHI Apps pada contoh ringkasan eksekutif SHI Team',fit:'contain',position:{left:714,top:160,width:470,height:410}});
  link(s,'Website SHI Apps','https://sciencehunter.id/',96,575,500);
  link(s,'Video produk / jasa SHI','https://youtu.be/wxOXiv3dolU',714,575,470);
}
{
  const s=base('Nilai tambah dan biaya awal',[sources.fiksi,sources.outline]);
  pair(s,['Nilai tambah','Siapa calon pelanggan dan siapa pengguna? Keduanya bisa berbeda.','Cara apa yang mereka gunakan sekarang?','Apa kelebihan yang dapat kalian buktikan?'],
    ['Biaya awal','Bahan, kemasan, tenaga, dan biaya operasional harus tercatat.','HPP per unit = biaya produksi untuk satu unit.','Harga jual dikurangi HPP masih perlu menutup biaya lain.']);
  note(s,'Bedakan harga perkiraan dan harga dari sumber. Klaim “murah” perlu pembanding.');
}
{
  const s=base('Contoh hitungan usaha sederhana',[sources.outline,'Angka pada slide ini adalah simulasi pembelajaran.']);
  text(s,'Simulasi kit kartu belajar',96,181,1080,50,34,true,C.navy);
  lines(s,['Biaya produksi 10 kit: Rp200.000. HPP: Rp20.000 per kit.',
    'Harga rencana: Rp30.000 per kit. Selisih dengan HPP: Rp10.000 per kit.',
    'Selisih tersebut belum memperhitungkan promosi, transportasi, dan biaya lain.',
    'Minat beli perlu diperiksa melalui wawancara. Penjualan belum terbukti.'],96,270,1080,26,74);
  note(s,'Ini contoh angka latihan, bukan hasil penjualan atau rekomendasi harga.');
}
{
  const s=base('Sumber pembanding dan kebaruan',[sources.outline,sources.opsi]);
  lines(s,['Cari sedikitnya tiga penelitian, produk, atau layanan yang dekat dengan ide kalian.',
    'Catat masalah, cara kerja atau metode, kelebihan, serta keterbatasannya.',
    'Tunjukkan bagian yang kalian ubah: konteks, cara, bahan, pengguna, atau fitur.',
    'Jelaskan mengapa perubahan itu penting dan bagaimana kalian akan mengujinya.']);
  note(s,'Hindari klaim “pertama di dunia” sebelum melakukan penelusuran yang memadai.');
}
{
  const s=base('Bukti awal dan validasi',[sources.previous,sources.fiksi]);
  pair(s,['Jalur penelitian','Lakukan pengamatan awal atau uji kecil untuk memeriksa kelayakan metode.','Contoh: uji tabel diary pada dua siswa yang bersedia.','Catat bagian instrumen yang membingungkan.'],
    ['Jalur usaha','Wawancarai calon pengguna dan periksa masalah serta solusi saat ini.','Contoh: minta tiga calon pengguna menanggapi sketsa kit belajar.','Catat masukan yang mengubah desain atau harga.']);
  note(s,'Uji kecil adalah bukti awal. Sampel kecil belum mewakili seluruh siswa atau pasar.');
}
{
  const s=base('Etika penelitian dan penggunaan AI',[sources.previous,sources.opsi,OPSI]);
  lines(s,['Minta persetujuan. Gunakan kode partisipan dan data minimum yang diperlukan.',
    'Simpan catatan asli. Data, wawancara, dan transaksi harus benar-benar terjadi.',
    'AI boleh membantu menyusun pertanyaan atau merapikan tulisan. Periksa sumber dan isinya.',
    'Tulis kontribusi tiap anggota serta bantuan AI. Beri sumber untuk kutipan dan gambar.']);
  note(s,'Kegiatan berisiko dan eksperimen yang melibatkan manusia perlu persetujuan guru.');
}
{
  const s=base('Umpan balik untuk proposal kalian',[sources.previous]);
  lines(s,['Sampaikan ide kelompok secara singkat: masalah, jalur, dan bukti yang masih kurang.',
    'Kelompok lain memberi satu pertanyaan tentang metode atau calon pelanggan.',
    'Catat satu masukan yang paling membantu dan alasan kalian menerimanya.',
    'Gunakan catatan itu untuk memperbaiki proposal versi 2.']);
  note(s,'Pertanyaan diskusi: bukti apa yang bisa membuat kelompok mengubah kesimpulan atau desain?');
}
{
  const s=base('Tugas lanjutan: Proposal Versi 2',[sources.previous,sources.outline]);
  lines(s,['Lanjutkan proposal mini dari pertemuan terakhir dengan judul atau ide yang sama.',
    'Perjelas masalah dan pilih jalur penelitian OPSI atau rencana usaha FIKSI.',
    'Tambahkan tabel tiga sumber pembanding dan penjelasan kontribusi ide kalian.',
    'Sertakan minimal satu bukti awal yang benar-benar kalian kumpulkan.']);
  note(s,'Jika jalur berubah, jelaskan alasan dan bukti yang mendasarinya.');
}
{
  const s=base('Bagian tambahan sesuai pilihan jalur',[sources.outline,sources.fiksi,sources.opsi]);
  pair(s,['Penelitian / OPSI','Rumusan masalah, tujuan, objek atau variabel, dan rencana metode.','Contoh instrumen serta rencana analisis data.','Keterbatasan dan langkah menjaga etika.'],
    ['Rencana usaha / FIKSI','Pengguna, calon pelanggan, nilai tambah, dan sketsa prototype.','Ringkasan wawancara serta biaya, HPP, dan harga perkiraan.','Cara menjangkau pelanggan dan rencana validasi berikutnya.']);
  note(s,'Latihan kelas ini menyiapkan bahan awal. Format pendaftaran mengikuti pedoman ajang.');
}
{
  const s=base('Hasil yang dikumpulkan',[sources.previous]);
  lines(s,['PDF 4–6 halaman atau presentasi 6–8 slide, dengan nama seluruh anggota.',
    'Lampiran: tabel sumber, bukti awal, sketsa atau instrumen, dan pembagian peran.',
    'Tabel revisi: bagian lama, masukan atau temuan, serta perubahan pada versi 2.',
    'Rencana langkah berikutnya: kegiatan, penanggung jawab, kebutuhan, dan target.']);
  note(s,'Penilaian: ketajaman masalah, bukti, mutu metode atau usaha, kelayakan, dan kejujuran.');
}
{
  const s=base('Pengumpulan tugas',[sources.previous]);
  text(s,'Proposal kalian berkembang\nmelalui bukti dan masukan',96,194,1070,116,41,true,C.navy);
  link(s,'Kirim ke ataka.ahmad@gmail.com','mailto:ataka.ahmad@gmail.com',96,363);
  text(s,'Subject email:\nSMA Teladan X - Proposal Versi 2 OPSI FIKSI - [Nama Kelompok]',96,435,1060,95,25,true,C.navy);
  note(s,'Sertakan file hasil, lampiran, pilihan jalur, dan nama seluruh anggota kelompok.');
}
{
  const s=base('Pedoman dan bahan pendamping',[OPSI,FIKSI,sources.outline,sources.opsi]);
  link(s,'Panduan resmi OPSI 2026',OPSI,96,190);
  text(s,'Gunakan untuk memahami arah penelitian dan format ajang.',96,238,1080,50,24);
  link(s,'Informasi resmi dan panduan FIKSI 2026',FIKSI,96,328);
  text(s,'Gunakan untuk memahami kategori usaha, luaran, dan penilaian.',96,376,1080,50,24);
  text(s,'Bahan belajar: outline pematangan ide dan panduan menulis proposal\nyang sudah tersedia dalam materi SMA Teladan.',96,473,1080,80,24);
  note(s,'Pedoman 2026 adalah referensi belajar. Periksa aturan tahun ajang yang akan diikuti.');
}

await fs.mkdir(BUILD,{recursive:true});
for (const [i,s] of deck.slides.items.entries()) {
  const png=await deck.export({slide:s,format:'png',scale:1});
  await fs.writeFile(path.join(BUILD,`slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await png.arrayBuffer()));
}
await (await PresentationFile.exportPptx(deck)).save(path.join(BUILD,'candidate.pptx'));
await fs.writeFile(path.join(BUILD,'links.json'),JSON.stringify(links,null,2));
// Export retains editable text. Add standard OOXML hyperlinks to labelled shapes.
const {execFileSync}=await import('node:child_process');
execFileSync(PYTHON,[path.join(ROOT,'scripts/add_opsi_fiksi_links.py'),path.join(BUILD,'candidate.pptx'),path.join(BUILD,'links.json')]);
const {finalizePresentation}=await import(pathToFileURL(path.join(SKILL,'container_tools/artifact_tool_utils.mjs')).href);
const result=await finalizePresentation({workspaceDir:ROOT,candidatePath:path.join(BUILD,'candidate.pptx'),finalPath:FINAL,
  pythonExecutable:PYTHON,integrityValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_package_integrity.py'),
  layoutValidatorPath:path.join(SKILL,'container_tools/inspect_presentation_layout_geometry.py'),
  layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit'],
  fontPolicy:{basis:'design',families:['Aptos']},verifyArtifactToolImport:true,
  receiptPath:path.join(BUILD,'validation.json')});
console.log(JSON.stringify({final:FINAL,slides:deck.slides.items.length,result}));
