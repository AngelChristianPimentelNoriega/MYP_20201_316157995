#include <stdio.h>
#include <string.h>
void swap(int numeros[], int i , int j){
  int temporal = numeros[i];
  numeros[i] = numeros[j];
  numeros[j] = temporal;
}
int particion(int numeros[], int i, int j)
{
  int pivote = numeros[j];
  int bajo = (i-1);
  for(int k = i; k < j; k++)
    if(numeros[k] <= pivote)
      {
	bajo++;
	swap(numeros,bajo,k);
      }
  swap(numeros, bajo+1,j);
  return(bajo+1);
}
void quicksort(int numeros[], int i, int j)
{
  if(i < j)
    {
    int pi = particion(numeros, i, j);
    quicksort(numeros,i, pi -1);
    quicksort(numeros,pi+1,j);
    }
}


int main ()
{
  int elementos;
  scanf("%d",&elementos);
  int total[elementos];
  for(int i = 0; i < elementos; i++)
    scanf("%d",&total[i]);
  quicksort(total, 0, elementos-1);
  for(int i = 0; i < elementos; i++)
    printf("%d ",total[i]);
  return 0;
}
