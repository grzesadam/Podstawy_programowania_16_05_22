# Podstawy_programowania_16_05_22

## Badanie rozkładu liczby wartości w przedziale klasowym histogramu

W rozwiązaniu zadania wykorzystaj bibliotekę numpy i matplotlib. 

1) Napisz (wykorzystaj wcześniej napisaną) funkcję generującą N liczb losowych o rozkładzie równomiernym z przedziału [a, b]
2) Ustal K wartości przedziałów klasowych (bins), według których tworzony będzie histogram. Niech przedziały klasowe będą jednakowej długości.
3) Napisz funkcję która wywoła funkcję z punktu 1) M razy i zapisze liczby wartości trafaiających do każdego z przedziałów klasowych zdefiniowanych w punkcie 2. Wynikiem działania tej funkcji powinna być macierz o K kolumnach i M wierszach
4) Wykreśl histogram wartości dla każdej kolumny. Wykres wykonaj w ten sposób, aby miał K paneli (podwykresów - wykorzystaj subplots). Jeśli np. K=12, wykres powinien mieć 3x4 paneli dla każdego z przedziałów. Na każdym z paneli powinna znależć się legenda, która określi przedział klasowy dla którego wykreślony jest histogram, wartość średnią kolumny oraz odchylenie standardowe. 
5) Zadbaj o odpowiednie opisy osi. W jednym wierszu powinny się znaleźć maksymalnie 4 histogramy. Zdecyduj czy przedziały klasowe dla poszczególnych histogramów powinny zostać dobrane automatycznie, czy lepiej je ustalić.
6) Obliczenia wykonaj dla N równego 100, 1000, 10000, K równego np. 5, 10, 20, M równego 100, 1000, 10000
7) Co można powiedzieć o rozkładzie liczby wartości w przedziale histogramu? Ewentualnie wykonaj odpowiedni test statystyczny.
8) Napisany program wykorzystaj do zbadania innych rozkładów w punkcie 1, tzn. zamiast rozkładu równoniemrnego zbadaj np. rozkład normalny, Poissona, Chi^2. 
