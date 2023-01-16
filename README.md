<!-- HEADINGD -->
# Rozwiązania przykładowych zadań z matury z informatyki

*Aby uruchomić programy trzeba mieć zainstalowany na swoim komputerze kompilator języka python 
[Link](https://www.python.org/downloads/), wersję języka z jakiej korzystamy możemy bezpośrednio sprawdzić w Visual Studio Code*

![Screenshot](./img/python.png)

*Program najlepiej uruchomić za pomocą **run python file***

![Screenshot](./img/run.png)

*Znajdziemy to w prawym górnym rogu okna*
*Jeżeli nie mamy takiej opcji, to z lewego paska narzędzi należy wybrać _Extensions_ (Ctrl+Shift+X) i zainstalować rozszerzenie języka python*

### Stałe elementy każdego zadania:

Na początku zadań należy zaimportować pliki potrzebne do wykonania zadania 
```python
    file = open('Tutaj podaj ścieżkę do pliku w którym znajdują się dane do zadania', 'r')
    answer_file = open('Tutaj podaj ścieżkę do pliku do którego zapiszesz odpowiedź', 'w';)
```
Dane z pliku zapisujemy do zmiennej text za pomocą wbudowanej funkcji readlines()

```python
    text = file.readlines()
```

Należy zamknąć również pliki w celu zwolnienia pamięci.
```python
file.close()
answer_file.close()
```
---
## Zadanie - WEGA
### Egzamin Maturalny z Informatyki rok 2018

<!-- LINK -->


>**Materiały do zadania:**

> **[Arkusz Egzaminacyjny](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2015/formula_od_2015/MIN-R2_1P-152.pdf)** 

> [Zasady oceniania](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2015/formula_od_2015/odpowiedzi/MIN-R1-N.pdf)

<!-- Tasks -->

| Numer zadania | Plik z programem |
| --------------|------------------|
|4.1 |**[Kliknij](./WEGA2018/main.py)**|
|4.2 |**[Kliknij](./WEGA2018/main2.py)**|
|4.3 |**[Kliknij](./WEGA2018/main3.py)**|

Wyniki: **[Kliknij](./WEGA2018/wyniki4.txt)**

---
