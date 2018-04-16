% function [Generacja, Rozwiazanie] = Projekt(Wielkosc_Bloku,Odleglosci,Wsporzedne_Bloku, Bloki, Liczba_populacji, Sukcesja, Czas, Elita)

% Ograniczenia algorytmu:
%- Nie mo¿na u¿ywaæ jednoczeœnie makromutacji i krzy¿owania
%- Wartosci wszystkich zmiennych powinny byæ dodatnie
%- Liczba bloków powinna zawieraæ siê w przedziale 5-50
%- Sukcesja powinna byæ mniejsza od Liczby_populacji
%- Powinna byæ wybrana tylko 1 z opcji tworzenia osiedla (linijka 15 lub 16)


clear all
close all
clc

Bloki = 35;
[Wielkosc_Bloku,Odleglosci,Wsporzedne_Bloku]=Osiedle(Bloki);
%[Wielkosc_Bloku, Odleglosci, Wsporzedne_Bloku, Bloki]=Wczytaj();

Liczba_populacji = 70;
Czas = 0;
Elita=1;
Sukcesja=5;
Liczba_mutacji = 2;        
Liczba_makromutacji = 3;     

Delay = 0;
Wizualizacja = 5; % co ile iteracji nastapi odswierzenie wizualizacji
Wykresy_koncowe = 0;

% Sta³e algorytmu
Roznorodnosc = 0;           
Rozwiazanie = [0 1000000];
Generacja=0;
Warunek=0;
WsplMonotonii=100;      

file=fopen('Najlepsze.txt','w');
fclose(file);

hold on
%% Generacja populacji bazowej 

Populacja=randperm(Bloki);
Populacja=[Populacja  Populacja(1,1)];
for i=1:Liczba_populacji-1
    
    x = randperm(Bloki);
    x=[x  x(1,1)];
    %%%%%%%%%%%%%%%%%% Sprawdzanie roznorodnosci %%%%%%%%%%%%%%%%%%
    if Roznorodnosc == 1
       
       fail = 0;   % Jesli istnieje juz taki osobnik - losuj jeszcze raz.
       ok = 0;     
       while ok == 0
            for k=1:size(Populacja,1)
                if x==Populacja(k,:)
                  fail=1;
                end
            end
            if fail==1
                x=randperm(Bloki);
                x=[x  x(1,1)];
            else ok=1;
            end
            fail=0;
       end 
    end
    Populacja=[Populacja;x];
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
end

 
while (Warunek==0)  %% Pêtla g³ówna 
% Zmiana parametrów w trakcie dzia³ania algorytmu

if Generacja == round(WsplMonotonii) 
    Liczba_mutacji = 1; 
    Liczba_makromutacji = 1;
    Sukcesja=2;
end



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Ocena przydatnoœci osobników i generacja populacji tymczasowej - PT

[Rozwiazanie, Najlepsze, ity] = Ocena_przydatnosci(Czas, Bloki, Wielkosc_Bloku, Odleglosci, Liczba_populacji, Rozwiazanie, Populacja, Generacja);
nr_elity=ity;

clear P;
clear PT
P=Populacja(ity(1:Sukcesja),:);
PT=zeros(Liczba_populacji,Bloki+1);

for i=1:Liczba_populacji
    PT(i,:)=P(randi(Sukcesja),:);
end
PT(:,Bloki+1)=PT(:,1);      %(PT - populacja tymczasowa) 
PO = PT;                    %(PO - populacja potomna) 

% Kolejna generacja
Generacja = Generacja+1;
if (Generacja==1) Rozwiazania=Rozwiazanie;
else Rozwiazania=[Rozwiazania; Rozwiazanie];
end
clear Najlepsi;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Dodatek nowych osobników w do populacji tymczasowej

if Roznorodnosc == 1
    clear x;
    for i=1:ceil(Sukcesja/2)
       x(i,:) = randperm(Bloki);
    end
    x(:,Bloki+1) = x(:,1);
    PT = [PT; x];
end

