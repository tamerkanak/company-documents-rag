# Şirket Bilgi Asistanı

Şirket içi PDF dokümanlarınızı yükleyin, anında ve kaynaklı yanıtlar alın! Bu uygulama, şirketlerin kendi belgeleri üzerinden güvenilir ve hızlı bilgiye ulaşmasını sağlar. RAG (Retrieval-Augmented Generation) mimarisiyle çalışır ve OpenRouter üzerinden Mistral LLM kullanır.

## Özellikler
- PDF dosyalarını yükleyip paragraf bazlı vektör veritabanı oluşturma
- Belgelerden arama ve LLM ile doğal dilde yanıt üretme
- Yanıtların sadece kullanılan kaynaklarla birlikte gösterilmesi
- Modern, kullanıcı dostu ve responsive web arayüzü (Flask tabanlı)
- Dark/Light mode geçişi
- Yükleme ve yanıt işlemlerinde canlı durum göstergeleri
- API anahtarı .env dosyasından otomatik alınır (güvenli kullanım)
- Şirket belgelerine özel, kurumsal odaklı çözüm

## Klasör Yapısı (Modüler)
```
rag/
  app.py            # Ana uygulama (Flask web arayüzü)
  pdf_utils.py       # PDF okuma ve paragraf çıkarma
  vector_db.py       # Vektör veritabanı işlemleri
  llm_utils.py       # LLM API çağrısı
  requirements.txt   # Gerekli Python paketleri
  templates/
    index.html       # Web arayüzü şablonu
  README.md          # Bu dosya
```

## Kullanılan Teknolojiler
- Flask (web arayüzü)
- chromadb (vektör veritabanı)
- sentence-transformers (embedding)
- pdfplumber (PDF okuma)
- requests (API çağrısı)
- python-dotenv (.env yönetimi)
- OpenRouter (LLM: mistralai/mistral-7b-instruct-v0.2)

## Kurulum

1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

2. Proje klasörüne bir `.env` dosyası oluşturun ve OpenRouter API anahtarınızı ekleyin:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

3. Uygulamayı başlatın:
   ```bash
   python app.py
   ```

4. Tarayıcınızda `http://localhost:5000` adresine gidin.
5. PDF dosyalarınızı yükleyin ve sorunuzu yazıp gönderin.

## Notlar
- PDF verisi sunucu tarafında kalır, dışa aktarılmaz.
- OpenRouter API anahtarınızı [openrouter.ai](https://openrouter.ai/) üzerinden alabilirsiniz.
- Yanıtlar yalnızca yüklenen belgelerdeki bilgilerle sınırlıdır.
- Dark/Light mode ve modern arayüz ile şirket içi bilgiye hızlı erişim sağlar.

---
Geliştirici: [Tamer Kanak](https://www.linkedin.com/in/tamerkanak)  