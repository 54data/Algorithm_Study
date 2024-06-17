import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		int t, k, n;
		Scanner sc = new Scanner(System.in); 
		t = sc.nextInt();
        int[] apt;
        
        while (t > 0) {
            apt =  new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14};
            k = sc.nextInt(); // 층
            n = sc.nextInt(); // 호
            
            for (int i = 0; i < k; i++) {
                for (int j = 0; j < n; j++) {
                    if (j == 0) {
                        apt[j] = 1;
                    } else if (j >= 1 && j <= n - 1) {
                        apt[j] += apt[j - 1];
                    } 
                }
            }
            
            System.out.println(apt[n - 1]);
            t--;
        }
        sc.close();
	}
}