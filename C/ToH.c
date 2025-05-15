#include <stdio.h>
#define SCHEIBEN 3 //Wir benutzen 3 Scheiben

int board[3][SCHEIBEN +1]; //Zwei Dimensonales Array
int count=1;

void show()
{
 int i,j,k,width,space;

 for(i=SCHEIBEN; i>=0; i--) {
   for(j=0; j<3; j++)
    {
     width = 2 * board[j][i];     //Breite der Scheibe
     space = (24 - width) / 2;   //Leerzeichen vom Rand weg
     for(k=1; k<=space; k++)
        putchar(' ');

     for(k=1; k<=width/2; k++) //Linke Seite der Scheibe
        putchar('H');

      putchar('I');           //Mittelpunkt
      for(k=1; k<=width/2; k++) //Rechte Seite der Scheibe
          putchar('H');

      for(k=1; k<=space;k++)
          putchar(' ');
      printf(" ");
      }
   printf("\n");
  }
 printf("------------------------------------------------------------------\n");
 printf("%d. Zug : ....\n",count++);
 while((i=getchar())!= '\n');
}

void bewege(int von, int nach)
{
 int i,j;
 printf("Bewege eine Platte von %d nach %d\n\n",von,nach);
 for(i=SCHEIBEN -1; !(board[von][i]); i--);
 for(j=SCHEIBEN -1; !(board[nach][j]) && j>=0; j--);
 board[nach][j+1] = board[von][i];
 board[von][i] = 0;
 show();
}

void hanoi(int von, int nach, int h)
{
 int temp;

 if(h==1) //Falls nur eine Scheibe auf dem Stapel ist
    bewege(von,nach);

 else
  {
   temp=3-von-nach; //Hier wird die Nummer des freien Stabes ermittelt
   hanoi(von,temp,h-1);
   bewege(von,nach);
   hanoi(temp,von,h-1);
   hanoi(von,nach,h-1);
  }
}

int main()
{
 int i,j;

 for(i=0; i<3; i++)
   for(j=0; j<=SCHEIBEN; j++)
     board[i][j] =0; //Array initialisieren

 for(i=0; i<SCHEIBEN; i++) //Alle Scheiben werden auf die erste Stange gelegt
   board[0][i] =SCHEIBEN -i; //Zuerst die Gr��te mit 4 dann Scheibe m. 3,2,1

 printf("\n\n\n\t\tDie Türme von Hanoi\n");
 printf("\t\t-------------------\n\n\n");show(); //Zeigt uns die Grundstellung des Spieles

 hanoi(0,2,SCHEIBEN); //Jetzt gehts los
 return 0;
}