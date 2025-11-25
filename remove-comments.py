#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML yorum satırlarını kaldıran script
Sadece <!-- --> ile açılıp kapanan HTML yorumlarını kaldırır
"""

import re
import glob
import os

def remove_html_comments(content):
    """HTML yorumlarını kaldırır"""
    # Çok satırlı yorumları da yakalamak için (?s) kullanıyoruz
    # Non-greedy (.*?) kullanarak en kısa eşleşmeyi alıyoruz
    pattern = r'(?s)<!--.*?-->'
    # Yorumları boş string ile değiştiriyoruz
    cleaned = re.sub(pattern, '', content)
    # Birden fazla boş satırı tek boş satıra indiriyoruz (temizlik için)
    cleaned = re.sub(r'\n\s*\n\s*\n+', '\n\n', cleaned)
    return cleaned

def process_html_files():
    """Tüm HTML dosyalarını işler"""
    html_files = glob.glob('*.html')
    processed = 0
    
    for file_path in html_files:
        try:
            # Dosyayı UTF-8 encoding ile oku
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Yorumları kaldır
            cleaned_content = remove_html_comments(content)
            
            # Dosyayı tekrar yaz
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            
            processed += 1
            print(f"✓ {file_path} işlendi")
            
        except Exception as e:
            print(f"✗ {file_path} işlenirken hata: {e}")
    
    print(f"\nToplam {processed} dosya işlendi!")

if __name__ == '__main__':
    print("HTML yorum satırları kaldırılıyor...\n")
    process_html_files()
    print("\nİşlem tamamlandı!")