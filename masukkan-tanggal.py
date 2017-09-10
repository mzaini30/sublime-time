import sublime, sublime_plugin, time, re
class InsertDatetimeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel();
        waktu = time.ctime();

        waktu = re.sub(r"Mon", r"Senin", waktu);
        waktu = re.sub(r"Tue", r"Selasa", waktu);
        waktu = re.sub(r"Wed", r"Rabu", waktu);
        waktu = re.sub(r"Thu", r"Kamis", waktu);
        waktu = re.sub(r"Fri", r"Jumat", waktu);
        waktu = re.sub(r"Sat", r"Sabtu", waktu);
        waktu = re.sub(r"Sun", r"Minggu", waktu);

        waktu = re.sub(r"Jan", r"Januari", waktu);
        waktu = re.sub(r"Feb", r"Februari", waktu);
        waktu = re.sub(r"Mar", r"Maret", waktu);
        waktu = re.sub(r"Apr", r"April", waktu);
        waktu = re.sub(r"May", r"Mai", waktu);
        waktu = re.sub(r"Jun", r"Juni", waktu);
        waktu = re.sub(r"Jul", r"Juli", waktu);
        waktu = re.sub(r"Aug", r"Agustus", waktu);
        waktu = re.sub(r"Sep", r"September", waktu);
        waktu = re.sub(r"Oct", r"Oktober", waktu);
        waktu = re.sub(r"Nov", r"November", waktu);
        waktu = re.sub(r"Des", r"Desember", waktu);

        waktu = waktu.split();
        waktu = ""+waktu[0]+", "+waktu[2]+" "+waktu[1]+" "+waktu[4]+" pukul "+waktu[3]+"";

        for s in sel:
            self.view.replace(edit, s, waktu)