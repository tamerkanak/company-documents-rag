# Şirket Belgeleri RAG Asistanı

Şirket içi PDF dokümanlarınızı yükleyin, anında ve kaynaklı yanıtlar alın! Bu uygulama, şirketlerin kendi belgeleri üzerinden güvenilir ve hızlı bilgiye ulaşmasını sağlar. RAG (Retrieval-Augmented Generation) mimarisiyle çalışır ve OpenRouter üzerinden Mistral LLM kullanır.

## Özellikler
- PDF dosyalarını yükleyip paragraf bazlı vektör veritabanı oluşturma
- Belgelerden arama ve LLM ile doğal dilde yanıt üretme
- Yanıtların sadece kullanılan kaynaklarla birlikte gösterilmesi
- Kullanıcı dostu, sade ve modern arayüz
- API anahtarı .env dosyasından otomatik alınır (güvenli kullanım)
- Şirket belgelerine özel, kurumsal odaklı çözüm

## Klasör Yapısı (Modüler)
```
rag/
  app.py            # Ana uygulama (Streamlit arayüzü)
  pdf_utils.py       # PDF okuma ve paragraf çıkarma
  vector_db.py       # Vektör veritabanı işlemleri
  llm_utils.py       # LLM API çağrısı
  ui_utils.py        # Footer ve görsel yardımcılar
  requirements.txt   # Gerekli Python paketleri
  README.md          # Bu dosya
```

## Kullanılan Teknolojiler
- Streamlit (arayüz)
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
   streamlit run app.py
   ```

4. Sol panelden PDF dosyalarınızı yükleyin ve sorunuzu yazıp gönderin.

## Notlar
- PDF verisi sunucu tarafında kalır, dışa aktarılmaz.
- OpenRouter API anahtarınızı [openrouter.ai](https://openrouter.ai/) üzerinden alabilirsiniz.
- Yanıtlar yalnızca yüklenen belgelerdeki bilgilerle sınırlıdır.
- Geliştirici: [Tamer Kanak](https://www.linkedin.com/in/tamerkanak)  