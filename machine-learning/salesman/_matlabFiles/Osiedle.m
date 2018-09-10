function[Wagi,Odleglosci,Tab] = Osiedle(Bloki)
% Uwaga! Aktualnie rozmiar osiedla wynosi prawie 1000x1000. Przy ustawieniu za duzej ilosci blokow, 
%        i za za duzej odleglosci pomiedzy nimi, program sie nie skonczy, bo
%        nie znajdzie miejsca na kolejne bloki (np. w tym przypadku 50 blokow z odlegloscia pomiedzy
%        nimi 20 najprawdopodobniej sie nigdy nie wykona)

close all;
clc;

%Bloki=10;
Next=1;
Tab=zeros(Bloki,2);

%% Wygenerowanie liczby mieszkañ w blokach 

	Wagi=randi([5 100],1,Bloki)';
    
%% Generator osiedla

hold on

while  Next<Bloki+1
% Wygenerowanie wspolrzednych kolejnego Bloku 
    
	los_x=randi([20 980],1,1); %rozmiar osiedle ustawiany w nawiasach kwadratowych
	los_y=randi([20 980],1,1);
    
% Sprawdzenie czy Blok nie nachodzi na inne 

    [z,dist_x]=knnsearch(Tab(:,1),los_x,'k',1);
    [z,dist_y]=knnsearch(Tab(:,2),los_y,'k',1);
	if dist_x>10    %odloglosci pomiedzy blokami, z tym, ze one i tak beda na siebie nachodzic 
	if dist_y>10    %ze wzgledu na wielkosc kola ustawiona w funkcji plot - linia 31/32
        
%Jesli nie, to narysuj ten Blok i wstaw go do tablicy (tablica wspolrzednych x i y Bloku)
		
	Tab(Next,1)=los_x;
	Tab(Next,2)=los_y;

    plot(los_x,los_y,'-mo','LineWidth',1,'MarkerEdgeColor','k','MarkerFaceColor',[1 0 0],'MarkerSize',round(Wagi(Next)/2))
      
    Next=Next+1;
    end
    end
end

%% Obliczenie odleglosci Blokow od siebie (kazdy od kazdego)
i=1;
j=1;

while i<Bloki+1
	while j<Bloki+1
        Odleglosci(i,j)=pdist([Tab(i,:);Tab(j,:)],'euclidean'); %obliczenie odleglosci punktow od siebie (tw. Pitagorasa)
        plot([Tab(i,1),Tab(j,1)],[Tab(i,2),Tab(j,2)],'Color',[0.7 0.7 1],'LineWidth',1)
      
    j=j+1;
    end
j=1;
i=i+1;
end
%Odleglosci

%% Dopiszwanie numerow do blokow

for i = 1:Bloki
    str=num2str(i);
    text(Tab(i,1)+20,Tab(i,2)+20,['\fontsize{16}','\color[rgb]{0 0 0 }',str])   
end

axis([0 1000 0 1000])

print('Osiedle/Osiedle','-dpng')

file=fopen('Osiedle/Wagi.txt','w');
fprintf(file, '%d ', Wagi);
fclose(file); 

file=fopen('Osiedle/Odleglosci.txt','w');
for i=1:Bloki
    fprintf(file, '%d ', Odleglosci(i,:));
    fprintf(file, '\n');
end
fclose(file); 

file=fopen('Osiedle/Tab.txt','w');
for i=1:Bloki
    fprintf(file, '%d ', Tab(i,:));
    fprintf(file, '\n');
end
fclose(file); 



