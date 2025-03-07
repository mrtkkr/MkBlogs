# MkBlogs

MkBlogs, kullanıcıların hesap oluşturabileceği, makaleler yazabileceği, resimler yükleyebileceği ve yazılara yorum yapıp cevap verebileceği Django tabanlı bir blog platformudur. Ayrıca kullanıcı kimlik doğrulama, şifre sıfırlama ve iletişim için bir iletişim sayfası içerir.

## Özellikler

- **Kullanıcı Kimlik Doğrulama:** Kullanıcılar kaydolabilir, giriş yapabilir ve şifrelerini sıfırlayabilir.
- **Makaleler Oluşturma:** Kullanıcılar istedikleri konularda makaleler yazıp yayınlayabilirler.
- **Resim Yükleme:** Kullanıcılar yazılarına resim yükleyebilirler.
- **Yorum Sistemi:** Kullanıcılar yazılara yorum yapabilir ve yorumlara cevap verebilirler.
- **İletişim Sayfası:** Kullanıcılar admin ile iletişim kurmak için bir iletişim formu kullanabilirler.

## Kurulum

### Gereksinimler
- Python 3.x
- Django
- SQLite (ya da tercih ettiğiniz başka bir veritabanı sistemi)

### Adımlar

1. **Repository'yi klonlayın:**

   ```bash
   git clone https://github.com/mrtkkr/MkBlogs.git
   cd MkBlogs

2. **Bağımlılıkları yükleyin:**
    pip install -r requirements.txt

2. **Veritabanı migrasyonlarını yapın:**
    python manage.py migrate

2. **Bir süper kullanıcı oluşturun (isteğe bağlı, admin erişimi için):**
    python manage.py createsuperuser

2. **Geliştirme sunucusunu başlatın:**
    python manage.py runserver

Uygulama şu adres üzerinden erişilebilir: http://127.0.0.1:8000/.
Böylece adım adım kurulumunuzu açıklayan kısmı tamamlamış olursunuz.

## Kullanım

### Kullanıcı Kaydı ve Giriş
- Yeni bir hesap oluşturmak için kayıt sayfasına gidin.
- Kayıt olduktan sonra giriş yaparak hesabınıza erişebilirsiniz.

### Makale Oluşturma
- Giriş yaptıktan sonra, makale oluşturma sayfasına giderek yazınızı yazabilirsiniz.
- Yazınıza resim eklemek için resim yükleme alanını kullanabilirsiniz.

### Makale ile Etkileşim
- Yazılara yorum yapabilirsiniz.
- Diğer kullanıcıların yorumlarına cevap verebilirsiniz.

### İletişim Sayfası
- Admin ile iletişim kurmak için iletişim formunu kullanabilirsiniz.


## Lisans
- Bu proje MIT Lisansı altında lisanslanmıştır.


