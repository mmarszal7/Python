function [Najlepsze,ity] = Bez_ograniczenia(Bloki, Odleglosci, Liczba_populacji, Populacja)


clear x;
    x=0;
    Droga=zeros(Liczba_populacji,1);
    
    for i=1:Liczba_populacji
       for j=1:Bloki
          x = x + Odleglosci(Populacja(i,j),Populacja(i,j+1));
          
       end
    Droga(i,1)=x;
    x=0;
    end
    [Najlepsze, ity]=sort(Droga);
    