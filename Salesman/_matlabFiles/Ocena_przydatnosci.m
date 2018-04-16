function[Rozwiazanie, Najlepsze, ity] = Ocena_przydatnosci(Czas, Bloki, Wagi, Odleglosci, Liczba_populacji, Rozwiazanie, Populacja, Generacja);


if (Czas ~= 0) 
    [Najlepsze,ity] = Ograniczenie_czas(Czas, Bloki,Wagi, Odleglosci, Liczba_populacji, Populacja);
    
    if(Najlepsze(1)>Rozwiazanie(1))
        Rozwiazanie(1) = Najlepsze(1);
        file=fopen('Najlepsze.txt','w');
        fprintf(file, '%f', Rozwiazanie(1));
        fprintf(file, '\n');
        fprintf(file, '%d ', Populacja(ity(1),:));
        fclose(file);      
    end
    
    clc
    fprintf('Aktualnie najlepsze rozwiazanie to: %8.4f\n', Rozwiazanie(1))
    fprintf('Generacja: %d\n', Generacja)
    
else
    [Najlepsze,ity] = Bez_ograniczenia(Bloki, Odleglosci, Liczba_populacji, Populacja);
    
    if(Najlepsze(1)<Rozwiazanie(2))
        Rozwiazanie(2) = Najlepsze(1);
        file=fopen('Najlepsze.txt','w');
        fprintf(file, '%f', Rozwiazanie(2));
        fprintf(file, '\n');
        fprintf(file, '%d ', Populacja(ity(1),:));
        fclose(file);
    end
    
    clc
    fprintf('Aktualnie najlepsze rozwiazanie to: %8.4f\n', Rozwiazanie(2))
    fprintf('Generacja: %d\n', Generacja)

end   

