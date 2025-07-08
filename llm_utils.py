import requests

def ask_llm(context: str, question: str, api_key: str, timeout=30) -> str:
    OPENROUTER_API_URL = 'https://openrouter.ai/api/v1/chat/completions'
    OPENROUTER_MODEL = 'mistralai/mistral-7b-instruct-v0.2'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    prompt = f"""
Sen bir belge analiz asistanısın. Görevin SADECE verilen belgelerden bilgi çıkarmak.

BELGELER:
{context}

Kullanıcının sorusu: {question}

KAYNAK NUMARALANDIRMA KURALLARI:
1. Her bilgi parçasını yazdığın anda, O BİLGİYİ HANGI PARAGRAFTAN ALDIĞINI belirt
2. Bir cümlede birden fazla paragraftan bilgi kullanıyorsan, her paragrafın numarasını ekle
3. Numara atamadan önce "Bu bilgiyi [X] numaralı paragraftan alıyorum" diye düşün
4. Sadece gerçekten kullandığın paragrafların numarasını yaz
5. Her cümlede kullandığın bilginin kaynak numarasını o cümlenin sonuna ekle

YANIT KURALLARI:
- SADECE yukarıdaki belgelerde yazılı bilgileri kullan
- Belgelerde olmayan bilgi için: "Bu bilgi belgelerde yer almıyor" yanıtını ver
- Yorum, tahmin, varsayım yapma
- Genel bilgi kullanma
- Her bilgi parçasının hemen ardından kaynak numarasını ekle [X]

ÖRNEK YANIT FORMATI:
"Şirketin kurulduğu yıl 2015'tir [1]. Çalışan sayısı 250 kişidir [3]. Merkez ofis İstanbul'da bulunmaktadır [1]."

YANIT VERME ADIMLARİ:
1. Soruyu oku
2. Hangi paragrafta cevap var kontrol et
3. Bilgiyi yaz ve hemen ardından o paragrafın numarasını ekle
4. Başka bilgi gerekiyorsa, yine aynı şekilde kaynak numarasıyla birlikte ekle
  
YANIT:
"""
    data = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "system", "content": "Sen belge analiz asistanısın. Sadece verilen belgelerdeki bilgileri kullanırsın ve her bilgiye kaynak numarası eklersin."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 800,
        "temperature": 0
    }
    resp = requests.post(OPENROUTER_API_URL, headers=headers, json=data, timeout=timeout)
    resp.raise_for_status()
    return resp.json()['choices'][0]['message']['content'] 