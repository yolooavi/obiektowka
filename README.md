# Proste metody szyfrowania, program szyfrujący teksty i demonstrujący możliwości łamania użytych szyfrów

## Programowanie Obiektowe II

Zespół: 41K8 P02

Członkowie zespołu:
- Blanka Wójcik
- Wiktoria Puchalska
- Lizaveta Rashchynskaya
- Zuzanna Cyunel

### Etap II

1. ### Projekt zawierający wybrane funkcjonalności

    Kod źródłowy wraz z wymaganą dokumentacją został zamieszczony w repozytorium pod następującym linkiem: https://github.com/yolooavi/obiektowka.git

    Kod ten jest aplikacją do szyfrowania i deszyfrowania tekstu, wykorzystując różne techniki szyfrowania, takie jak szyfr Cezara, szyfr podstawieniowy i szyfr przestawieniowy. Oprócz tego, umożliwia także generowanie skrótu SHA-256 oraz łamanie szyfru Cezara metodą brutalnej siły.

    Wzorce projektowe zastosowane w projekcie:
    - Singleton: Klasa Encryption została zaimplementowana jako Singleton, co oznacza, że istnieje tylko jedna instancja tej klasy w aplikacji. Zapewnia to, że wszystkie operacje szyfrowania i deszyfrowania korzystają z jednej instancji obiektu Encryption.
    - Fabryka: Klasa CipherFactory działa jako fabryka, która tworzy instancje różnych rodzajów szyfrów na podstawie żądania użytkownika. Dzięki temu można łatwo dodawać nowe rodzaje szyfrów bez konieczności zmiany logiki w głównej części programu.

    Program umożliwia użytkownikowi wybór jednej z następujących opcji:

       1. Szyfr Cezara
       2. Szyfr podstawieniowy
       3. Szyfr przestawieniowy
       4. Szyfrowanie SHA-256
       5. Łamanie szyfru Cezara metodą brutalnej siły
       6.  Wyjście z programu


2. ### Opracowanie koncepcji wizualnej programu.**

    Interakcja z programem odbywa się głównie poprzez wprowadzanie tekstu i otrzymywanie tekstowych odpowiedzi w zakresie szyfrowania, rozszefrowywania oraz łamania szyfrów. Dla tego rodzaju funkcjonalności interfejs tekstowy w konsoli jest wystarczający i wygodny. 

    Po uruchomieniu programu w konsoli wyświetla się menu opcji szyfrowania, które zawiera różne rodzaje szyfrów, które użytkownik może wybrać. 
    
    Następnie program prosi użytkownika o wybór jednej z opcji szyfrowania, podając numery odpowiadające poszczególnym szyfrom (1 - Szyfr Cezara, 2 - Szyfr podstawieniowy, itd.).

    Zakładając, że użytkownik wybiera opcję szyfrowania Szyfr Cezara (wpisując 1), zostaje on poproszony o podanie przesunięcia, czyli o ile liter zostaną przesunięte litery w takście. W przypadku podania liczby większej niż 25 nastąpi powrót do liter początkowych po przekroczeniu ostatniej litery alfabetu. Na przykład, przesunięcie o 34 będzie miało taki sam efekt jak przesunięcie o 8.

    W kolejnym kroju wyświetlony zostanie zaszyfrowany tekst oraz użytkownik zostanie zapytany, czy go chce odszyfrować.W przypadku wyboru "tak", przedstawiony zostanie odszyfrowany tekst, a użytkownik ponownie stanie przed wyborem wybory opcji szyfrowania. 

    Poniżej przestawiono screen ekranu reprezentujący opisany przypadek. 

    ![Screen ekranu](konsola_szyfr_cezara.png)
    Rys.1. Screen ekranu z konsoli. 

3. ### Raport ze stosowania metodologii programowania zwinnego

    Raport z Jiry stosowanej jako system zarządzania niniejszym projektem znajduje się pod następującym linkiem: https://wikipuchalska.atlassian.net/jira/software/projects/POII/boards/2

    ![Raport z Jiry](raport_jira_etap_II.png)
    Rys.2. Screen ekranu z Jiry
    
