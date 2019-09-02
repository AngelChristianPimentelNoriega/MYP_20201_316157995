import java.util.Scanner; 
public class Interprete {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
	System.out.println(procesa(sc.nextLine()));
    }
    private static int procesa(String s){
	String [] sumas = s.split("\\+");
	int resultado1 = 0;
	int resultado2 = 0;
	for(int i = 0; i < sumas.length; i++)
	    if(sumas[i].contains("*")){
		String [] producto = sumas[i].split("\\*");
		resultado2 = 1;
		for(int j = 0 ;j < producto.length; j++){
		    resultado2 *= Integer.parseInt(producto[j]);
		}
		resultado1 += resultado2;
	    }
	    else
		resultado1 += Integer.parseInt(sumas[i]);
	return resultado1;
    }
   
}
