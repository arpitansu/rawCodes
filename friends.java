import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.InterruptedIOException;
import java.util.Arrays;
import java.util.stream.IntStream;

class one{
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int pl;
        String x;int countIt=0;int whoWinnerIs =0;
        int n = Integer.parseInt(br.readLine());
        while (n-- > 0) {
            pl = Integer.parseInt(br.readLine());
            int score[] =new int[pl];
            for (int i = 0; i < pl; i++) {
                x = br.readLine();
                int[] a = toIntArray(x);
                /*for (int A:
                        a) {
                    System.out.println(A);
                }*/
                countIt = checkDuplicate(a);
                score[i] = cookieScore(countIt) + a[0];
            }
           /*for (int a:
                 score) {
                System.out.println(a);
            }*/
            whoWinnerIs = findwhoWinnerIs(pl,score);
            if (whoWinnerIs == 0) {
                System.out.println("chef");
            } else if (whoWinnerIs == -1) {
                System.out.println("tie");
            } else {
                System.out.println(whoWinnerIs + 1);
            }
        }
    }
    public static int cookieScore(int countIt){
        int distinct=0;
        if (countIt == 4){
            distinct=1;
        }
        else if (countIt == 5){
            distinct=2;
        }
        else if (countIt == 6){
            distinct=4;
        }
        return (distinct);

    }

    public static int findwhoWinnerIs(int n,int a[]) {
        int contain = 0,cont=0;
        int pos =-1;
        boolean tie = false;
        cont=IntStream.of(a).max().getAsInt();
        for (int i = 0; i < a.length; i++) {
            if (a[i] == cont)
                pos= i;
        }
        Arrays.sort(a);
        int max =a[a.length -1];
        int max2=a[a.length -2];
        if  (max == max2) {
            return -1;
        } else {
            return pos;
        }
    }
    public static int[] toIntArray(String x){
        String[] splited = x.split("\\s+");
        int[] ja=new int[splited.length];
            for (int j=0;j<splited.length;j++){
                ja[j]= Integer.parseInt(splited[j]);
            }
        return ja;
    }
    public static int checkDuplicate(int array[]) {
        int countIt=0;
        for (int i = 1; i < array.length; i++) {
            boolean found = false;
            for (int j = 1; j < i; j++)
                if (array[i] == array[j]) {
                    found = true;
                    break;
                }
            if (!found)
                countIt++;
        }
        return countIt;
    }
}