%% Krzy¿owanie 
% clear x;
% PO=PT*0;
% 
% ciag = round(0.8*Bloki);           % okresla jak duza czesc genomu bedzie  kopiowana
%  
%   for i=1:size(PO)
%     x=randi(Bloki-ciag);
%     PO(i,x:x+ciag)=PT(randi(Sukcesja),x:x+ciag);  
% 
%     if i==ceil(Liczba_populacji*0.25)  % zmiana dlugosci kopiowanego genomu;
%         ciag = round(0.6*Bloki);      % w tym przypadku zmiana nastêpuje dla 25% populacji potomnej i wynosi 60% genomu   
%     end                               %
%     
%     if i==ceil(Liczba_populacji*0.75)
%         ciag = round(0.5*Bloki);
%     end
%  end
%  
%  
% % Uzupelnienie reszty genomu wartosciami ktore nie zostaly skopiowane
%  
%  clear x;
%  for i=1:Liczba_populacji
%     for j=1:Bloki
%         while(PO(i,j) == 0)
%             x=randi(Bloki);
%                 if(length(find(PO(i,:)==x)) < 1)    %sprawdzenie czy w wektorze PO(2,: nie ma juz takiego x)
%                     PO(i,j) = x;
%                 end
%         end
%     end
%     PO(i,Bloki+1)=PO(i,1);
%  end
% 
% [Rozwiazanie, Najlepsze, ity] = Ocena_przydatnosci(Czas, Bloki, Wielkosc_Bloku, Odleglosci, Liczba_populacji, Rozwiazanie, PO, Generacja);
% Najlepsi=[PO(ity(1:3),:)];

%% Makromutacja 
PO=PT;
clear x;

for i=1:Liczba_populacji
     for j=1:Liczba_makromutacji
         x=randi([1 Bloki]);
         if(x>ceil(Bloki/2)) a=randi([2 ceil(Bloki/2)]); else a=randi([ceil(Bloki/2) Bloki]); end
         PO(i,[x a])=PO(i,[a x]); % zamiana miejscem 2 elementów       
     end
      PO(i,Bloki+1)=PO(i,1);
end

[Rozwiazanie, Najlepsze, ity] = Ocena_przydatnosci(Czas, Bloki, Wielkosc_Bloku, Odleglosci, Liczba_populacji, Rozwiazanie, PO, Generacja);
Najlepsi=[PO(ity(1:3),:)];


%% Mutacja 
% PO=PT;
% clear x;
% 
% for i=1:Liczba_populacji
%      for j=1:Liczba_mutacji
%          x=randi([2 Bloki-1]);
%          if(rand(1)>0.5) a=-1; else a=1; end
%          PO(i,[x x+a])=PO(i,[x+a x]); % zamiana miejscem 2 elementów       
%      end
%      PO(i,Bloki+1)=PO(i,1);
% end
% 
% [Rozwiazanie, Najlepsze, ity] = Ocena_przydatnosci(Czas, Bloki, Wielkosc_Bloku, Odleglosci, Liczba_populacji, Rozwiazanie, PO, Generacja);
% Najlepsi = [Najlepsi; PO(ity(1:Sukcesja),:)];

%% Mutacja osobników znajduj¹cych siê blisko siebie


clear col
clear row
clear z
clear x
PO=PT;


   [col,row]=find(Odleglosci<(max(max(Odleglosci))/2));
   for i=1:Liczba_populacji
       
     for j=1:Liczba_mutacji
         
         x=randi(length(col));
         while(col(x)==row(x) || length(find(PO(i,:)==col(x)))>1 || length(find(PO(i,:)==row(x)))>1)
             x=randi(length(col));
         end
         
         if find(PO(i,:)==row(x))<find(PO(i,:)==col(x))
             z=PO(i,find(PO(i,:)==col(x)));
              PO(i,find(PO(i,:)==row(x))+2:find(PO(i,:)==col(x))) = PO(i,find(PO(i,:)==row(x))+1:find(PO(i,:)==col(x))-1);
               PO(i,find(PO(i,:)==row(x))+1)=z;
         else
             z=PO(i,find(PO(i,:)==row(x)));
              PO(i,find(PO(i,:)==col(x))+2:find(PO(i,:)==row(x))) = PO(i,find(PO(i,:)==col(x))+1:find(PO(i,:)==row(x))-1);
               PO(i,find(PO(i,:)==col(x))+1)=z;
         end      
             
     end
     q=find(PO(i,:)==PO(i,1));
     PO(i,[q(2) length(PO(i,:))]) =  PO(i,[length(PO(i,:)) q(2)]);  
   end  
   
[Rozwiazanie, Najlepsze, ity] = Ocena_przydatnosci(Czas, Bloki, Wielkosc_Bloku, Odleglosci, Liczba_populacji, Rozwiazanie, PO, Generacja);
Najlepsi = [Najlepsi; PO(ity(1:Sukcesja),:)];


%% Odwracanie odcinkow genomu

