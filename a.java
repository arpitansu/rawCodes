import java.util.Scanner;

class a{
	public static void main(String[] args) {
		Scanner t = new Scanner(System.in);
		int te = t.nextInt();
		while (te>0){;
			Scanner sc = new Scanner(System.in);
			float basicSalary = sc.nextFloat();

			if(basicSalary<1500){
				a.below(basicSalary);
			}
			else if(basicSalary>=1500){
				a.above(basicSalary);
			}
			--te;
		}
	}

	public static void below(float basicSalary){

		float grossSalary = basicSalary+(basicSalary*10/100)+(basicSalary*90/100);
		System.out.println((Double)grossSalary);
	}

	public static void above(float basicSalary){

		float grossSalary = (basicSalary+500+(basicSalary*98/100));
		System.out.println((Double)grossSalary);
	}
}
