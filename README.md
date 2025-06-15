# Flask Denemesi Projesi

Bu proje, temel Flask özelliklerini kullanarak basit web sayfaları oluşturmayı ve kullanıcıdan veri alıp işlemeyi gösteren bir örnek uygulamadır.

## Proje Özellikleri

* Ana sayfa (`/`): Basit bir HTML metni gösterir.
* `/hello` ve `/hello-admin`: Farklı HTML şablonlarını render eder.
* `/hello-user/<name>`: URL'den aldığı kullanıcı adına göre sayfa gösterir; admin ise özel sayfaya yönlendirir.
* `/add/<number1>/<number2>`: İki sayıyı toplar ve sonucu bir HTML sayfasında gösterir.
* `/login`: Kullanıcı adı ile giriş formu sunar, POST işlemi ile kullanıcıyı `/hello-user/<name>` sayfasına yönlendirir.
* `/student` ve `/result`: Öğrenci notlarının girildiği form ve sonuçların gösterildiği sayfa.

## Kullanılan Teknolojiler

* Python 
* Flask Framework
* HTML 

## Kurulum ve Çalıştırma

1. **Sanal ortam oluştur (isteğe bağlı ama önerilir):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

2. **Gerekli paketleri yükle:**

   ```bash
   pip install flask
   ```

3. **Uygulamayı çalıştır:**

   ```bash
   python app.py
   ```

4. Tarayıcıda aşağıdaki adresleri ziyaret edebilirsin:

   * `http://127.0.0.1:5000/` — Ana sayfa
   * `http://127.0.0.1:5000/hello` — Hello sayfası
   * `http://127.0.0.1:5000/hello-admin` — Admin sayfası
   * `http://127.0.0.1:5000/hello-user/<name>` — Kullanıcı sayfası (örnek: `/hello-user/ali`)
   * `http://127.0.0.1:5000/add/5/7` — İki sayının toplamı (örnek: 5+7)
   * `http://127.0.0.1:5000/login` — Giriş formu
   * `http://127.0.0.1:5000/student` — Öğrenci not formu
   * `/result` — Öğrenci notlarının sonucu (form POST ile gönderilir)

## Şablon Dosyaları (Templates)

`templates` klasöründe aşağıdaki HTML dosyaları yer almalıdır:

* `hello.html`
* `hello-admin.html`
* `hello-user.html`
* `add.html`
* `login.html`
* `student.html`
* `student_result.html`


## Kısa Açıklama

* `render_template` fonksiyonu HTML dosyalarını kullanıcıya sunar.
* `redirect` ve `url_for` fonksiyonları sayfa yönlendirmeleri için kullanılır.
* Formlardan veri alma `request.form` ile yapılır.
* URL parametreleri rota fonksiyonlarında parametre olarak alınır.

