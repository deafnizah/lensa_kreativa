from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 's3cr3t_k3y'  # Gunakan key yang aman untuk produksi

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pesan', methods=['GET', 'POST'])
def pesan():
    if request.method == 'POST':
        # Menangkap data form pemesanan
        nama = request.form['nama']
        tanggal = request.form['tanggal']
        paket = request.form['paket']
        sesi = request.form['sesi']
        
        # Menyimpan data di session untuk konfirmasi
        session['nama'] = nama
        session['tanggal'] = tanggal
        session['paket'] = paket
        session['sesi'] = sesi
        
        return redirect(url_for('confirm'))
    
    # Jika method GET, tampilkan halaman form pemesanan
    return render_template('pesan.html')

@app.route('/confirm')
def confirm():
    # Mengambil data dari session untuk ditampilkan di halaman konfirmasi
    if 'nama' not in session:
        return redirect(url_for('pesan'))  # Jika session kosong, kembali ke form pemesanan
    
    return render_template('confirm.html', 
                           nama=session['nama'],
                           tanggal=session['tanggal'],
                           paket=session['paket'],
                           sesi=session['sesi'])

if __name__ == '__main__':
    app.run(debug=True)