clear x;
clear y;
clear z;
clear q;
PO=PT;


   for i=1:size(PO)
      y=randi([1 ceil(Bloki-2)]);
       
       y=randi([1 ceil(Bloki-2)]); %ile odcinamy
       x=randi([2 Bloki-y]);       %gdzie odcinamy
       z=PO(i,x:x+y);              %odciecie
         for j=1:ceil(y/2)
             z([j length(z)-j+1]) = z([length(z)-j+1 j]);
         end
       PO(i,x:x+y)=z;
    q=find(PO(i,:)==PO(i,1));
    PO(i,[q(2) length(PO(i,:))]) =  PO(i,[length(PO(i,:)) q(2)]);     
   end



%% Tworzenie nowej populacji na podstawie populacji potomnej


if Elita>0
    Populacja = [PO; Najlepsi; Populacja(nr_elity(1:Elita),:)];
else
    Populacja=[PO; Najlepsi];
end


%% Sprawdzenie warunku dzialania algorytmu


if (Generacja-WsplMonotonii>0)
    if (Rozwiazanie == Rozwiazania(Generacja-WsplMonotonii,:))
         Warunek=1;
    end
end



%% Ilustracja najlepszego rozwiazania

if (mod(Generacja,Wizualizacja)==0 && Wizualizacja>0)
    % Odczytanie z pliku aktualnie najlepszej sciezki
    Najlepsza_sciezka = dlmread('Najlepsze.txt','');
    Najlepsza_sciezka = Najlepsza_sciezka(2,:);
    
          
    % Odczytanie wspolrzednych dla blokow w kolejnosci takiej jak
    % Najlepsza_sciezka
    xy = Wsporzedne_Bloku(Najlepsza_sciezka,:);
    
    % Narysowanie Najlepszej_sciezki
    Wczytaj();
    
    figure(1)
    plot(xy(1,1),xy(1,2),'-mo','LineWidth',1,'MarkerEdgeColor','k','MarkerFaceColor',[0 1 1],'MarkerSize',round(Wielkosc_Bloku(Najlepsza_sciezka(1))/2)) 
    plot(xy(:,1),xy(:,2),'k','LineWidth',2) 
    text(Wsporzedne_Bloku(Najlepsza_sciezka(1),1)+20,Wsporzedne_Bloku(Najlepsza_sciezka(1),2)+20,['\fontsize{16}','\color[rgb]{0 0 1 }',num2str(Najlepsza_sciezka(1))])
    
    % Krzywa konwergencji
    pause(Delay);
    if (Czas ~= 0) 
         figure(2)
         hold off
         plot(1:Generacja, Rozwiazania(:,1))
         hold on
    else
         figure(2)
         hold off
         plot(1:Generacja, Rozwiazania(:,2))
         hold on
    end 
end


end





%% Koncowa krzywa konwergencji i obrana sciezka
if Wykresy_koncowe==1  
    
fprintf('\n\n');
if (Czas ~= 0) 
    fprintf('Koniec. Najlepsze rozwiazanie to: %8.4f\n', Rozwiazanie(1))
    figure(2)
    plot(1:Generacja, Rozwiazania(:,1)) 
else
    fprintf('Koniec. Najlepsze rozwiazanie to: %8.4f\n', Rozwiazanie(2))
    figure(2)
    plot(1:Generacja, Rozwiazania(:,2)) 
end   


% Koncowa sciezka
   
Najlepsza_sciezka = dlmread('Najlepsze.txt','');
Najlepsza_sciezka = Najlepsza_sciezka(2,:);
    
% Okreslenie wspolrzednych blokow dla Najlepszej_sciezki
xy = Wsporzedne_Bloku(Najlepsza_sciezka,:);
        
% Ilustracja Najlepszej_sciezki
close(1)
Wczytaj();
figure(1)
hold on

plot(xy(1,1),xy(1,2),'-mo','LineWidth',1,'MarkerEdgeColor','k','MarkerFaceColor',[0 1 1],'MarkerSize',round(Wielkosc_Bloku(Najlepsza_sciezka(1))/2)) 
plot(xy(:,1),xy(:,2),'k','LineWidth',2) 
text(Wsporzedne_Bloku(Najlepsza_sciezka(1),1)+20,Wsporzedne_Bloku(Najlepsza_sciezka(1),2)+20,['\fontsize{16}','\color[rgb]{0 0 1 }',num2str(Najlepsza_sciezka(1))])
    
end


