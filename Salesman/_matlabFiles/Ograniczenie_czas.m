function[Najlepsze, ity] = Ograniczenie_czas(Czas, Bloki, Wagi, Odleglosci, Liczba_populacji, Populacja)

%%
x=0;
y=0;
Droga=zeros(Liczba_populacji,1);
Rozniesione_ulotki=zeros(Liczba_populacji,1);
j=1;

for i=1:Liczba_populacji
    while(x<Czas && j<Bloki)
        y = y + Wagi(Populacja(i,j));
        x = x + Odleglosci(Populacja(i,j),Populacja(i,j+1));
        j=j+1;
    end
    Droga(i,1)=x;
    Rozniesione_ulotki(i,1) = y;
    y=0;
    x=0;
    j=1;
end

[Najlepsze, ity]=sort(Rozniesione_ulotki,'descend');